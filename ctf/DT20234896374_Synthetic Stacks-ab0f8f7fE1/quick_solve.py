import os, base64, subprocess, cv2

file = r'c:\Users\GAURAB\Downloads\DT20234896374_Synthetic Stacks-ab0f8f7fE1\ab0f8f7fE1.txt'
out = r'c:\Users\GAURAB\Downloads\DT20234896374_Synthetic Stacks-ab0f8f7fE1\temp_extract'

print('='*50)
print('SYNTHETIC STACKS - FLAG CAPTURE')
print('='*50)

# Step 1
with open(file, 'rb') as f: magic = f.read(6)
print(f'\n[1] File Type: 7-Zip Archive')
print(f'    Magic Bytes: {" ".join(f"{b:02X}" for b in magic)}')

# Step 2
os.makedirs(out, exist_ok=True)
subprocess.run([r'C:\Program Files\7-Zip\7z.exe', 'x', file, f'-o{out}', '-p123456', '-y'], capture_output=True)
print(f'[2] Archive Password: 123456')

# Step 3
with open(f'{out}\\hq.txt', 'r') as f: b64 = f.read().strip()
png = base64.b64decode(b64)
print(f'[3] Hidden File: Base64 encoded PNG')

# Step 4
png_path = f'{out}\\qr.png'
with open(png_path, 'wb') as f: f.write(png)
img = cv2.imread(png_path)
data, _, _ = cv2.QRCodeDetector().detectAndDecode(img)
flag = data[data.index('HQX{'):data.index('}')+1]

print(f'[4] QR Code: Contains the flag')
print()
print('='*50)
print(f'FLAG: {flag}')
print('='*50)
