#!/usr/bin/python3
import sys
from collections import defaultdict


def print_statistics(file_size, status_counts):
    """Print statistics based on file size and status code counts."""
    
    print(f"Total file size: {file_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def parse_line(line):
    """Parse a line of input and extract IP address, status code, and file size."""
    
    parts = line.split()
    if len(parts) != 10:
        return None, None
    ip_address, _, _, status_code_str, file_size_str = parts[:4] + [parts[6], parts[8]]
    try:
        status_code = int(status_code_str)
        file_size = int(file_size_str)
        return ip_address, (status_code, file_size)
    except ValueError:
        return None, None

file_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        ip_address, data = parse_line(line.strip())
        if data is not None:
            status_code, size = data
            file_size += size
            status_counts[status_code] += 1
            line_count += 1
        if line_count % 10 == 0:
            print_statistics(file_size, status_counts)
except KeyboardInterrupt:
    print_statistics(file_size, status_counts)
