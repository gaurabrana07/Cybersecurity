#!/usr/bin/env python3
"""
PDF Hidden Flag Extractor
CTF Challenge: Paper Scripts - 300
"""

import re
import os

def extract_flag_from_pdf(pdf_path):
    """Extract hidden flag from PDF JavaScript objects."""
    
    with open(pdf_path, 'rb') as f:
        content = f.read()
    
    # Search for JavaScript action objects - the JS is between /JS ( and ) >>
    js_pattern = rb'/JS\s*\((.*?)\)\s*\n>>'
    matches = re.findall(js_pattern, content, re.DOTALL)
    
    flags_found = []
    
    for match in matches:
        decoded = match.decode('latin-1', errors='ignore')
        
        # PDF uses octal escapes: \134 = backslash, so \134x48 = \x48
        # First convert \134 to backslash
        decoded = decoded.replace('\\134', '\\')
        
        # Now find hex escape patterns \x## 
        hex_pattern = r'\\x([0-9a-fA-F]{2})'
        hex_chars = re.findall(hex_pattern, decoded)
        
        if hex_chars:
            # Convert hex to characters
            result = ''.join(chr(int(h, 16)) for h in hex_chars)
            
            # Look for flag pattern HQX{...}
            flag_match = re.search(r'HQX\{[a-f0-9]+\}', result)
            if flag_match:
                flags_found.append(flag_match.group())
    
    return flags_found


def generate_report(pdf_path, flags):
    """Generate bullet-point methodology report."""
    
    report = f"""CTF: Paper Scripts - 300
Target: {os.path.basename(pdf_path)}

METHODOLOGY
-----------
• Opened PDF in binary mode
• Located JavaScript action object
• Decoded octal escapes
• Decoded hex escapes to ASCII
• Reconstructed flag string

FLAG
----
"""
    
    if flags:
        for flag in flags:
            report += f"• {flag}\n"
    else:
        report += "• No flag found\n"
    
    return report


def main():
    pdf_path = r"c:\Users\GAURAB\Downloads\DT20234896374_Paper Scripts-AB8e5416e3\AB8e5416e3.pdf"
    
    flags = extract_flag_from_pdf(pdf_path)
    report = generate_report(pdf_path, flags)
    print(report)
    
    report_path = os.path.join(os.path.dirname(pdf_path), "extraction_report.txt")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)


if __name__ == "__main__":
    main()
