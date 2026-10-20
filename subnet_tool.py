#!/usr/bin/env python3
"""Display useful IPv4 subnet details using Python's standard library."""

import argparse
import ipaddress
import sys


def describe_network(value: str) -> dict[str, str | int]:
    """Parse an IPv4 interface/CIDR and return common network properties."""
    interface = ipaddress.ip_interface(value)
    if interface.version != 4:
        raise ValueError("This starter tool currently supports IPv4 only.")

    network = interface.network
    return {
        "Input": str(interface),
        "Network": str(network),
        "Netmask": str(network.netmask),
        "Broadcast": str(network.broadcast_address),
        "Usable host count": network.num_addresses - (2 if network.prefixlen <= 30 else 0),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cidr", help="IPv4 address with prefix, e.g. 192.0.2.10/24")
    args = parser.parse_args()

    try:
        details = describe_network(args.cidr)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    for label, value in details.items():
        print(f"{label + ':':20} {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
