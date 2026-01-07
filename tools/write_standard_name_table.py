#!/usr/bin/env python3

"""
Convert a metadata standard-name XML library file to another format.
"""

# Python library imports
from collections import OrderedDict
import xml.etree.ElementTree as ET
import os.path
import argparse
import sys
import re
import yaml

################################################
# Add lib modules to python path
################################################

_CURR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_CURR_DIR, "lib"))

#######################################
# Import needed framework python modules
#######################################

from xml_tools import validate_xml_file, read_xml_file
from xml_tools import find_schema_file, find_schema_version

#######################################
# Regular expressions
#######################################

_REAL_SUBST_RE = re.compile(r"(.*\d)p(\d.*)")

_DROPPED_LINK_CHARS_RE = re.compile(r"[^a-z_-]")

#######################################
# Custom representer for OrderedDict
#######################################

def ordered_dict_representer(dumper, data):
    return dumper.represent_mapping(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items())
yaml.add_representer(OrderedDict, ordered_dict_representer)

########################################################################
def convert_text_to_link(text_str):
########################################################################
    """
    When Markdown converts a header string into
    an internal document link it applies certain
    text conversion rules.  This function thus
    applies those same rules to a given string
    in order to produce the correct link.
    """

    # First trim the string to remove leading/trailing white space:
    link_str = text_str.strip()

    # Next, make sure all text is lowercase:
    link_str = link_str.lower()

    # Then, replace all spaces with dashes:
    link_str = link_str.replace(" ", "-")

    # Finally, remove all characters that aren't
    # letters, underscores, or dashes:
    link_str = _DROPPED_LINK_CHARS_RE.sub("", link_str)

    return link_str

########################################################################
def standard_name_to_description(prop_dict, context=None):
########################################################################
    """Translate a standard_name to its default description
    Note: This code is copied from the CCPP Framework.
    >>> standard_name_to_description({'standard_name':'cloud_optical_depth_layers_from_0p55mu_to_0p99mu'})
    'Cloud optical depth layers from 0.55mu to 0.99mu'
    >>> standard_name_to_description({'local_name':'foo'}) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    CCPPError: No standard name to convert foo to description
    >>> standard_name_to_description({}) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    CCPPError: No standard name to convert to description
    >>> standard_name_to_description({'local_name':'foo'}, context=ParseContext(linenum=3, filename='foo.F90')) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    CCPPError: No standard name to convert foo to description at foo.F90:3
    >>> standard_name_to_description({}, context=ParseContext(linenum=3, filename='foo.F90')) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    CCPPError: No standard name to convert to description at foo.F90:3
    """
    # We assume that standard_name has been checked for validity
    # Make the first char uppercase and replace each underscore with a space
    if 'standard_name' in prop_dict:
        standard_name = prop_dict['standard_name']
        if standard_name:
            description = standard_name[0].upper() + re.sub("_", " ",
                                                          standard_name[1:])
        else:
            description = ''
        # end if
        # Next, substitute a decimal point for the p in [:digit]p[:digit]
        match = _REAL_SUBST_RE.match(description)
        while match is not None:
            description = match.group(1) + '.' + match.group(2)
            match = _REAL_SUBST_RE.match(description)
        # end while
    else:
        description = ''
        if 'local_name' in prop_dict:
            lname = ' {}'.format(prop_dict['local_name'])
        else:
            lname = ''
        # end if
        ctxt = context_string(context)
        emsg = 'No standard name to convert{} to description{}'
        raise CCPPError(emsg.format(lname, ctxt))
    # end if
    return description

###############################################################################
def parse_command_line(args, program_description):
###############################################################################
    parser = argparse.ArgumentParser(description=program_description,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("standard_name_file",
                        metavar='<standard names filename>',
                        type=str, help="XML file with standard name library")
    parser.add_argument("--output-filename", metavar='<output filename>',
                        type=str, default='Metadata-standard-names',
                        help="Name of output file (without extension)")
    parser.add_argument("--output-format", metavar='[md|yaml]', type=str, default=None,
                        required=True, help="Format of output file")
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
        sec_name_link = convert_text_to_link(sec_name)  # convert string to link text
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
                sec_comment = sec_comment[cind + 2:]
            else:
                snl.write('{}\n'.format(sec_comment))
                sec_comment = ''
            # end if
        # end while
    # end if
    for std_name in sec:
        if std_name.tag == 'section':
            parse_section(snl, std_name, level + '#')
            continue
        stdn_name = std_name.get('name')
        stdn_description = std_name.get('description')
        if stdn_description is None:
            sdict = {'standard_name': stdn_name}
            stdn_description = standard_name_to_description(sdict)
        # end if
        snl.write("* `{}`: {}\n".format(stdn_name, stdn_description))
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
            # end if
        # end for
    # end for
# end for

###############################################################################
def convert_xml_to_yaml(root, library_name, yaml_file):
###############################################################################
    yaml_data = OrderedDict()
    yaml_data['library_name'] = library_name
    yaml_data['section'] = []

    for section in root.findall('section'):
        yaml_data['section'].append(parse_section(section))

    yaml.dump(yaml_data, yaml_file, default_flow_style=False)


###############################################################################
def parse_section(section):
###############################################################################
    sec_data = OrderedDict()
    sec_data['name'] = section.get('name')

    # ---- Format section comment ----
    sec_comment = section.get('comment')
    if sec_comment:
        sec_comment = sec_comment.replace('```', '')
        sec_comment = sec_comment.split('\n')
        sec_comment = [' '.join(x.split()) for x in sec_comment if x.strip()]
        sec_comment = ' '.join(sec_comment)
    sec_data['comment'] = sec_comment

    # ---- Parse standard names (only direct children) ----
    sec_data['standard_names'] = []

    for std_name in section.findall('standard_name'):
        stdn_name = std_name.get('name')
        stdn_description = std_name.get('description')

        if stdn_description is None:
            sdict = {'standard_name': stdn_name}
            stdn_description = standard_name_to_description(sdict)

        std_type = std_name.find('type')
        if std_type is None:
            continue

        std_name_data = OrderedDict()
        std_name_data['name'] = stdn_name
        std_name_data['description'] = stdn_description
        std_name_data['type'] = std_type.text
        std_name_data['kind'] = std_type.get('kind')

        units = std_type.get('units')
        try:
            std_name_data['units'] = int(units) if units is not None else None
        except (ValueError, TypeError):
            std_name_data['units'] = units

        sec_data['standard_names'].append(std_name_data)

    # If no standard names in section, delete key/value pair
    if not sec_data['standard_names']:
        del sec_data['standard_names']

    # ---- Recurse into subsections ----
    subsections = []
    for subsection in section.findall('section'):
        subsections.append(parse_section(subsection))

    if subsections:
        sec_data['section'] = subsections

    return sec_data

###############################################################################
def main_func():
###############################################################################
    """Validate and parse the standard names database file and generate
    a document containing the data."""
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

    outfile_name = args.output_filename
    if args.output_format == 'md':
        with open(f"{outfile_name}.md", "w") as md_file:
            convert_xml_to_markdown(root, library_name, md_file)
    elif args.output_format == 'yaml':
        with open(f"{outfile_name}.yaml", "w") as yaml_file:
            convert_xml_to_yaml(root, library_name, yaml_file)
    else:
        emsg = "Unsupported output format, '{}'"
        raise ValueError(emsg.format(args.output_format))
    # end if

###############################################################################
if __name__ == "__main__":
    main_func()
