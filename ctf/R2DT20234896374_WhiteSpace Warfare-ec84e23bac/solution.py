abc = open('ec84e23bac.txt', 'r', encoding='utf-8').read()

binary = ""
for char in abc:
    if ord(char) == 0x200C:      # Zero Width Non-Joiner
        binary += '0'
    elif ord(char) == 0x200B:    # Zero Width Joiner
        binary += '1'

flag = ""
for i in range(0, len(binary), 8):
    byte = binary[i:i+8]
    if len(byte) == 8:
        flag += chr(int(byte, 2))

print(flag)
