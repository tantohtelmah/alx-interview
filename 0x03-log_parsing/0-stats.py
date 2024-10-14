#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

def print_stats():
    """ Prints the current statistics """

    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    """ Handles keyboard interruption """

    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Define the log line pattern
log_pattern = re.compile(
    r'^(?P<ip>[\d.]+) - \[.*?\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)$'
)

line_count = 0

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status = match.group('status')
            size = int(match.group('size'))

            total_size += size
            if status in status_counts:
                status_counts[status] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print_stats()
