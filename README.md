# Python Network Toolkit

**Status:** Starter project — run the tests and validate the examples before describing it as completed.

A small, dependency-free Python toolkit for common network administration tasks. It demonstrates input validation, IPv4 subnet calculations, CSV inventory validation, and basic automated testing.

## Features

- Validate IPv4 addresses and CIDR notation.
- Calculate network address, broadcast address, subnet mask, and usable host count.
- Validate a simple CSV device inventory for missing or malformed fields and duplicate IP addresses.
- Includes unit tests using Python's built-in `unittest`.

## Requirements

- Python 3.10+
- No third-party dependencies

## Run

From this repository directory:

```bash
python subnet_tool.py 192.0.2.10/24
python inventory_check.py sample_inventory.csv
python -m unittest discover -s tests -v
```

Use `python3` instead of `python` where required by your operating system.

## Example

```text
$ python subnet_tool.py 192.0.2.10/24
Input:             192.0.2.10/24
Network:           192.0.2.0/24
Netmask:           255.255.255.0
Broadcast:         192.0.2.255
Usable host count: 254
```

## Sample data and safety

`sample_inventory.csv` uses documentation-only IP addresses from `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24`. Replace sample records only with data you are authorised to use, and do not commit company inventories.

## Suggested extensions

- Add IPv6 support.
- Add JSON output.
- Add a command-line option to export validation findings.
- Add tests for edge cases such as `/31` and `/32`.
- Add CI using GitHub Actions.

## Evidence to add after testing

Record the Python version, test command and result, a short explanation of one issue found, and a screenshot of the tool running with synthetic data.
