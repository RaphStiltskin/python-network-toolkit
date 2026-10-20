#!/usr/bin/env python3
"""Check a CSV device inventory for missing fields and duplicate IPv4 addresses."""

import argparse
import csv
import ipaddress
import sys
from collections import Counter
from pathlib import Path

REQUIRED_FIELDS = ("hostname", "ip_address", "device_type", "location")


def check_inventory(path: Path) -> list[str]:
    findings: list[str] = []
    rows: list[dict[str, str]] = []

    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        missing_headers = [field for field in REQUIRED_FIELDS if field not in (reader.fieldnames or [])]
        if missing_headers:
            return [f"Missing required CSV column(s): {', '.join(missing_headers)}"]

        for line_number, raw_row in enumerate(reader, start=2):
            row = {key: (value or "").strip() for key, value in raw_row.items() if key}
            rows.append(row)
            for field in REQUIRED_FIELDS:
                if not row.get(field):
                    findings.append(f"Line {line_number}: '{field}' is empty.")

            address = row.get("ip_address", "")
            if address:
                try:
                    if ipaddress.ip_address(address).version != 4:
                        findings.append(f"Line {line_number}: '{address}' is not IPv4.")
                except ValueError:
                    findings.append(f"Line {line_number}: '{address}' is not a valid IP address.")

    valid_addresses = []
    for row in rows:
        address = row.get("ip_address", "")
        try:
            if ipaddress.ip_address(address).version == 4:
                valid_addresses.append(address)
        except ValueError:
            pass

    counts = Counter(valid_addresses)
    for address, count in sorted(counts.items()):
        if count > 1:
            findings.append(f"Duplicate IPv4 address '{address}' appears {count} times.")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path, help="Path to inventory CSV")
    args = parser.parse_args()

    try:
        findings = check_inventory(args.csv_file)
    except OSError as exc:
        print(f"Could not read file: {exc}", file=sys.stderr)
        return 2

    if findings:
        print(f"Found {len(findings)} finding(s):")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Inventory check passed: required fields are populated and IPv4 addresses are valid and unique.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
