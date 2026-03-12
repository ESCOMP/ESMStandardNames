#!/usr/bin/env python3
"""
Sort the <standard_name> elements alphabetically by their "name" attribute within each <section>
(subsection) of an ESM Standard Names XML file.

The original file may contain comments, attributes, and nested sections. The script preserves the
overall structure of the XML with all elements and comments.

Usage:
    python sort_standard_names.py [input.xml] [output.xml]

If the output file is omitted, the input file will be overwritten.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

def sort_section(section: ET.Element) -> None:
    """Sort <standard_name> children of *section* alphabetically.
    The sorting key is the ``name`` attribute of each <standard_name> element.
    The relative order of non‑<standard_name> children (e.g., comments, other tags)
    is preserved.
    """
    # Find all <standard_name> children and remember where they appeared
    std_children: list[ET.Element] = []
    positions: list[int] = []

    for idx, child in enumerate(list(section)):
        if child.tag == "standard_name":
            std_children.append(child)
            positions.append(idx)

    if not std_children:
        return

    # Sort by name attribute
    std_children.sort(key=lambda e: e.get("name", ""))

    # Remove all original standard_name children
    for child in std_children:
        section.remove(child)

    # Insert sorted children at the first original position
    insert_at = positions[0]
    for child in reversed(std_children):  # reversed to maintain order when inserting
        section.insert(insert_at, child)


def process_file(xml_path: Path) -> ET.ElementTree:
    """Parse *xml_path*, sort all subsections, and return the ElementTree."""
    tree = ET.parse(str(xml_path))
    root = tree.getroot()

    # Recursively sort each section element
    for section in root.iter("section"):
        sort_section(section)

    return tree


def main() -> None:
    parser = argparse.ArgumentParser(description="Alphabetically sort standard names within each subsection of the ESM Standard Names XML file.")
    parser.add_argument("input", nargs="?", default="standard_names.xml", help="Input XML file (default: standard_names.xml)")
    parser.add_argument("output", nargs="?", default="", help="Output file (default: overwrite input)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file {input_path} does not exist.", file=sys.stderr)
        sys.exit(1)

    tree = process_file(input_path)

    if hasattr(ET, "indent"):
        ET.indent(tree, space="  ", level=0)

    output_path = Path(args.output) if args.output else input_path
    tree.write(str(output_path), xml_declaration=True, encoding="utf-8")
    print(f"Sorted standard names written to {output_path}")


if __name__ == "__main__":
    main()
