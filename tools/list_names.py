#!/usr/bin/env python3
"""
Print an alphabetized list of all <standard_name> names from ESM Standard Names XML file.
"""

from __future__ import annotations

import sys
from pathlib import Path
import xml.etree.ElementTree as ET


def extract_names(xml_path: Path) -> list[str]:
    """
    Return a sorted list of all 'name' attributes from <standard_name> elements.
    """
    tree = ET.parse(str(xml_path))
    root = tree.getroot()

    # Find every <standard_name> element anywhere in the document.
    names = [
        elem.get("name")
        for elem in root.iter("standard_name")
        if elem.get("name") is not None
    ]

    return sorted(names, key=str.lower)


def main() -> None:
    """Main function for command-line execution"""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <standard_names.xml>", file=sys.stderr)
        sys.exit(1)

    xml_file = Path(sys.argv[1])
    if not xml_file.exists():
        print(f"Error: {xml_file} not found.", file=sys.stderr)
        sys.exit(1)

    for name in extract_names(xml_file):
        print(name)


if __name__ == "__main__":
    main()
