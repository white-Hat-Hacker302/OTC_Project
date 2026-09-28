#!/usr/bin/env python3
"""
============================================================
 PUBLIC FOOTPRINT AUDITOR
 Author: Cyber Security Engineer - Mr. Sabaz Ali Khan
 Purpose: Help individuals review their own publicly
          visible information and improve privacy.
============================================================
"""

import argparse
import concurrent.futures
import json
import os
import re
import socket
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime

# ---------------- Banner ----------------
BANNER = r"""
⣟⢯⣻⡝⣯⢻⡝⣯⢻⡝⣯⢻⡝⣯⢻⡝⣯⢻⡝⣯⢻⡝⣯⢻⡝⣯⢻⣝⣯⣻⣝⢯⣻⢭⣻⣝⣯⣝⢯⣏⢿⡹⣝⢯⡝⣯⡝⣯⡝⣯⡝⣯⠽⣭⢯⡽⣭⢯⠽⣭⠯⡽⣭⢯⡝
⣯⢏⡷⣽⡹⢯⣽⡹⢯⡽⣭⢯⡽⣞⢯⡽⣚⣧⢟⡞⣧⣟⠮⠗⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠓⠛⠽⢎⣟⢶⣛⡶⣽⢲⡻⣜⡻⣜⢧⡻⣜⡏⡿⣜⢯⡳⣝⢮⡽
⣯⢯⡽⢶⣛⣯⢶⣛⣯⢞⣧⠿⣼⣹⢮⣗⣻⡼⠟⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠺⢵⣫⢷⡹⢧⡻⣝⢮⡳⣝⢾⡱⣏⢾⡱⣏⢾⣱
⣟⡮⣟⣭⠷⣞⡽⣞⡼⣏⡾⣝⡧⣟⡾⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢯⣏⢷⡹⣎⢷⡹⣎⢷⡹⣎⢷⡹⣎⠷
⣯⢷⡻⣼⢻⡝⣾⡹⣞⡽⣞⢧⠟⠊⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣷⡹⢮⢷⡹⣎⢷⡹⣎⠷⣭⢻
⣟⡾⣝⣳⢯⣻⡼⣏⡷⣯⠟⠁⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⢹⣿⣿⣿⣟⣷⣉⠻⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠈⠻⡽⣎⢷⡹⣎⢷⣹⢻⡜⣯
⣟⡾⣹⢧⡿⣱⣟⣾⡽⠃⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣵⣿⣿⣿⣿⣿⢺⣿⣿⣿⣿⢮⣳⣖⡘⣿⣿⣟⣯⣿⣟⣿⣶⣄⠀⠀⠀⠀⠀⠀⠈⢻⢮⡽⣹⢎⡷⣫⢞⡵
⣯⡽⣛⣮⣽⣳⣿⠎⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣿⡿⢛⠿⠋⠙⠘⠛⠛⠿⣿⢯⣷⢳⡮⠼⣿⣿⣿⣟⣿⣻⣾⣟⣷⣄⠀⠀⠀⠀⠀⠀⠙⣾⣱⡻⣜⢧⡻⣼
⣧⢿⣻⠼⣧⣿⠇⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⣤⠃⠀⠀⠀⠀⠀⠀⠘⢧⠘⢇⢿⡃⣸⣿⣟⣿⡿⣿⣧⣿⣟⣿⣄⠀⠀⠀⠀⠀⠀⠘⣧⡻⣼⣛⢧⢧
⣟⡾⣭⢿⣿⠋⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣺⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠸⠃⠀⣯⣆⣧⣻⣿⡿⣿⣟⣷⣿⢾⣯⢿⣷⡀⠀⠀⠀⠀⠀⠘⣗⣧⣛⣮⢻
⡿⣼⣻⣿⠏⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⣁⡴⣷⠶⡤⠤⠤⠄⡤⠤⠴⣶⣶⢦⣹⠿⣿⣿⣿⣿⣿⢿⣿⣾⡿⣯⣿⣞⣿⡄⠀⠀⠀⠀⠀⠘⣶⢫⡞⣽
⣟⣷⣿⡟⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢹⢹⡼⣿⠷⣉⢎⣱⣉⠲⣉⠶⢿⢿⢀⣇⢈⣿⣿⣿⣿⣿⣿⣿⣾⢿⣟⣷⣿⣳⡿⡄⠀⠀⠀⠀⠀⢹⡳⣽⢳
⣿⣾⣿⠁⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣧⠘⠄⠑⠛⠓⠚⢚⠋⠀⠙⠒⠘⢛⠚⠈⠈⢢⣷⣿⣿⣿⣿⣾⣿⣻⣿⣟⣿⣾⣻⣽⣷⠀⠀⠀⠀⠀⠀⢿⣱⢯
⣿⣿⡟⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡷⢾⡀⠀⠀⠀⠐⠤⣒⠆⠀⠀⠀⠀⣴⣶⣿⢼⣧⣿⣿⣿⣿⣿⣿⣟⣿⣿⣾⣟⣷⡿⡇⠀⠀⠀⠀⠀⢸⣽⢺
⣿⣿⡇⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⢹⣷⡀⠀⠀⠠⠴⠶⠤⠄⠀⠀⣰⡿⣿⣿⣯⢻⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣽⣯⣿⢿⠀⠀⠀⠀⠀⠈⣞⣯
⣿⣿⠅⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡌⣿⣿⡦⡀⠀⠀⠋⠀⠀⠀⣾⣿⣧⢿⡘⣟⠇⣿⣿⣿⣿⣿⣿⣿⣽⣿⣾⣿⣽⣾⣿⠀⠀⠀⠀⠀⠀⡿⣼
⣿⣿⠂⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣾⣿⣿⣿⡇⢿⣿⡇⠈⢑⡚⣲⠖⠉⠀⣿⣟⡣⡻⡼⣷⡷⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⢿⣾⠀⠀⠀⠀⠀⠀⣟⣳
⣿⣿⡃⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⡿⣵⣿⣿⠇⠀⠀⠁⠀⠄⠀⠀⣿⣿⣿⡬⢸⣿⣿⣵⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣟⣳
⣿⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣯⣾⣿⣿⣻⠀⠀⠀⠀⠀⠀⠀⠀⠘⢛⣿⣷⣵⣝⠿⣿⡐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡟⠀⠀⠀⠀⠀⢠⢯⢷
⣿⣿⣷⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣵⣿⣿⣿⣿⣿⡄⠀⠀⢀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣾⣿⣷⣬⠷⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⢸⣻⢞
⣿⣿⣿⡆⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⡿⢟⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⡿⣏⢷⣫⢴⣨⣙⠻⢿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣟⣧⣟
⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢀⣾⣿⣿⣿⣿⣿⡿⣯⢗⣻⣎⢷⣻⡗⣮⢣⡍⢿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⣸⣛⡶⣽
⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠻⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠣⣿⣿⣿⣿⣿⢯⡿⣝⣯⢳⡞⣿⣿⣽⣳⡿⡼⡘⣿⣿⡿⠁⠀⠀⠀⠀⠀⢰⣯⠽⣞⡽
⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠙⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣽⡿⣽⣏⢾⣫⡽⣿⣿⣿⣿⢽⣱⢇⢻⠟⠀⠀⠀⠀⠀⠀⢠⣟⡞⣯⡽⣞
⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⠛⠛⢻⣿⣿⣿⠀⣿⣿⣿⣾⣯⡟⣷⡞⣯⢳⣽⣾⣿⣿⣿⣿⢻⣾⠈⠀⠀⠀⠀⠀⠀⢰⣿⢹⡞⣧⡟⣾
⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⡗⠒⠒⠒⠒⢲⣿⣿⣿⠀⣿⣿⣿⣽⣾⣟⡷⣽⠾⣽⣻⢿⣿⣿⣿⣯⠟⠁⠀⠀⠀⠀⠀⠀⣠⡿⣭⢷⡻⣼⢳⡽
⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣾⣿⣿⣿⣷⣯⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⢀⣼⣟⣳⡻⢮⣽⢳⡯⣽
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⢳⡞⣧⣟⣻⡼⣳⡽⣳
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⡿⣿⣿⡫⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣻⡼⢯⣽⢳⡾⣱⢯⣳⢽⣳
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⡟⣧⢷⣛⡿⡼⣏⡷⢯⣳⣏⡷⣫
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣻⢧⡿⣭⡟⣽⡞⣽⡽⣹⢯⣗⡾⣹⢷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣶⣾⣿⣿⣿⣟⢿⣚⣧⣟⢾⣳⡽⢧⣟⣧⢿⣹⠷⣾⣹⢯⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⡿⣿⣻⡽⣞⣭⢿⣻⣞⣞⣯⣳⢻⣻⡼⢾⣭⢷⡻⢧⣟⢾⣹
"""

SUBTITLE = """
  ============================================================
   PUBLIC FOOTPRINT AUDITOR  v1.0
   Author : Cyber Security Engineer - Mr. Sabaz Ali Khan
   Purpose: Review your own publicly visible information
            and improve your personal privacy.
  ============================================================
"""

# ---------------- Config ----------------
TIMEOUT = 10
HEADERS = {"User-Agent": "Mozilla/5.0 (PublicFootprintAuditor/1.0)"}

USERNAME_SITES = [
    # (site name, profile URL template, "found" indicator)
    ("GitHub",    "https://github.com/{u}",            None),
    ("Reddit",    "https://www.reddit.com/user/{u}",   None),
    ("Twitter/X", "https://x.com/{u}",                 None),
    ("Instagram", "https://www.instagram.com/{u}/",    None),
    ("Facebook",  "https://www.facebook.com/{u}",      None),
    ("TikTok",    "https://www.tiktok.com/@{u}",       None),
    ("Pinterest", "https://www.pinterest.com/{u}/",    None),
    ("Medium",    "https://medium.com/@{u}",           None),
    ("Steam",     "https://steamcommunity.com/id/{u}", None),
    ("Spotify",   "https://open.spotify.com/user/{u}", None),
    ("LinkedIn",  "https://www.linkedin.com/in/{u}",   None),
    ("YouTube",   "https://www.youtube.com/@{u}",      None),
]

PASTE_SITES = [
    ("Pastebin (search)", "https://pastebin.com/search?q=%22{q}%22"),
    ("Google dork: \"{q}\" (site:pastebin.com OR site:ghostbin.com OR site:justpaste.it)",
     "https://www.google.com/search?q=%22{q}%22+site%3Apastebin.com+OR+site%3Ajustpaste.it"),
]

EMAIL_SERVICES_STATUS = [
    ("HaveIBeenPwned (account page)", "https://haveibeenpwned.com/account/{e}"),
    ("DeHashed (search)",             "https://dehashed.com/search?query=%22{e}%22"),
    ("IntelX (search)",               "https://intelx.io/?s={e}"),
    ("Epieos (email OSINT)",          "https://epieos.com/?q={e}"),
]

COLORS = {
    "red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m",
    "cyan": "\033[96m", "magenta": "\033[95m", "reset": "\033[0m", "bold": "\033[1m",
}

def c(text, color):
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"


# ---------------- HTTP helper ----------------
def http_get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.read(200000).decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


# ---------------- Modules ----------------
def check_username(username):
    """Check a username across popular public platforms."""
    results = []
    def probe(item):
        name, template, _ = item
        url = template.format(u=username)
        status, body = http_get(url)
        found = status == 200 and ("Page Not found" not in body and "Sorry, nobody" not in body)
        return (name, url, status, found)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        results = list(ex.map(probe, USERNAME_SITES))
    print(c(f"\n[*] Username footprint for '{username}'", "cyan"))
    found_count = 0
    for name, url, status, found in results:
        if found:
            found_count += 1
            print(c(f"    [FOUND   ] {name:<12} -> {url}", "red"))
        elif status == 0:
            print(c(f"    [ERROR   ] {name:<12} (network/blocked)", "yellow"))
        else:
            print(c(f"    [NOT FOUND] {name:<12} (HTTP {status})", "green"))
    print(c(f"    => {found_count} publicly visible profile(s) found", "magenta"))
    return results


def check_email_exposure(email):
    """Check email against public breach/leak lookup services (manual review links)."""
    if not re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        print(c("    [!] Invalid email format.", "red"))
        return
    print(c(f"\n[*] Email exposure checks for '{email}'", "cyan"))
    print(c("    Open these trusted services to verify breach status:", "yellow"))
    for name, template in EMAIL_SERVICES_STATUS:
        print(f"      - {name}: {template.format(e=email)}")
    # Pastebin-style paste search
    print(c("\n[*] Paste-site exposure (google dork links):", "cyan"))
    for name, template in PASTE_SITES:
        print(f"      - {name}: {template.format(q=email)}")


def check_domain(domain):
    """Basic passive checks on a domain you own (DNS records)."""
    print(c(f"\n[*] Passive DNS footprint for '{domain}'", "cyan"))
    for rtype, fn in (("A", socket.gethostbyname),):
        try:
            print(f"    {rtype} record: {fn(domain)}")
        except Exception as e:
            print(c(f"    {rtype} record: not resolvable ({e})", "yellow"))
    # Subdomain-ish common hosts
    for sub in ["www", "mail", "ftp", "dev", "test", "vpn", "remote", "cpanel", "webmail"]:
        host = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(host)
            print(c(f"    [FOUND] {host} -> {ip}", "red"))
        except Exception:
            print(c(f"    [--] {host} not resolvable", "green"))


def check_full_name(full_name):
    """Generate OSINT search links for a person's own name."""
    q = full_name.replace(" ", "+")
    quoted = "%22" + full_name.replace(" ", "+%22+") + "%22"
    print(c(f"\n[*] Public search footprint for '{full_name}'", "cyan"))
    links = [
        ("Google (exact name)", f"https://www.google.com/search?q=%22{full_name.replace(' ', '+')}%22"),
        ("Bing (exact name)",   f"https://www.bing.com/search?q=%22{full_name.replace(' ', '+')}%22"),
        ("DuckDuckGo",          f"https://duckduckgo.com/?q=%22{full_name.replace(' ', '+')}%22"),
        ("Google Images",       f"https://www.google.com/search?q=%22{full_name.replace(' ', '+')}%22&tbm=isch"),
        ("Whitepages/People (remove yourself!)", f"https://www.google.com/search?q=%22{full_name.replace(' ', '+')}%22+whitepages+OR+spokeo+OR+beenverified"),
        ("Facebook search",     f"https://www.facebook.com/search/people/?q={q}"),
        ("LinkedIn people",     f"https://www.linkedin.com/search/results/people/?keywords={q}"),
    ]
    for name, url in links:
        print(f"      - {name}: {url}")
    print(c("    TIP: data-broker listings (Spokeo, Whitepages, BeenVerified) have", "yellow"))
    print(c("    opt-out pages — request removal from each one.", "yellow"))


def privacy_report(name=None, username=None, email=None, domain=None, outfile=None):
    report = {
        "generated": datetime.now().isoformat(),
        "tool": "Public Footprint Auditor v1.0 by Mr. Sabaz Ali Khan",
        "inputs": {"name": name, "username": username, "email": email, "domain": domain},
        "note": "Review results manually via provided trusted services; remove/lock down any unwanted exposure.",
        "recommendations": [
            "Remove yourself from data-broker sites (Spokeo, Whitepages, BeenVerified, MyLife) via their opt-out forms.",
            "Set social profiles to private; remove old posts containing phone/address/birthdate.",
            "Use haveibeenpwned.com to check breaches and change reused passwords immediately.",
            "Enable 2FA (authenticator app, not SMS) on all critical accounts.",
            "Scrub metadata (EXIF GPS) from photos before uploading.",
            "Use a separate email alias for public signups.",
            "Check Google search results for your name and use Google's 'Remove personal information' request form.",
        ],
    }
    text = json.dumps(report, indent=2)
    if outfile:
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(text)
        print(c(f"\n[+] Privacy report saved to {outfile}", "green"))
    else:
        print(c("\n[*] PRIVACY RECOMMENDATIONS", "cyan"))
        for i, r in enumerate(report["recommendations"], 1):
            print(f"    {i}. {r}")


# ---------------- Main ----------------
def main():
    print(c(BANNER, "magenta"))
    print(c(SUBTITLE, "cyan"))

    p = argparse.ArgumentParser(description="Public Footprint Auditor - audit your own public exposure")
    p.add_argument("-n", "--name", help="Your full name (search footprint)")
    p.add_argument("-u", "--username", help="Username to check across platforms")
    p.add_argument("-e", "--email", help="Email to check for exposure")
    p.add_argument("-d", "--domain", help="Domain you own (DNS footprint)")
    p.add_argument("-o", "--output", help="Save privacy report to JSON file")
    p.add_argument("--all", action="store_true", help="Run interactive mode")
    args = p.parse_args()

    if not any([args.name, args.username, args.email, args.domain, args.all]):
        p.print_help()
        return

    start = time.time()
    if args.all:
        args.name = input("Full name (Enter to skip): ").strip() or None
        args.username = input("Username (Enter to skip): ").strip() or None
        args.email = input("Email (Enter to skip): ").strip() or None
        args.domain = input("Domain (Enter to skip): ").strip() or None

    if args.name:
        check_full_name(args.name)
    if args.username:
        check_username(args.username)
    if args.email:
        check_email_exposure(args.email)
    if args.domain:
        check_domain(args.domain)

    privacy_report(args.name, args.username, args.email, args.domain, args.output)
    print(c(f"\n[*] Scan completed in {time.time() - start:.1f}s", "green"))
    print(c("    Stay safe. — Mr. Sabaz Ali Khan", "magenta"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(c("\n[!] Aborted by user.", "red"))
        sys.exit(1)
