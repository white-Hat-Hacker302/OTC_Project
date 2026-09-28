#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=====================================================
  SCAM MESSAGE ANALYZER
  Developed by: Cyber Security Engineer Mr. Sabaz Ali Khan
  Purpose: SMS / WhatsApp / Email messages mein scam
           ki nishaniyan (red flags) detect aur samjhana.
  Language: Roman Urdu (Hindi-English mix)
=====================================================
"""

import re
import sys
from datetime import datetime

# ---------------- BANNER ----------------
BANNER = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⡈⠐⠠⢁⠂⠐⢀⣾⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠿⣷⡄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⠠⢁⠂⠄⠀⣛⠀⡟⢁⣠⣄⠀⠀⠀⠙⢻⡟⠉⠀⠀⢀⣴⣦⣬⠃⣬⣅⠀⢂⠐⡀⢂⠐⠠⠀⠄⠠⠀⠄⠠⢀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡁⢂⠈⠀⠾⡛⢱⡿⢿⣿⣿⣿⣦⣄⣠⣼⣷⣤⣤⣶⠿⠿⢿⣟⠆⢉⡛⠆⠀⢂⠐⠠⠈⠄⠡⠈⠄⠡⢈⠐⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡐⢀⠂⢠⣾⡟⣸⣰⡿⠁⠀⠀⠙⣿⡇⣿⣿⠸⣿⠁⢀⣀⣀⣙⡸⠎⢿⡆⠀⠂⠌⠠⠁⠌⠠⠁⠌⡐⢀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⠀⠟⡸⢛⣤⣼⣿⣿⣿⣤⣼⠇⣿⣿⠀⢧⣿⣿⣿⣿⣿⣿⣧⣄⠃⠀⢃⠘⡀⢃⠘⡀⠃⠄⠠⢀⠘⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢂⠡⠈⠄⢈⡾⠋⢹⣿⣿⣿⣿⡟⢡⣴⣿⣿⣷⣦⡙⢿⣿⣿⣿⣿⠀⠙⠀⠈⡀⢂⠐⡀⠂⠄⠡⢈⠐⡀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠄⢂⠡⠀⢸⠀⠀⢸⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⡇⠸⢿⣿⣿⡟⠀⠀⠀⠀⡐⢀⠂⠄⠡⢈⠐⡀⢂⠐⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠄⡐⠠⠀⠀⠀⠀⠙⠋⠉⠀⠀⠉⠉⠙⠛⠋⠉⠀⠀⠀⠀⠁⠀⠀⠀⠀⢀⠐⠠⠈⠄⡁⢂⠐⡀⠂⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢈⠐⠠⠁⠄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢀⣀⠀⠀⢀⠂⠌⠠⢁⠂⡐⢀⠂⠄⠡⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⠈⠄⠡⢈⠐⡀⠸⣿⣦⡀⠀⠀⠛⠒⠚⠛⠛⠛⠛⠀⢀⣴⣿⠃⠀⠌⡀⠂⠌⡐⢀⠂⡐⠠⠈⠄⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠡⢈⠐⡀⠂⠄⠀⢻⣿⣿⣷⣶⣦⣤⣤⣤⣤⣤⣶⣾⣿⣿⡿⠀⠐⠠⢀⠁⢂⠐⡀⠂⠄⠡⢈⠐⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⡐⢀⠂⠄⠡⠈⠄⠘⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⡿⠃⠀⠌⡐⠠⠈⠄⠂⠄⠡⢈⠐⠠⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡐⠠⠈⠄⠡⢈⠐⠀⠀⠙⠃⣿⣿⣿⣿⣿⣿⣿⣿⡗⠋⠀⣤⠀⠀⠀⠡⠈⠄⠡⢈⠐⠠⠈⠄⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠄⠡⠈⠄⡁⠂⠀⠀⣤⡀⠀⢻⣿⣿⣿⣿⣿⣿⣿⠇⣠⣾⣿⠀⣰⠀⠀⠀⣈⡀⠀⠈⠀⠁⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡈⠄⠁⠂⠀⠀⠀⠀⢻⣿⣷⠬⠉⠉⠉⠉⠉⠉⠀⠚⢿⣿⣿⢀⣿⡀⠀⠀⢹⣿⣿⣿⣿⣶⡶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⢸⣧⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣾⣿⡇⠀⠁⠀⢻⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣟⡿⠀⠀⠀⠀⣿⣿⣦⠘⣿⣶⠖⣠⠆⠀⠀⢳⣤⡙⢿⣟⣼⣿⣿⡇⠀⠐⡀⠈⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⠃⠀⠀⠀⠀⢿⣿⣿⣷⣌⣿⣾⠏⠀⡀⠀⠸⡿⠿⠾⠿⠿⠿⠿⠷⠀⠀⠄⠀⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢠⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢠⠀⡄⣴⠀⠀⡄⠐⠀⠀⢻⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠠⠀⠀⠀⠀⢀⠀⠠⠀⠄⢂⠐⠠⢈⠐⡈⠐⡀⢂⠐⠘⢷⡭⠂⠄⡁⢂⠀⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠐⠠⠈⡐⠠⠈⠄⠡⠈⠄⡈⠐⡀⠂⠄⠡⠐⠠⠨⠄⠆⠠⠌⠠⠐⠠⢀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡿⠿⠿⠀⣼⡿⠿⣿⡆⢠⣿⠿⢿⣷⠀⣼⡿⠿⣿⡆⢸⣿⠀⣿⡿⠿⠿⠀⠾⢿⣿⠿⠇⠘⣿⡄⣰⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣧⣤⡄⠀⢿⣧⣤⣤⡁⢨⣿⠀⢀⣿⠀⣿⡇⠀⠀⠁⢸⣿⠀⣿⣧⣤⡄⠀⠀⢸⣿⠀⠀⠀⠘⢿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡏⠁⠁⠀⣤⣍⣈⣿⡇⢸⣿⣀⣀⣿⠀⣿⣇⣀⣤⡄⢸⣿⠀⣿⣇⣉⣀⠀⠀⢸⣿⠀⠀⠀⠀⢸⣯⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⠃⠀⠀⠀⠙⠛⠛⠛⠁⠀⠛⠛⠛⠋⠀⠘⠛⠛⠛⠁⠘⠛⠀⠛⠛⠛⠛⠀⠀⠘⠛⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

CREDIT = """
=====================================================================
   SCAM MESSAGE ANALYZER v1.0
   Developed by: Cyber Security Engineer Mr. Sabaz Ali Khan
   Education Purpose Only - Stay Safe From Scammers!
=====================================================================
"""

# ---------------- SCAM RULES ----------------
# Har rule: (regex pattern, nishani/warning, risk score)
SCAM_RULES = [
    # 1. Paisa / Lottery Scams
    (r"(?i)\b(congratulations|jeet|winner|lucky draw|prize|lottery|jackpot|kbc)\b",
     "Lottery/Prize scam: Aap jeetay hain bina kisi entry ke - classic scam!", 25),

    # 2. Urgency / Threat
    (r"(?i)\b(urgent|immediately|foran|turant|24 hours|last chance|act now|expire|suspend|block ho jayega)\b",
     "Urgency tactic: Scammers aapko jaldi decision lene par majboor karte hain.", 20),

    # 3. OTP / PIN maangna
    (r"(?i)\b(otp|pin|password|cvv|one time password|verification code)\b",
     "OTP/PIN request: Koi bhi asli bank ya company OTP nahi maangta!", 30),

    # 4. Links (phishing)
    (r"https?://[^\s]+|bit\.ly|tinyurl|t\.co/\w+|\b[a-z0-9-]+\.xyz|\b[a-z0-9-]+\.top",
     "Suspicious link: Phishing website ho sakta hai - click na karein!", 20),

    # 5. Money transfer / KYC
    (r"(?i)\b(send money|transfer|paytm|google pay|upi|easypaisa|jazzcash|bank transfer|kyc|wallet)\b",
     "Money/KYC request: Paise ya KYC details ki demand scam ki bari nishani hai.", 20),

    # 6. Government / Authority impersonation
    (r"(?i)\b(fia|police|cyber crime|income tax|customs|fedex|dhl|courier parcel|rbi|state bank)\b",
     "Authority impersonation: Asli agencies kabhi SMS/WhatsApp par paisa nahi maangti.", 15),

    # 7. Jobs / Earn money
    (r"(?i)\b(work from home|earn \d+|part time job|easy money|investment|double your money|crypto|forex|bitcoin profit)\b",
     "Fake job/investment offer: 'Easy money' schemes hamesha fraud hoti hain.", 20),

    # 8. Too good to be true
    (r"(?i)\b(free|gift|iphone|prize money|refund|cashback|rs\.?\s*\d+[,\d]*(?:/|-| )(?:only|just))\b",
     "Too good to be true: Muft ka lalach scam ka sab se bara hathiyar hai.", 10),

    # 9. Emotional manipulation
    (r"(?i)\b(help|emergency|hospital|jaan ka khatra|bimari|need money|stuck abroad)\b",
     "Emotional manipulation: Fake emergency se paise nikalwane ki koshish.", 15),

    # 10.陌生 foreign numbers / weird chars
    (r"(?i)(vodafone|airtel|jio)-?(?:\s)*deadline|\bdear customer\b|\bdear user\b",
     "Generic greeting: 'Dear Customer' - asli companies aapka naam use karti hain.", 10),
]

# ---------------- ANALYSIS ENGINE ----------------
def analyze_message(message: str):
    findings = []
    total_score = 0

    for pattern, warning, score in SCAM_RULES:
        matches = re.findall(pattern, message, flags=re.IGNORECASE)
        if matches:
            matched_text = ", ".join(sorted(set(m if isinstance(m, str) else m[0] for m in matches)))[:60]
            findings.append({
                "warning": warning,
                "evidence": matched_text,
                "score": score
            })
            total_score += score

    # URL extraction for detail
    urls = re.findall(r"(?:https?://|www\.)[^\s]+", message)

    return findings, min(total_score, 100), urls

def risk_verdict(score: int) -> str:
    if score >= 60:
        return "[!!] HIGH RISK - Yeh message ALMOST PAKKA scam hai! Reply/delete karein."
    elif score >= 30:
        return "[!] MEDIUM RISK - Shak ki nishaniyan hain, careful rahein."
    elif score > 0:
        return "[?] LOW RISK - Thoray se suspicious elements hain."
    else:
        return "[OK] KOI SCAM NISHANI nahi mili - lekin phir bhi alert rahein!"

def print_report(message: str):
    print(CREDIT)
    print(f"\n[+] Analysis Time : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"[+] Message Length: {len(message)} characters\n")
    print("-" * 70)
    print(" ANALYSIS REPORT")
    print("-" * 70)

    findings, score, urls = analyze_message(message)

    if not findings:
        print("  (Koi suspicious pattern nahi mila)")
    else:
        for i, f in enumerate(findings, 1):
            print(f"\n  #{i} - RISK POINTS: {f['score']}")
            print(f"      Nishani  : {f['warning']}")
            print(f"      Evidence : {f['evidence']}")

    if urls:
        print(f"\n  [*] Mile hue links ({len(urls)}):")
        for u in urls[:5]:
            print(f"      -> {u}")
        print("      Tip: Link par click karne ke bajaye browser mein manually type karein.")

    print("-" * 70)
    print(f"  TOTAL SCAM SCORE : {score}/100")
    print(f"  VERDICT          : {risk_verdict(score)}")
    print("-" * 70)
    print("""
  SURAKSHA TIPS (Safety Tips):
   1. Kabhi OTP, PIN ya password share na karein.
   2. Unknown links par click na karein.
   3. Bank/Company ko official number se verify karein.
   4. 'Too good to be true' offers par shak karein.
   5. Report karein: FIA Cyber Crime (Pakistan) / Cybercrime.gov.in (India)
""")

# ---------------- MAIN ----------------
def main():
    print(BANNER)
    print(CREDIT)

    # File se ya direct input
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
            message = f.read()
        print(f"[+] File '{sys.argv[1]}' se message load kiya gaya.\n")
    else:
        print("Apna message paste karein (khatam karne ke liye khali line par ENTER dabayen):\n")
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip() == "":
                break
            lines.append(line)
        message = "\n".join(lines)

    if not message.strip():
        print("[-] Koi message enter nahi hua. Exit.")
        return

    print_report(message)

    while input("\nDoosra message check karna hai? (y/n): ").lower().startswith("y"):
        print("\nNaya message paste karein (khali line par ENTER = khatam):\n")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        if lines:
            print_report("\n".join(lines))

    print("\nShukriya! Stay Safe - Mr. Sabaz Ali Khan\n")

if __name__ == "__main__":
    main()
