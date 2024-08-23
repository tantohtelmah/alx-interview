#!/usr/bin/python3
"""
Main file for testing
"""


def validUTF8(data):
    """ Initialize a variable to keep track of the expected number of bytes"""
    expected_bytes = 0

    for byte in data:
        # Check if it's a continuation byte (starts with '10')
        if expected_bytes > 0:
            if (byte >> 6) != 0b10:
                return False
            expected_bytes -= 1
        else:
            # Determine the number of expected bytes based on the first byte
            if byte >> 7 == 0:
                # Single-byte character
                expected_bytes = 0
            elif byte >> 5 == 0b110:
                # Two-byte character
                expected_bytes = 1
            elif byte >> 4 == 0b1110:
                # Three-byte character
                expected_bytes = 2
            elif byte >> 3 == 0b11110:
                # Four-byte character
                expected_bytes = 3
            else:
                # Invalid start byte
                return False

    # Ensure all expected bytes were consumed
    return expected_bytes == 0
