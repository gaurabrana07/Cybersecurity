"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║            TCS HACKQUEST - EXAM DAY STRATEGY & TIPS                              ║
║                    Read This Before You Start!                                    ║
╚══════════════════════════════════════════════════════════════════════════════════╝

🎯 FINAL TIPS FOR TOMORROW - READ THIS ON EXAM DAY!
"""

print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    🎯 EXAM DAY STRATEGY & TIPS                                   ║
║                         TCS HACKQUEST ROUND 2                                    ║
╚══════════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ TIME MANAGEMENT (6-Hour Competition)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────────────┐
│  Phase          │  Time        │  Strategy                                      │
├─────────────────┼──────────────┼────────────────────────────────────────────────┤
│  First Pass     │  0-30 min    │  Read ALL challenges, solve EASY ones first    │
│  Easy Wins      │  30min-2hr   │  Complete Beginner challenges (encoding, etc)  │
│  Medium         │  2hr-4hr     │  Work on Intermediate challenges               │
│  Hard Attempts  │  4hr-5.5hr   │  Try Expert challenges                         │
│  Review         │  Last 30min  │  Check all submissions, retry stuck ones       │
└─────────────────┴──────────────┴────────────────────────────────────────────────┘

💡 GOLDEN RULE: If stuck for 15+ minutes, MOVE ON and come back later!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 POINT STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Points Distribution (typical):
  • Beginner: 50-100 points each
  • Intermediate: 150-250 points each  
  • Expert: 300-500 points each

STRATEGY:
  ✓ 5 Beginner challenges = 500 points (quick wins!)
  ✓ 3 Intermediate = 600 points (steady progress)
  ✓ 1 Expert = 400 points (bonus if you can)
  
  >> Solve ALL easy challenges before attempting hard ones!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 FIRST 5 MINUTES - SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before touching any challenge:

1. ✓ Open CyberChef in a browser tab: https://gchq.github.io/CyberChef
2. ✓ Open CrackStation: https://crackstation.net
3. ✓ Open dCode: https://www.dcode.fr
4. ✓ Keep your Quick_Decoder_Tool.py ready
5. ✓ Have Notepad ready for notes
6. ✓ Note the FLAG FORMAT: HQ10FLAG{...} or HQ10{...}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 CHALLENGE APPROACH CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For EVERY challenge, ask yourself:

□ What category is this? (Web, Crypto, Forensics, Stego, RE)
□ What is the input? (Text, File, URL, Image)
□ Is there a hint in the challenge name/description?
□ Have I seen something like this before?

ENCODING CHALLENGE:
  □ Does it look like Base64? (A-Za-z0-9+/=)
  □ Does it look like Hex? (0-9A-Fa-f, even length)
  □ Is it Caesar/ROT? (Shifted letters)
  □ Try CyberChef "Magic" operation!

WEB CHALLENGE:
  □ View page source (Ctrl+U)
  □ Check robots.txt
  □ Open DevTools (F12)
  □ Check cookies
  □ Try SQLi: ' OR '1'='1'--

FILE/IMAGE CHALLENGE:
  □ Run: strings filename | grep -i flag
  □ Run: exiftool filename
  □ Run: binwalk filename
  □ Run: file filename (check real type)
  □ Check file size (too big = hidden data)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ COMMON MISTAKES TO AVOID
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ DON'T:
  • Spend too long on one challenge (15 min max!)
  • Forget to try the obvious (view source, strings)
  • Submit flag without correct format
  • Panic if stuck
  • Ignore hints in challenge names
  • Skip easy challenges to try hard ones

✅ DO:
  • Read the challenge description CAREFULLY
  • Try simple things first (Base64, Hex, ROT13)
  • Check flag format before submitting
  • Take short breaks if frustrated
  • Keep notes of what you've tried
  • Ask: "What would the challenge creator expect?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 FLAG SUBMISSION TIPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Expected formats for TCS HackQuest Season 10:
  • HQ10FLAG{your_flag_here}
  • HQ10{your_flag_here}
  • flag{your_flag_here}

BEFORE SUBMITTING:
  □ Check for extra spaces (before/after)
  □ Check capitalization (flags are case-sensitive!)
  □ Check for special characters
  □ Try with and without curly braces
  □ If unsure, try: HQ10FLAG{yourflag} and HQ10{yourflag}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠️ QUICK REFERENCE COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Find flag in file
strings file.bin | grep -i flag
strings file.bin | grep -i "HQ10"

# Check file type
file unknown_file

# Extract metadata
exiftool image.jpg

# Find embedded files
binwalk -e suspicious.png

# Decode Base64
echo "encoded_string" | base64 -d

# Decode Hex
echo "48656c6c6f" | xxd -r -p

# Calculate hash
echo -n "text" | md5sum
echo -n "text" | sha256sum

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💪 MOTIVATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Remember:
  • You've prepared well! Trust your preparation.
  • Stay calm. Panic is your enemy.
  • Easy points are still points!
  • Every challenge has a solution - think logically.
  • If something seems too hard, it might be simpler than you think.

CTF MINDSET:
  "What is the most obvious thing I haven't tried yet?"
  "What would a challenge creator hide here?"
  "Have I checked the basics?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 PRE-EXAM CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Night Before:
  □ Get enough sleep (7-8 hours)
  □ Review cheatsheets one more time
  □ Make sure all tools are installed/accessible
  □ Test your internet connection
  □ Prepare snacks and water

Exam Day:
  □ Log in 15 minutes early
  □ Have Quick_Decoder_Tool.py ready
  □ Open all bookmarked websites
  □ Take deep breaths and stay calm
  □ START WITH EASY CHALLENGES!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║                    🍀 GOOD LUCK, GAURAB! 🍀                                      ║
║                                                                                  ║
║                You've got this! Trust your preparation!                          ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")

# Quick reference that can be printed
print("\n" + "="*80)
print("QUICK REFERENCE CARD (Screenshot this!)")
print("="*80)
print("""
┌─────────────────────────────────────────────────────────────────┐
│ ENCODING DETECTION:                                             │
│   Base64: A-Za-z0-9+/ with = padding                           │
│   Hex: 0-9A-F only, even length                                │
│   Binary: Only 0 and 1, groups of 8                            │
│   ROT13: Try if text looks like gibberish letters              │
├─────────────────────────────────────────────────────────────────┤
│ FIRST THINGS TO TRY:                                            │
│   1. CyberChef "Magic" (auto-detect)                           │
│   2. strings command on files                                  │
│   3. View source on web pages                                  │
│   4. exiftool on images                                        │
│   5. binwalk on suspicious files                               │
├─────────────────────────────────────────────────────────────────┤
│ SQL INJECTION:                                                  │
│   Login bypass: admin'--  OR  ' OR '1'='1'--                   │
│   UNION: ' UNION SELECT null,null,null--                       │
├─────────────────────────────────────────────────────────────────┤
│ FILE SIGNATURES:                                                │
│   PNG: 89 50 4E 47 (.PNG)                                      │
│   JPEG: FF D8 FF                                               │
│   PDF: 25 50 44 46 (%PDF)                                      │
│   ZIP: 50 4B 03 04 (PK..)                                      │
├─────────────────────────────────────────────────────────────────┤
│ HASH LENGTHS:                                                   │
│   MD5: 32 chars | SHA1: 40 chars | SHA256: 64 chars            │
├─────────────────────────────────────────────────────────────────┤
│ URLS:                                                           │
│   CyberChef: gchq.github.io/CyberChef                          │
│   CrackStation: crackstation.net                               │
│   dCode: dcode.fr                                              │
└─────────────────────────────────────────────────────────────────┘
""")

input("\nPress Enter to exit and GO WIN! 🏆")
