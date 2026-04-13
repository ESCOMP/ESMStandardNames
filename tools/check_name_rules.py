#!/usr/bin/env python3

"""
Check standard names database file for violations of standard name character rules
"""

import argparse
import os.path
import re
import xml.etree.ElementTree as ET

#Import custom helper functions from lib/ directory
from lib import find_schema_file, validate_xml_file, read_xml_file

def main():
    # pylint: disable=too-many-locals
    """Parse the standard names database file and output a dictionary
    where the keys are any standard names in violation of character rules,
    and the values are lists of the specific rules violated
    """
    #Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("-s","--standard_name_file",default="standard_names.xml",
                        metavar='<standard names filename>',
                        type=str, help="XML file with standard name library")
    args = parser.parse_args()

    stdname_file = os.path.abspath(args.standard_name_file)
    _, root = read_xml_file(stdname_file)

    # Validate the XML file
    schema_name = os.path.basename(stdname_file)[0:-4]
    schema_root = os.path.dirname(stdname_file)
    schema_path = os.path.join(schema_root,schema_name)
    schema_file = find_schema_file(schema_path)
    if schema_file:
        try:
            validate_xml_file(stdname_file, schema_name, None,
                            schema_path=schema_root, error_on_noxmllint=True)
        except ValueError as exc:
            raise ValueError(f"Invalid standard names file, {stdname_file}") from exc
    else:
        raise FileNotFoundError(f'Cannot find schema file, {schema_name}')

    #Parse list of standard names and see if any names violate one or more rules
    violators = {}
    legal_first_char = re.compile('[a-z]')
    valid_name_chars = re.compile('[a-z0-9_]')
    for name in root.findall('.//standard_name'):
        sname = name.attrib['name']
        violations = []
        if legal_first_char.sub('', sname[0]):
            violations.append('First character is not a lowercase letter')
        testchars = valid_name_chars.sub('', sname)
        if testchars:
            violations.append(f'Invalid characters are present: "{testchars}"')

        # If any violations were detected, add an entry to "violators" dictionary
        if violations:
            violators[sname] = violations

    # Check for non-ascii characters (ord > 127)
    for elem in ET.tostringlist(root, encoding='unicode'):
        violations = []
        badchars = ''
        badchars=''.join([i if ord(i) > 127 else '' for i in elem])
        if badchars:
            violations.append(f'Non-ascii characters found in {elem}: {badchars}')
        if violations:
            violators[elem] = f'Non-ascii characters found: {badchars}'

    if violators:
        raise Exception(f"Violating entries found:\n{violators}") # pylint: disable=broad-exception-raised

    print(f'Success! All entries in {args.standard_name_file} follow the rules.')

if __name__ == "__main__":
    main()
