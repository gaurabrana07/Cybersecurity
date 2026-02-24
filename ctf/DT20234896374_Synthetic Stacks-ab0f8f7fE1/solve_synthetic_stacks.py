"""
Synthetic Stacks CTF Challenge Solver
=====================================
This script automatically extracts the hidden flag from the multi-layered vault.

Challenge: Synthetic Stacks - 300 points
Description: Corporations store their darkest secrets inside digital vaults - 
             layered, encrypted, and disguised as harmless files.
"""

import os
import sys
import base64
import subprocess
import tempfile

def print_banner():
    pass

def step1_identify_file_type(file_path):
    """
    STEP 1: Identify the true file type
    The .txt file is actually a 7-Zip archive in disguise
    """
    with open(file_path, 'rb') as f:
        magic_bytes = f.read(6)
    
    # 7-Zip magic bytes: 37 7A BC AF 27 1C
    seven_zip_magic = bytes([0x37, 0x7A, 0xBC, 0xAF, 0x27, 0x1C])
    
    if magic_bytes == seven_zip_magic:
        return "7z"
    else:
        return None

def step2_extract_archive(file_path, output_dir, password=None):
    """
    STEP 2: Extract the 7-Zip archive
    The archive may or may not be password protected
    """
    # Common passwords to try (including filename patterns)
    passwords_to_try = [
        "",  # No password
        os.path.splitext(os.path.basename(file_path))[0],  # Filename without extension
        "password",
        "123456",
        "flag",
        "secret",
        "vault",
        "synthetic",
        "stacks",
    ]
    
    seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"
    
    if not os.path.exists(seven_zip_path):
        print("ERROR: 7-Zip not found")
        return None
    
    os.makedirs(output_dir, exist_ok=True)
    
    for pwd in passwords_to_try:
        try:
            cmd = [seven_zip_path, 'x', file_path, f'-o{output_dir}', '-y']
            if pwd:
                cmd.append(f'-p{pwd}')
            else:
                cmd.append('-p')  # Empty password
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                extracted_files = os.listdir(output_dir)
                return extracted_files
        except Exception as e:
            continue
    
    return None

def step3_decode_base64(file_path):
    """
    STEP 3: Decode Base64 encoded content
    The extracted file contains Base64 encoded PNG data
    """
    with open(file_path, 'r') as f:
        content = f.read().strip()
    
    # Check if it's Base64 encoded PNG (starts with iVBORw0KGgo)
    if content.startswith('iVBORw0KGgo'):
        try:
            decoded_bytes = base64.b64decode(content)
            return decoded_bytes
        except Exception as e:
            return None
    else:
        return None

def step4_decode_qr_code(image_bytes, output_path):
    """
    STEP 4: Decode QR code from PNG image
    The PNG image contains a QR code with the flag
    """
    # Save the image temporarily
    with open(output_path, 'wb') as f:
        f.write(image_bytes)
    
    try:
        import cv2
        
        img = cv2.imread(output_path)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        
        if data:
            return data
        else:
            return None
    except ImportError:
        print("ERROR: OpenCV not installed")
        return None

def main():
    print_banner()
    
    # Configuration
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "ab0f8f7fE1.txt")
    extract_dir = os.path.join(script_dir, "extracted_by_solver")
    
    if not os.path.exists(input_file):
        print("ERROR: Input file not found")
        sys.exit(1)
    
    # STEP 1: Identify file type
    file_type = step1_identify_file_type(input_file)
    if file_type != "7z":
        sys.exit(1)
    
    # STEP 2: Extract archive
    extracted_files = step2_extract_archive(input_file, extract_dir)
    if not extracted_files:
        sys.exit(1)
    
    # STEP 3: Decode Base64
    extracted_file = os.path.join(extract_dir, extracted_files[0])
    image_bytes = step3_decode_base64(extracted_file)
    if not image_bytes:
        sys.exit(1)
    
    # STEP 4: Decode QR code
    qr_image_path = os.path.join(extract_dir, "qr_code.png")
    flag_data = step4_decode_qr_code(image_bytes, qr_image_path)
    
    # Print results
    if flag_data:
        # Extract just the flag
        if "HQX{" in flag_data:
            flag_start = flag_data.index("HQX{")
            flag_end = flag_data.index("}", flag_start) + 1
            flag = flag_data[flag_start:flag_end]
            print(f"FLAG: {flag}")
        else:
            print(f"FLAG: {flag_data}")

if __name__ == "__main__":
    main()
