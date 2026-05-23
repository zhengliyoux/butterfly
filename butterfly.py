#!/usr/bin/env python3
"""
╔══════════════════════════════════════╗
║   SkyWings NGS v2.0 — by Putra      ║
║   Termux Network Intelligence Suite ║
╚══════════════════════════════════════╝
"""

import os
import time
import random
import socket
import platform
import threading
import subprocess
import json
import re
import ipaddress
from datetime import datetime

# ══════════════════════════════════════════
#  ANSI COLOR PALETTE
# ══════════════════════════════════════════
R   = "\033[0m"
BLD = "\033[1m"
DIM = "\033[2m"
UL  = "\033[4m"

# Base colors
BLK = "\033[30m"
RED = "\033[31m"
GRN = "\033[32m"
YLW = "\033[33m"
BLU = "\033[34m"
MAG = "\033[35m"
CYN = "\033[36m"
WHT = "\033[37m"

# Bright colors
BRED = "\033[1;31m"
BGRN = "\033[1;32m"
BYLW = "\033[1;33m"
BBLU = "\033[1;34m"
BMAG = "\033[1;35m"
BCYN = "\033[1;36m"
BWHT = "\033[1;37m"

# 256-color extras
ORG  = "\033[38;5;208m"
PINK = "\033[38;5;201m"
TEAL = "\033[38;5;51m"
LIME = "\033[38;5;46m"
GOLD = "\033[38;5;220m"

# Background
BG_BLK = "\033[40m"
BG_RED = "\033[41m"
BG_GRN = "\033[42m"
BG_BLU = "\033[44m"

RAINBOW = [BRED, BGRN, BYLW, BBLU, BMAG, BCYN, ORG, PINK, TEAL, LIME]

LOG_FILE = "skywings_output.log"

# ══════════════════════════════════════════
#  CORE UTILITIES
# ══════════════════════════════════════════

def run_cmd(cmd: str, timeout: int = 15):
    """Execute shell command safely."""
    try:
        return subprocess.run(
            cmd, shell=True, capture_output=True,
            text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return None
    except Exception:
        return None

def rcolor() -> str:
    """Return random rainbow color."""
    return random.choice(RAINBOW)

def clear_screen():
    os.system("clear")

def save_log(data: str):
    try:
        with open(LOG_FILE, "a") as fp:
            fp.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {data}\n")
    except Exception:
        pass

def format_bytes(size) -> str:
    try:
        size = int(size)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f}{unit}"
            size //= 1024
        return f"{size:.1f}TB"
    except Exception:
        return "?"

def normalize_url(url: str) -> str:
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url

def strip_scheme(url: str) -> str:
    return url.strip().replace("https://", "").replace("http://", "").split("/")[0]

def is_valid_target(target: str) -> bool:
    return bool(target and target.strip())

def get_ip(target: str):
    try:
        return socket.gethostbyname(target.strip())
    except socket.gaierror:
        return None

def get_all_ips(target: str) -> list:
    try:
        infos = socket.getaddrinfo(target.strip(), None)
        return list(dict.fromkeys([i[4][0] for i in infos]))
    except Exception:
        return []

def calc_latency(host: str, count: int = 3):
    result = run_cmd(f"ping -c {count} -W 2 {host}", timeout=count * 3 + 5)
    if not result or result.returncode != 0:
        return None
    for line in result.stdout.split("\n"):
        if "rtt" in line or "round-trip" in line:
            try:
                return float(line.split("/")[4])
            except Exception:
                pass
    return None

def tool_check(tool: str) -> bool:
    result = run_cmd(f"which {tool}")
    if not result or not result.stdout.strip():
        install_map = {
            "nmap":       "pkg install nmap",
            "whois":      "pkg install whois",
            "traceroute": "pkg install traceroute",
            "curl":       "pkg install curl",
            "openssl":    "pkg install openssl",
            "dig":        "pkg install dnsutils",
        }
        hint = install_map.get(tool, "")
        print(BRED + f"  [✗] '{tool}' belum terinstall." + R)
        if hint:
            print(BYLW + f"      Install: {hint}" + R)
        return False
    return True

# ══════════════════════════════════════════
#  UI COMPONENTS
# ══════════════════════════════════════════

W = 46  # box width

def box_top(color=BCYN):
    print(color + "┌" + "─" * W + "┐" + R)

def box_mid(color=BCYN):
    print(color + "├" + "─" * W + "┤" + R)

def box_bot(color=BCYN):
    print(color + "└" + "─" * W + "┘" + R)

def box_row(text: str, color=BCYN, text_color=BWHT, pad=True):
    content = text[:W] if len(text) > W else text
    spaces  = W - len(content)
    left    = spaces // 2 if pad else 0
    right   = spaces - left if pad else spaces
    print(color + "│" + text_color + " " * left + content + " " * right + color + "│" + R)

def box_left(text: str, color=BCYN, text_color=WHT):
    content = (" " + text)[:W]
    padding = " " * (W - len(content))
    print(color + "│" + text_color + content + padding + color + "│" + R)

def separator(char="─", color=BCYN, width=None):
    w = width or W + 2
    print(color + char * w + R)

def section_title(text: str, color=BCYN):
    line = "─" * ((W - len(text) - 2) // 2)
    print(color + line + " " + BLD + text + R + color + " " + line + R)

def status_badge(label: str, ok: bool):
    if ok:
        return BGRN + f" ✔ {label} " + R
    return BRED + f" ✘ {label} " + R

def latency_color(ms: float) -> str:
    if ms < 30:   return BGRN
    if ms < 100:  return BYLW
    if ms < 300:  return ORG
    return BRED

def http_code_color(code: str) -> str:
    if code.startswith("2"):  return BGRN
    if code.startswith("3"):  return BYLW
    if code.startswith("4"):  return ORG
    return BRED

def prompt_str() -> str:
    return (
        BLD + rcolor() + "SkyWings" + R +
        BCYN + "@root" + R +
        BRED + " ❯ " + R
    )

def press_enter():
    input(DIM + BYLW + "\n  [ ENTER untuk kembali ]" + R)

def loading_bar(text: str, delay: float = 0.012):
    chars = "▏▎▍▌▋▊▉█"
    bar_w = 20
    for i in range(bar_w + 1):
        filled  = "█" * i
        unfill  = "░" * (bar_w - i)
        pct     = int(i / bar_w * 100)
        c       = rcolor()
        spin    = chars[i % len(chars)]
        print(f"\r  {c}{spin} {text} [{BWHT}{filled}{DIM}{unfill}{c}] {pct:3d}%{R}", end="", flush=True)
        time.sleep(delay)
    print()

# ══════════════════════════════════════════
#  HEADER / LOGO
# ══════════════════════════════════════════

LOGO_ART = r"""
 ____  _           __        ___                 
/ ___|| | ___   _ _\ \      / (_)_ __   __ _ ___ 
\___ \| |/ / | | \ \ \ /\ / /| | '_ \ / _` / __|
 ___) |   <| |_| |\ \ V  V / | | | | | (_| \__ \
|____/|_|\_\\__, | \_\_/\_/  |_|_| |_|\__, |___/
            |___/                      |___/     
"""

def show_logo():
    clear_screen()
    color = rcolor()
    print(color + BLD + LOGO_ART + R)

    # Info box
    now = datetime.now()
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except Exception:
        local_ip = "N/A"

    box_top(BCYN)
    box_row("🔰 SKYWINGS NGS v2.0 — Network Intelligence", BCYN, BWHT)
    box_mid(BCYN)
    box_left(f"  Script by  : Putra (SkyWings)", BCYN, BYLW)
    box_left(f"  Version    : 2.0  Codename: Wings Point O", BCYN, BYLW)
    box_left(f"  Platform   : Termux CLI / Linux", BCYN, BYLW)
    box_left(f"  Local IP   : {local_ip}", BCYN, BYLW)
    box_left(f"  Time       : {now:%Y-%m-%d %H:%M:%S}", BCYN, BYLW)
    box_bot(BCYN)
    print()

def kali_header(title: str, icon: str = "🔍"):
    color = rcolor()
    bar   = "═" * W
    print()
    print(color + BLD + "╔" + bar + "╗" + R)
    label = f"  {icon}  {title}"
    pad   = W - len(label)
    print(color + BLD + "║" + BWHT + label + " " * pad + color + "║" + R)
    print(color + BLD + "╚" + bar + "╝" + R)
    print()

def screen_mode(title: str, icon: str = "🔍"):
    """Decorator: clears screen, shows header, waits for enter on return."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            clear_screen()
            kali_header(title, icon)
            try:
                result = func(*args, **kwargs)
            except KeyboardInterrupt:
                print(BYLW + "\n  [!] Dibatalkan." + R)
                result = None
            press_enter()
            return result
        return wrapper
    return decorator

# ══════════════════════════════════════════
#  COMMON PORT TABLE
# ══════════════════════════════════════════

COMMON_PORTS = {
    21:   "FTP",        22:   "SSH",       23:   "TELNET",
    25:   "SMTP",       53:   "DNS",       80:   "HTTP",
    110:  "POP3",      143:   "IMAP",     443:   "HTTPS",
    445:  "SMB",       587:   "SMTP-TLS", 993:   "IMAPS",
    995:  "POP3S",    1433:   "MSSQL",   3306:   "MYSQL",
    3389: "RDP",      5432:   "PGSQL",   5900:   "VNC",
    6379: "REDIS",    8080:   "HTTP-ALT",8443:   "HTTPS-ALT",
    8888: "JUPYTER", 27017:   "MONGODB",
}

HIGH_RISK_PORTS = {21, 23, 3389, 5900, 6379, 27017, 1433, 3306}
MED_RISK_PORTS  = {22, 25, 80, 8080, 8443, 445, 5432}

# ══════════════════════════════════════════
#  BANNER GRAB
# ══════════════════════════════════════════

def grab_banner(ip: str, port: int, timeout: float = 2.0):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, port))
        probes = {
            80:   b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n",
            8080: b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n",
            8443: b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n",
        }
        probe = probes.get(port, b"\r\n")
        if probe:
            s.send(probe)
        raw    = s.recv(512).decode(errors="ignore").strip()
        s.close()
        lines  = [ln.strip() for ln in raw.split("\n") if ln.strip()]
        return lines[0][:100] if lines else None
    except Exception:
        return None

# ══════════════════════════════════════════
#  DNS LOOKUP
# ══════════════════════════════════════════

def dns_lookup_raw(target: str):
    """Resolve A + reverse DNS. Returns IP or None."""
    ip = get_ip(target)
    if ip:
        print(BGRN + f"  [A]    {target} → {ip}" + R)
        try:
            rev = socket.gethostbyaddr(ip)
            if rev and rev[0] and rev[0] != target:
                print(BCYN + f"  [rDNS] {ip} → {rev[0]}" + R)
        except Exception:
            pass
        save_log(f"DNS {target}->{ip}")
        return ip
    else:
        print(BRED + f"  [DNS]  Gagal resolve: {target}" + R)
        return None

@screen_mode("DNS LOOKUP", "🌐")
def dns_lookup_menu(target: str):
    target = target.strip()
    if not is_valid_target(target):
        print(BRED + "  [!] Target tidak valid." + R)
        return

    section_title("RESOLUSI")
    ip = dns_lookup_raw(target)

    all_ips = get_all_ips(target)
    if len(all_ips) > 1:
        print(BCYN + f"  [Multi] {', '.join(all_ips)}" + R)

    # IPv6
    try:
        info = socket.getaddrinfo(target, None, socket.AF_INET6)
        if info:
            print(BCYN + f"  [AAAA]  {info[0][4][0]}" + R)
    except Exception:
        pass

    if not ip:
        return

    separator()

    if tool_check("dig"):
        for rtype in ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA"]:
            r = run_cmd(f"dig {target} {rtype} +noall +answer +time=3 2>/dev/null", timeout=8)
            if r and r.stdout.strip():
                section_title(f"{rtype} Records", BCYN)
                for line in r.stdout.strip().split("\n")[:8]:
                    print(f"  {line}")
    else:
        r = run_cmd(f"nslookup {target} 2>/dev/null")
        if r and r.stdout.strip():
            section_title("NSLookup", BCYN)
            print(r.stdout[:600])

# ══════════════════════════════════════════
#  QUICK NETWORK INFO
# ══════════════════════════════════════════

@screen_mode("QUICK NETWORK INFO", "⚡")
def quick_info(target: str):
    target = target.strip()
    if not is_valid_target(target):
        print(BRED + "  [!] Target tidak valid." + R)
        return

    ip        = get_ip(target)
    is_priv   = False
    if ip:
        try:
            is_priv = ipaddress.ip_address(ip).is_private
        except Exception:
            pass

    box_top()
    box_left(f"  Target  : {target}")
    box_left(f"  IP      : {ip or 'Gagal resolve'}", text_color=BWHT)
    if ip:
        box_left(f"  Type    : {'🏠 Private/LAN' if is_priv else '🌍 Public'}")
    box_bot()

    # ── Ping ──────────────────────────────
    print()
    section_title("PING TEST (4 pkt)", BCYN)
    r = run_cmd(f"ping -c 4 -W 2 {target}", timeout=20)
    if r and r.returncode == 0 and r.stdout:
        for line in r.stdout.strip().split("\n"):
            if "time=" in line:
                try:
                    ms  = float(re.search(r"time=([\d.]+)", line).group(1))
                    col = latency_color(ms)
                    print(col + f"  {line.strip()}" + R)
                except Exception:
                    print(f"  {line.strip()}")
            elif "rtt" in line or "packet" in line:
                print(BGRN + f"  {line.strip()}" + R)

        lat = calc_latency(target)
        if lat is not None:
            q   = ["Excellent", "Good", "Fair", "Poor"][
                0 if lat < 20 else (1 if lat < 80 else (2 if lat < 150 else 3))
            ]
            col = latency_color(lat)
            print(col + f"\n  ▶ Avg Latency: {lat:.1f} ms  [{q}]" + R)
    else:
        print(BYLW + "  [-] Host tidak reachable (ICMP mungkin diblokir)" + R)

    separator()

    # ── DNS ───────────────────────────────
    section_title("DNS", BCYN)
    dns_lookup_raw(target)
    all_ips = get_all_ips(target)
    if len(all_ips) > 1:
        print(BCYN + f"  [Multi-IP] {', '.join(all_ips[:5])}" + R)

    separator()

    # ── Quick ports ───────────────────────
    section_title("QUICK PORT CHECK", BCYN)
    if ip:
        crit = [(80,"HTTP"), (443,"HTTPS"), (22,"SSH"),
                (21,"FTP"), (3306,"MYSQL"), (3389,"RDP")]
        for p, svc in crit:
            s = socket.socket()
            s.settimeout(1)
            t0     = time.time()
            status = s.connect_ex((ip, p)) == 0
            t_ms   = round((time.time() - t0) * 1000, 1)
            s.close()
            badge  = BGRN + "●" if status else BRED + "○"
            label  = BGRN + "OPEN  " if status else BRED + "CLOSED"
            resp   = f"  ({t_ms}ms)" if status else ""
            print(f"  {badge}{R} {label}{R}  {p:5}  {DIM}{svc}{R}{resp}")

    separator()

    # ── TTL / OS hint ─────────────────────
    section_title("TTL / OS FINGERPRINT", BCYN)
    r2 = run_cmd(f"ping -c 1 -W 2 {target}", timeout=5)
    if r2 and r2.stdout:
        for line in r2.stdout.split("\n"):
            if "ttl=" in line.lower():
                try:
                    ttl    = int(re.search(r"ttl=(\d+)", line, re.I).group(1))
                    os_g   = ("Linux/Unix/Android" if ttl <= 64 else
                               "Windows"           if ttl <= 128 else
                               "Cisco/Network Device")
                    print(BYLW + f"  TTL {ttl}  →  {os_g}" + R)
                except Exception:
                    pass

# ══════════════════════════════════════════
#  PORT SCAN
# ══════════════════════════════════════════

@screen_mode("PORT SCAN", "🔌")
def port_scan(target: str):
    target = target.strip()
    if not is_valid_target(target):
        print(BRED + "  [!] Target tidak valid." + R)
        return

    ip = get_ip(target)
    if not ip:
        print(BRED + f"  [!] Tidak bisa resolve: {target}" + R)
        return

    box_top()
    box_left(f"  Target : {target} ({ip})")
    box_left(f"  Ports  : {len(COMMON_PORTS)} common  +  custom")
    box_left(f"  Mode   : Threaded + Banner + Risk Label")
    box_bot()
    print()
    print(BYLW + "  [?] Custom port tambahan? (misal: 8888,9090) / Enter=skip:" + R)
    extra = input("      > ").strip()

    extra_ports: dict = {}
    for ep in extra.split(","):
        ep = ep.strip()
        if ep.isdigit():
            extra_ports[int(ep)] = "CUSTOM"

    all_ports = {**COMMON_PORTS, **extra_ports}
    open_ports: list = []
    lock = threading.Lock()

    header = (
        f"  {'PORT':<7} {'SERVICE':<13} {'STATUS':<8} {'RTT':<8} {'RISK':<12} BANNER"
    )
    separator()
    print(DIM + header + R)
    separator()

    def check_port(p: int, svc: str):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.8)
            t0     = time.time()
            opened = s.connect_ex((ip, p)) == 0
            rtt    = round((time.time() - t0) * 1000, 1)
            s.close()

            with lock:
                if opened:
                    banner  = grab_banner(ip, p) or ""
                    b_str   = f"  {DIM}{banner[:50]}{R}" if banner else ""
                    is_high = p in HIGH_RISK_PORTS
                    is_med  = p in MED_RISK_PORTS
                    risk_s  = (BRED + "HIGH-RISK" if is_high else
                                BYLW + "MEDIUM"   if is_med  else
                                BGRN + "LOW")
                    print(
                        BGRN + f"  {p:<7}" +
                        BWHT + f"{svc:<13}" +
                        BGRN + "OPEN    " +
                        BCYN + f"{rtt:5.1f}ms  " + R +
                        risk_s + R + b_str
                    )
                    open_ports.append(p)
                    save_log(f"PORT OPEN {target}:{p} ({svc})")
                else:
                    print(
                        DIM + BRED + f"  {p:<7}{svc:<13}CLOSED" + R
                    )
        except Exception as exc:
            with lock:
                print(BRED + f"  {p:<7} ERROR: {exc}" + R)

    threads = [threading.Thread(target=check_port, args=(p, svc))
               for p, svc in sorted(all_ports.items())]
    for th in threads: th.start()
    for th in threads: th.join()

    separator()
    count_open = len(open_ports)
    color      = BGRN if count_open == 0 else (BYLW if count_open < 5 else BRED)
    print(color + f"  [+] {count_open}/{len(all_ports)} port terbuka." + R)
    if open_ports:
        print(BCYN + f"  Open: {sorted(open_ports)}" + R)
        high = [p for p in open_ports if p in HIGH_RISK_PORTS]
        if high:
            print(BRED + f"  [!] HIGH-RISK ports terbuka: {high}" + R)

# ══════════════════════════════════════════
#  PING
# ══════════════════════════════════════════

@screen_mode("PING TARGET", "📡")
def ping_target(target: str):
    target = target.strip()
    if not is_valid_target(target):
        print(BRED + "  [!] Target tidak valid." + R)
        return

    print(BYLW + "  [?] Jumlah paket (1–50, default 5):" + R)
    c     = input("      > ").strip()
    count = int(c) if c.isdigit() and 1 <= int(c) <= 50 else 5

    print(BCYN + f"\n  Ping {target}  ×{count}...\n" + R)
    result = run_cmd(f"ping -c {count} {target}", timeout=count * 3 + 5)

    if result and result.returncode == 0 and result.stdout:
        times = []
        for line in result.stdout.split("\n"):
            if "time=" in line:
                try:
                    ms  = float(re.search(r"time=([\d.]+)", line).group(1))
                    times.append(ms)
                    col = latency_color(ms)
                    print(col + f"  {line.strip()}" + R)
                except Exception:
                    print(f"  {line.strip()}")
            elif line.strip():
                print(f"  {DIM}{line.strip()}{R}")

        if len(times) >= 2:
            separator()
            section_title("STATISTIK", BCYN)
            mn  = min(times)
            mx  = max(times)
            avg = sum(times) / len(times)
            jit = mx - mn
            jq  = ("Stabil" if jit < 10 else "OK" if jit < 50 else "Tidak Stabil")
            jc  = (BGRN    if jit < 10 else BYLW if jit < 50 else BRED)

            print(BGRN + f"  Min    : {mn:.2f} ms" + R)
            print(BRED  + f"  Max    : {mx:.2f} ms" + R)
            print(BYLW  + f"  Avg    : {avg:.2f} ms" + R)
            print(jc    + f"  Jitter : {jit:.2f} ms  [{jq}]" + R)

        for line in result.stdout.split("\n"):
            m = re.search(r"(\d+)% packet loss", line)
            if m:
                loss = int(m.group(1))
                col  = BGRN if loss == 0 else (BYLW if loss < 20 else BRED)
                icon = "✔" if loss == 0 else "✘"
                print(col + f"  Loss   : {loss}%  {icon}" + R)
    else:
        print(BRED + "  [-] Ping gagal — host mungkin blokir ICMP." + R)

# ══════════════════════════════════════════
#  TRACEROUTE
# ══════════════════════════════════════════

@screen_mode("TRACE ROUTE", "🗺️")
def trace_route(target: str):
    target = target.strip()
    if not is_valid_target(target):
        print(BRED + "  [!] Target tidak valid." + R)
        return
    if not tool_check("traceroute"):
        return

    print(BCYN + f"  Tracing route ke {target}  (max 20 hop)...\n" + R)
    result = run_cmd(f"traceroute -m 20 -w 2 {target}", timeout=90)

    if result and result.stdout.strip():
        timeout_hops = 0
        print(f"  {'HOP':<5} {'HOST/IP':<35} {'LATENCY'}")
        separator()
        for line in result.stdout.strip().split("\n"):
            if "* * *" in line:
                timeout_hops += 1
                print(DIM + BRED + f"  {line}  [timeout/filtered]" + R)
            else:
                ms_vals = re.findall(r"([\d.]+) ms", line)
                if ms_vals:
                    avg_hop = sum(float(v) for v in ms_vals) / len(ms_vals)
                    col     = latency_color(avg_hop)
                    print(col + f"  {line}" + R)
                else:
                    print(f"  {line}")
        if timeout_hops > 5:
            print(BYLW + f"\n  [i] {timeout_hops} hop timeout — kemungkinan ada firewall." + R)
    else:
        print(BRED + "  [-] Traceroute gagal." + R)

# ══════════════════════════════════════════
#  NMAP
# ══════════════════════════════════════════

@screen_mode("NMAP SCANNER", "🗡️")
def advanced_scan(target: str):
    target = target.strip()
    if not is_valid_target(target):
        print(BRED + "  [!] Target tidak valid." + R)
        return
    if not tool_check("nmap"):
        return

    box_top(BMAG)
    box_row("Pilih mode scan:", BMAG, BWHT)
    box_mid(BMAG)
    box_left("  [1]  Fast scan        -F --open", BMAG, BGRN)
    box_left("  [2]  Service Version  -sV", BMAG, BCYN)
    box_left("  [3]  OS Detection     -O", BMAG, BCYN)
    box_left("  [4]  Full + Script    -A", BMAG, BYLW)
    box_left("  [5]  UDP Scan         -sU -F", BMAG, ORG)
    box_left("  [6]  Stealth SYN      -sS -F", BMAG, BRED)
    box_bot(BMAG)

    mode  = input(prompt_str()).strip()
    flags = {
        "1": "-F --open",
        "2": "-sV --version-intensity 5",
        "3": "-O",
        "4": "-A",
        "5": "-sU -F",
        "6": "-sS -F",
    }.get(mode, "-F --open")

    print(BCYN + f"\n  Nmap {target}  [{flags}]\n" + R)
    res = run_cmd(f"nmap {flags} {target}", timeout=120)

    if res and res.stdout:
        for line in res.stdout.split("\n"):
            ll = line.lower()
            if "open" in ll:
                print(BGRN + f"  {line}" + R)
            elif "filtered" in ll or "closed" in ll:
                print(DIM + BRED + f"  {line}" + R)
            elif "host is up" in ll or "scan report" in ll:
                print(BYLW + f"  {line}" + R)
            else:
                print(f"  {line}")
        save_log(f"NMAP {target}: {flags}")
    else:
        print(BRED + "  [-] Nmap gagal." + R)

# ══════════════════════════════════════════
#  FIREWALL CHECK
# ══════════════════════════════════════════

@screen_mode("FIREWALL CHECK", "🛡️")
def firewall_check():
    """Check iptables / ufw / nftables status."""
    section_title("iptables", BCYN)
    r = run_cmd("iptables -L -n -v 2>/dev/null")
    if r and r.stdout.strip():
        print(r.stdout[:2000])
    else:
        print(BYLW + "  [i] iptables tidak aktif / butuh root." + R)

    section_title("UFW", BCYN)
    ufw = run_cmd("ufw status verbose 2>/dev/null")
    if ufw and ufw.stdout.strip():
        print(ufw.stdout[:500])
    else:
        print(BYLW + "  [i] UFW tidak aktif." + R)

    section_title("nftables", BCYN)
    nft = run_cmd("nft list ruleset 2>/dev/null")
    if nft and nft.stdout.strip():
        print(nft.stdout[:500])
    else:
        print(BYLW + "  [i] nftables tidak aktif." + R)

# ══════════════════════════════════════════
#  SAVE OUTPUT
# ══════════════════════════════════════════

def save_output_demo(target: str):
    target = target.strip()
    if not is_valid_target(target):
        print(BRED + "  [!] Target tidak valid." + R)
        return
    try:
        ip = get_ip(target)
        with open("scan_result.txt", "a") as fp:
            fp.write(f"\n{'='*44}\n")
            fp.write(f"Time   : {datetime.now()}\n")
            fp.write(f"Target : {target}\n")
            fp.write(f"IP     : {ip or 'Gagal resolve'}\n")
            if ip:
                fp.write("Ports  :\n")
                for p, svc in sorted(COMMON_PORTS.items()):
                    s = socket.socket()
                    s.settimeout(0.5)
                    if s.connect_ex((ip, p)) == 0:
                        fp.write(f"  OPEN {p} ({svc})\n")
                    s.close()
        print(BGRN + "  [+] Saved → scan_result.txt" + R)
        save_log(f"SAVED {target}")
    except Exception as exc:
        print(BRED + f"  [-] Gagal save: {exc}" + R)

# ══════════════════════════════════════════
#  SYSTEM INFO
# ══════════════════════════════════════════

@screen_mode("SYSTEM INFO", "💻")
def system_info():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except Exception:
        local_ip = "N/A"

    box_top(BGRN)
    box_left(f"  OS       : {platform.system()} {platform.release()}", BGRN, BWHT)
    box_left(f"  Version  : {platform.version()[:55]}", BGRN, WHT)
    box_left(f"  Node     : {platform.node()}", BGRN, BWHT)
    box_left(f"  Machine  : {platform.machine()}", BGRN, BWHT)
    box_left(f"  CPU      : {platform.processor() or 'N/A'}", BGRN, BWHT)
    box_left(f"  Local IP : {local_ip}", BGRN, BCYN)
    box_bot(BGRN)

    if tool_check("curl"):
        r = run_cmd("curl -s --max-time 5 ifconfig.me 2>/dev/null")
        if r and r.stdout.strip():
            print(BCYN + f"\n  Public IP : {r.stdout.strip()}" + R)

    # Memory
    mem = run_cmd("free -h 2>/dev/null")
    if mem and mem.stdout:
        separator()
        section_title("MEMORY", BCYN)
        for line in mem.stdout.strip().split("\n"):
            print(f"  {line}")

    # Disk
    disk = run_cmd("df -h 2>/dev/null")
    if disk and disk.stdout:
        separator()
        section_title("DISK", BCYN)
        for line in disk.stdout.strip().split("\n")[:6]:
            print(f"  {line}")

    # Uptime
    up = run_cmd("uptime 2>/dev/null")
    if up and up.stdout:
        separator()
        print(BCYN + f"  Uptime : {up.stdout.strip()}" + R)

    # Network interfaces
    ifc = run_cmd("ip addr show 2>/dev/null || ifconfig 2>/dev/null")
    if ifc and ifc.stdout:
        separator()
        section_title("INTERFACES", BCYN)
        for line in ifc.stdout.split("\n"):
            if "inet " in line or ": <" in line:
                print(f"  {line.strip()}")

    # Top processes
    top_r = run_cmd("ps aux --sort=-%cpu 2>/dev/null | head -7")
    if top_r and top_r.stdout:
        separator()
        section_title("TOP CPU PROSES", BCYN)
        for line in top_r.stdout.strip().split("\n"):
            print(f"  {line}")

# ══════════════════════════════════════════
#  FAST SCAN (multi-target)
# ══════════════════════════════════════════

@screen_mode("FAST SCAN", "⚡")
def fast_scan(targets: list):
    if not targets:
        print(BRED + "  [!] Tidak ada target." + R)
        return

    results: dict = {}
    lock = threading.Lock()

    def scan(t: str):
        t = t.strip()
        if not t:
            return
        start = time.time()
        r     = run_cmd(f"ping -c 1 -W 1 {t}", timeout=5)
        ms    = round((time.time() - start) * 1000, 1)
        ip    = get_ip(t)

        with lock:
            if r and r.returncode == 0:
                open_p = []
                if ip:
                    for p in [80, 443, 22]:
                        s = socket.socket()
                        s.settimeout(0.5)
                        if s.connect_ex((ip, p)) == 0:
                            open_p.append(p)
                        s.close()
                ports_str = f"  ports:{open_p}" if open_p else ""
                results[t] = ("UP", ip)
                lat_col   = latency_color(ms)
                print(
                    BGRN + f"  ● UP    " + R +
                    f"{t:<24}" +
                    BCYN + f"→ {ip or '?':<16}" + R +
                    lat_col + f"{ms:6.1f}ms" + R +
                    BYLW + ports_str + R
                )
            else:
                results[t] = ("DOWN", None)
                print(BRED + f"  ○ DOWN  {t}" + R)

    print(BCYN + f"  Scanning {len(targets)} target...\n" + R)
    print(f"  {'STATUS':<8} {'TARGET':<24} {'IP':<18} {'RTT'}")
    separator()

    threads = [threading.Thread(target=scan, args=(t,)) for t in targets]
    for th in threads: th.start()
    for th in threads: th.join()

    separator()
    up = sum(1 for v in results.values() if v[0] == "UP")
    col = BGRN if up == len(targets) else (BYLW if up > 0 else BRED)
    print(col + f"  [+] {up}/{len(targets)} host aktif." + R)

# ══════════════════════════════════════════
#  WHOIS
# ══════════════════════════════════════════

@screen_mode("WHOIS LOOKUP", "🔎")
def whois_lookup(t: str):
    t = strip_scheme(t)
    if not is_valid_target(t):
        print(BRED + "  [!] Target tidak valid." + R)
        return
    if not tool_check("whois"):
        return

    print(BCYN + f"  Querying WHOIS: {t}\n" + R)
    r = run_cmd(f"whois {t}", timeout=20)

    if not (r and r.stdout.strip()):
        print(BRED + "  [-] WHOIS gagal." + R)
        return

    important = ["registrar", "name server", "expir", "creat", "updat",
                 "status", "registrant", "dnssec", "tech", "admin"]
    seen: set = set()

    for line in r.stdout.split("\n")[:120]:
        if not line.strip() or line.startswith("%"):
            continue
        key = line.split(":")[0].lower().strip() if ":" in line else ""
        if key in seen:
            continue
        if not any(x in key for x in important):
            continue
        seen.add(key)

        if "expir" in key:
            try:
                date_part = line.split(":", 1)[1].strip()
                for fmt in ["%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d", "%d-%b-%Y"]:
                    try:
                        exp       = datetime.strptime(date_part[:10], fmt[:10])
                        days_left = (exp - datetime.utcnow()).days
                        if days_left < 0:
                            print(BRED + f"  {line}  ← EXPIRED {abs(days_left)} hari lalu!" + R)
                        elif days_left < 30:
                            print(BYLW + f"  {line}  ← {days_left} hari lagi!" + R)
                        else:
                            print(BGRN + f"  {line}  ({days_left} hari lagi)" + R)
                        break
                    except Exception:
                        continue
                else:
                    print(BYLW + f"  {line}" + R)
            except Exception:
                print(BYLW + f"  {line}" + R)
        else:
            print(BYLW + f"  {line}" + R)

    save_log(f"WHOIS {t}")

# ══════════════════════════════════════════
#  GEO IP
# ══════════════════════════════════════════

@screen_mode("GEO IP LOOKUP", "📍")
def geo_ip(t: str):
    t = strip_scheme(t)
    if not is_valid_target(t):
        print(BRED + "  [!] Target tidak valid." + R)
        return
    if not tool_check("curl"):
        return

    ip    = get_ip(t)
    query = ip if ip else t
    print(BCYN + f"  GeoIP: {t}  →  {query}\n" + R)

    r = run_cmd(f"curl -s --max-time 10 ipinfo.io/{query}")
    if not (r and r.stdout.strip()):
        print(BRED + "  [-] Gagal GeoIP. Cek koneksi internet." + R)
        return

    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        print(r.stdout[:500])
        return

    if data.get("bogon"):
        print(BYLW + "  [i] IP private/bogon — tidak ada geo info." + R)
        return

    box_top(BCYN)
    fields = [
        ("IP",       "ip"),       ("Hostname", "hostname"),
        ("Kota",     "city"),     ("Region",   "region"),
        ("Negara",   "country"),  ("Lokasi",   "loc"),
        ("ISP/ORG",  "org"),      ("Postal",   "postal"),
        ("Timezone", "timezone"),
    ]
    for label, key in fields:
        val = data.get(key, "—")
        col = BWHT if val and val != "—" else DIM
        box_left(f"  {label:<10}: {val}", text_color=col)
    box_bot(BCYN)

    loc = data.get("loc", "")
    if loc:
        lat, lon = loc.split(",")
        print(BCYN + f"\n  🗺  Maps: https://maps.google.com/?q={lat},{lon}" + R)

    org = data.get("org", "")
    hosting_kw = ["hosting","server","cloud","datacenter","vps","aws","azure",
                  "google","digitalocean","linode","vultr","ovh"]
    if any(kw in org.lower() for kw in hosting_kw):
        print(BYLW + "\n  [i] Kemungkinan Hosting / VPN / Cloud" + R)

    save_log(f"GEOIP {t}: {data.get('city')},{data.get('country')}")

# ══════════════════════════════════════════
#  HTTP HEADER SCAN
# ══════════════════════════════════════════

@screen_mode("HTTP HEADER SCAN", "🌐")
def http_header_scan(t: str):
    t = t.strip()
    if not is_valid_target(t):
        print(BRED + "  [!] Target tidak valid." + R)
        return
    if not tool_check("curl"):
        return

    print(BCYN + f"  Fetching headers: {t}\n" + R)

    r = run_cmd(
        f"curl -I -s --max-time 10 -L -A 'Mozilla/5.0' --max-redirs 5 {t}"
    )
    if not (r and r.stdout.strip()):
        t_http = t.replace("https://", "http://")
        r      = run_cmd(f"curl -I -s --max-time 10 {t_http}")
        if not (r and r.stdout.strip()):
            print(BRED + "  [-] Gagal ambil header." + R)
            return

    SEC_HEADERS = {
        "strict-transport-security": "HSTS",
        "content-security-policy":   "CSP",
        "x-frame-options":           "X-Frame-Options",
        "x-xss-protection":          "X-XSS-Protection",
        "x-content-type-options":    "X-Content-Type-Options",
        "referrer-policy":           "Referrer-Policy",
        "permissions-policy":        "Permissions-Policy",
    }
    found_sec: list = []
    redirect_n = 0

    separator()
    for line in r.stdout.split("\n"):
        line = line.strip()
        if not line:
            continue
        low = line.lower()

        if line.startswith("HTTP/"):
            parts   = line.split()
            code    = parts[1] if len(parts) > 1 else "?"
            col     = http_code_color(code)
            descs   = {"200":"OK","301":"Moved","302":"Found","403":"Forbidden",
                       "404":"Not Found","500":"Internal Error","503":"Unavailable"}
            desc    = descs.get(code, "")
            print(col + BLD + f"  {line}  {desc}" + R)
            if code.startswith("3"):
                redirect_n += 1

        elif "location:" in low:
            print(BYLW + f"  {line}  ← redirect" + R)

        elif "set-cookie:" in low:
            issues = []
            if "httponly" not in low: issues.append("NO HttpOnly")
            if "secure"   not in low: issues.append("NO Secure")
            if "samesite" not in low: issues.append("NO SameSite")
            col = BRED if issues else BGRN
            flag = f"  [{', '.join(issues)}]" if issues else "  [✔ OK]"
            print(BCYN + f"  {line}" + col + flag + R)

        elif any(x in low for x in ["server:", "x-powered-by:", "via:", "x-generator:"]):
            print(BYLW + f"  {line}  ← fingerprint" + R)

        elif any(k in low for k in SEC_HEADERS):
            for k, desc in SEC_HEADERS.items():
                if k in low:
                    found_sec.append(desc)
            print(BGRN + f"  {line}" + R)
        else:
            print(f"  {DIM}{line}{R}")

    if redirect_n:
        print(BYLW + f"\n  [i] {redirect_n} redirect." + R)

    # ── Security report ──────────────────
    separator()
    section_title("SECURITY HEADERS REPORT", BCYN)
    score = 0
    for name in SEC_HEADERS.values():
        if name in found_sec:
            print(BGRN + f"  ✔  {name}" + R)
            score += 1
        else:
            print(BRED + f"  ✘  {name}  — MISSING" + R)

    grade = "A" if score >= 6 else ("B" if score >= 4 else ("C" if score >= 2 else "F"))
    g_col = (BGRN if grade == "A" else BYLW if grade in ("B","C") else BRED)
    separator()
    print(g_col + BLD + f"  Score: {score}/{len(SEC_HEADERS)}   Grade: {grade}" + R)
    save_log(f"HTTP HEADER {t} score:{score}/7")

# ══════════════════════════════════════════
#  SSL CHECK
# ══════════════════════════════════════════

@screen_mode("SSL / TLS CHECK", "🔒")
def ssl_check(t: str):
    t = strip_scheme(t)
    if not is_valid_target(t):
        print(BRED + "  [!] Target tidak valid." + R)
        return
    if not tool_check("openssl"):
        return

    print(BCYN + f"  Connecting: {t}:443\n" + R)
    r = run_cmd(
        f"echo | openssl s_client -connect {t}:443 -servername {t} 2>/dev/null",
        timeout=15
    )
    if not (r and r.stdout.strip()):
        print(BRED + "  [-] Koneksi SSL gagal." + R)
        return

    issues: list = []
    separator()

    for line in r.stdout.split("\n"):
        line = line.strip()
        if any(x in line for x in ["subject=", "issuer="]):
            print(BCYN + f"  {line}" + R)
        elif "notBefore" in line:
            print(BGRN + f"  Issued  : {line}" + R)
        elif "notAfter" in line:
            try:
                date_str = line.split("=", 1)[1].strip()
                exp      = datetime.strptime(date_str, "%b %d %H:%M:%S %Y %Z")
                sisa     = (exp - datetime.utcnow()).days
                if sisa < 0:
                    issues.append("Sertifikat EXPIRED")
                    print(BRED + f"  ✘ EXPIRED: {date_str}" + R)
                elif sisa < 14:
                    issues.append(f"Sertifikat habis {sisa} hari lagi")
                    print(BRED + f"  ⚠ Expire: {date_str} ← {sisa} hari lagi! SEGERA RENEW!" + R)
                elif sisa < 30:
                    print(BYLW + f"  ⚠ Expire: {date_str} ← {sisa} hari lagi" + R)
                else:
                    print(BGRN + f"  ✔ Valid : {date_str}  ({sisa} hari lagi)" + R)
            except Exception:
                print(BGRN + f"  {line}" + R)
        elif "Verify return code" in line:
            ok  = "0 (ok)" in line.lower()
            col = BGRN if ok else BRED
            print(col + f"  {'✔' if ok else '✘'} {line}" + R)
            if not ok:
                issues.append("SSL Verify GAGAL")
        elif "Protocol" in line:
            if any(old in line for old in ["TLSv1 ", "TLSv1.0", "TLSv1.1", "SSLv3", "SSLv2"]):
                issues.append(f"Protokol deprecated: {line.strip()}")
                print(BRED + f"  ✘ {line}  ← DEPRECATED!" + R)
            else:
                print(BGRN + f"  ✔ {line}" + R)
        elif "Cipher" in line:
            print(BYLW + f"  {line}" + R)

    separator()
    section_title("PROTOCOL TEST", BCYN)
    for flag, label in [("-tls1_2","TLS 1.2"), ("-tls1_1","TLS 1.1"), ("-tls1","TLS 1.0")]:
        pr = run_cmd(
            f"echo | openssl s_client {flag} -connect {t}:443 -servername {t} 2>&1 | grep -c 'Cipher'",
            timeout=8
        )
        supported = pr and pr.stdout.strip() == "1"
        is_old    = label in ("TLS 1.1", "TLS 1.0")
        col       = (BRED if (is_old and supported) else BGRN if supported else DIM + BRED)
        mark      = ("✔ Supported" if supported else "✘ Not supported")
        depr      = " ← DEPRECATED!" if (is_old and supported) else ""
        if is_old and supported:
            issues.append(f"{label} masih aktif")
        print(col + f"  {mark:<14} {label}{depr}" + R)

    separator()
    if issues:
        print(BRED + "\n  [!] ISSUES:" + R)
        for iss in issues:
            print(BRED + f"      • {iss}" + R)
    else:
        print(BGRN + "\n  ✔ SSL/TLS OK — tidak ada masalah." + R)

    save_log(f"SSL CHECK {t} issues:{len(issues)}")

# ══════════════════════════════════════════
#  DIR BRUTEFORCE
# ══════════════════════════════════════════

@screen_mode("DIRECTORY SCAN", "📂")
def dir_bruteforce(t: str):
    t = t.strip().rstrip("/")
    if not is_valid_target(t):
        print(BRED + "  [!] Target tidak valid." + R)
        return
    if not tool_check("curl"):
        return

    paths = [
        "admin","login","dashboard","panel","administrator",
        "wp-admin","wp-login.php","phpmyadmin","cpanel",
        ".env",".git/config",".htaccess","web.config",
        "config.php","config.json","settings.py",
        "robots.txt","sitemap.xml","readme.txt","CHANGELOG.md",
        "composer.json","package.json",
        "api","api/v1","api/v2","graphql","swagger",
        "swagger-ui","swagger.json","openapi.json",
        "backup","backup.zip","db.sql","dump.sql",
        "dev","test","beta","staging","debug",
        "phpinfo.php","info.php","server-status",
        "uploads","files","media","images","assets",
    ]

    found: list = []
    lock   = threading.Lock()

    box_top(BCYN)
    box_left(f"  Target : {t}")
    box_left(f"  Paths  : {len(paths)}  |  Mode: Threaded")
    box_bot(BCYN)
    print()

    COL_MAP = {
        "200": (BGRN,  "FOUND  "),
        "301": (BYLW,  "REDIR  "),
        "302": (BYLW,  "REDIR  "),
        "307": (BYLW,  "REDIR  "),
        "308": (BYLW,  "REDIR  "),
        "401": (BMAG,  "AUTH   "),
        "403": (BCYN,  "FORBID "),
    }

    def check_path(p: str):
        url = f"{t}/{p}"
        r   = run_cmd(
            f"curl -o /dev/null -s -w '%{{http_code}}:%{{size_download}}' "
            f"--max-time 5 -L {url}",
            timeout=8
        )
        if not r:
            return
        parts = r.stdout.strip().split(":")
        code  = parts[0]
        size  = format_bytes(parts[1]) if len(parts) > 1 else "?"

        with lock:
            col, label = COL_MAP.get(code, (DIM + BRED, f"{code:<7}"))
            print(col + f"  [{label}]  {url:<50}  {size}" + R)
            if code == "200":
                found.append(url)
                save_log(f"DIR FOUND {url}")

    threads = [threading.Thread(target=check_path, args=(p,)) for p in paths]
    for th in threads: th.start()
    time.sleep(0.05)
    for th in threads: th.join()

    separator()
    print(BCYN + f"  [+] {len(found)} path ditemukan." + R)
    if found:
        print(BGRN + "\n  FOUND:" + R)
        for item in found:
            print(BGRN + f"    ✔  {item}" + R)

# ══════════════════════════════════════════
#  SUBDOMAIN SCAN
# ══════════════════════════════════════════

@screen_mode("SUBDOMAIN SCAN", "🕸️")
def subdomain_scan(d: str):
    d = strip_scheme(d)
    if not is_valid_target(d):
        print(BRED + "  [!] Domain tidak valid." + R)
        return

    subs = [
        "www","mail","api","dev","test","beta","cpanel",
        "ftp","smtp","pop","imap","webmail","m","mobile",
        "app","admin","portal","shop","blog","forum",
        "support","help","cdn","static","media","img",
        "images","assets","upload","vpn","remote","git",
        "gitlab","jenkins","ci","staging","uat","prod",
        "ns1","ns2","mx","autodiscover","autoconfig",
        "dashboard","panel","manage","status","monitor",
        "grafana","kibana","phpmyadmin",
    ]

    found: list = []
    lock   = threading.Lock()

    box_top(BCYN)
    box_left(f"  Target  : {d}")
    box_left(f"  Words   : {len(subs)} subdomain")
    box_bot(BCYN)
    print()

    def check(s: str):
        host = f"{s}.{d}"
        ip   = get_ip(host)
        with lock:
            if ip:
                print(BGRN + f"  ✔  {host:<40} → {ip}" + R)
                found.append((host, ip))
                save_log(f"SUBDOMAIN {host}->{ip}")

    threads = [threading.Thread(target=check, args=(s,)) for s in subs]
    for th in threads: th.start()
    for th in threads: th.join()

    separator()
    print(BCYN + f"  [+] {len(found)} subdomain aktif." + R)
    if not found:
        print(BRED + "  [-] Tidak ada subdomain ditemukan." + R)

# ══════════════════════════════════════════
#  FULL SECURITY REPORT
# ══════════════════════════════════════════

@screen_mode("FULL SECURITY REPORT", "🛡️")
def security_report(t: str):
    t   = strip_scheme(t.strip())
    if not is_valid_target(t):
        print(BRED + "  [!] Target tidak valid." + R)
        return

    url        = normalize_url(t)
    ip         = get_ip(t)
    all_ips    = get_all_ips(t)
    start_time = time.time()
    risk_score = 0
    findings:  list = []

    box_top(BRED)
    box_left(f"  Target : {t}", BRED, BWHT)
    box_left(f"  IP     : {ip or 'Gagal resolve'}", BRED, BCYN)
    box_left(f"  URL    : {url}", BRED, DIM + WHT)
    box_left(f"  Time   : {datetime.now():%Y-%m-%d %H:%M:%S}", BRED, DIM + WHT)
    box_bot(BRED)
    print()

    # ── 1. DNS ──────────────────────────
    section_title("1/6 · DNS", BCYN)
    dns_lookup_raw(t)
    if len(all_ips) > 1:
        print(BCYN + f"  [Multi-IP / CDN] {', '.join(all_ips[:5])}" + R)

    # ── 2. Ping + TTL ───────────────────
    separator()
    section_title("2/6 · PING & LATENCY", BCYN)
    r_ping = run_cmd(f"ping -c 3 -W 2 {t}", timeout=15)
    if r_ping and r_ping.returncode == 0:
        for line in r_ping.stdout.strip().split("\n"):
            if "rtt" in line or "packet" in line:
                print(BGRN + f"  {line.strip()}" + R)
        lat = calc_latency(t)
        if lat:
            q   = ["Excellent","Good","Fair","Poor"][
                0 if lat < 20 else 1 if lat < 80 else 2 if lat < 150 else 3
            ]
            col = latency_color(lat)
            print(col + f"  Avg: {lat:.1f}ms  [{q}]" + R)
    else:
        print(BYLW + "  Host tidak respon ping (ICMP mungkin diblokir)" + R)

    r_p1 = run_cmd(f"ping -c 1 -W 2 {t}", timeout=5)
    if r_p1 and r_p1.stdout:
        for line in r_p1.stdout.split("\n"):
            if "ttl=" in line.lower():
                try:
                    ttl = int(re.search(r"ttl=(\d+)", line, re.I).group(1))
                    os_g = ("Linux/Unix" if ttl <= 64 else
                             "Windows"   if ttl <= 128 else
                             "Network Device")
                    print(BYLW + f"  TTL {ttl}  →  {os_g}" + R)
                except Exception:
                    pass

    # ── 3. Port scan ────────────────────
    separator()
    section_title("3/6 · PORT SCAN", BCYN)
    open_p: list = []
    lock = threading.Lock()

    if ip:
        def pscan(p: int, svc: str):
            s = socket.socket()
            s.settimeout(0.6)
            if s.connect_ex((ip, p)) == 0:
                with lock:
                    banner   = grab_banner(ip, p)
                    b_str    = f"  {DIM}{banner[:40]}{R}" if banner else ""
                    is_risk  = p in HIGH_RISK_PORTS
                    col      = BRED if is_risk else BGRN
                    label    = "[HIGH-RISK]" if is_risk else ""
                    print(col + f"  ● {p:<6} {svc:<13} {label}" + R + b_str)
                    open_p.append(p)
            s.close()

        ths = [threading.Thread(target=pscan, args=(p, svc))
               for p, svc in COMMON_PORTS.items()]
        for th in ths: th.start()
        for th in ths: th.join()

        risky = [p for p in open_p if p in HIGH_RISK_PORTS]
        risk_score += len(risky) * 2
        if risky:
            findings.append(f"Port high-risk terbuka: {risky}")
        print(BCYN + f"\n  [{len(open_p)} port terbuka dari {len(COMMON_PORTS)}]" + R)

    # ── 4. HTTP Header ──────────────────
    separator()
    section_title("4/6 · HTTP HEADER", BCYN)
    if tool_check("curl"):
        r_hdr = run_cmd(f"curl -I -s --max-time 8 {url}")
        if r_hdr and r_hdr.stdout:
            sec_found = 0
            sec_keys  = ["strict-transport-security","content-security-policy",
                         "x-frame-options","x-content-type-options",
                         "referrer-policy","permissions-policy","x-xss-protection"]
            for line in r_hdr.stdout.split("\n")[:20]:
                ln = line.strip()
                if not ln:
                    continue
                low = ln.lower()
                if any(k in low for k in sec_keys):
                    sec_found += 1
                col = BYLW if any(x in low for x in ["server","powered"]) else ""
                print((col or "") + f"  {ln}" + R)
            missing = 7 - sec_found
            if missing > 3:
                risk_score += 2
                findings.append(f"{missing} security header hilang")
            print(BCYN + f"  Security headers: {sec_found}/7" + R)

    # ── 5. SSL ──────────────────────────
    separator()
    section_title("5/6 · SSL / TLS", BCYN)
    if tool_check("openssl"):
        r_ssl = run_cmd(
            f"echo | openssl s_client -connect {t}:443 -servername {t} 2>/dev/null"
        )
        if r_ssl and r_ssl.stdout:
            for line in r_ssl.stdout.split("\n"):
                line = line.strip()
                if "notAfter" in line:
                    try:
                        date_str = line.split("=", 1)[1].strip()
                        exp      = datetime.strptime(date_str, "%b %d %H:%M:%S %Y %Z")
                        sisa     = (exp - datetime.utcnow()).days
                        if sisa < 0:
                            risk_score += 5
                            findings.append("SSL EXPIRED")
                            print(BRED + f"  ✘ SSL EXPIRED! {date_str}" + R)
                        elif sisa < 30:
                            risk_score += 2
                            findings.append(f"SSL hampir expired ({sisa} hari)")
                            print(BYLW + f"  ⚠ SSL {sisa} hari lagi: {date_str}" + R)
                        else:
                            print(BGRN + f"  ✔ SSL OK — {sisa} hari lagi: {date_str}" + R)
                    except Exception:
                        print(f"  {line}")
                elif "Verify return code" in line:
                    ok  = "0 (ok)" in line.lower()
                    col = BGRN if ok else BRED
                    print(col + f"  {'✔' if ok else '✘'} {line}" + R)
        else:
            print(BRED + "  ✘ HTTPS tidak aktif / SSL gagal" + R)
            findings.append("HTTPS tidak aktif")
            risk_score += 3

    # ── 6. Summary ──────────────────────
    elapsed = round(time.time() - start_time, 1)
    separator()
    section_title("6/6 · SUMMARY", BCYN)

    print(BCYN + f"  Duration : {elapsed}s")
    print(f"  Target   : {t}")
    print(f"  IP       : {ip or 'N/A'}" + R)

    if findings:
        print(BRED + "\n  [!] FINDINGS:" + R)
        for item in findings:
            print(BRED + f"      • {item}" + R)

    risk_label = ("LOW" if risk_score < 3 else "MEDIUM" if risk_score < 7 else "HIGH")
    r_col      = (BGRN if risk_score < 3 else BYLW if risk_score < 7 else BRED)

    separator()
    print(r_col + BLD + f"  Risk Score : {risk_score}   [{risk_label}]" + R)
    separator()

    save_output_demo(t)
    print(BGRN + BLD + "\n  ✔ Full Security Report selesai!" + R)
    save_log(f"FULL REPORT {t} risk:{risk_label}({risk_score})")

# ══════════════════════════════════════════
#  AI VOICE
# ══════════════════════════════════════════

def ai_voice_mode():
    try:
        import pyttsx3
        engine = pyttsx3.init()
        text   = input(BCYN + "  AI Voice> " + R)
        engine.say(text)
        engine.runAndWait()
    except ImportError:
        print(BRED + "  [-] Voice tidak tersedia." + R)
        print(BYLW + "      Install: pip install pyttsx3" + R)
    except Exception as exc:
        print(BRED + f"  [-] Error: {exc}" + R)

# ══════════════════════════════════════════
#  SUB-MENUS
# ══════════════════════════════════════════

def menu_item(num: str, label: str, desc: str, col=BWHT):
    num_s  = BCYN + f"  [{num}]" + R
    lbl_s  = BLD + col + f"  {label:<18}" + R
    desc_s = DIM + WHT + desc + R
    print(f"{num_s}{lbl_s}{desc_s}")

def sub_menu_header(title: str, color=BCYN, icon="🔧"):
    clear_screen()
    kali_header(title, icon)

def sub_back():
    separator(color=DIM + BCYN)
    print(DIM + BCYN + "  [0]  ← Kembali ke Main Menu" + R)
    separator(color=DIM + BCYN)

def get_target(prompt: str = "Target") -> str:
    return input(BYLW + f"  {prompt}: " + R).strip()

# ── Network ────────────────────────────────────────────────────

def menu_network():
    while True:
        sub_menu_header("NETWORK TOOLS", BGRN, "🌐")
        menu_item("1", "Quick Info",  "Network info + latency + ports", BGRN)
        menu_item("2", "Multi Scan",  "Ping banyak target sekaligus",   BGRN)
        menu_item("3", "Trace Route", "Lacak rute hop ke target",       BGRN)
        menu_item("4", "Ping Target", "ICMP ping dengan statistik",     BGRN)
        menu_item("5", "Port Scan",   "Scan port + banner + risk",      BGRN)
        sub_back()

        p = input(prompt_str()).strip()
        if   p == "0": break
        elif p == "1":
            t = get_target()
            if t: quick_info(t)
        elif p == "2":
            raw = input(BYLW + "  Targets (pisah spasi): " + R).strip()
            if raw: fast_scan(raw.split())
        elif p == "3":
            t = get_target()
            if t: trace_route(t)
        elif p == "4":
            t = get_target()
            if t: ping_target(t)
        elif p == "5":
            t = get_target()
            if t: port_scan(t)
        else:
            print(BRED + "  [!] Pilihan tidak valid." + R)
            time.sleep(0.5)

# ── Web Intel ──────────────────────────────────────────────────

def menu_webintel():
    while True:
        sub_menu_header("WEB INTEL TOOLS", BCYN, "🌐")
        menu_item("6",  "Web Info",    "Header + DNS sekaligus",        BCYN)
        menu_item("7",  "HTTP Header", "Security header analysis",      BCYN)
        menu_item("8",  "Dir Scan",    "Brute-force direktori / path",  BCYN)
        menu_item("9",  "Subdomain",   "Enumerate subdomain aktif",     BCYN)
        menu_item("10", "SSL Check",   "Validasi sertifikat TLS",       BCYN)
        sub_back()

        p = input(prompt_str()).strip()
        if   p == "0": break
        elif p == "6":
            t = get_target("Web/Domain")
            if t:
                http_header_scan(normalize_url(t))
                clear_screen()
                kali_header("WEB INFO — DNS", "🌐")
                dns_lookup_raw(t)
                press_enter()
        elif p == "7":
            t = get_target("URL")
            if t: http_header_scan(normalize_url(t))
        elif p == "8":
            t = get_target("URL")
            if t: dir_bruteforce(normalize_url(t))
        elif p == "9":
            t = get_target("Domain")
            if t: subdomain_scan(t)
        elif p == "10":
            t = get_target("Domain")
            if t: ssl_check(t)
        else:
            print(BRED + "  [!] Pilihan tidak valid." + R)
            time.sleep(0.5)

# ── OSINT ──────────────────────────────────────────────────────

def menu_osint():
    while True:
        sub_menu_header("OSINT TOOLS", BYLW, "🕵️")
        menu_item("11", "WHOIS",      "Info registrasi domain",         BYLW)
        menu_item("12", "Geo IP",     "Lokasi & ISP dari IP/domain",   BYLW)
        menu_item("13", "DNS Lookup", "Semua DNS record (A/MX/NS/..)", BYLW)
        sub_back()

        p = input(prompt_str()).strip()
        if   p == "0":  break
        elif p == "11":
            t = get_target()
            if t: whois_lookup(t)
        elif p == "12":
            t = get_target("IP/Domain")
            if t: geo_ip(t)
        elif p == "13":
            t = get_target("Domain")
            if t: dns_lookup_menu(t)
        else:
            print(BRED + "  [!] Pilihan tidak valid." + R)
            time.sleep(0.5)

# ── System ─────────────────────────────────────────────────────

def menu_system():
    while True:
        sub_menu_header("SYSTEM TOOLS", BGRN, "💻")
        menu_item("14", "Firewall",   "Cek iptables / UFW / nftables", BGRN)
        menu_item("15", "System Info","OS, RAM, Disk, IP, Proses",     BGRN)
        sub_back()

        p = input(prompt_str()).strip()
        if   p == "0":  break
        elif p == "14": firewall_check()
        elif p == "15": system_info()
        else:
            print(BRED + "  [!] Pilihan tidak valid." + R)
            time.sleep(0.5)

# ── Advanced ───────────────────────────────────────────────────

def menu_advanced():
    while True:
        sub_menu_header("ADVANCED TOOLS", BMAG, "🗡️")
        menu_item("16", "Nmap Scan",  "6 mode scan nmap lengkap",      BMAG)
        menu_item("17", "Full Report","Security audit menyeluruh",      BMAG)
        menu_item("18", "Save Output","Simpan hasil scan ke file",      BMAG)
        sub_back()

        p = input(prompt_str()).strip()
        if   p == "0":  break
        elif p == "16":
            t = get_target()
            if t: advanced_scan(t)
        elif p == "17":
            t = get_target()
            if t: security_report(t)
        elif p == "18":
            t = get_target()
            if t:
                clear_screen()
                kali_header("SAVE OUTPUT", "💾")
                save_output_demo(t)
                press_enter()
        else:
            print(BRED + "  [!] Pilihan tidak valid." + R)
            time.sleep(0.5)

# ── AI Tools ───────────────────────────────────────────────────

def menu_aitools():
    while True:
        sub_menu_header("AI TOOLS", BCYN, "🤖")
        menu_item("19", "AI Voice",  "Text-to-speech via pyttsx3",     BCYN)
        menu_item("20", "Fast Scan", "Ping paralel banyak target",      BCYN)
        sub_back()

        p = input(prompt_str()).strip()
        if   p == "0":  break
        elif p == "19":
            ai_voice_mode()
            press_enter()
        elif p == "20":
            raw = input(BYLW + "  Targets (pisah spasi): " + R).strip()
            if raw: fast_scan(raw.split())
        else:
            print(BRED + "  [!] Pilihan tidak valid." + R)
            time.sleep(0.5)

# ══════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════

def main_menu():
    while True:
        clear_screen()
        now = datetime.now()

        # Status bar
        print(rcolor() + BLD + f"""
  ┌{'─'*W}┐
  │  ⚡ SYSTEM LIVE  ·  {now:%H:%M:%S}  ·  SKYWINGS ACTIVE{' '*(W-49)}│
  └{'─'*W}┘
""" + R)

        cats = [
            ("1", "🌐", "NETWORK",   "Scan jaringan & port",      BGRN),
            ("2", "🌍", "WEB INTEL", "Analisa web, header, SSL",  BCYN),
            ("3", "🕵️", "OSINT",     "WHOIS, GeoIP, DNS",        BYLW),
            ("4", "💻", "SYSTEM",    "Info OS, firewall, proses", BGRN),
            ("5", "🗡️", "ADVANCED",  "Nmap, full report, save",  BMAG),
            ("6", "🤖", "AI TOOLS",  "Voice, fast scan AI",       BCYN),
        ]

        for num, ico, name, desc, col in cats:
            print(
                col + BLD + f"  [{num}] {ico}  {name:<12}" + R +
                DIM + WHT + f"  {desc}" + R
            )

        separator(color=DIM + BCYN)
        print(BRED + "  [0]  EXIT" + R)
        separator(color=DIM + BCYN)

        p = input(prompt_str()).strip()

        dispatch = {
            "1": ("ENTERING NETWORK",   menu_network),
            "2": ("ENTERING WEB INTEL", menu_webintel),
            "3": ("ENTERING OSINT",     menu_osint),
            "4": ("ENTERING SYSTEM",    menu_system),
            "5": ("ENTERING ADVANCED",  menu_advanced),
            "6": ("ENTERING AI TOOLS",  menu_aitools),
        }

        if p in dispatch:
            label, fn = dispatch[p]
            loading_bar(label)
            fn()
        elif p == "0":
            print(rcolor() + "\n  ✦ SKYWINGS DOWN. Stay safe.\n" + R)
            break
        else:
            print(BRED + "  [!] Pilihan tidak valid." + R)
            time.sleep(0.5)

# ══════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════

def main():
    try:
        show_logo()
        loading_bar("SKYWINGS v2.0 BOOTING", delay=0.02)
        print()

        while True:
            kali_header("SKYWINGS v2.0  —  by Putra", "🔰")

            box_top(BCYN)
            box_left("  help    →  masuk menu fitur", BCYN, BWHT)
            box_left("  info    →  system info",      BCYN, BWHT)
            box_left("  clear   →  bersihkan layar",  BCYN, BWHT)
            box_left("  exit    →  keluar",            BCYN, BWHT)
            box_bot(BCYN)
            print()

            cmd = input(prompt_str()).strip().lower()

            if cmd == "help":
                loading_bar("ENTERING FEATURE MODE")
                main_menu()
            elif cmd == "info":
                system_info()
            elif cmd == "clear":
                clear_screen()
            elif cmd == "exit":
                print(rcolor() + "\n  ✦ SKYWINGS. Stay safe.\n" + R)
                break
            else:
                print(BRED + "  [-] Command tidak dikenal. Ketik 'help'." + R)

    except KeyboardInterrupt:
        print(rcolor() + "\n\n  ✦ Interrupted. SKYWINGS DOWN.\n" + R)

if __name__ == "__main__":
    main()
