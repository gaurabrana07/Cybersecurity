#!/usr/bin/env python3
"""
Address Abyss - CTF Challenge Solution
Extracts the hidden flag from network logs by parsing specific IP patterns.
"""

import re
from pathlib import Path


def extract_flag(log_file: str) -> str:
    """
    Extract the flag from IP logs by finding valid entries matching:
    - IPv4: 92.7.X.Y where X is index and Y is a single hex digit or character
    - IPv6-like: 2510:a1:X::Y where X (hex) is index and Y is the character
    """
    
    # Dictionary to store index -> character mappings
    flag_chars = {}
    
    # Read the log file
    with open(log_file, 'r') as f:
        lines = f.readlines()
    
    # Regex patterns for valid IPs
    # IPv4: 92.7.X.Y where Y is a single character (0-9, a-f)
    ipv4_pattern = re.compile(r'^92\.7\.(\d+)\.([0-9a-fA-F])$')
    
    # IPv6-like: 2510:a1:X::Y where X is hex index and Y is single character
    # Y can be hex digit or special chars like {, }
    ipv6_pattern = re.compile(r'^2510:a1:([0-9a-fA-F]+)::(.+)$')
    
    for line in lines:
        line = line.strip()
        
        # Check IPv4 pattern
        ipv4_match = ipv4_pattern.match(line)
        if ipv4_match:
            index = int(ipv4_match.group(1))
            char = ipv4_match.group(2)
            flag_chars[index] = char
            continue
        
        # Check IPv6-like pattern
        ipv6_match = ipv6_pattern.match(line)
        if ipv6_match:
            # Index is in hex
            index_hex = ipv6_match.group(1)
            char = ipv6_match.group(2)
            
            # Only consider entries where char is a single character
            if len(char) == 1:
                try:
                    index = int(index_hex, 16)
                    flag_chars[index] = char
                except ValueError:
                    continue
    
    # Build the flag by sorting indices
    if not flag_chars:
        return "No flag found!"
    
    max_index = max(flag_chars.keys())
    flag = ""
    
    for i in range(max_index + 1):
        if i in flag_chars:
            flag += flag_chars[i]
        else:
            flag += "?"  # Missing character
    
    return flag


def main():
    # Get the log file path
    script_dir = Path(__file__).parent
    log_file = script_dir / "ip_logs_50DF6ce4BF.txt"
    
    if not log_file.exists():
        print(f"Error: Log file not found at {log_file}")
        return
    
    flag = extract_flag(str(log_file))
    print(f"Flag: {flag}")


if __name__ == "__main__":
    main()
