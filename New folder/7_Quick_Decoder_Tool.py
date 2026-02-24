"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║            TCS HACKQUEST - QUICK DECODER TOOL                                    ║
║                    Use This During the Exam!                                      ║
╚══════════════════════════════════════════════════════════════════════════════════╝

This is a utility tool you can use during the competition.
Run it and quickly decode/encode data without switching to websites!
"""

import base64
import hashlib
import binascii
import codecs
import urllib.parse

def print_menu():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    QUICK DECODER TOOL                                            ║
╚══════════════════════════════════════════════════════════════════════════════════╝

  ENCODING/DECODING:
  1.  Base64 Decode          2.  Base64 Encode
  3.  Hex to ASCII           4.  ASCII to Hex
  5.  Binary to ASCII        6.  ASCII to Binary
  7.  URL Decode             8.  URL Encode
  9.  ROT13                  10. Caesar Bruteforce (all 26 shifts)
  11. XOR Single-byte Brute  12. XOR with Key
  
  HASHING:
  13. Generate MD5           14. Generate SHA1
  15. Generate SHA256
  
  UTILITIES:
  16. Reverse String         17. Character Codes (ASCII values)
  18. Magic Decode (Auto)    19. Multi-layer Decode
  
  0.  Exit
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    DECODING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════════

def base64_decode():
    print("\n📦 BASE64 DECODE")
    data = input("Enter Base64 string: ").strip()
    try:
        # Try multiple times for nested Base64
        result = data
        decode_count = 0
        while True:
            try:
                decoded = base64.b64decode(result).decode('utf-8', errors='replace')
                if decoded == result:
                    break
                result = decoded
                decode_count += 1
                print(f"  Decode #{decode_count}: {result}")
            except:
                break
        print(f"\n✅ Final Result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")

def base64_encode():
    print("\n📦 BASE64 ENCODE")
    data = input("Enter text to encode: ")
    result = base64.b64encode(data.encode()).decode()
    print(f"\n✅ Result: {result}")

def hex_to_ascii():
    print("\n🔢 HEX TO ASCII")
    data = input("Enter hex string (with or without spaces): ").strip()
    # Remove common separators
    data = data.replace(" ", "").replace("\\x", "").replace("0x", "").replace(":", "")
    try:
        result = bytes.fromhex(data).decode('utf-8', errors='replace')
        print(f"\n✅ Result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")

def ascii_to_hex():
    print("\n🔢 ASCII TO HEX")
    data = input("Enter text: ")
    result = data.encode().hex()
    spaced = ' '.join(result[i:i+2] for i in range(0, len(result), 2))
    print(f"\n✅ Result (no spaces): {result}")
    print(f"✅ Result (with spaces): {spaced}")

def binary_to_ascii():
    print("\n💻 BINARY TO ASCII")
    data = input("Enter binary (space-separated or continuous): ").strip()
    try:
        # Handle both formats
        if ' ' in data:
            bytes_list = data.split()
        else:
            # Split into 8-bit chunks
            bytes_list = [data[i:i+8] for i in range(0, len(data), 8)]
        
        result = ''.join(chr(int(b, 2)) for b in bytes_list if b)
        print(f"\n✅ Result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")

def ascii_to_binary():
    print("\n💻 ASCII TO BINARY")
    data = input("Enter text: ")
    result = ' '.join(format(ord(c), '08b') for c in data)
    print(f"\n✅ Result: {result}")

def url_decode():
    print("\n🌐 URL DECODE")
    data = input("Enter URL-encoded string: ")
    result = urllib.parse.unquote(data)
    print(f"\n✅ Result: {result}")

def url_encode():
    print("\n🌐 URL ENCODE")
    data = input("Enter text: ")
    result = urllib.parse.quote(data)
    print(f"\n✅ Result: {result}")

def rot13():
    print("\n🔄 ROT13")
    data = input("Enter text: ")
    result = codecs.encode(data, 'rot_13')
    print(f"\n✅ Result: {result}")

def caesar_bruteforce():
    print("\n🔓 CAESAR BRUTEFORCE (All 26 shifts)")
    data = input("Enter ciphertext: ")
    print("\n" + "-"*60)
    
    for shift in range(26):
        result = ""
        for char in data:
            if char.isalpha():
                offset = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - offset - shift) % 26 + offset)
            else:
                result += char
        
        # Highlight if it contains common words
        highlight = ""
        lower = result.lower()
        if any(word in lower for word in ['flag', 'hq10', 'the', 'password', 'secret', 'key']):
            highlight = " ⭐ POSSIBLE MATCH!"
        
        print(f"Shift {shift:2d}: {result}{highlight}")

def xor_bruteforce():
    print("\n🔐 XOR SINGLE-BYTE BRUTEFORCE")
    print("Enter data format:")
    print("  1. Hex string (e.g., 4a5b6c)")
    print("  2. Decimal bytes (e.g., 74,91,108)")
    print("  3. Raw text")
    
    fmt = input("Choose (1/2/3): ").strip()
    data_input = input("Enter data: ").strip()
    
    try:
        if fmt == "1":
            data = bytes.fromhex(data_input.replace(" ", ""))
        elif fmt == "2":
            data = bytes([int(x.strip()) for x in data_input.split(",")])
        else:
            data = data_input.encode()
        
        print("\n" + "-"*60)
        print("Showing results containing printable ASCII:\n")
        
        found_any = False
        for key in range(256):
            decrypted = bytes([b ^ key for b in data])
            try:
                text = decrypted.decode('ascii')
                if text.isprintable() or 'flag' in text.lower():
                    found_any = True
                    highlight = ""
                    if any(word in text.lower() for word in ['flag', 'hq10', 'password', 'secret']):
                        highlight = " ⭐ POSSIBLE MATCH!"
                    print(f"Key {key:3d} (0x{key:02X}): {text}{highlight}")
            except:
                pass
        
        if not found_any:
            print("No fully printable results found. Showing all:")
            for key in range(256):
                decrypted = bytes([b ^ key for b in data])
                text = ''.join(chr(b) if 32 <= b < 127 else '.' for b in decrypted)
                print(f"Key {key:3d}: {text}")
                
    except Exception as e:
        print(f"❌ Error: {e}")

def xor_with_key():
    print("\n🔐 XOR WITH KEY")
    print("Enter data format:")
    print("  1. Hex string")
    print("  2. Decimal bytes")
    print("  3. Raw text")
    
    fmt = input("Data format (1/2/3): ").strip()
    data_input = input("Enter data: ").strip()
    key_input = input("Enter key (text or hex with 0x prefix): ").strip()
    
    try:
        if fmt == "1":
            data = bytes.fromhex(data_input.replace(" ", ""))
        elif fmt == "2":
            data = bytes([int(x.strip()) for x in data_input.split(",")])
        else:
            data = data_input.encode()
        
        if key_input.startswith("0x"):
            key = bytes.fromhex(key_input[2:])
        else:
            key = key_input.encode()
        
        result = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
        
        print(f"\n✅ Result (text): {result.decode('utf-8', errors='replace')}")
        print(f"✅ Result (hex): {result.hex()}")
    except Exception as e:
        print(f"❌ Error: {e}")

def generate_md5():
    print("\n#️⃣ MD5 HASH")
    data = input("Enter text: ")
    result = hashlib.md5(data.encode()).hexdigest()
    print(f"\n✅ MD5: {result}")

def generate_sha1():
    print("\n#️⃣ SHA1 HASH")
    data = input("Enter text: ")
    result = hashlib.sha1(data.encode()).hexdigest()
    print(f"\n✅ SHA1: {result}")

def generate_sha256():
    print("\n#️⃣ SHA256 HASH")
    data = input("Enter text: ")
    result = hashlib.sha256(data.encode()).hexdigest()
    print(f"\n✅ SHA256: {result}")

def reverse_string():
    print("\n↩️ REVERSE STRING")
    data = input("Enter text: ")
    print(f"\n✅ Reversed: {data[::-1]}")

def character_codes():
    print("\n📊 CHARACTER CODES")
    data = input("Enter text: ")
    print("\n" + "-"*60)
    print(f"{'Char':<6} {'Dec':<6} {'Hex':<6} {'Binary':<10}")
    print("-"*60)
    for c in data:
        print(f"{repr(c):<6} {ord(c):<6} 0x{ord(c):02X}   {format(ord(c), '08b')}")

def magic_decode():
    print("\n🪄 MAGIC DECODE (Auto-detect)")
    data = input("Enter unknown data: ").strip()
    
    print("\n" + "="*60)
    print("Attempting various decodings...")
    print("="*60)
    
    results = []
    
    # Try Base64
    try:
        decoded = base64.b64decode(data).decode('utf-8', errors='ignore')
        if decoded and decoded.isprintable():
            results.append(("Base64", decoded))
    except:
        pass
    
    # Try Hex
    try:
        clean = data.replace(" ", "").replace("\\x", "").replace("0x", "")
        if all(c in '0123456789abcdefABCDEF' for c in clean) and len(clean) % 2 == 0:
            decoded = bytes.fromhex(clean).decode('utf-8', errors='ignore')
            if decoded:
                results.append(("Hex", decoded))
    except:
        pass
    
    # Try Binary
    try:
        clean = data.replace(" ", "")
        if all(c in '01' for c in clean) and len(clean) % 8 == 0:
            bytes_list = [clean[i:i+8] for i in range(0, len(clean), 8)]
            decoded = ''.join(chr(int(b, 2)) for b in bytes_list)
            if decoded:
                results.append(("Binary", decoded))
    except:
        pass
    
    # Try URL decode
    try:
        if '%' in data:
            decoded = urllib.parse.unquote(data)
            if decoded != data:
                results.append(("URL", decoded))
    except:
        pass
    
    # Try ROT13
    try:
        decoded = codecs.encode(data, 'rot_13')
        lower = decoded.lower()
        if any(word in lower for word in ['flag', 'the', 'and', 'password']):
            results.append(("ROT13", decoded))
    except:
        pass
    
    # Try decimal ASCII
    try:
        if ',' in data or ' ' in data:
            nums = [int(x.strip()) for x in data.replace(',', ' ').split() if x.strip().isdigit()]
            if all(0 <= n < 256 for n in nums):
                decoded = ''.join(chr(n) for n in nums)
                if decoded:
                    results.append(("Decimal ASCII", decoded))
    except:
        pass
    
    if results:
        for encoding, decoded in results:
            print(f"\n✅ {encoding}: {decoded}")
    else:
        print("\n❌ Could not auto-detect encoding. Try manual options.")

def multi_layer_decode():
    print("\n🔄 MULTI-LAYER DECODE")
    print("Keep decoding until you get readable text")
    print("Enter 'q' to quit\n")
    
    data = input("Enter initial data: ").strip()
    
    while True:
        print(f"\nCurrent: {data[:100]}{'...' if len(data) > 100 else ''}")
        print("\nApply which decoding?")
        print("  1. Base64  2. Hex  3. ROT13  4. URL  5. Reverse")
        print("  6. Binary  7. Done/Quit")
        
        choice = input("Choice: ").strip()
        
        try:
            if choice == "1":
                data = base64.b64decode(data).decode('utf-8', errors='replace')
            elif choice == "2":
                clean = data.replace(" ", "").replace("\\x", "").replace("0x", "")
                data = bytes.fromhex(clean).decode('utf-8', errors='replace')
            elif choice == "3":
                data = codecs.encode(data, 'rot_13')
            elif choice == "4":
                data = urllib.parse.unquote(data)
            elif choice == "5":
                data = data[::-1]
            elif choice == "6":
                clean = data.replace(" ", "")
                bytes_list = [clean[i:i+8] for i in range(0, len(clean), 8)]
                data = ''.join(chr(int(b, 2)) for b in bytes_list)
            elif choice == "7" or choice.lower() == "q":
                break
                
            print(f"\n✅ Result: {data}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print(f"\n📋 FINAL RESULT: {data}")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════════════════════════

def main():
    functions = {
        "1": base64_decode,
        "2": base64_encode,
        "3": hex_to_ascii,
        "4": ascii_to_hex,
        "5": binary_to_ascii,
        "6": ascii_to_binary,
        "7": url_decode,
        "8": url_encode,
        "9": rot13,
        "10": caesar_bruteforce,
        "11": xor_bruteforce,
        "12": xor_with_key,
        "13": generate_md5,
        "14": generate_sha1,
        "15": generate_sha256,
        "16": reverse_string,
        "17": character_codes,
        "18": magic_decode,
        "19": multi_layer_decode,
    }
    
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()
        
        if choice == "0":
            print("\nGood luck! 🍀\n")
            break
        elif choice in functions:
            functions[choice]()
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
