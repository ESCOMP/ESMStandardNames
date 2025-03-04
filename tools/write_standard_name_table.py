#!/usr/bin/env python3

"""
Convert a metadata standard-name XML library file to a documentation format.
"""

# Python library imports
import xml.etree.ElementTree as ET
import os.path
import argparse
import sys
import re

################################################
#Add CCPP framework (lib) modules to python path
################################################

_CURR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_CURR_DIR, "lib"))

#######################################
#Import needed framework python modules
#######################################

from xml_tools import validate_xml_file, read_xml_file
from xml_tools import find_schema_file, find_schema_version

#######################################
#Regular expressions
#######################################

_REAL_SUBST_RE = re.compile(r"(.*\d)p(\d.*)")

_DROPPED_LINK_CHARS_RE = re.compile(r"[^a-z_-]")

########################################################################
def convert_text_to_link(text_str):

    """
    When Markdown converts a header string into
    an internal document link it applies certain
    text conversion rules.  This function thus
    applies those same rules to a given string
    in order to produce the correct link.
    """

    #First trim the string to remove leading/trailing white space:
    link_str = text_str.strip()

    #Next, make sure all text is lowercase:
    link_str = link_str.lower()

    #Then, replace all spaces with dashes:
    link_str = link_str.replace(" ", "-")

    #Finally, remove all characters that aren't
    #letters, underscores, or dashes:
    link_str = _DROPPED_LINK_CHARS_RE.sub("",link_str)

    return link_str

########################################################################
def standard_name_to_long_name(prop_dict, context=None):
########################################################################
    """Translate a standard_name to its default long_name
    Note: This code is copied from the CCPP Framework.
    >>> standard_name_to_long_name({'standard_name':'cloud_optical_depth_layers_from_0p55mu_to_0p99mu'})
    'Cloud optical depth layers from 0.55mu to 0.99mu'
    >>> standard_name_to_long_name({'local_name':'foo'}) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    CCPPError: No standard name to convert foo to long name
    >>> standard_name_to_long_name({}) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    CCPPError: No standard name to convert to long name
    >>> standard_name_to_long_name({'local_name':'foo'}, context=ParseContext(linenum=3, filename='foo.F90')) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    CCPPError: No standard name to convert foo to long name at foo.F90:3
    >>> standard_name_to_long_name({}, context=ParseContext(linenum=3, filename='foo.F90')) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    CCPPError: No standard name to convert to long name at foo.F90:3
    """
    # We assume that standar_name has been checked for validity
    # Make the first char uppercase and replace each underscore with a space
    if 'standard_name' in prop_dict:
        standard_name = prop_dict['standard_name']
        if standard_name:
            long_name = standard_name[0].upper() + re.sub("_", " ",
                                                          standard_name[1:])
        else:
            long_name = ''
        # end if
        # Next, substitute a decimal point for the p in [:digit]p[:digit]
        match = _REAL_SUBST_RE.match(long_name)
        while match is not None:
            long_name = match.group(1) + '.' + match.group(2)
            match = _REAL_SUBST_RE.match(long_name)
        # end while
    else:
        long_name = ''
        if 'local_name' in prop_dict:
            lname = ' {}'.format(prop_dict['local_name'])
        else:
            lname = ''
        # end if
        ctxt = context_string(context)
        emsg = 'No standard name to convert{} to long name{}'
        raise CCPPError(emsg.format(lname, ctxt))
    # end if
    return long_name

###############################################################################
def parse_command_line(args, description):
###############################################################################
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("standard_name_file",
                        metavar='<standard names filename>',
                        type=str, help="XML file with standard name library")
    parser.add_argument("--output-filename", metavar='<output filename>',
                        type=str, default='Metadata-standard-names',
                        help="Name of output file (without extension)")
    parser.add_argument("--output-format", metavar='md', type=str, default='md',
                        help="Format of output file")
    pargs = parser.parse_args(args)
    return pargs

###############################################################################
def convert_xml_to_markdown(root, library_name, snl):
###############################################################################
    snl.write('# {}\n'.format(library_name))
    # Write a table of contents for top-level sections
    snl.write('#### Table of Contents\n')
    for section in root:
        sec_name = section.get('name')
        sec_name_link = convert_text_to_link(sec_name) #convert string to link text
        snl.write(f"* [{sec_name}](#{sec_name_link})\n")
    # end for
    snl.write('\n')
    for section in root:
        parse_section(snl, section)

###############################################################################
def parse_section(snl, sec, level='##'):
###############################################################################
        # Step through the sections
        sec_name = sec.get('name')
        sec_comment = sec.get('comment')
        snl.write(f'{level} {sec_name}\n')
        if sec_comment is not None:
            # First, squeeze out the spacing
            while sec_comment.find('  ') >= 0:
                sec_comment = sec_comment.replace('  ', ' ')
            while sec_comment:
                sec_comment = sec_comment.lstrip()
                cind = sec_comment.find('\\n')
                if cind > 0:
                    snl.write('{}\n'.format(sec_comment[0:cind]))
                    sec_comment = sec_comment[cind+2:]
                else:
                    snl.write('{}\n'.format(sec_comment))
                    sec_comment = ''
        for std_name in sec:
            if std_name.tag == 'section':
                parse_section(snl, std_name, level + '#')
                continue
            stdn_name = std_name.get('name')
            stdn_longname = std_name.get('long_name')
            if stdn_longname is None:
                sdict = {'standard_name':stdn_name}
                stdn_longname = standard_name_to_long_name(sdict)
            # end if
            snl.write("* `{}`: {}\n".format(stdn_name, stdn_longname))
            # Should only be a type in the standard_name text
            for item in std_name:
                if item.tag == 'type':
                    txt = item.text
                    kind = item.get('kind')
                    if kind is None:
                        kstr = ''
                    else:
                        kstr = "(kind={})".format(kind)
                    # end if
                    units = item.get('units')
                    snl.write('    * `{}{}`: units = {}\n'.format(txt, kstr,
                                                                  units))
                else:
                    emsg = "Unknown standard name property, '{}'"
                    raise ValueError(emsg.format(item.tag))

###############################################################################
def main_func():
###############################################################################
    """Validate and parse the standard names database file and generate
    a document containing the data.
    Currently, only the Markdown format is supported for output.
    """
    # Parse command line arguments
    args = parse_command_line(sys.argv[1:], __doc__)
    stdname_file = os.path.abspath(args.standard_name_file)
    # Read the XML file
    _, root = read_xml_file(stdname_file)
    library_name = root.get('name')
    # Validate the XML file (needs to be here to grab the version)
    version = find_schema_version(root)
    schema_name = os.path.basename(stdname_file)[0:-4]
    schema_root = os.path.dirname(stdname_file)
    schema_file = find_schema_file(schema_name, version)
    if not schema_file:
        emsg = 'Cannot find schema file, {}, for version {}'
        raise ValueError(emsg.format(schema_name, version))
    # end if
    try:
        emsg = "Invalid standard names file, {}".format(stdname_file)
        file_ok = validate_xml_file(stdname_file, schema_name, version,
                                    None, schema_path=schema_root,
                                    error_on_noxmllint=True)
    except ValueError as valerr:
        cemsg = "{}".format(valerr).split('\n')[0]
        if cemsg[0:12] == 'Execution of':
            xstart = cemsg.find("'")
            if xstart >= 0:
                xend = cemsg[xstart + 1:].find("'") + xstart + 1
                emsg += '\n' + cemsg[xstart + 1:xend]
            # end if (else, just keep original message)
        elif cemsg[0:18] == 'validate_xml_file:':
            emsg += "\n" + cemsg
        # end if
        raise ValueError(emsg)
    # end try
    if args.output_format != 'md':
        emsg = "Unsupported output format, '{}'"
        raise ValueError(emsg.format(args.output_format))
    # end if
    outfile_name = args.output_filename
    with open("{}.{}".format(outfile_name, args.output_format), "w") as snl:
        convert_xml_to_markdown(root, library_name, snl)
    # end with


###############################################################################
if __name__ == "__main__":
    main_func()
