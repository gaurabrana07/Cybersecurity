"""
Quiet Leak - Automated Solver
Extracts exfiltrated credentials from DNS-over-HTTPS traffic in pcap
"""

from scapy.all import rdpcap, Raw
import base64
import re

def solve(pcap_file):
    print("[*] Loading pcap file...")
    packets = rdpcap(pcap_file)
    
    print("[*] Searching for DNS-over-HTTPS exfiltration...")
    flag_parts = []
    
    for i, pkt in enumerate(packets):
        if not pkt.haslayer(Raw):
            continue
            
        data = pkt[Raw].load
        if b'POST /dns-query' not in data:
            continue
        
        # Extract base64 subdomain from DNS query
        body_start = data.find(b'\r\n\r\n') + 4
        body = data[body_start:]
        
        for j in range(len(body)):
            length = body[j]
            if 10 < length < 60:
                subdomain = body[j+1:j+1+length]
                try:
                    sub_str = subdomain.decode('ascii')
                    padded = sub_str + '=' * (4 - len(sub_str) % 4) if len(sub_str) % 4 else sub_str
                    decoded = base64.b64decode(padded).decode('utf-8')
                    
                    # Check for flag or hex data
                    if decoded.startswith('HQX{') or decoded.endswith('}'):
                        flag_parts.append((i, decoded, 'flag'))
                        print(f"    [+] Packet {i}: {decoded}")
                    elif re.match(r'^[a-f0-9]{8}$', decoded):
                        flag_parts.append((i, decoded, 'hex'))
                        print(f"    [+] Packet {i}: {decoded}")
                    elif decoded.startswith('EXFIL:'):
                        print(f"    [!] Packet {i}: {decoded}")
                    break
                except:
                    continue
    
    print("\n[*] Assembling flag...")
    
    # Sort by packet number and extract parts
    flag_parts.sort(key=lambda x: x[0])
    
    # Extract components
    start = ""
    end = ""
    middle = []
    
    for _, decoded, ptype in flag_parts:
        if decoded.startswith('HQX{'):
            start = decoded.replace('HQX{', '')
        elif decoded.endswith('}'):
            end = decoded.replace('}', '')
        elif ptype == 'hex':
            middle.append(decoded)
    
    # Assemble: start + middle[1] + middle[0] + end (based on correct order)
    flag = f"HQX{{{start}{middle[1]}{middle[0]}{end}}}"
    
    print(f"\n[*] FLAG: {flag}")
    return flag

if __name__ == "__main__":
    import sys
    pcap = sys.argv[1] if len(sys.argv) > 1 else "7C3dF59EAe.pcap"
    solve(pcap)
