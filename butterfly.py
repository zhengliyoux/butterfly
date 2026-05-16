import os
import time
import random
import socket
import platform
import threading
import subprocess
import json
import ssl
import re
import ipaddress
from datetime import datetime

# ================= STYLE =================
RESET   = "\033[0m"
GREEN   = "\033[1;32m"
CYAN    = "\033[1;36m"
RED     = "\033[1;31m"
YELLOW  = "\033[1;33m"
BOLD    = "\033[1m"
MAGENTA = "\033[1;35m"
WHITE   = "\033[1;37m"
BLUE    = "\033[1;34m"
DIM     = "\033[2m"
BG_DARK = "\033[48;5;234m"

LOG_FILE = "skywings_output.log"

# ================= SAFE RUN =================
def run(cmd, timeout=15):
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        print(RED + f"[TIMEOUT] Command habis waktu: {cmd[:40]}" + RESET)
        return None
    except Exception as e:
        print(RED + f"[ERROR] {e}" + RESET)
        return None

# ================= HELPER =================
def normalize_url(url):
    url = url.strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url

def tool_check(tool):
    r = run(f"which {tool}")
    if not r or not r.stdout.strip():
        print(RED + f"[!] '{tool}' belum terinstall." + RESET)
        install_map = {
            "nmap":       "pkg install nmap",
            "whois":      "pkg install whois",
            "traceroute": "pkg install traceroute",
            "curl":       "pkg install curl",
            "openssl":    "pkg install openssl",
            "dig":        "pkg install dnsutils",
        }
        hint = install_map.get(tool)
        if hint:
            print(YELLOW + f"    Install: {hint}" + RESET)
        return False
    return True

def is_valid_target(target):
    return bool(target and target.strip())

def is_ip(target):
    try:
        ipaddress.ip_address(target.strip())
        return True
    except ValueError:
        return False

def get_ip(target):
    try:
        return socket.gethostbyname(target.strip())
    except socket.gaierror:
        return None

def get_all_ips(target):
    try:
        infos = socket.getaddrinfo(target.strip(), None)
        ips = list(dict.fromkeys([i[4][0] for i in infos]))
        return ips
    except:
        return []

def strip_scheme(url):
    return url.strip().replace("https://","").replace("http://","").split("/")[0]

def print_sep(char="─", color=CYAN, width=50):
    print(color + "  " + char * width + RESET)

def save_log(data):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {data}\n")
    except Exception as e:
        print(RED + f"[LOG ERROR] {e}" + RESET)

def format_bytes(size):
    try:
        size = int(size)
        for unit in ['B','KB','MB','GB']:
            if size < 1024:
                return f"{size:.1f}{unit}"
            size /= 1024
        return f"{size:.1f}TB"
    except:
        return f"{size}B"

def calc_latency(host, count=3):
    r = run(f"ping -c {count} -W 2 {host}", timeout=count*3+5)
    if not r or r.returncode != 0:
        return None
    for line in r.stdout.split("\n"):
        if "rtt" in line or "round-trip" in line:
            try:
                avg = line.split("/")[4]
                return float(avg)
            except:
                pass
    return None

# ================= AI COLOR =================
COLORS = [
    "\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m",
    "\033[1;35m","\033[1;36m","\033[38;5;208m",
    "\033[38;5;201m","\033[38;5;51m","\033[38;5;46m",
]

def ai_color():
    return random.choice(COLORS)

def clear():
    os.system("clear")

# ================= LOADING =================
def loading(teks):
    bar_width = 30
    for i in range(0, 101, 2):
        filled = int(bar_width * i / 100)
        bar = "█" * filled + "░" * (bar_width - filled)
        print(f"\r  {CYAN}[{bar}]{RESET} {ai_color()}{i:3d}%{RESET}  {DIM}{teks}...{RESET}", end="")
        time.sleep(0.02)
    print(f"\r  {GREEN}[{'█'*bar_width}]{RESET} {GREEN}100%{RESET}  {teks}... {GREEN}DONE{RESET}     ")

def fancy_loading(text):
    bar_width = 30
    for i in range(1, 101):
        filled = int(bar_width * i / 100)
        bar = "█" * filled + "░" * (bar_width - filled)
        print(f"\r  {CYAN}[{bar}]{RESET} {ai_color()}{i:3d}%{RESET}  {text}", end="")
        time.sleep(0.012)
    print()

# ================= PROMPT =================
def skywings_codex():
    return (
        "\n  " +
        BOLD + "\033[38;5;51m" + "╔══" + RESET +
        BOLD + "\033[38;5;201m" + "SkyWings" + RESET +
        CYAN + "@" + RESET +
        GREEN + "root" + RESET +
        RED + " ➤ " + RESET
    )

# ================= UI =================
W = 52

def kali_header(title):
    color = CYAN
    now = datetime.now().strftime("%H:%M:%S")
    top    = "╔" + "═" * W + "╗"
    mid    = f"║  {'🔐 SkyWings':^5}  ::  {title:<30}  ║"
    bot    = "╚" + "═" * W + "╝"
    print()
    print(color + BOLD + f"  {top}")
    print(f"  {mid}")
    print(f"  {bot}" + RESET)
    print()

def line_fx():
    print(ai_color() + "  " + "═"*W + RESET)

def section_title(text, icon="◈"):
    print()
    print(f"  {BOLD}{CYAN}{icon} {text}{RESET}")
    print(f"  {DIM}{'─'*W}{RESET}")

# ================= SCREEN MODE =================
def enter_back():
    print()
    print_sep("─", DIM, W)
    input(f"  {YELLOW}[ ↵  Tekan ENTER untuk kembali ]{RESET} ")

def screen_mode(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            clear()
            kali_header(title)
            result = func(*args, **kwargs)
            enter_back()
            return result
        return wrapper
    return decorator

# ================= LOGO =================
def logo():
    clear()

    frames = [
        "\033[38;5;51m",
        "\033[38;5;45m",
        "\033[38;5;39m",
        "\033[38;5;33m",
        "\033[38;5;201m",
        "\033[38;5;207m",
    ]
    c = random.choice(frames)
    c2 = random.choice(frames)

    print()
    print(c + BOLD + r"""
   ███████╗██╗  ██╗██╗   ██╗
   ██╔════╝██║ ██╔╝╚██╗ ██╔╝
   ███████╗█████╔╝  ╚████╔╝
   ╚════██║██╔═██╗   ╚██╔╝
   ███████║██║  ██╗   ██║
   ╚══════╝╚═╝  ╚═╝   ╚═╝
""" + RESET)

    print(c2 + BOLD + r"""
  ██╗    ██╗██╗███╗   ██╗ ██████╗ ███████╗
  ██║    ██║██║████╗  ██║██╔════╝ ██╔════╝
  ██║ █╗ ██║██║██╔██╗ ██║██║  ███╗███████╗
  ██║███╗██║██║██║╚██╗██║██║   ██║╚════██║
  ╚███╔███╔╝██║██║ ╚████║╚██████╔╝███████║
   ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
""" + RESET)

    print(f"  {CYAN}{'═'*52}{RESET}")
    print(f"  {BOLD}{CYAN}  🔐  SYSTEM INITIALIZED  ::  SKYWINGS ACTIVE{RESET}")
    print(f"  {CYAN}{'═'*52}{RESET}")
    print()

    info_lines = [
        ("Script by",  "SkyWings"),
        ("Version",    "v1.1  ·  Wings Point O"),
        ("System",     "Termux CLI"),
        ("Status",     "🟢 ONLINE"),
    ]
    for k, v in info_lines:
        print(f"  {DIM}{k:<12}{RESET}{YELLOW}{v}{RESET}")

    print()

# ============================================================
#  FEATURES
# ============================================================

COMMON_PORTS = {
    21:"FTP",      22:"SSH",       23:"TELNET",
    25:"SMTP",     53:"DNS",       80:"HTTP",
    110:"POP3",   143:"IMAP",    443:"HTTPS",
    445:"SMB",    587:"SMTP-TLS",993:"IMAPS",
    995:"POP3S", 1433:"MSSQL",  3306:"MYSQL",
    3389:"RDP",  5432:"PGSQL",  5900:"VNC",
    6379:"REDIS",8080:"HTTP-ALT",8443:"HTTPS-ALT",
    8888:"JUPYTER",27017:"MONGODB",
}

def grab_banner(ip, port, timeout=2.0):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, port))
        probes = {
            80:  b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n",
            8080:b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n",
            8443:b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n",
            21:  None,
            22:  None,
            25:  None,
            110: None,
            143: None,
            3306:None,
        }
        probe = probes.get(port, b"\r\n")
        if probe:
            s.send(probe)
        banner = s.recv(512).decode(errors="ignore").strip()
        s.close()
        lines = [l.strip() for l in banner.split("\n") if l.strip()]
        result = lines[0] if lines else ""
        return result[:100] if result else None
    except:
        return None

def dns_lookup_raw(target):
    target = target.strip()
    ip = get_ip(target)
    if ip:
        print(f"  {GREEN}◉ DNS-A   {RESET}{CYAN}{target}{RESET}  →  {WHITE}{ip}{RESET}")
        try:
            rev = socket.gethostbyaddr(ip)
            if rev and rev[0] and rev[0] != target:
                print(f"  {CYAN}◉ rDNS    {RESET}{ip}  →  {WHITE}{rev[0]}{RESET}")
        except:
            pass
        save_log(f"DNS {target}->{ip}")
        return ip
    else:
        print(f"  {RED}✗ DNS     Gagal resolve: {target}{RESET}")
        return None

@screen_mode("DNS LOOKUP")
def dns_lookup_menu(target):
    target = target.strip()
    if not is_valid_target(target):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return

    section_title("Resolving Target")
    ip = dns_lookup_raw(target)

    all_ips = get_all_ips(target)
    if len(all_ips) > 1:
        print(f"  {CYAN}◉ All IPs {RESET}{', '.join(all_ips)}")

    try:
        info = socket.getaddrinfo(target, None, socket.AF_INET6)
        if info:
            ipv6 = info[0][4][0]
            print(f"  {CYAN}◉ IPv6    {RESET}{ipv6}")
    except:
        pass

    if not ip:
        return

    if tool_check("whois"):
        r_asn = run(f"whois -h whois.cymru.com ' -v {ip}' 2>/dev/null", timeout=8)
        if r_asn and r_asn.stdout.strip():
            lines = [l for l in r_asn.stdout.strip().split("\n") if l.strip() and not l.startswith("AS")]
            if lines:
                print(f"  {YELLOW}◉ ASN     {RESET}{lines[0].strip()}")

    print_sep()

    if tool_check("dig"):
        record_types = ["A","AAAA","MX","NS","TXT","CNAME","SOA"]
        for rtype in record_types:
            r = run(f"dig {target} {rtype} +noall +answer +time=3 2>/dev/null", timeout=8)
            if r and r.stdout.strip():
                section_title(f"{rtype} Records", "◈")
                for line in r.stdout.strip().split("\n")[:10]:
                    print(f"    {DIM}{line}{RESET}")
    else:
        r = run(f"nslookup {target} 2>/dev/null")
        if r and r.stdout.strip():
            section_title("NSLookup")
            print(r.stdout[:800])

@screen_mode("QUICK NETWORK INFO")
def quick_info(target):
    target = target.strip()
    if not is_valid_target(target):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return

    ip = get_ip(target)
    is_private = False
    if ip:
        try:
            is_private = ipaddress.ip_address(ip).is_private
        except:
            pass

    section_title("Target Information")
    print(f"  {DIM}{'Target':<12}{RESET}{WHITE}{target}{RESET}")
    print(f"  {DIM}{'IP':<12}{RESET}{WHITE}{ip or 'Gagal resolve'}{RESET}")
    if ip:
        type_label = "Private / LAN" if is_private else "Public"
        type_color = YELLOW if is_private else GREEN
        print(f"  {DIM}{'Type':<12}{RESET}{type_color}{type_label}{RESET}")

    print_sep()

    section_title("Ping Test  (4 packets)")
    r = run(f"ping -c 4 -W 2 {target}", timeout=20)
    if r and r.returncode == 0 and r.stdout:
        for line in r.stdout.strip().split("\n"):
            if "time=" in line:
                try:
                    ms_val = float(re.search(r"time=([\d.]+)", line).group(1))
                    color = GREEN if ms_val < 50 else (YELLOW if ms_val < 150 else RED)
                    print(f"  {color}{line.strip()}{RESET}")
                except:
                    print(f"  {GREEN}{line.strip()}{RESET}")
            elif "rtt" in line or "packet" in line:
                print(f"  {GREEN}{line.strip()}{RESET}")
    else:
        print(f"  {RED}✗ Host tidak reachable  (ICMP mungkin diblokir){RESET}")

    lat = calc_latency(target)
    if lat is not None:
        q = "Excellent" if lat < 20 else ("Good" if lat < 80 else ("Fair" if lat < 150 else "Poor"))
        color = GREEN if lat < 80 else (YELLOW if lat < 150 else RED)
        print(f"\n  {color}◉ Avg Latency : {lat:.1f} ms  [{q}]{RESET}")

    print_sep()
    section_title("DNS")
    dns_lookup_raw(target)
    all_ips = get_all_ips(target)
    if len(all_ips) > 1:
        print(f"  {CYAN}◉ Multi-IP  {RESET}{', '.join(all_ips[:5])}")

    print_sep()
    section_title("Quick Port Check")
    if ip:
        critical_ports = [(80,"HTTP"),(443,"HTTPS"),(22,"SSH"),(21,"FTP"),(3306,"MYSQL"),(3389,"RDP")]
        for p, svc in critical_ports:
            s = socket.socket()
            s.settimeout(1)
            t_start = time.time()
            status = "OPEN" if s.connect_ex((ip, p)) == 0 else "CLOSED"
            t_ms = round((time.time()-t_start)*1000,1)
            s.close()
            if status == "OPEN":
                print(f"  {GREEN}● OPEN   {p:5}  {svc:<12}  {t_ms}ms{RESET}")
            else:
                print(f"  {RED}○ CLOSED {p:5}  {svc}{RESET}")

    print_sep()
    section_title("TTL / OS Fingerprint")
    r2 = run(f"ping -c 1 -W 2 {target}", timeout=5)
    if r2 and r2.stdout:
        for line in r2.stdout.split("\n"):
            if "ttl=" in line.lower():
                try:
                    ttl = int(re.search(r"ttl=(\d+)", line, re.I).group(1))
                    if ttl <= 64:
                        os_guess = "Linux / Unix / Android"
                    elif ttl <= 128:
                        os_guess = "Windows"
                    else:
                        os_guess = "Cisco / Network Device"
                    print(f"  {YELLOW}◉ TTL : {ttl}  →  {os_guess}{RESET}")
                except:
                    pass

@screen_mode("PORT SCAN")
def port_scan(target):
    target = target.strip()
    if not is_valid_target(target):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    ip = get_ip(target)
    if not ip:
        print(f"  {RED}✗ Tidak bisa resolve: {target}{RESET}")
        return

    section_title("Scan Configuration")
    print(f"  {DIM}{'Target':<12}{RESET}{WHITE}{target}  ({ip}){RESET}")
    print(f"  {DIM}{'Ports':<12}{RESET}{WHITE}{len(COMMON_PORTS)} common + custom{RESET}")
    print(f"  {DIM}{'Mode':<12}{RESET}{WHITE}Threaded · Banner Grab · Risk Label{RESET}")

    print()
    print(f"  {YELLOW}Tambah custom port? contoh: 8888,9090  /  Enter = skip{RESET}")
    extra = input(f"  {DIM}> {RESET}").strip()
    extra_ports = {}
    if extra:
        for ep in extra.split(","):
            ep = ep.strip()
            if ep.isdigit():
                extra_ports[int(ep)] = "CUSTOM"

    all_ports = {**COMMON_PORTS, **extra_ports}
    open_ports = []
    lock = threading.Lock()

    HIGH_RISK = {21,23,3389,5900,6379,27017,1433,3306}
    MED_RISK  = {22,25,80,8080,8443,445,5432}

    print_sep()
    print(f"  {BOLD}{WHITE}{'STATUS':<10}{'PORT':<8}{'SERVICE':<15}{'RESP':>7}  INFO{RESET}")
    print_sep("─", DIM, W)

    def check_port(p, svc):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.8)
            t0 = time.time()
            res = s.connect_ex((ip, p))
            resp_ms = round((time.time()-t0)*1000, 1)
            s.close()
            with lock:
                if res == 0:
                    banner = grab_banner(ip, p)
                    b_str = f"  {DIM}{banner}{RESET}" if banner else ""
                    if p in HIGH_RISK:
                        risk_tag = f" {RED}[HIGH-RISK]{RESET}"
                    elif p in MED_RISK:
                        risk_tag = f" {YELLOW}[MED]{RESET}"
                    else:
                        risk_tag = ""
                    print(f"  {GREEN}● OPEN   {RESET}{p:<8}{svc:<15}{resp_ms:>6.1f}ms{risk_tag}{b_str}")
                    open_ports.append(p)
                    save_log(f"PORT OPEN {target}:{p} ({svc})")
                else:
                    print(f"  {RED}○ CLOSED {RESET}{p:<8}{svc}{RESET}")
        except Exception as e:
            with lock:
                print(f"  {RED}✗ ERROR  {p:<8}{e}{RESET}")

    threads = []
    for p, svc in sorted(all_ports.items()):
        th = threading.Thread(target=check_port, args=(p, svc))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()

    print_sep()
    print(f"\n  {CYAN}◉ Selesai :  {WHITE}{len(open_ports)}{CYAN} / {len(all_ports)} port terbuka{RESET}")
    if open_ports:
        print(f"  {GREEN}◉ Open    :  {sorted(open_ports)}{RESET}")
        high = [p for p in open_ports if p in HIGH_RISK]
        if high:
            print(f"  {RED}⚠ HIGH-RISK port terbuka :  {high}{RESET}")

@screen_mode("PING TARGET")
def ping_target(target):
    target = target.strip()
    if not is_valid_target(target):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    print(f"  {YELLOW}Jumlah paket (1–50, default 5) :{RESET}")
    c = input(f"  {DIM}> {RESET}").strip()
    count = int(c) if c.isdigit() and 1 <= int(c) <= 50 else 5
    print(f"\n  {CYAN}◉ Ping  {target}  ×{count}...{RESET}\n")

    r = run(f"ping -c {count} {target}", timeout=count*3+5)
    if r and r.returncode == 0 and r.stdout:
        times = []
        for line in r.stdout.split("\n"):
            if "time=" in line:
                try:
                    ms = float(re.search(r"time=([\d.]+)", line).group(1))
                    times.append(ms)
                    color = GREEN if ms < 50 else (YELLOW if ms < 150 else RED)
                    print(f"  {color}{line.strip()}{RESET}")
                except:
                    print(f"  {line.strip()}")
            elif line.strip():
                print(f"  {DIM}{line.strip()}{RESET}")

        if len(times) >= 2:
            print_sep()
            section_title("Statistics")
            print(f"  {DIM}{'Min':<10}{RESET}{WHITE}{min(times):.2f} ms{RESET}")
            print(f"  {DIM}{'Max':<10}{RESET}{WHITE}{max(times):.2f} ms{RESET}")
            print(f"  {DIM}{'Avg':<10}{RESET}{WHITE}{sum(times)/len(times):.2f} ms{RESET}")
            jitter = max(times) - min(times)
            jitter_q = "Stabil" if jitter < 10 else ("OK" if jitter < 50 else "Tidak Stabil")
            color = GREEN if jitter < 10 else (YELLOW if jitter < 50 else RED)
            print(f"  {DIM}{'Jitter':<10}{RESET}{color}{jitter:.2f} ms  [{jitter_q}]{RESET}")

        for line in r.stdout.split("\n"):
            if "packet loss" in line or "received" in line:
                match = re.search(r"(\d+)% packet loss", line)
                if match:
                    loss = int(match.group(1))
                    color = GREEN if loss == 0 else (YELLOW if loss < 20 else RED)
                    print(f"  {DIM}{'Loss':<10}{RESET}{color}{loss}%{RESET}")
    else:
        print(f"  {RED}✗ Ping gagal.  Host mungkin blokir ICMP.{RESET}")

@screen_mode("TRACE ROUTE")
def trace_route(target):
    target = target.strip()
    if not is_valid_target(target):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    if not tool_check("traceroute"):
        return
    print(f"  {CYAN}◉ Tracing route ke {target}  (max 20 hop)...{RESET}\n")

    r = run(f"traceroute -m 20 -w 2 {target}", timeout=90)
    if r and r.stdout.strip():
        timeout_hops = 0
        for line in r.stdout.strip().split("\n"):
            if "* * *" in line:
                timeout_hops += 1
                print(f"  {RED}{line}  ← timeout / filtered{RESET}")
            else:
                ms_vals = re.findall(r"([\d.]+) ms", line)
                if ms_vals:
                    avg_hop = sum(float(v) for v in ms_vals) / len(ms_vals)
                    color = GREEN if avg_hop < 50 else (YELLOW if avg_hop < 150 else RED)
                    print(f"  {color}{line}{RESET}")
                else:
                    print(f"  {DIM}{line}{RESET}")
        if timeout_hops > 5:
            print(f"\n  {YELLOW}⚠ {timeout_hops} hop timeout — kemungkinan ada firewall di tengah rute.{RESET}")
    else:
        print(f"  {RED}✗ Traceroute gagal.{RESET}")

@screen_mode("NMAP SCANNER")
def advanced_scan(target):
    target = target.strip()
    if not is_valid_target(target):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    if not tool_check("nmap"):
        return

    section_title("Pilih Mode Scan")
    options = [
        ("1", "Fast scan",       "-F --open",                   GREEN),
        ("2", "Service version", "-sV --version-intensity 5",   CYAN),
        ("3", "OS Detection",    "-O",                           YELLOW),
        ("4", "Full + Script",   "-A",                           MAGENTA),
        ("5", "UDP Scan",        "-sU -F",                       BLUE),
        ("6", "Stealth SYN",     "-sS -F",                       RED),
    ]
    for num, label, flag, col in options:
        print(f"  {col}  [{num}]  {label:<18}{DIM}{flag}{RESET}")

    print()
    mode = input(skywings_codex()).strip()
    flags = {
        "1":"-F --open",
        "2":"-sV --version-intensity 5",
        "3":"-O",
        "4":"-A",
        "5":"-sU -F",
        "6":"-sS -F",
    }.get(mode, "-F --open")

    print(f"\n  {CYAN}◉ Nmap  {target}  [{flags}]{RESET}\n")
    result = run(f"nmap {flags} {target}", timeout=120)
    if result and result.stdout:
        for line in result.stdout.split("\n"):
            if "open" in line.lower():
                print(f"  {GREEN}{line}{RESET}")
            elif "filtered" in line.lower() or "closed" in line.lower():
                print(f"  {RED}{line}{RESET}")
            else:
                print(f"  {DIM}{line}{RESET}")
        save_log(f"NMAP {target}: {flags}")
    else:
        print(f"  {RED}✗ Nmap gagal.{RESET}")

@screen_mode("FIREWALL CHECK")
def firewall_check():
    section_title("iptables")
    r = run("iptables -L -n -v 2>/dev/null")
    if r and r.stdout.strip():
        print(r.stdout[:2000])
    else:
        print(f"  {YELLOW}⚠ iptables tidak aktif / butuh root.{RESET}")

    ufw = run("ufw status verbose 2>/dev/null")
    if ufw and ufw.stdout.strip():
        section_title("UFW")
        print(ufw.stdout[:500])

    nft = run("nft list ruleset 2>/dev/null")
    if nft and nft.stdout.strip():
        section_title("nftables")
        print(nft.stdout[:500])

def save_output_demo(target):
    target = target.strip()
    if not is_valid_target(target):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    try:
        ip = get_ip(target)
        with open("scan_result.txt", "a") as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Time   : {datetime.now()}\n")
            f.write(f"Target : {target}\n")
            f.write(f"IP     : {ip or 'Gagal resolve'}\n")
            if ip:
                f.write("Ports  :\n")
                for p, svc in sorted(COMMON_PORTS.items()):
                    s = socket.socket()
                    s.settimeout(0.5)
                    if s.connect_ex((ip, p)) == 0:
                        f.write(f"  OPEN {p} ({svc})\n")
                    s.close()
        print(f"  {GREEN}◉ Saved  →  scan_result.txt{RESET}")
        save_log(f"SAVED {target}")
    except Exception as e:
        print(f"  {RED}✗ Gagal save: {e}{RESET}")

@screen_mode("SYSTEM INFO")
def system_info():
    section_title("OS & Machine")
    info = [
        ("OS",       f"{platform.system()} {platform.release()}"),
        ("Version",  platform.version()[:60]),
        ("Node",     platform.node()),
        ("Machine",  platform.machine()),
        ("CPU",      platform.processor() or "N/A"),
    ]
    for k, v in info:
        print(f"  {DIM}{k:<12}{RESET}{WHITE}{v}{RESET}")

    try:
        print(f"  {DIM}{'Local IP':<12}{RESET}{GREEN}{socket.gethostbyname(socket.gethostname())}{RESET}")
    except:
        pass

    if tool_check("curl"):
        r = run("curl -s --max-time 5 ifconfig.me 2>/dev/null")
        if r and r.stdout.strip():
            print(f"  {DIM}{'Public IP':<12}{RESET}{CYAN}{r.stdout.strip()}{RESET}")

    mem = run("free -h 2>/dev/null")
    if mem and mem.stdout:
        section_title("Memory")
        print(mem.stdout)

    disk = run("df -h 2>/dev/null")
    if disk and disk.stdout:
        section_title("Disk Usage")
        for l in disk.stdout.strip().split("\n")[:5]:
            print(f"  {l}")

    up = run("uptime 2>/dev/null")
    if up and up.stdout:
        print(f"\n  {DIM}{'Uptime':<12}{RESET}{WHITE}{up.stdout.strip()}{RESET}")

    ifconfig = run("ip addr show 2>/dev/null || ifconfig 2>/dev/null")
    if ifconfig and ifconfig.stdout:
        section_title("Network Interfaces")
        for line in ifconfig.stdout.split("\n"):
            if "inet " in line or ": <" in line or "flags" in line:
                print(f"  {DIM}{line.strip()}{RESET}")

    top_r = run("ps aux --sort=-%cpu 2>/dev/null | head -6")
    if top_r and top_r.stdout:
        section_title("Top Processes  (CPU)")
        for l in top_r.stdout.strip().split("\n"):
            print(f"  {l}")

@screen_mode("FAST SCAN")
def fast_scan(targets):
    if not targets:
        print(f"  {RED}✗ Tidak ada target.{RESET}")
        return
    results = {}
    lock = threading.Lock()

    def scan(t):
        t = t.strip()
        if not t:
            return
        start = time.time()
        r = run(f"ping -c 1 -W 1 {t}", timeout=5)
        ms = round((time.time()-start)*1000, 1)
        ip = get_ip(t)
        with lock:
            if r and r.returncode == 0:
                open_p = []
                for p in [80, 443, 22]:
                    s = socket.socket()
                    s.settimeout(0.5)
                    if ip and s.connect_ex((ip, p)) == 0:
                        open_p.append(p)
                    s.close()
                port_str = f"  {DIM}ports:{open_p}{RESET}" if open_p else ""
                results[t] = ("UP", ip)
                print(f"  {GREEN}● UP    {t:<24}→  {ip or '?':<18} {ms}ms{port_str}{RESET}")
            else:
                results[t] = ("DOWN", None)
                print(f"  {RED}○ DOWN  {t}{RESET}")

    print(f"  {CYAN}◉ Scanning {len(targets)} target parallel...\n{RESET}")
    print_sep("─", DIM, W)
    threads = [threading.Thread(target=scan, args=(t,)) for t in targets]
    for th in threads: th.start()
    for th in threads: th.join()

    up = sum(1 for v in results.values() if v[0]=="UP")
    print_sep()
    print(f"  {CYAN}◉ {WHITE}{up}{CYAN} / {len(targets)} host aktif.{RESET}")

@screen_mode("WHOIS")
def whois_lookup(t):
    t = strip_scheme(t)
    if not is_valid_target(t):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    if not tool_check("whois"):
        return
    print(f"  {CYAN}◉ WHOIS  {t}...{RESET}\n")

    r = run(f"whois {t}", timeout=20)
    if r and r.stdout.strip():
        lines = [l for l in r.stdout.split("\n") if l.strip() and not l.startswith("%")]
        important_keys = ["registrar","name server","expir","creat","updat","status","registrant","dnssec","tech","admin"]
        seen = set()
        for line in lines[:120]:
            key = line.split(":")[0].lower().strip() if ":" in line else ""
            if key in seen:
                continue
            if any(x in key for x in important_keys):
                seen.add(key)
                if "expir" in key:
                    try:
                        date_part = line.split(":",1)[1].strip()
                        for fmt in ["%Y-%m-%dT%H:%M:%SZ","%Y-%m-%d","%d-%b-%Y"]:
                            try:
                                exp_date = datetime.strptime(date_part[:10], fmt[:len(date_part[:10])])
                                days_left = (exp_date - datetime.utcnow()).days
                                if days_left < 0:
                                    print(f"  {RED}◉ {line}  ← EXPIRED {abs(days_left)} hari lalu!{RESET}")
                                elif days_left < 30:
                                    print(f"  {YELLOW}◉ {line}  ← {days_left} hari lagi!{RESET}")
                                else:
                                    print(f"  {GREEN}◉ {line}  ({days_left} hari lagi){RESET}")
                                break
                            except:
                                continue
                        else:
                            print(f"  {YELLOW}{line}{RESET}")
                    except:
                        print(f"  {YELLOW}{line}{RESET}")
                else:
                    print(f"  {YELLOW}{line}{RESET}")
            else:
                print(f"  {DIM}{line}{RESET}")
        save_log(f"WHOIS {t}")
    else:
        print(f"  {RED}✗ WHOIS gagal.{RESET}")

@screen_mode("GEO IP")
def geo_ip(t):
    t = strip_scheme(t)
    if not is_valid_target(t):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    if not tool_check("curl"):
        return
    ip = get_ip(t)
    query = ip if ip else t
    print(f"  {CYAN}◉ GeoIP  {t}  →  {query}{RESET}\n")

    r = run(f"curl -s --max-time 10 ipinfo.io/{query}")
    if r and r.stdout.strip():
        try:
            data = json.loads(r.stdout)
            if data.get("bogon"):
                print(f"  {YELLOW}⚠ IP private/bogon — tidak ada geo info.{RESET}")
                return
            print_sep()
            fields = [
                ("IP",        "ip"),
                ("Hostname",  "hostname"),
                ("Kota",      "city"),
                ("Region",    "region"),
                ("Negara",    "country"),
                ("Lokasi",    "loc"),
                ("ISP / ORG", "org"),
                ("Postal",    "postal"),
                ("Timezone",  "timezone"),
            ]
            for label, key in fields:
                val = data.get(key, "N/A")
                color = WHITE if val and val != "N/A" else RED
                print(f"  {DIM}{label:<12}{RESET}{color}{val}{RESET}")

            loc = data.get("loc","")
            if loc:
                lat, lon = loc.split(",")
                print(f"\n  {CYAN}◉ Maps  →  https://maps.google.com/?q={lat},{lon}{RESET}")

            org = data.get("org","")
            hosting_keywords = ["hosting","server","cloud","datacenter","vps","aws","azure","google","digitalocean","linode","vultr","ovh"]
            if any(kw in org.lower() for kw in hosting_keywords):
                print(f"  {YELLOW}⚠ Kemungkinan Hosting / VPN / Cloud{RESET}")

            save_log(f"GEOIP {t}: {data.get('city')},{data.get('country')}")
        except json.JSONDecodeError:
            print(r.stdout[:500])
    else:
        print(f"  {RED}✗ Gagal GeoIP. Cek internet.{RESET}")

@screen_mode("HTTP HEADER")
def http_header_scan(t):
    t = t.strip()
    if not is_valid_target(t):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    if not tool_check("curl"):
        return
    print(f"  {CYAN}◉ Headers dari  {t}...{RESET}\n")

    r = run(f"curl -I -s --max-time 10 -L -A 'Mozilla/5.0' --max-redirs 5 {t}")
    if not (r and r.stdout.strip()):
        t_http = t.replace("https://","http://")
        r = run(f"curl -I -s --max-time 10 {t_http}")
        if not (r and r.stdout.strip()):
            print(f"  {RED}✗ Gagal ambil header.{RESET}")
            return

    security_headers = {
        "strict-transport-security":"HSTS",
        "content-security-policy":"CSP",
        "x-frame-options":"Clickjacking Protect",
        "x-xss-protection":"XSS Protect",
        "x-content-type-options":"MIME Sniff Protect",
        "referrer-policy":"Referrer Policy",
        "permissions-policy":"Permissions Policy",
    }
    found_sec = []
    redirect_count = 0

    print_sep()
    for line in r.stdout.split("\n"):
        line = line.strip()
        if not line:
            continue
        low = line.lower()
        if line.startswith("HTTP/"):
            parts = line.split()
            code = parts[1] if len(parts) > 1 else "?"
            desc = {
                "200":"OK","301":"Moved Permanently","302":"Found",
                "304":"Not Modified","400":"Bad Request","401":"Unauthorized",
                "403":"Forbidden","404":"Not Found","500":"Internal Server Error",
                "503":"Service Unavailable"
            }.get(code,"")
            color = GREEN if code.startswith("2") else (YELLOW if code.startswith("3") else RED)
            print(f"  {color}{BOLD}{line}  {desc}{RESET}")
            if code.startswith("3"):
                redirect_count += 1
        elif "location:" in low:
            print(f"  {YELLOW}{line}  ← redirect{RESET}")
        elif "set-cookie:" in low:
            issues = []
            if "httponly" not in low:
                issues.append("NO HttpOnly")
            if "secure" not in low:
                issues.append("NO Secure")
            if "samesite" not in low:
                issues.append("NO SameSite")
            flag_str = f"  ⚠ {', '.join(issues)}" if issues else "  ✓"
            flag_color = RED if issues else GREEN
            print(f"  {CYAN}{line}{flag_color}{flag_str}{RESET}")
        elif any(x in low for x in ["server:","x-powered-by:","via:","x-generator:"]):
            print(f"  {YELLOW}{line}  ← fingerprint{RESET}")
        elif any(k in low for k in security_headers):
            for k, desc in security_headers.items():
                if k in low:
                    found_sec.append(desc)
            print(f"  {GREEN}{line}{RESET}")
        else:
            print(f"  {DIM}{line}{RESET}")

    if redirect_count > 0:
        print(f"\n  {YELLOW}⚠ {redirect_count} redirect terjadi.{RESET}")

    print_sep()
    section_title("Security Headers Report")
    score = 0
    for s in security_headers.values():
        if s in found_sec:
            print(f"  {GREEN}✓  {s}{RESET}")
            score += 1
        else:
            print(f"  {RED}✗  {s}  — MISSING{RESET}")

    grade = "A" if score >= 6 else ("B" if score >= 4 else ("C" if score >= 2 else "F"))
    g_color = GREEN if grade == "A" else (YELLOW if grade in "BC" else RED)
    print(f"\n  {g_color}{BOLD}Security Score :  {score} / {len(security_headers)}   Grade : {grade}{RESET}")
    save_log(f"HTTP HEADER {t} score:{score}/7")

@screen_mode("SSL CHECK")
def ssl_check(t):
    t = strip_scheme(t)
    if not is_valid_target(t):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    if not tool_check("openssl"):
        return
    print(f"  {CYAN}◉ SSL Check  {t}:443{RESET}\n")

    r = run(
        f"echo | openssl s_client -connect {t}:443 -servername {t} 2>/dev/null",
        timeout=15
    )
    if not (r and r.stdout.strip()):
        print(f"  {RED}✗ Koneksi SSL gagal.{RESET}")
        return

    print_sep()
    issues = []
    for line in r.stdout.split("\n"):
        line = line.strip()
        if any(x in line for x in ["subject=","issuer="]):
            print(f"  {CYAN}{line}{RESET}")
        elif "notBefore" in line:
            print(f"  {GREEN}◉ Issued  : {line}{RESET}")
        elif "notAfter" in line:
            try:
                date_str = line.split("=",1)[1].strip()
                exp = datetime.strptime(date_str, "%b %d %H:%M:%S %Y %Z")
                sisa = (exp - datetime.utcnow()).days
                if sisa < 0:
                    issues.append("Sertifikat EXPIRED")
                    print(f"  {RED}✗ Expired : {date_str}  ← SUDAH EXPIRED!{RESET}")
                elif sisa < 14:
                    issues.append(f"Sertifikat habis {sisa} hari lagi")
                    print(f"  {RED}⚠ Expired : {date_str}  ← {sisa} hari lagi! SEGERA RENEW!{RESET}")
                elif sisa < 30:
                    print(f"  {YELLOW}⚠ Expired : {date_str}  ← {sisa} hari lagi!{RESET}")
                else:
                    print(f"  {GREEN}✓ Expired : {date_str}  ({sisa} hari lagi){RESET}")
            except:
                print(f"  {GREEN}{line}{RESET}")
        elif "Verify return code" in line:
            color = GREEN if "0 (ok)" in line.lower() else RED
            mark = "✓" if "0 (ok)" in line.lower() else "✗"
            if mark == "✗":
                issues.append("SSL Verify GAGAL")
            print(f"  {color}{mark} {line}{RESET}")
        elif "Protocol" in line:
            if any(old in line for old in ["TLSv1 ","TLSv1.0","TLSv1.1","SSLv3","SSLv2"]):
                issues.append(f"Protokol lama: {line.strip()}")
                print(f"  {RED}⚠ {line}  ← DEPRECATED!{RESET}")
            else:
                print(f"  {GREEN}✓ {line}{RESET}")
        elif "Cipher" in line:
            print(f"  {YELLOW}◉ {line}{RESET}")

    print_sep()
    section_title("Protocol Test")
    for proto, label in [("-tls1_2","TLSv1.2"),("-tls1_1","TLSv1.1"),("-tls1","TLSv1.0")]:
        pr = run(f"echo | openssl s_client {proto} -connect {t}:443 -servername {t} 2>&1 | grep -c 'Cipher'", timeout=8)
        if pr and pr.stdout.strip() == "1":
            color = GREEN if "1.2" in label else RED
            mark = "✓" if "1.2" in label else "✗ DEPRECATED"
            if "DEPRECATED" in mark:
                issues.append(f"{label} masih aktif")
            print(f"  {color}{mark}  {label} supported{RESET}")
        else:
            print(f"  {RED}○  {label} tidak support / timeout{RESET}")

    print_sep()
    if issues:
        print(f"\n  {RED}{BOLD}⚠ ISSUES DITEMUKAN :{RESET}")
        for iss in issues:
            print(f"    {RED}→  {iss}{RESET}")
    else:
        print(f"\n  {GREEN}{BOLD}✓ SSL OK — Tidak ada masalah ditemukan.{RESET}")

    save_log(f"SSL CHECK {t} issues:{len(issues)}")

@screen_mode("DIR SCAN")
def dir_bruteforce(t):
    t = t.strip().rstrip("/")
    if not is_valid_target(t):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
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
    found = []
    lock = threading.Lock()

    section_title("Scan Configuration")
    print(f"  {DIM}{'Target':<12}{RESET}{WHITE}{t}{RESET}")
    print(f"  {DIM}{'Paths':<12}{RESET}{WHITE}{len(paths)} entries  ·  Threaded{RESET}")
    print_sep()

    def check_path(p):
        url = f"{t}/{p}"
        r = run(
            f"curl -o /dev/null -s -w '%{{http_code}}:%{{size_download}}' --max-time 5 -L {url}",
            timeout=8
        )
        if not r:
            return
        parts = r.stdout.strip().split(":")
        code = parts[0]
        size = format_bytes(parts[1]) if len(parts) > 1 else "?"
        with lock:
            if code == "200":
                print(f"  {GREEN}● 200  FOUND   {url}  [{size}]{RESET}")
                found.append(url)
                save_log(f"DIR FOUND {url}")
            elif code in ("301","302","307","308"):
                print(f"  {YELLOW}◉ {code}  REDIR   {url}{RESET}")
            elif code == "403":
                print(f"  {CYAN}◈ 403  FORBID  {url}{RESET}")
            elif code == "401":
                print(f"  {MAGENTA}◈ 401  AUTH    {url}{RESET}")
            else:
                print(f"  {DIM}○ {code}  MISS    {url}{RESET}")

    threads = []
    for p in paths:
        th = threading.Thread(target=check_path, args=(p,))
        th.start()
        threads.append(th)
        time.sleep(0.04)
    for th in threads:
        th.join()

    print_sep()
    print(f"  {CYAN}◉ Selesai :  {WHITE}{len(found)}{CYAN} path ditemukan.{RESET}")
    if found:
        section_title("Found List")
        for f in found:
            print(f"    {GREEN}→  {f}{RESET}")

@screen_mode("SUBDOMAIN")
def subdomain_scan(d):
    d = strip_scheme(d)
    if not is_valid_target(d):
        print(f"  {RED}✗ Domain tidak valid.{RESET}")
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
    found = []
    lock = threading.Lock()

    section_title("Scan Configuration")
    print(f"  {DIM}{'Target':<12}{RESET}{WHITE}{d}{RESET}")
    print(f"  {DIM}{'Words':<12}{RESET}{WHITE}{len(subs)} subdomain{RESET}")
    print_sep()

    def check(s):
        host = f"{s}.{d}"
        ip = get_ip(host)
        with lock:
            if ip:
                print(f"  {GREEN}● FOUND  {host:<38}→  {ip}{RESET}")
                found.append((host, ip))
                save_log(f"SUBDOMAIN {host}->{ip}")

    print(f"  {CYAN}◉ Scanning...{RESET}\n")
    threads = [threading.Thread(target=check, args=(s,)) for s in subs]
    for th in threads: th.start()
    for th in threads: th.join()

    print_sep()
    print(f"  {CYAN}◉ Selesai :  {WHITE}{len(found)}{CYAN} subdomain aktif.{RESET}")
    if not found:
        print(f"  {RED}✗ Tidak ada subdomain yang ditemukan.{RESET}")

@screen_mode("FULL SECURITY REPORT")
def security_report(t):
    t = strip_scheme(t.strip())
    if not is_valid_target(t):
        print(f"  {RED}✗ Target tidak valid.{RESET}")
        return
    url = normalize_url(t)
    ip = get_ip(t)
    all_ips = get_all_ips(t)
    start_time = time.time()

    section_title("Report Information")
    print(f"  {DIM}{'Target':<12}{RESET}{WHITE}{t}{RESET}")
    print(f"  {DIM}{'IP':<12}{RESET}{WHITE}{ip or 'Gagal resolve'}{RESET}")
    print(f"  {DIM}{'URL':<12}{RESET}{WHITE}{url}{RESET}")
    print(f"  {DIM}{'Time':<12}{RESET}{WHITE}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    print_sep()

    risk_score = 0
    findings = []

    # 1. DNS
    section_title("[ 1 / 6 ]  DNS", "◈")
    dns_lookup_raw(t)
    if len(all_ips) > 1:
        print(f"  {CYAN}◉ Multi-IP / CDN  {', '.join(all_ips[:5])}{RESET}")

    # 2. PING + Latency
    section_title("[ 2 / 6 ]  Ping & Latency", "◈")
    r = run(f"ping -c 3 -W 2 {t}", timeout=15)
    if r and r.returncode == 0:
        for line in r.stdout.strip().split("\n"):
            if "rtt" in line or "packet" in line:
                print(f"  {GREEN}{line.strip()}{RESET}")
        lat = calc_latency(t)
        if lat:
            q = "Excellent" if lat < 20 else ("Good" if lat < 80 else "Fair")
            print(f"  {GREEN}◉ Status : AKTIF  ·  Avg : {lat:.1f}ms  [{q}]{RESET}")
    else:
        print(f"  {RED}✗ Tidak respon ping  (ICMP mungkin diblokir){RESET}")

    r_ping1 = run(f"ping -c 1 -W 2 {t}", timeout=5)
    if r_ping1 and r_ping1.stdout:
        for line in r_ping1.stdout.split("\n"):
            if "ttl=" in line.lower():
                try:
                    ttl = int(re.search(r"ttl=(\d+)", line, re.I).group(1))
                    os_g = "Linux/Unix" if ttl <= 64 else ("Windows" if ttl <= 128 else "Network Device")
                    print(f"  {YELLOW}◉ TTL : {ttl}  →  {os_g}{RESET}")
                except: pass

    # 3. PORT SCAN
    section_title("[ 3 / 6 ]  Port Scan", "◈")
    HIGH_RISK = {21,23,3389,5900,6379,27017,1433}
    if ip:
        open_p = []
        lock = threading.Lock()
        def pscan(p, svc):
            s = socket.socket()
            s.settimeout(0.6)
            if s.connect_ex((ip, p)) == 0:
                with lock:
                    banner = grab_banner(ip, p)
                    b_str = f"  {DIM}{banner}{RESET}" if banner else ""
                    is_risk = p in HIGH_RISK
                    color = RED if is_risk else GREEN
                    label = "  [HIGH-RISK]" if is_risk else ""
                    print(f"  {color}● OPEN  {p:5}  ({svc}){label}{b_str}{RESET}")
                    open_p.append(p)
            s.close()
        ths = [threading.Thread(target=pscan, args=(p,svc)) for p,svc in COMMON_PORTS.items()]
        for th in ths: th.start()
        for th in ths: th.join()
        risky = [p for p in open_p if p in HIGH_RISK]
        risk_score += len(risky) * 2
        if risky:
            findings.append(f"Port high-risk terbuka: {risky}")
        print(f"  {CYAN}◉ {len(open_p)} port terbuka dari {len(COMMON_PORTS)}{RESET}")

    # 4. HTTP HEADER
    section_title("[ 4 / 6 ]  HTTP Header", "◈")
    if tool_check("curl"):
        r2 = run(f"curl -I -s --max-time 8 {url}")
        if r2 and r2.stdout:
            sec_found = 0
            sec_total = 7
            sec_keys = ["strict-transport-security","content-security-policy","x-frame-options",
                        "x-content-type-options","referrer-policy","permissions-policy","x-xss-protection"]
            for line in r2.stdout.split("\n")[:20]:
                l = line.strip()
                if l:
                    low = l.lower()
                    if any(k in low for k in sec_keys):
                        sec_found += 1
                    color = YELLOW if any(x in low for x in ["server","powered"]) else DIM
                    print(f"  {color}{l}{RESET}")
            missing = sec_total - sec_found
            if missing > 3:
                risk_score += 2
                findings.append(f"{missing} security header hilang")
            print(f"  {CYAN}◉ Security headers : {sec_found} / {sec_total}{RESET}")

    # 5. SSL
    section_title("[ 5 / 6 ]  SSL", "◈")
    if tool_check("openssl"):
        r3 = run(f"echo | openssl s_client -connect {t}:443 -servername {t} 2>/dev/null")
        if r3 and r3.stdout:
            for line in r3.stdout.split("\n"):
                line = line.strip()
                if "notAfter" in line:
                    try:
                        date_str = line.split("=",1)[1].strip()
                        exp = datetime.strptime(date_str, "%b %d %H:%M:%S %Y %Z")
                        sisa = (exp - datetime.utcnow()).days
                        if sisa < 0:
                            risk_score += 5
                            findings.append("SSL EXPIRED")
                            print(f"  {RED}✗ SSL EXPIRED!  {date_str}{RESET}")
                        elif sisa < 30:
                            risk_score += 2
                            findings.append(f"SSL hampir expired ({sisa} hari)")
                            print(f"  {YELLOW}⚠ SSL {sisa} hari lagi expire :  {date_str}{RESET}")
                        else:
                            print(f"  {GREEN}✓ SSL OK — {sisa} hari lagi :  {date_str}{RESET}")
                    except:
                        print(f"  {DIM}{line}{RESET}")
                elif "Verify return code" in line:
                    color = GREEN if "0 (ok)" in line.lower() else RED
                    mark = "✓" if "0 (ok)" in line.lower() else "✗"
                    print(f"  {color}{mark} {line}{RESET}")
        else:
            print(f"  {RED}✗ Tidak support HTTPS / SSL gagal{RESET}")
            findings.append("HTTPS tidak aktif atau SSL gagal")
            risk_score += 3

    # 6. SUMMARY
    elapsed = round(time.time()-start_time, 1)
    section_title("[ 6 / 6 ]  Summary", "◈")
    print_sep()
    print(f"  {DIM}{'Duration':<14}{RESET}{WHITE}{elapsed}s{RESET}")
    print(f"  {DIM}{'Target':<14}{RESET}{WHITE}{t}{RESET}")
    print(f"  {DIM}{'IP':<14}{RESET}{WHITE}{ip or 'N/A'}{RESET}")

    if findings:
        print(f"\n  {RED}{BOLD}⚠ FINDINGS :{RESET}")
        for f in findings:
            print(f"    {RED}→  {f}{RESET}")

    risk_label = "LOW" if risk_score < 3 else ("MEDIUM" if risk_score < 7 else "HIGH")
    r_color = GREEN if risk_score < 3 else (YELLOW if risk_score < 7 else RED)
    print(f"\n  {r_color}{BOLD}Risk Score :  {risk_score}  [{risk_label}]{RESET}")

    print_sep()
    save_output_demo(t)
    print(f"\n  {GREEN}{BOLD}✓ Full Security Report Selesai!{RESET}")
    save_log(f"FULL REPORT {t} risk:{risk_label}({risk_score})")

# ================= AI =================
try:
    import pyttsx3
    engine = pyttsx3.init()
except:
    engine = None

def ai_voice_mode():
    if engine:
        text = input("  AI Voice : ")
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"  {RED}✗ Voice tidak tersedia.{RESET}")
        print(f"  {YELLOW}  Install : pip install pyttsx3{RESET}")

# ============================================================
#  SUB-MENU DASHBOARDS
# ============================================================

def sub_header(title, color=CYAN):
    clear()
    bar = "═" * W
    print()
    print(f"  {color}{BOLD}╔{bar}╗")
    print(f"  ║  🔐 SkyWings  ::  {title:<{W-18}}║")
    print(f"  ╚{bar}╝{RESET}")
    print()

def sub_back_prompt():
    print()
    print(f"  {DIM}{'─'*W}{RESET}")
    print(f"  {CYAN}  [0]  ←  Kembali ke Main Menu{RESET}")
    print(f"  {DIM}{'─'*W}{RESET}")
    print()

def _menu_item(num, label, desc, color=CYAN):
    print(f"  {color}  [{num:>2}]  {label:<20}{DIM}{desc}{RESET}")

# ─── NETWORK ───────────────────────────────────────────────
def menu_network():
    while True:
        sub_header("NETWORK", GREEN)
        print(f"  {GREEN}{BOLD}◈  NETWORK TOOLS{RESET}")
        print()
        _menu_item("1",  "Quick Scan",   "Info Cepat",      GREEN)
        _menu_item("2",  "Multi Scan",   "Banyak Target",   GREEN)
        _menu_item("3",  "Trace Route",  "Lacak Rute",      GREEN)
        _menu_item("4",  "Ping Target",  "ICMP Ping",       GREEN)
        _menu_item("5",  "Port Scan",    "Scan Port",       GREEN)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "1":
            t = input(f"\n  {YELLOW}Target : {RESET}").strip()
            if t: quick_info(t)
        elif p == "2":
            raw = input(f"\n  {YELLOW}Targets (pisah spasi) : {RESET}").strip()
            if raw: fast_scan(raw.split())
        elif p == "3":
            t = input(f"\n  {YELLOW}Target : {RESET}").strip()
            if t: trace_route(t)
        elif p == "4":
            t = input(f"\n  {YELLOW}Target : {RESET}").strip()
            if t: ping_target(t)
        elif p == "5":
            t = input(f"\n  {YELLOW}Target : {RESET}").strip()
            if t: port_scan(t)
        else:
            print(f"\n  {RED}✗ Pilihan tidak valid.{RESET}")
            time.sleep(0.6)

# ─── WEB INTEL ─────────────────────────────────────────────
def menu_webintel():
    while True:
        sub_header("WEB INTEL", CYAN)
        print(f"  {CYAN}{BOLD}◈  WEB INTEL TOOLS{RESET}")
        print()
        _menu_item("6",  "Web Info",    "Header + DNS",       CYAN)
        _menu_item("7",  "HTTP Header", "Security Header",    CYAN)
        _menu_item("8",  "Dir Scan",    "Brute Path",         CYAN)
        _menu_item("9",  "Subdomain",   "Enum Subdomain",     CYAN)
        _menu_item("10", "SSL Check",   "Cek Sertifikat",     CYAN)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "6":
            t = input(f"\n  {YELLOW}Web / Domain : {RESET}").strip()
            if t:
                http_header_scan(normalize_url(t))
                clear()
                kali_header("WEB INFO - DNS")
                dns_lookup_raw(t)
                enter_back()
        elif p == "7":
            t = input(f"\n  {YELLOW}URL : {RESET}").strip()
            if t: http_header_scan(normalize_url(t))
        elif p == "8":
            t = input(f"\n  {YELLOW}URL : {RESET}").strip()
            if t: dir_bruteforce(normalize_url(t))
        elif p == "9":
            t = input(f"\n  {YELLOW}Domain : {RESET}").strip()
            if t: subdomain_scan(t)
        elif p == "10":
            t = input(f"\n  {YELLOW}Domain : {RESET}").strip()
            if t: ssl_check(t)
        else:
            print(f"\n  {RED}✗ Pilihan tidak valid.{RESET}")
            time.sleep(0.6)

# ─── OSINT ─────────────────────────────────────────────────
def menu_osint():
    while True:
        sub_header("OSINT", YELLOW)
        print(f"  {YELLOW}{BOLD}◈  OSINT TOOLS{RESET}")
        print()
        _menu_item("11", "WHOIS",      "Info Domain",   YELLOW)
        _menu_item("12", "GEO IP",     "Lokasi IP",     YELLOW)
        _menu_item("13", "DNS Lookup", "DNS Records",   YELLOW)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "11":
            t = input(f"\n  {YELLOW}Target : {RESET}").strip()
            if t: whois_lookup(t)
        elif p == "12":
            t = input(f"\n  {YELLOW}IP / Domain : {RESET}").strip()
            if t: geo_ip(t)
        elif p == "13":
            t = input(f"\n  {YELLOW}Domain : {RESET}").strip()
            if t: dns_lookup_menu(t)
        else:
            print(f"\n  {RED}✗ Pilihan tidak valid.{RESET}")
            time.sleep(0.6)

# ─── SYSTEM ────────────────────────────────────────────────
def menu_system():
    while True:
        sub_header("SYSTEM", GREEN)
        print(f"  {GREEN}{BOLD}◈  SYSTEM TOOLS{RESET}")
        print()
        _menu_item("14", "Firewall",    "Cek Firewall",  GREEN)
        _menu_item("15", "System Info", "Info OS & RAM", GREEN)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "14":
            firewall_check()
        elif p == "15":
            system_info()
        else:
            print(f"\n  {RED}✗ Pilihan tidak valid.{RESET}")
            time.sleep(0.6)

# ─── ADVANCED ──────────────────────────────────────────────
def menu_advanced():
    while True:
        sub_header("ADVANCED", MAGENTA)
        print(f"  {MAGENTA}{BOLD}◈  ADVANCED TOOLS{RESET}")
        print()
        _menu_item("16", "Nmap Scan",   "Advanced Scan",   MAGENTA)
        _menu_item("17", "Full Report", "Laporan Lengkap", MAGENTA)
        _menu_item("18", "Save Output", "Simpan Hasil",    MAGENTA)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "16":
            t = input(f"\n  {YELLOW}Target : {RESET}").strip()
            if t: advanced_scan(t)
        elif p == "17":
            t = input(f"\n  {YELLOW}Target : {RESET}").strip()
            if t: security_report(t)
        elif p == "18":
            t = input(f"\n  {YELLOW}Target : {RESET}").strip()
            if t:
                clear()
                kali_header("SAVE OUTPUT")
                save_output_demo(t)
                enter_back()
        else:
            print(f"\n  {RED}✗ Pilihan tidak valid.{RESET}")
            time.sleep(0.6)

# ─── AI TOOLS ──────────────────────────────────────────────
def menu_aitools():
    while True:
        sub_header("AI TOOLS", CYAN)
        print(f"  {CYAN}{BOLD}◈  AI TOOLS{RESET}")
        print()
        _menu_item("19", "AI Voice",  "Text to Speech", CYAN)
        _menu_item("20", "Fast Scan", "Ping Paralel",   CYAN)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "19":
            ai_voice_mode()
            enter_back()
        elif p == "20":
            raw = input(f"\n  {YELLOW}Targets (pisah spasi) : {RESET}").strip()
            if raw: fast_scan(raw.split())
        else:
            print(f"\n  {RED}✗ Pilihan tidak valid.{RESET}")
            time.sleep(0.6)

# ============================================================
#  MAIN MENU
# ============================================================

def main_menu():
    while True:
        clear()
        now = datetime.now()
        bar = "═" * W

        print()
        print(f"  {CYAN}{BOLD}╔{bar}╗")
        print(f"  ║{'🔓  SYSTEM STATUS  ::  LIVE':^{W}}║")
        print(f"  ║  {DIM}Date : {now.strftime('%Y-%m-%d')}   Time : {now.strftime('%H:%M:%S')}{CYAN}{' '*(W-38)}║")
        print(f"  ╚{bar}╝{RESET}")
        print()

        categories = [
            ("1", "NETWORK",   "Scan Jaringan",  GREEN),
            ("2", "WEB INTEL", "Analisa Web",    CYAN),
            ("3", "OSINT",     "Intelijen",      YELLOW),
            ("4", "SYSTEM",    "Info Sistem",    GREEN),
            ("5", "ADVANCED",  "Scan Lanjutan",  MAGENTA),
            ("6", "AI TOOLS",  "Fitur AI",       CYAN),
        ]

        for num, name, desc, col in categories:
            print(f"  {col}  [{num}]  {BOLD}{name:<14}{RESET}{DIM}{desc}{RESET}")

        print()
        print(f"  {DIM}{'─'*W}{RESET}")
        print(f"  {RED}  [0]  EXIT{RESET}")
        print(f"  {DIM}{'─'*W}{RESET}")

        p = input(skywings_codex()).strip()

        if p == "1":
            fancy_loading("ENTERING NETWORK")
            menu_network()
        elif p == "2":
            fancy_loading("ENTERING WEB INTEL")
            menu_webintel()
        elif p == "3":
            fancy_loading("ENTERING OSINT")
            menu_osint()
        elif p == "4":
            fancy_loading("ENTERING SYSTEM")
            menu_system()
        elif p == "5":
            fancy_loading("ENTERING ADVANCED")
            menu_advanced()
        elif p == "6":
            fancy_loading("ENTERING AI TOOLS")
            menu_aitools()
        elif p == "0":
            print(f"\n  {CYAN}◉ SKYWINGS DOWN.  Stay safe.{RESET}\n")
            break
        else:
            print(f"\n  {RED}✗ Pilihan tidak valid.{RESET}")
            time.sleep(0.6)

# ================= MAIN =================
def main():
    clear()
    logo()
    loading("SKYWINGS  v1.0  BOOTING")
    time.sleep(0.3)

    while True:
        kali_header("SKYWINGS BY PUTRA")

        print(f"  {DIM}{'─'*W}{RESET}")
        cmds = [
            ("help",  "Masuk ke semua fitur"),
            ("info",  "System info"),
            ("clear", "Bersihkan layar"),
            ("exit",  "Keluar"),
        ]
        for cmd, desc in cmds:
            print(f"  {GREEN}  {cmd:<8}{RESET}{DIM}{desc}{RESET}")
        print(f"  {DIM}{'─'*W}{RESET}")

        cmd = input(skywings_codex()).strip()

        if cmd == "help":
            fancy_loading("ENTERING FEATURE MODE")
            main_menu()
        elif cmd == "info":
            system_info()
        elif cmd == "clear":
            clear()
        elif cmd == "exit":
            print(f"\n  {CYAN}◉ SKYWINGS.  Stay safe.{RESET}\n")
            break
        else:
            print(f"\n  {RED}✗ Command tidak dikenal. Ketik 'help'.{RESET}")

if __name__ == "__main__":
    main()
