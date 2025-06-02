#!/usr/bin/env python3
# Copyright (C) 2025 Tipz Team
# SPDX-License-Identifier: Apache-2.0
"""
Usage:
    plfsutils.py --help
    plfsutils.py <filename>
"""

import os

def main(file_arg, output_arg, action_arg, extra_arg):
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

        decoded_string = transformed_bytes.decode('utf-8').strip()
        lines = decoded_string.split('\n')

        target_list.extend(lines)

    # Write list to pl.fs file
    def write_plfs(file_path, target_list):
        content = ''.join([f"{s}\n" for s in target_list])
        original_bytes = content.encode('utf-8')
        a_byte = ord('a')

        transformed_bytes = bytearray()
        for b in original_bytes:
            not_b = (~b) & 0xFF
            transformed_byte = not_b ^ a_byte
            transformed_bytes.append(transformed_byte)

        with open(file_path, 'wb') as f:
            f.write(transformed_bytes)

    print("plfsutils (c) Tipz Team 2025")

    # Parse input file
    filename = file_arg
    parse_plfs(filename, oppo_apk_list)

    # Decide which action to take
    action = action_arg
    extra = extra_arg

    if action == "add":
        if not extra:
            print('No packages are provided for addition.')
            return

        output_filename = output_arg
        if output_filename == None:
            output_filename = filename

        print('Packages to add:')
        print('\n'.join(map(str, extra)))
        print()

        oppo_apk_list.extend(extra)
        write_plfs(output_filename, oppo_apk_list)

        print(f'Done! Written to {output_filename}.')

    elif action == "list":
        print('List of packages:')
        print('\n'.join(map(str, oppo_apk_list)))

if __name__ == '__main__':
    import sys, argparse

    parser = argparse.ArgumentParser(description="plfsutils (c) Tipz Team 2025", add_help=False)
    required = parser.add_argument_group('Required')
    required.add_argument("filename", help="Path to pl.fs file")
    required.add_argument("action", help="Perform specified action - add, list")
    required.add_argument("extra", nargs=argparse.REMAINDER, help=argparse.SUPPRESS)
    optional = parser.add_argument_group('Optional')
    optional.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    optional.add_argument("-o", "--output", help="Path to output pl.fs file")
    args = parser.parse_args()

    sys.exit(main(args.filename, args.output, args.action, args.extra))

