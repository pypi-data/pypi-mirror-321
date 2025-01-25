#!/usr/bin/env python3

import argparse
import json
import os

from ziploc.main import decrypt, encrypt

PROJECT_PATH = os.getcwd()


def process_json(data, password, is_encrypt):
    try:
        if is_encrypt:
            return encrypt(data, password)
        else:
            return decrypt(data, password)
    except (ValueError, KeyError) as e:
        print(f"[ZIPLOC/ERROR] {e}")
        raise e


def main():
    parser = argparse.ArgumentParser(description="Ziploc CLI tool")
    parser.add_argument("--file", required=True, help="Path to the JSON file")
    parser.add_argument(
        "--password", required=True, help="Encryption/Decryption password (in hex)"
    )
    parser.add_argument("--encrypt", action="store_true", help="Encrypt the JSON file")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the JSON file")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--key", help="Key path in the JSON file")
    parser.add_argument("--value", help="Value to update at the key path")
    parser.add_argument("--value-file", help="Path to the file containing the value")

    args = parser.parse_args()

    json_file_path = os.path.join(PROJECT_PATH, args.file)
    if not os.path.exists(json_file_path):
        raise FileNotFoundError(f'[ZIPLOC/ERROR] missing "{json_file_path}"')

    with open(json_file_path, "r") as f:
        json_data = json.load(f)

    output_path = (
        os.path.join(PROJECT_PATH, args.output) if args.output else json_file_path
    )

    if args.encrypt or args.decrypt:
        processed_json = process_json(json_data, args.password, args.encrypt)
        with open(output_path, "w") as f:
            json.dump(processed_json, f, indent=2)
        print(f"[ZIPLOC] successfully {'encrypted' if args.encrypt else 'decrypted'}")
        return

    if args.key:
        key_path_parts = args.key.split(".")

        if args.value or args.value_file:
            value = args.value
            if args.value_file:
                with open(args.value_file, "r") as f:
                    value = f.read().strip()

            entry = json_data
            for part in key_path_parts[:-1]:
                entry = entry.setdefault(part, {})
            entry[key_path_parts[-1]] = encrypt(value, args.password)

            with open(output_path, "w") as f:
                json.dump(json_data, f, indent=2)

            decrypted_value = decrypt(entry[key_path_parts[-1]], args.password)
            print(f'[ZIPLOC] "{args.key}" updated to "{decrypted_value}"')
        else:
            entry = json_data
            for part in key_path_parts:
                entry = entry.get(part)
                if entry is None:
                    raise KeyError(f'[ZIPLOC/ERROR] missing "{part}"')

            print(decrypt(entry, args.password))


if __name__ == "__main__":
    main()
