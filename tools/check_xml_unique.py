#!/usr/bin/env python3

"""
Remove duplicates from a metadata standard-name XML library file.
"""

import argparse
import sys
import os.path

#Import custom helper functions from lib/ directory
from lib import validate_xml_file, read_xml_file

def parse_command_line(args, description):
    """Parse and return command-line arguments"""
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-s", "--standard_name_file", default="standard_names.xml",
                        metavar='<standard names filename>',
                        type=str, help="XML file with standard name library")
    parser.add_argument("--field", type=str, default="name",
                        help="Field to check for uniqueness; default is 'name'")
    parser.add_argument("--debug", action='store_true',
                        help="flag for additional debug print statements")

    pargs = parser.parse_args(args)
    return pargs

def main_func():
    # pylint: disable=too-many-branches
    """Parse the standard names database file and notify of duplicates.
    """
    # Parse command line arguments
    args = parse_command_line(sys.argv[1:], __doc__)
    stdname_file = os.path.abspath(args.standard_name_file)
    _, root = read_xml_file(stdname_file)

    # Validate the XML file
    schema_root = os.path.dirname(stdname_file)
    schema_path = os.path.join(schema_root,"standard_names.xsd")
    validate_xml_file(stdname_file, schema_path, logger=None, error_on_noxmllint=True)

    #get list of all standard names
    all_std_names = []
    for name in root.findall('.//standard_name'):
        try:
            if args.field == 'cfname':
                # Extract from cfname subelement
                cfname_elem = name.find('cfname')
                if cfname_elem is not None and cfname_elem.text is not None:
                    all_std_names.append(cfname_elem.text.strip())
                elif args.debug:
                    print(f"WARNING: no cfname subelement for standard name {name.attrib['name']}")
            else:
                # Extract from attribute
                all_std_names.append(name.attrib[args.field])
        except KeyError:
            if args.debug:
                print(f"WARNING: no field {args.field} for standard name {name.attrib['name']} ")
    #get list of all unique and duplicate standard names, in source order
    seen = set()
    uniq_std_names = []
    dup_std_names = []
    for x in all_std_names:
        if x not in seen:
            uniq_std_names.append(x)
            seen.add(x)
        else:
            dup_std_names.append(x)

    if len(dup_std_names)>0:
        print(f'The following duplicate {args.field} entries were found:')
        for dup in dup_std_names:
            if args.field == 'cfname':
                rm_elements = root.findall(f'.//standard_name[cfname="{dup}"]')[1:]
            else:
                rm_elements = root.findall(f'.//standard_name[@{args.field}="{dup}"]')[1:]
            print(f"{dup}, ({len(rm_elements)} duplicate(s))")
            # exit with status 1 to indicate failure
            sys.exit(1)
    else:
        print(f'No duplicate {args.field}s were found.')


if __name__ == "__main__":
    main_func()
