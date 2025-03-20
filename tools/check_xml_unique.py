#!/usr/bin/env python3

"""
Remove duplicates from a metadata standard-name XML library file.
"""

import argparse
import sys
import os.path
import xml.etree.ElementTree as ET
import copy

################################################
# Add lib modules to python path
################################################

_CURR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_CURR_DIR, "lib"))

#######################################
#Import needed framework python modules
#######################################

from xml_tools import find_schema_file, find_schema_version, validate_xml_file, read_xml_file

###############################################################################
def parse_command_line(args, description):
###############################################################################
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("standard_name_file",
                        metavar='<standard names filename>',
                        type=str, help="XML file with standard name library")
    parser.add_argument("--overwrite", action='store_true',
                        help="flag to remove duplicates and overwrite the file")

    pargs = parser.parse_args(args)
    return pargs

###############################################################################
def main_func():
###############################################################################
    """Parse the standard names database file and notify of duplicates.
    """
    # Parse command line arguments
    args = parse_command_line(sys.argv[1:], __doc__)
    stdname_file = os.path.abspath(args.standard_name_file)
    tree, root = read_xml_file(stdname_file)

    # Validate the XML file
    version = find_schema_version(root)
    schema_name = os.path.basename(stdname_file)[0:-4]
    schema_root = os.path.dirname(stdname_file)
    schema_path = os.path.join(schema_root,schema_name)
    schema_file = find_schema_file(schema_path, version)
    if schema_file:
        try:
            validate_xml_file(stdname_file, schema_name, version, None,
                            schema_path=schema_root, error_on_noxmllint=True)
        except ValueError:
            raise ValueError(f"Invalid standard names file, {stdname_file}")
    else:
        raise ValueError(f'Cannot find schema file, {schema_name}, for {version=}')

    #get list of all standard names
    all_std_names = []
    for name in root.findall('./section/standard_name'):
        all_std_names.append(name.attrib['name'])

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

    if args.overwrite:
        #delete all duplicate elements after the first
        if len(dup_std_names)>0:
            print('The following duplicate standard names were found:')
            for dup in dup_std_names:
                rm_elements = root.findall('./section/standard_name[@name="%s"]'%dup)[1:]
                print(f"{dup}, ({len(rm_elements)} duplicate(s))")
            print(f'Removing duplicates and overwriting {stdname_file}')
            for dup in dup_std_names:
                first_use = True #Logical that indicates the first use of the duplicated name
                rm_parents = root.findall('./section/standard_name[@name="%s"]..'%dup)
                for par in rm_parents:
                    rm_ele = par.findall('./standard_name[@name="%s"]'%dup)
                    for ele in rm_ele:
                        if first_use:
                            #Now all future uses of the name will be removed:
                            first_use = False
                        else:
                            par.remove(ele)
            #Overwrite the xml file with the new, duplicate-free element tree:
            tree.write(stdname_file, "utf-8")
        else:
            print('No duplicate standard names were found.')
    else:
        #write out duplicate standard names
        if len(dup_std_names)>0:
            print('The following duplicate standard names were found:')
            for dup in dup_std_names:
                rm_elements = root.findall('./section/standard_name[@name="%s"]'%dup)[1:]
                print(f"{dup}, ({len(rm_elements)} duplicate(s))")
            sys.exit(1)
        else:
            print('No duplicate standard names were found.')

###############################################################################
if __name__ == "__main__":
    main_func()
