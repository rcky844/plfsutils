#!/usr/bin/env python3
# Copyright (C) 2025 Tipz Team
# SPDX-License-Identifier: Apache-2.0
"""
Usage:
    plfsutils.py --help
    plfsutils.py <filename>
"""

import os

def main(file_arg):
    oppo_apk_list = []

    # Parse pl.fs file into list
    def parse_plfs(file_path, target_list):
        with open(file_path, 'rb') as file:
            file_content = file.read()

        a_byte = ord('a')
        transformed_bytes = bytearray()

        for byte in file_content:
            temp = byte ^ a_byte
            transformed_byte = (~temp) & 0xFF
            transformed_bytes.append(transformed_byte)

        decoded_string = transformed_bytes.decode('utf-8')
        lines = decoded_string.split('\n')

        target_list.extend(lines)

    print("plfsutils (c) Tipz Team 2025")
    filename = file_arg
    parse_plfs(filename, oppo_apk_list)

    # Print result to console
    print('List of packages:')
    print('\n'.join(filter(None, map(str.strip, oppo_apk_list))))

if __name__ == '__main__':
    import sys, argparse

    parser = argparse.ArgumentParser(description="plfsutils (c) Tipz Team 2025", add_help=False)
    required = parser.add_argument_group('Required')
    required.add_argument("filename", help="Path to pl.fs file")
    optional = parser.add_argument_group('Optional')
    optional.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    args = parser.parse_args()

    sys.exit(main(args.filename))

