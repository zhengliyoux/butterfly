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
RESET = "\033[0m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
BOLD = "\033[1m"
MAGENTA = "\033[1;35m"
WHITE = "\033[1;37m"

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
    """Resolve semua IP (A records) dari domain."""
    try:
        infos = socket.getaddrinfo(target.strip(), None)
        ips = list(dict.fromkeys([i[4][0] for i in infos]))
        return ips
    except:
        return []

def strip_scheme(url):
    return url.strip().replace("https://","").replace("http://","").split("/")[0]

def print_sep(char="─", color=CYAN, width=42):
    print(color + char * width + RESET)

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
    """Hitung average latency via ping, return ms atau None."""
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
    for i in range(0, 101, 4):
        print(f"\r{ai_color()}{teks}... {i}%{RESET}", end="")
        time.sleep(0.03)
    print()

def fancy_loading(text):
    for i in range(1, 101):
        print(f"\r{ai_color()}{text}... {i}%{RESET}", end="")
        time.sleep(0.015)
    print()

# ================= PROMPT =================
def skywings_codex():
    return (
        BOLD + ai_color() + "SkyWings" +
        RESET + CYAN + "@root" +
        RESET + RED + ":" +
        YELLOW + "#" +
        RESET + " "
    )

# ================= UI =================
LINE = "━"*42
def kali_header(title):
    color = ai_color()
    print(color + BOLD + f"""
┏{LINE}┓
┃  🧸 SkyWings :: {title}
┗{LINE}┛
""" + RESET)

def line_fx():
    print(ai_color() + "="*42 + RESET)

# ================= SCREEN MODE =================
def enter_back():
    input(YELLOW + "\n[ ENTER untuk kembali ]" + RESET)

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
    print(ai_color() + BOLD + """
╭━━━┳╮╭━┳╮╱╱╭┳╮╭╮╭┳━━╮
┃╭━╮┃┃┃╭┫╰╮╭╯┃┃┃┃┃┣┫┣╯
┃╰━━┫╰╯╯╰╮╰╯╭┫┃┃┃┃┃┃┃╱
╰━━╮┃╭╮┃╱╰╮╭╯┃╰╯╰╯┃┃┃╱
┃╰━╯┃┃┃╰╮╱┃┃╱╰╮╭╮╭╋┫┣╮
╰━━━┻╯╰━╯╱╰╯╱╱╰╯╰╯╰━━╯
╭━╮╱╭┳━━━┳━━━╮
┃┃╰╮┃┃╭━╮┃╭━╮┃
┃╭╮╰╯┃┃╱╰┫╰━━╮
┃┃╰╮┃┃┃╭━╋━━╮┃
┃┃╱┃┃┃╰┻━┃╰━╯┃
╰╯╱╰━┻━━━┻━━━╯
""" + RESET)

    print(CYAN + "[ SYSTEM INITIALIZED :: SKYWINGS ACTIVE...]" + RESET)

    print(ai_color() + """
==========================================
(🎭 OLAA ) I'M SKYWINGS
==========================================
""" + RESET)

    print(YELLOW + """
Script by   : SkyWings
Version     : 1.1
Codename    : Wings Point O
System      : Termux CLI
""" + RESET)

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

# ---------- Banner grab (improved: lebih banyak protokol) ----------
def grab_banner(ip, port, timeout=2.0):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, port))
        probes = {
            80:  b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n",
            8080:b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n",
            8443:b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n",
            21:  None,   # FTP kirim banner sendiri
            22:  None,   # SSH kirim banner sendiri
            25:  None,   # SMTP kirim banner sendiri
            110: None,
            143: None,
            3306:None,
        }
        probe = probes.get(port, b"\r\n")
        if probe:
            s.send(probe)
        banner = s.recv(512).decode(errors="ignore").strip()
        s.close()
        # Bersihkan banner: ambil baris pertama yang meaningful
        lines = [l.strip() for l in banner.split("\n") if l.strip()]
        result = lines[0] if lines else ""
        return result[:100] if result else None
    except:
        return None

# ---------- DNS (improved: lebih banyak record type, reverse DNS) ----------
def dns_lookup_raw(target):
    target = target.strip()
    ip = get_ip(target)
    if ip:
        print(GREEN + f"  [DNS-A]  {target} -> {ip}" + RESET)
        # Reverse DNS
        try:
            rev = socket.gethostbyaddr(ip)
            if rev and rev[0] and rev[0] != target:
                print(CYAN + f"  [rDNS]   {ip} -> {rev[0]}" + RESET)
        except:
            pass
        save_log(f"DNS {target}->{ip}")
        return ip
    else:
        print(RED + f"  [DNS] Gagal resolve: {target}" + RESET)
        return None

@screen_mode("DNS LOOKUP")
def dns_lookup_menu(target):
    target = target.strip()
    if not is_valid_target(target):
        print(RED + "[!] Target tidak valid." + RESET)
        return

    ip = dns_lookup_raw(target)

    # Semua IP
    all_ips = get_all_ips(target)
    if len(all_ips) > 1:
        print(CYAN + f"  [All IPs] {', '.join(all_ips)}" + RESET)

    # IPv6
    try:
        info = socket.getaddrinfo(target, None, socket.AF_INET6)
        if info:
            ipv6 = info[0][4][0]
            print(CYAN + f"  [IPv6]   {ipv6}" + RESET)
    except:
        pass

    if not ip:
        return

    # ASN lookup via whois sederhana
    if tool_check("whois"):
        r_asn = run(f"whois -h whois.cymru.com ' -v {ip}' 2>/dev/null", timeout=8)
        if r_asn and r_asn.stdout.strip():
            lines = [l for l in r_asn.stdout.strip().split("\n") if l.strip() and not l.startswith("AS")]
            if lines:
                print(YELLOW + f"  [ASN]    {lines[0].strip()}" + RESET)

    print_sep()

    if tool_check("dig"):
        record_types = ["A","AAAA","MX","NS","TXT","CNAME","SOA"]
        for rtype in record_types:
            r = run(f"dig {target} {rtype} +noall +answer +time=3 2>/dev/null", timeout=8)
            if r and r.stdout.strip():
                print(CYAN + f"\n[{rtype} Records]" + RESET)
                for line in r.stdout.strip().split("\n")[:10]:
                    print(f"  {line}")
    else:
        r = run(f"nslookup {target} 2>/dev/null")
        if r and r.stdout.strip():
            print(CYAN + "\n[NSLookup]" + RESET)
            print(r.stdout[:800])

# ---------- Quick Info (improved: latency, TTL, lebih informatif) ----------
@screen_mode("QUICK NETWORK INFO")
def quick_info(target):
    target = target.strip()
    if not is_valid_target(target):
        print(RED + "[!] Target tidak valid." + RESET)
        return

    ip = get_ip(target)
    is_private = False
    if ip:
        try:
            is_private = ipaddress.ip_address(ip).is_private
        except:
            pass

    print(CYAN + f"  Target    : {target}")
    print(f"  IP        : {ip or 'Gagal resolve'}")
    if ip:
        print(f"  Type      : {'Private/LAN' if is_private else 'Public'}" + RESET)
    print_sep()

    # Ping dengan latency detail
    print(CYAN + "\n[PING TEST - 4 packets]" + RESET)
    r = run(f"ping -c 4 -W 2 {target}", timeout=20)
    if r and r.returncode == 0 and r.stdout:
        for line in r.stdout.strip().split("\n"):
            if "time=" in line:
                # Warnai berdasarkan latency
                try:
                    ms_val = float(re.search(r"time=([\d.]+)", line).group(1))
                    color = GREEN if ms_val < 50 else (YELLOW if ms_val < 150 else RED)
                    print(color + f"  {line.strip()}" + RESET)
                except:
                    print(GREEN + f"  {line.strip()}" + RESET)
            elif "rtt" in line or "packet" in line:
                print(GREEN + f"  {line.strip()}" + RESET)
    else:
        print(RED + "  [-] Host tidak reachable (mungkin blokir ICMP)" + RESET)

    # Average latency summary
    lat = calc_latency(target)
    if lat is not None:
        q = "Excellent" if lat < 20 else ("Good" if lat < 80 else ("Fair" if lat < 150 else "Poor"))
        color = GREEN if lat < 80 else (YELLOW if lat < 150 else RED)
        print(color + f"  Avg Latency: {lat:.1f}ms  [{q}]" + RESET)

    print_sep()
    print(CYAN + "\n[DNS]" + RESET)
    dns_lookup_raw(target)
    all_ips = get_all_ips(target)
    if len(all_ips) > 1:
        print(CYAN + f"  [Multi-IP] {', '.join(all_ips[:5])}" + RESET)

    print_sep()
    print(CYAN + "\n[QUICK PORT CHECK]" + RESET)
    if ip:
        critical_ports = [(80,"HTTP"),(443,"HTTPS"),(22,"SSH"),(21,"FTP"),(3306,"MYSQL"),(3389,"RDP")]
        for p, svc in critical_ports:
            s = socket.socket()
            s.settimeout(1)
            t_start = time.time()
            status = "OPEN" if s.connect_ex((ip, p)) == 0 else "CLOSED"
            t_ms = round((time.time()-t_start)*1000,1)
            s.close()
            color = GREEN if status == "OPEN" else RED
            resp = f"  ({t_ms}ms)" if status == "OPEN" else ""
            print(color + f"  {status:6}  {p:5} ({svc}){resp}" + RESET)

    # TTL check
    print_sep()
    print(CYAN + "\n[TTL / OS FINGERPRINT]" + RESET)
    r2 = run(f"ping -c 1 -W 2 {target}", timeout=5)
    if r2 and r2.stdout:
        for line in r2.stdout.split("\n"):
            if "ttl=" in line.lower():
                try:
                    ttl = int(re.search(r"ttl=(\d+)", line, re.I).group(1))
                    if ttl <= 64:
                        os_guess = "Linux/Unix/Android"
                    elif ttl <= 128:
                        os_guess = "Windows"
                    else:
                        os_guess = "Cisco/Network Device"
                    print(YELLOW + f"  TTL: {ttl}  -> Kemungkinan OS: {os_guess}" + RESET)
                except:
                    pass

# ---------- Port Scan threaded (improved: response time, risk label) ----------
@screen_mode("PORT SCAN")
def port_scan(target):
    target = target.strip()
    if not is_valid_target(target):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    ip = get_ip(target)
    if not ip:
        print(RED + f"[!] Tidak bisa resolve: {target}" + RESET)
        return

    print(CYAN + f"  Target : {target} ({ip})")
    print(f"  Ports  : {len(COMMON_PORTS)} (common) + custom")
    print(f"  Mode   : Threaded + Banner Grab + Risk Label" + RESET)
    print_sep()
    print(YELLOW + "[?] Tambah custom port? contoh: 8888,9090 / Enter=skip:" + RESET)
    extra = input("  > ").strip()
    extra_ports = {}
    if extra:
        for ep in extra.split(","):
            ep = ep.strip()
            if ep.isdigit():
                extra_ports[int(ep)] = "CUSTOM"

    all_ports = {**COMMON_PORTS, **extra_ports}
    open_ports = []
    lock = threading.Lock()

    # Risk level per port
    HIGH_RISK = {21,23,3389,5900,6379,27017,1433,3306}
    MED_RISK  = {22,25,80,8080,8443,445,5432}

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
                    b_str = f" | {banner}" if banner else ""
                    risk = "[HIGH-RISK]" if p in HIGH_RISK else ("[MED]" if p in MED_RISK else "")
                    risk_color = RED if p in HIGH_RISK else (YELLOW if p in MED_RISK else "")
                    print(GREEN + f"  [OPEN]   {p:5d}  {svc:<13} {resp_ms:5.1f}ms" +
                          risk_color + f" {risk}" +
                          CYAN + f"{b_str}" + RESET)
                    open_ports.append(p)
                    save_log(f"PORT OPEN {target}:{p} ({svc})")
                else:
                    print(RED + f"  [CLOSED] {p:5d}  {svc}" + RESET)
        except Exception as e:
            with lock:
                print(RED + f"  [ERROR]  {p:5d}  {e}" + RESET)

    threads = []
    for p, svc in sorted(all_ports.items()):
        th = threading.Thread(target=check_port, args=(p, svc))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()

    print_sep()
    print(CYAN + f"\n[+] Selesai. {len(open_ports)}/{len(all_ports)} port terbuka." + RESET)
    if open_ports:
        print(GREEN + f"    Open: {sorted(open_ports)}" + RESET)
        high = [p for p in open_ports if p in HIGH_RISK]
        if high:
            print(RED + f"    [!] High-Risk Ports Terbuka: {high}" + RESET)

# ---------- Ping (improved: statistik detail, jitter, packet loss) ----------
@screen_mode("PING TARGET")
def ping_target(target):
    target = target.strip()
    if not is_valid_target(target):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    print(YELLOW + "[?] Jumlah paket (1-50, default 5):" + RESET)
    c = input("  > ").strip()
    count = int(c) if c.isdigit() and 1 <= int(c) <= 50 else 5
    print(CYAN + f"[*] Ping {target} x{count}..." + RESET)
    r = run(f"ping -c {count} {target}", timeout=count*3+5)
    if r and r.returncode == 0 and r.stdout:
        times = []
        for line in r.stdout.split("\n"):
            if "time=" in line:
                try:
                    ms = float(re.search(r"time=([\d.]+)", line).group(1))
                    times.append(ms)
                    color = GREEN if ms < 50 else (YELLOW if ms < 150 else RED)
                    print(color + f"  {line.strip()}" + RESET)
                except:
                    print(f"  {line.strip()}")
            elif line.strip():
                print(f"  {line.strip()}")

        # Statistik tambahan
        if len(times) >= 2:
            print_sep()
            print(CYAN + "[STATISTIK]" + RESET)
            print(f"  Min    : {min(times):.2f} ms")
            print(f"  Max    : {max(times):.2f} ms")
            print(f"  Avg    : {sum(times)/len(times):.2f} ms")
            jitter = max(times) - min(times)
            jitter_q = "Stabil" if jitter < 10 else ("OK" if jitter < 50 else "Tidak Stabil")
            color = GREEN if jitter < 10 else (YELLOW if jitter < 50 else RED)
            print(color + f"  Jitter : {jitter:.2f} ms  [{jitter_q}]" + RESET)

        # Packet loss parse
        for line in r.stdout.split("\n"):
            if "packet loss" in line or "received" in line:
                match = re.search(r"(\d+)% packet loss", line)
                if match:
                    loss = int(match.group(1))
                    color = GREEN if loss == 0 else (YELLOW if loss < 20 else RED)
                    print(color + f"  Loss   : {loss}%" + RESET)
    else:
        print(RED + "[-] Ping gagal. Host mungkin blokir ICMP." + RESET)

# ---------- Traceroute (improved: latency per hop, asterisk count) ----------
@screen_mode("TRACE ROUTE")
def trace_route(target):
    target = target.strip()
    if not is_valid_target(target):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    if not tool_check("traceroute"):
        return
    print(CYAN + f"[*] Tracing route ke {target} (max 20 hop)..." + RESET)
    r = run(f"traceroute -m 20 -w 2 {target}", timeout=90)
    if r and r.stdout.strip():
        timeout_hops = 0
        for line in r.stdout.strip().split("\n"):
            if "* * *" in line:
                timeout_hops += 1
                print(RED + f"  {line}  [timeout/filtered]" + RESET)
            else:
                # Highlight high latency hops
                ms_vals = re.findall(r"([\d.]+) ms", line)
                if ms_vals:
                    avg_hop = sum(float(v) for v in ms_vals) / len(ms_vals)
                    color = GREEN if avg_hop < 50 else (YELLOW if avg_hop < 150 else RED)
                    print(color + f"  {line}" + RESET)
                else:
                    print(f"  {line}")
        if timeout_hops > 5:
            print(YELLOW + f"\n  [i] {timeout_hops} hop timeout — kemungkinan ada firewall di tengah rute." + RESET)
    else:
        print(RED + "[-] Traceroute gagal." + RESET)

# ---------- Nmap ----------
@screen_mode("NMAP SCANNER")
def advanced_scan(target):
    target = target.strip()
    if not is_valid_target(target):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    if not tool_check("nmap"):
        return
    print(CYAN + "[*] Pilih mode scan:" + RESET)
    print(GREEN + "  [1] Fast scan       (-F --open)")
    print("  [2] Service version (-sV)")
    print("  [3] OS Detection    (-O)")
    print("  [4] Full + Script   (-A)")
    print("  [5] UDP Scan        (-sU -F)")
    print("  [6] Stealth SYN     (-sS -F)" + RESET)
    mode = input(skywings_codex()).strip()
    flags = {
        "1":"-F --open",
        "2":"-sV --version-intensity 5",
        "3":"-O",
        "4":"-A",
        "5":"-sU -F",
        "6":"-sS -F",
    }.get(mode, "-F --open")
    print(CYAN + f"[*] Nmap {target}  [{flags}]" + RESET)
    result = run(f"nmap {flags} {target}", timeout=120)
    if result and result.stdout:
        for line in result.stdout.split("\n"):
            if "open" in line.lower():
                print(GREEN + f"  {line}" + RESET)
            elif "filtered" in line.lower() or "closed" in line.lower():
                print(RED + f"  {line}" + RESET)
            else:
                print(f"  {line}")
        save_log(f"NMAP {target}: {flags}")
    else:
        print(RED + "[-] Nmap gagal." + RESET)

# ---------- Firewall ----------
@screen_mode("FIREWALL CHECK")
def firewall_check():
    print(CYAN + "[*] Checking iptables..." + RESET)
    r = run("iptables -L -n -v 2>/dev/null")
    if r and r.stdout.strip():
        print(r.stdout[:2000])
    else:
        print(YELLOW + "[i] iptables tidak aktif / butuh root." + RESET)
    ufw = run("ufw status verbose 2>/dev/null")
    if ufw and ufw.stdout.strip():
        print(CYAN + "\n[UFW]" + RESET)
        print(ufw.stdout[:500])
    nft = run("nft list ruleset 2>/dev/null")
    if nft and nft.stdout.strip():
        print(CYAN + "\n[nftables]" + RESET)
        print(nft.stdout[:500])

# ---------- Save ----------
def save_output_demo(target):
    target = target.strip()
    if not is_valid_target(target):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    try:
        ip = get_ip(target)
        with open("scan_result.txt", "a") as f:
            f.write(f"\n{'='*42}\n")
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
        print(GREEN + "[+] Saved -> scan_result.txt" + RESET)
        save_log(f"SAVED {target}")
    except Exception as e:
        print(RED + f"[-] Gagal save: {e}" + RESET)

# ---------- System Info (improved: top proses, network interface) ----------
@screen_mode("SYSTEM INFO")
def system_info():
    print(GREEN + f"  OS       : {platform.system()} {platform.release()}")
    print(f"  Version  : {platform.version()[:60]}")
    print(f"  Node     : {platform.node()}")
    print(f"  Machine  : {platform.machine()}")
    print(f"  CPU      : {platform.processor() or 'N/A'}" + RESET)
    try:
        print(GREEN + f"  Local IP : {socket.gethostbyname(socket.gethostname())}" + RESET)
    except:
        pass

    if tool_check("curl"):
        r = run("curl -s --max-time 5 ifconfig.me 2>/dev/null")
        if r and r.stdout.strip():
            print(CYAN + f"  Public IP: {r.stdout.strip()}" + RESET)

    mem = run("free -h 2>/dev/null")
    if mem and mem.stdout:
        print(CYAN + "\n[MEMORY]" + RESET)
        print(mem.stdout)

    disk = run("df -h 2>/dev/null")
    if disk and disk.stdout:
        print(CYAN + "[DISK]" + RESET)
        for l in disk.stdout.strip().split("\n")[:5]:
            print(f"  {l}")

    up = run("uptime 2>/dev/null")
    if up and up.stdout:
        print(CYAN + f"\n  Uptime : {up.stdout.strip()}" + RESET)

    # Network interfaces
    ifconfig = run("ip addr show 2>/dev/null || ifconfig 2>/dev/null")
    if ifconfig and ifconfig.stdout:
        print(CYAN + "\n[NETWORK INTERFACES]" + RESET)
        for line in ifconfig.stdout.split("\n"):
            if "inet " in line or ": <" in line or "flags" in line:
                print(f"  {line.strip()}")

    # Top proses CPU
    top_r = run("ps aux --sort=-%cpu 2>/dev/null | head -6")
    if top_r and top_r.stdout:
        print(CYAN + "\n[TOP PROSES (CPU)]" + RESET)
        for l in top_r.stdout.strip().split("\n"):
            print(f"  {l}")

# ---------- Fast Scan threaded (improved: port check + latency) ----------
@screen_mode("FAST SCAN")
def fast_scan(targets):
    if not targets:
        print(RED + "[!] Tidak ada target." + RESET)
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
                # Quick check port 80 + 443
                open_p = []
                for p in [80, 443, 22]:
                    s = socket.socket()
                    s.settimeout(0.5)
                    if ip and s.connect_ex((ip, p)) == 0:
                        open_p.append(p)
                    s.close()
                port_str = f" ports:{open_p}" if open_p else ""
                results[t] = ("UP", ip)
                print(GREEN + f"  [UP]   {t:<22} -> {ip or '?'}  ({ms}ms){port_str}" + RESET)
            else:
                results[t] = ("DOWN", None)
                print(RED + f"  [DOWN] {t}" + RESET)

    print(CYAN + f"[*] Scanning {len(targets)} target parallel...\n" + RESET)
    threads = [threading.Thread(target=scan, args=(t,)) for t in targets]
    for th in threads: th.start()
    for th in threads: th.join()

    up = sum(1 for v in results.values() if v[0]=="UP")
    print_sep()
    print(CYAN + f"[+] {up}/{len(targets)} host aktif." + RESET)

# ---------- Whois (improved: parse lebih clean, highlight expiry) ----------
@screen_mode("WHOIS")
def whois_lookup(t):
    t = strip_scheme(t)
    if not is_valid_target(t):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    if not tool_check("whois"):
        return
    print(CYAN + f"[*] WHOIS {t}..." + RESET)
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
                # Highlight expiry mendekati atau sudah lewat
                if "expir" in key:
                    try:
                        date_part = line.split(":",1)[1].strip()
                        # Coba parse berbagai format
                        for fmt in ["%Y-%m-%dT%H:%M:%SZ","%Y-%m-%d","%d-%b-%Y"]:
                            try:
                                exp_date = datetime.strptime(date_part[:10], fmt[:len(date_part[:10])])
                                days_left = (exp_date - datetime.utcnow()).days
                                if days_left < 0:
                                    print(RED + f"  {line}  <- EXPIRED {abs(days_left)} hari lalu!" + RESET)
                                elif days_left < 30:
                                    print(YELLOW + f"  {line}  <- {days_left} hari lagi!" + RESET)
                                else:
                                    print(GREEN + f"  {line}  ({days_left} hari lagi)" + RESET)
                                break
                            except:
                                continue
                        else:
                            print(YELLOW + f"  {line}" + RESET)
                    except:
                        print(YELLOW + f"  {line}" + RESET)
                else:
                    print(YELLOW + f"  {line}" + RESET)
            else:
                print(f"  {line}")
        save_log(f"WHOIS {t}")
    else:
        print(RED + "[-] WHOIS gagal." + RESET)

# ---------- GeoIP (improved: map link, ISP detail, timezone) ----------
@screen_mode("GEO IP")
def geo_ip(t):
    t = strip_scheme(t)
    if not is_valid_target(t):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    if not tool_check("curl"):
        return
    ip = get_ip(t)
    query = ip if ip else t
    print(CYAN + f"[*] GeoIP: {t} -> {query}" + RESET)

    # Primary: ipinfo.io
    r = run(f"curl -s --max-time 10 ipinfo.io/{query}")
    if r and r.stdout.strip():
        try:
            data = json.loads(r.stdout)
            if data.get("bogon"):
                print(YELLOW + "[i] IP private/bogon — tidak ada geo info." + RESET)
                return
            print_sep()
            fields = [
                ("IP","ip"),("Hostname","hostname"),("Kota","city"),
                ("Region","region"),("Negara","country"),("Lokasi","loc"),
                ("ISP/ORG","org"),("Postal","postal"),("Timezone","timezone"),
            ]
            for label, key in fields:
                val = data.get(key, "N/A")
                color = GREEN if val and val != "N/A" else RED
                print(color + f"  {label:<10}: {val}" + RESET)

            loc = data.get("loc","")
            if loc:
                lat, lon = loc.split(",")
                print(CYAN + f"\n  Maps     : https://maps.google.com/?q={lat},{lon}" + RESET)

            # Tambahan: cek apakah VPN/hosting (org biasanya "AS..." + nama provider)
            org = data.get("org","")
            hosting_keywords = ["hosting","server","cloud","datacenter","vps","aws","azure","google","digitalocean","linode","vultr","ovh"]
            if any(kw in org.lower() for kw in hosting_keywords):
                print(YELLOW + f"  [i] Kemungkinan Hosting/VPN/Cloud" + RESET)

            save_log(f"GEOIP {t}: {data.get('city')},{data.get('country')}")
        except json.JSONDecodeError:
            print(r.stdout[:500])
    else:
        print(RED + "[-] Gagal GeoIP. Cek internet." + RESET)

# ---------- HTTP Header (improved: lebih detail, cookie check, redirect chain) ----------
@screen_mode("HTTP HEADER")
def http_header_scan(t):
    t = t.strip()
    if not is_valid_target(t):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    if not tool_check("curl"):
        return
    print(CYAN + f"[*] Headers dari {t}..." + RESET)

    # Ambil header dengan redirect chain
    r = run(f"curl -I -s --max-time 10 -L -A 'Mozilla/5.0' --max-redirs 5 {t}")
    if not (r and r.stdout.strip()):
        # Fallback ke http
        t_http = t.replace("https://","http://")
        r = run(f"curl -I -s --max-time 10 {t_http}")
        if not (r and r.stdout.strip()):
            print(RED + "[-] Gagal ambil header (coba manual)." + RESET)
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
            print(color + BOLD + f"  {line}  {desc}" + RESET)
            if code.startswith("3"):
                redirect_count += 1
        elif "location:" in low:
            print(YELLOW + f"  {line}  <- redirect ke sini" + RESET)
        elif "set-cookie:" in low:
            # Check cookie flags
            issues = []
            if "httponly" not in low:
                issues.append("NO HttpOnly")
            if "secure" not in low:
                issues.append("NO Secure")
            if "samesite" not in low:
                issues.append("NO SameSite")
            flag_str = f"  [!] {', '.join(issues)}" if issues else "  [OK]"
            flag_color = RED if issues else GREEN
            print(CYAN + f"  {line}" + flag_color + flag_str + RESET)
        elif any(x in low for x in ["server:","x-powered-by:","via:","x-generator:"]):
            print(YELLOW + f"  {line}  <- fingerprint info" + RESET)
        elif any(k in low for k in security_headers):
            for k, desc in security_headers.items():
                if k in low:
                    found_sec.append(desc)
            print(GREEN + f"  {line}" + RESET)
        else:
            print(f"  {line}")

    if redirect_count > 0:
        print(YELLOW + f"\n  [i] {redirect_count} redirect terjadi." + RESET)

    print_sep()
    print(CYAN + "\n[SECURITY HEADERS REPORT]" + RESET)
    score = 0
    for s in security_headers.values():
        if s in found_sec:
            print(GREEN + f"  [OK] {s}" + RESET)
            score += 1
        else:
            print(RED + f"  [!!] {s} — MISSING" + RESET)

    grade = "A" if score >= 6 else ("B" if score >= 4 else ("C" if score >= 2 else "F"))
    g_color = GREEN if grade == "A" else (YELLOW if grade in "BC" else RED)
    print(g_color + f"\n  Security Score: {score}/{len(security_headers)}  Grade: {grade}" + RESET)
    save_log(f"HTTP HEADER {t} score:{score}/7")

# ---------- SSL Check (improved: cipher, protocol version, chain) ----------
@screen_mode("SSL CHECK")
def ssl_check(t):
    t = strip_scheme(t)
    if not is_valid_target(t):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    if not tool_check("openssl"):
        return
    print(CYAN + f"[*] SSL Check: {t}:443" + RESET)
    r = run(
        f"echo | openssl s_client -connect {t}:443 -servername {t} 2>/dev/null",
        timeout=15
    )
    if not (r and r.stdout.strip()):
        print(RED + "[-] Koneksi SSL gagal." + RESET)
        return

    print_sep()
    issues = []
    for line in r.stdout.split("\n"):
        line = line.strip()
        if any(x in line for x in ["subject=","issuer="]):
            print(CYAN + f"  {line}" + RESET)
        elif "notBefore" in line:
            print(GREEN + f"  Issued  : {line}" + RESET)
        elif "notAfter" in line:
            try:
                date_str = line.split("=",1)[1].strip()
                exp = datetime.strptime(date_str, "%b %d %H:%M:%S %Y %Z")
                sisa = (exp - datetime.utcnow()).days
                if sisa < 0:
                    issues.append("Sertifikat EXPIRED")
                    print(RED + f"  Expired : {date_str} <- SUDAH EXPIRED!" + RESET)
                elif sisa < 14:
                    issues.append(f"Sertifikat habis {sisa} hari lagi")
                    print(RED + f"  Expired : {date_str} <- {sisa} hari lagi! SEGERA RENEW!" + RESET)
                elif sisa < 30:
                    print(YELLOW + f"  Expired : {date_str} <- {sisa} hari lagi!" + RESET)
                else:
                    print(GREEN + f"  Expired : {date_str} ({sisa} hari lagi)" + RESET)
            except:
                print(GREEN + f"  {line}" + RESET)
        elif "Verify return code" in line:
            color = GREEN if "0 (ok)" in line.lower() else RED
            mark = "[OK]" if "0 (ok)" in line.lower() else "[FAIL]"
            if "[FAIL]" in mark:
                issues.append("SSL Verify GAGAL")
            print(color + f"  {mark} {line}" + RESET)
        elif "Protocol" in line:
            # Flag protokol lama
            if any(old in line for old in ["TLSv1 ","TLSv1.0","TLSv1.1","SSLv3","SSLv2"]):
                issues.append(f"Protokol lama: {line.strip()}")
                print(RED + f"  {line}  <- DEPRECATED!" + RESET)
            else:
                print(GREEN + f"  {line}" + RESET)
        elif "Cipher" in line:
            print(YELLOW + f"  {line}" + RESET)

    # Test protokol lama
    print_sep()
    print(CYAN + "[PROTOCOL TEST]" + RESET)
    for proto, label in [("-tls1_2","TLSv1.2"),("-tls1_1","TLSv1.1"),("-tls1","TLSv1.0")]:
        pr = run(f"echo | openssl s_client {proto} -connect {t}:443 -servername {t} 2>&1 | grep -c 'Cipher'", timeout=8)
        if pr and pr.stdout.strip() == "1":
            color = GREEN if "1.2" in label else RED
            mark = "[OK]" if "1.2" in label else "[DEPRECATED]"
            if "DEPRECATED" in mark:
                issues.append(f"{label} masih aktif")
            print(color + f"  {mark} {label} supported" + RESET)
        else:
            print(RED + f"  [NO]  {label} tidak support / timeout" + RESET)

    print_sep()
    if issues:
        print(RED + "\n[!] ISSUES DITEMUKAN:" + RESET)
        for iss in issues:
            print(RED + f"    - {iss}" + RESET)
    else:
        print(GREEN + "\n[+] SSL OK — Tidak ada masalah ditemukan." + RESET)

    save_log(f"SSL CHECK {t} issues:{len(issues)}")

# ---------- Dir Scan threaded ----------
@screen_mode("DIR SCAN")
def dir_bruteforce(t):
    t = t.strip().rstrip("/")
    if not is_valid_target(t):
        print(RED + "[!] Target tidak valid." + RESET)
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
    print(CYAN + f"[*] Target : {t}")
    print(f"[*] Paths  : {len(paths)} | Threaded" + RESET)
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
                print(GREEN + f"  [200 FOUND]  {url}  [{size}]" + RESET)
                found.append(url)
                save_log(f"DIR FOUND {url}")
            elif code in ("301","302","307","308"):
                print(YELLOW + f"  [{code} REDIR]  {url}" + RESET)
            elif code == "403":
                print(CYAN + f"  [403 FORBID] {url}" + RESET)
            elif code == "401":
                print(MAGENTA + f"  [401 AUTH]   {url}" + RESET)
            else:
                print(RED + f"  [{code} MISS]  {url}" + RESET)

    threads = []
    for p in paths:
        th = threading.Thread(target=check_path, args=(p,))
        th.start()
        threads.append(th)
        time.sleep(0.04)
    for th in threads:
        th.join()
    print_sep()
    print(CYAN + f"[+] Selesai. {len(found)} path ditemukan." + RESET)
    if found:
        print(GREEN + "[FOUND LIST]" + RESET)
        for f in found:
            print(GREEN + f"    {f}" + RESET)

# ---------- Subdomain threaded ----------
@screen_mode("SUBDOMAIN")
def subdomain_scan(d):
    d = strip_scheme(d)
    if not is_valid_target(d):
        print(RED + "[!] Domain tidak valid." + RESET)
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
    print(CYAN + f"  Target  : {d}")
    print(f"  Words   : {len(subs)} subdomain" + RESET)
    print_sep()

    def check(s):
        host = f"{s}.{d}"
        ip = get_ip(host)
        with lock:
            if ip:
                print(GREEN + f"  [FOUND] {host:<35} -> {ip}" + RESET)
                found.append((host, ip))
                save_log(f"SUBDOMAIN {host}->{ip}")

    print(CYAN + "[*] Scanning..." + RESET)
    threads = [threading.Thread(target=check, args=(s,)) for s in subs]
    for th in threads: th.start()
    for th in threads: th.join()
    print_sep()
    print(CYAN + f"[+] Selesai. {len(found)} subdomain aktif." + RESET)
    if not found:
        print(RED + "[-] Tidak ada subdomain yang ditemukan." + RESET)

# ---------- Full Security Report (improved: summary + risk score) ----------
@screen_mode("FULL SECURITY REPORT")
def security_report(t):
    t = strip_scheme(t.strip())
    if not is_valid_target(t):
        print(RED + "[!] Target tidak valid." + RESET)
        return
    url = normalize_url(t)
    ip = get_ip(t)
    all_ips = get_all_ips(t)
    start_time = time.time()

    print(CYAN + f"""
  Target : {t}
  IP     : {ip or 'Gagal resolve'}
  URL    : {url}
  Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
""" + RESET)
    print_sep()

    risk_score = 0
    findings = []

    # 1. DNS
    print(YELLOW + BOLD + "[ 1/6 ] DNS" + RESET)
    dns_lookup_raw(t)
    if len(all_ips) > 1:
        print(CYAN + f"  [Multi-IP / CDN] {', '.join(all_ips[:5])}" + RESET)

    # 2. PING + Latency
    print(YELLOW + BOLD + "\n[ 2/6 ] PING & LATENCY" + RESET)
    r = run(f"ping -c 3 -W 2 {t}", timeout=15)
    if r and r.returncode == 0:
        for line in r.stdout.strip().split("\n"):
            if "rtt" in line or "packet" in line:
                print(GREEN + f"  {line.strip()}" + RESET)
        lat = calc_latency(t)
        if lat:
            q = "Excellent" if lat < 20 else ("Good" if lat < 80 else "Fair")
            print(GREEN + f"  Status: AKTIF  Avg: {lat:.1f}ms [{q}]" + RESET)
    else:
        print(RED + "  Status: Tidak respon ping (ICMP mungkin diblokir)" + RESET)

    # TTL / OS hint
    r_ping1 = run(f"ping -c 1 -W 2 {t}", timeout=5)
    if r_ping1 and r_ping1.stdout:
        for line in r_ping1.stdout.split("\n"):
            if "ttl=" in line.lower():
                try:
                    ttl = int(re.search(r"ttl=(\d+)", line, re.I).group(1))
                    os_g = "Linux/Unix" if ttl <= 64 else ("Windows" if ttl <= 128 else "Network Device")
                    print(YELLOW + f"  TTL: {ttl} -> Kemungkinan OS: {os_g}" + RESET)
                except: pass

    # 3. PORT SCAN
    print(YELLOW + BOLD + "\n[ 3/6 ] PORT SCAN" + RESET)
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
                    b_str = f" | {banner}" if banner else ""
                    is_risk = p in HIGH_RISK
                    color = RED if is_risk else GREEN
                    label = "[HIGH-RISK]" if is_risk else ""
                    print(color + f"  OPEN  {p:5} ({svc}) {label}{b_str}" + RESET)
                    open_p.append(p)
            s.close()
        ths = [threading.Thread(target=pscan, args=(p,svc)) for p,svc in COMMON_PORTS.items()]
        for th in ths: th.start()
        for th in ths: th.join()
        risky = [p for p in open_p if p in HIGH_RISK]
        risk_score += len(risky) * 2
        if risky:
            findings.append(f"Port high-risk terbuka: {risky}")
        print(CYAN + f"  [{len(open_p)} port terbuka dari {len(COMMON_PORTS)}]" + RESET)

    # 4. HTTP HEADER
    print(YELLOW + BOLD + "\n[ 4/6 ] HTTP HEADER" + RESET)
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
                    color = YELLOW if any(x in low for x in ["server","powered"]) else ""
                    print(color + f"  {l}" + RESET)
            missing = sec_total - sec_found
            if missing > 3:
                risk_score += 2
                findings.append(f"{missing} security header hilang")
            print(CYAN + f"  Security headers: {sec_found}/{sec_total}" + RESET)

    # 5. SSL
    print(YELLOW + BOLD + "\n[ 5/6 ] SSL" + RESET)
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
                            print(RED + f"  SSL EXPIRED! {date_str}" + RESET)
                        elif sisa < 30:
                            risk_score += 2
                            findings.append(f"SSL hampir expired ({sisa} hari)")
                            print(YELLOW + f"  SSL {sisa} hari lagi expire: {date_str}" + RESET)
                        else:
                            print(GREEN + f"  SSL OK — {sisa} hari lagi: {date_str}" + RESET)
                    except:
                        print(f"  {line}")
                elif "Verify return code" in line:
                    color = GREEN if "0 (ok)" in line.lower() else RED
                    print(color + f"  {line}" + RESET)
        else:
            print(RED + "  Tidak support HTTPS / SSL gagal" + RESET)
            findings.append("HTTPS tidak aktif atau SSL gagal")
            risk_score += 3

    # 6. SUMMARY & RISK
    elapsed = round(time.time()-start_time, 1)
    print(YELLOW + BOLD + "\n[ 6/6 ] SUMMARY" + RESET)
    print_sep()
    print(CYAN + f"  Scan Duration : {elapsed}s")
    print(f"  Target        : {t}")
    print(f"  IP            : {ip or 'N/A'}" + RESET)

    if findings:
        print(RED + "\n  [!] FINDINGS:" + RESET)
        for f in findings:
            print(RED + f"      - {f}" + RESET)

    risk_label = "LOW" if risk_score < 3 else ("MEDIUM" if risk_score < 7 else "HIGH")
    r_color = GREEN if risk_score < 3 else (YELLOW if risk_score < 7 else RED)
    print(r_color + f"\n  Risk Score    : {risk_score}  [{risk_label}]" + RESET)

    print_sep()
    save_output_demo(t)
    print(GREEN + BOLD + "\n[+] Full Security Report Selesai!" + RESET)
    save_log(f"FULL REPORT {t} risk:{risk_label}({risk_score})")

# ================= AI =================
try:
    import pyttsx3
    engine = pyttsx3.init()
except:
    engine = None

def ai_voice_mode():
    if engine:
        text = input("AI Voice: ")
        engine.say(text)
        engine.runAndWait()
    else:
        print(RED + "[-] Voice tidak tersedia." + RESET)
        print(YELLOW + "    Install: pip install pyttsx3" + RESET)

# ============================================================
#  SUB-MENU DASHBOARDS
# ============================================================

def sub_header(title, color=CYAN):
    clear()
    print(color + BOLD + f"""
╔{"═"*42}╗
║  🧸 SkyWings :: {title:<23}║
╚{"═"*42}╝
""" + RESET)

def sub_back_prompt():
    print(CYAN + "  [0] ← Kembali ke Main Menu" + RESET)
    print(CYAN + "═"*42 + RESET)

# ─── NETWORK ───────────────────────────────────────────────
def menu_network():
    while True:
        sub_header("NETWORK", GREEN)
        print(GREEN + BOLD + "  ┌─ NETWORK TOOLS ────────────────────┐" + RESET)
        print(GREEN + "  │  [1]  Quick Scan    - Info Cepat      │")
        print(GREEN + "  │  [2]  Multi Scan    - Banyak Target   │")
        print(GREEN + "  │  [3]  Trace Route   - Lacak Rute      │")
        print(GREEN + "  │  [4]  Ping Target   - ICMP Ping       │")
        print(GREEN + "  │  [5]  Port Scan     - Scan Port       │")
        print(GREEN + "  └────────────────────────────────────────┘" + RESET)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "1":
            t = input(YELLOW + "  Target: " + RESET).strip()
            if t: quick_info(t)
        elif p == "2":
            raw = input(YELLOW + "  Targets (pisah spasi): " + RESET).strip()
            if raw: fast_scan(raw.split())
        elif p == "3":
            t = input(YELLOW + "  Target: " + RESET).strip()
            if t: trace_route(t)
        elif p == "4":
            t = input(YELLOW + "  Target: " + RESET).strip()
            if t: ping_target(t)
        elif p == "5":
            t = input(YELLOW + "  Target: " + RESET).strip()
            if t: port_scan(t)
        else:
            print(RED + "  [!] Pilihan tidak valid." + RESET)
            time.sleep(0.6)

# ─── WEB INTEL ─────────────────────────────────────────────
def menu_webintel():
    while True:
        sub_header("WEB INTEL", CYAN)
        print(CYAN + BOLD + "  ┌─ WEB INTEL TOOLS ──────────────────┐" + RESET)
        print(CYAN + "  │  [6]  Web Info      - Header + DNS    │")
        print(CYAN + "  │  [7]  HTTP Header   - Security Header │")
        print(CYAN + "  │  [8]  Dir Scan      - Brute Path      │")
        print(CYAN + "  │  [9]  Subdomain     - Enum Subdomain  │")
        print(CYAN + "  │  [10] SSL Check     - Cek Sertifikat  │")
        print(CYAN + "  └────────────────────────────────────────┘" + RESET)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "6":
            t = input(YELLOW + "  Web/Domain: " + RESET).strip()
            if t:
                http_header_scan(normalize_url(t))
                clear()
                kali_header("WEB INFO - DNS")
                dns_lookup_raw(t)
                enter_back()
        elif p == "7":
            t = input(YELLOW + "  URL: " + RESET).strip()
            if t: http_header_scan(normalize_url(t))
        elif p == "8":
            t = input(YELLOW + "  URL: " + RESET).strip()
            if t: dir_bruteforce(normalize_url(t))
        elif p == "9":
            t = input(YELLOW + "  Domain: " + RESET).strip()
            if t: subdomain_scan(t)
        elif p == "10":
            t = input(YELLOW + "  Domain: " + RESET).strip()
            if t: ssl_check(t)
        else:
            print(RED + "  [!] Pilihan tidak valid." + RESET)
            time.sleep(0.6)

# ─── OSINT ─────────────────────────────────────────────────
def menu_osint():
    while True:
        sub_header("OSINT", YELLOW)
        print(YELLOW + BOLD + "  ┌─ OSINT TOOLS ───────────────────────┐" + RESET)
        print(YELLOW + "  │  [11] WHOIS        - Info Domain      │")
        print(YELLOW + "  │  [12] GEO IP       - Lokasi IP        │")
        print(YELLOW + "  │  [13] DNS Lookup   - DNS Records      │")
        print(YELLOW + "  └────────────────────────────────────────┘" + RESET)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "11":
            t = input(YELLOW + "  Target: " + RESET).strip()
            if t: whois_lookup(t)
        elif p == "12":
            t = input(YELLOW + "  IP/Domain: " + RESET).strip()
            if t: geo_ip(t)
        elif p == "13":
            t = input(YELLOW + "  Domain: " + RESET).strip()
            if t: dns_lookup_menu(t)
        else:
            print(RED + "  [!] Pilihan tidak valid." + RESET)
            time.sleep(0.6)

# ─── SYSTEM ────────────────────────────────────────────────
def menu_system():
    while True:
        sub_header("SYSTEM", GREEN)
        print(GREEN + BOLD + "  ┌─ SYSTEM TOOLS ──────────────────────┐" + RESET)
        print(GREEN + "  │  [14] Firewall     - Cek Firewall     │")
        print(GREEN + "  │  [15] System Info  - Info OS & RAM    │")
        print(GREEN + "  └────────────────────────────────────────┘" + RESET)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "14":
            firewall_check()
        elif p == "15":
            system_info()
        else:
            print(RED + "  [!] Pilihan tidak valid." + RESET)
            time.sleep(0.6)

# ─── ADVANCED ──────────────────────────────────────────────
def menu_advanced():
    while True:
        sub_header("ADVANCED", MAGENTA)
        print(MAGENTA + BOLD + "  ┌─ ADVANCED TOOLS ────────────────────┐" + RESET)
        print(MAGENTA + "  │  [16] Nmap Scan    - Advanced Scan   │")
        print(MAGENTA + "  │  [17] Full Report  - Laporan Lengkap │")
        print(MAGENTA + "  │  [18] Save Output  - Simpan Hasil    │")
        print(MAGENTA + "  └────────────────────────────────────────┘" + RESET)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "16":
            t = input(YELLOW + "  Target: " + RESET).strip()
            if t: advanced_scan(t)
        elif p == "17":
            t = input(YELLOW + "  Target: " + RESET).strip()
            if t: security_report(t)
        elif p == "18":
            t = input(YELLOW + "  Target: " + RESET).strip()
            if t:
                clear()
                kali_header("SAVE OUTPUT")
                save_output_demo(t)
                enter_back()
        else:
            print(RED + "  [!] Pilihan tidak valid." + RESET)
            time.sleep(0.6)

# ─── AI TOOLS ──────────────────────────────────────────────
def menu_aitools():
    while True:
        sub_header("AI TOOLS", CYAN)
        print(CYAN + BOLD + "  ┌─ AI TOOLS ──────────────────────────┐" + RESET)
        print(CYAN + "  │  [19] AI Voice     - Text to Speech  │")
        print(CYAN + "  │  [20] Fast Scan    - Ping Paralel    │")
        print(CYAN + "  └────────────────────────────────────────┘" + RESET)
        sub_back_prompt()

        p = input(skywings_codex()).strip()
        if p == "0":
            break
        elif p == "19":
            ai_voice_mode()
            enter_back()
        elif p == "20":
            raw = input(YELLOW + "  Targets (pisah spasi): " + RESET).strip()
            if raw: fast_scan(raw.split())
        else:
            print(RED + "  [!] Pilihan tidak valid." + RESET)
            time.sleep(0.6)

# ============================================================
#  MAIN MENU (KATEGORI)
# ============================================================

def main_menu():
    while True:
        clear()
        print(ai_color() + BOLD + f"""
╔══════════════════════════════════════════╗
║        🔓 SYSTEM STATUS LIVE             ║
║  Time : {datetime.now().strftime('%H:%M:%S')}  |  SKYWINGS ACTIVE    ║
╚══════════════════════════════════════════╝
""" + RESET)

        print(GREEN + BOLD  + "  ┌─ [ NETWORK ] ──────────────────────┐")
        print(GREEN         + "  │  [1]  NETWORK    - Scan Jaringan   │")
        print(GREEN         + "  └─────────────────────────────────────┘" + RESET)

        print(CYAN + BOLD   + "  ┌─ [ WEB INTEL ] ─────────────────────┐")
        print(CYAN          + "  │  [2]  WEB INTEL  - Analisa Web      │")
        print(CYAN          + "  └─────────────────────────────────────┘" + RESET)

        print(YELLOW + BOLD + "  ┌─ [ OSINT ] ─────────────────────────┐")
        print(YELLOW        + "  │  [3]  OSINT      - Intelijen        │")
        print(YELLOW        + "  └─────────────────────────────────────┘" + RESET)

        print(GREEN + BOLD  + "  ┌─ [ SYSTEM ] ────────────────────────┐")
        print(GREEN         + "  │  [4]  SYSTEM     - Info Sistem      │")
        print(GREEN         + "  └─────────────────────────────────────┘" + RESET)

        print(MAGENTA + BOLD+ "  ┌─ [ ADVANCED ] ──────────────────────┐")
        print(MAGENTA       + "  │  [5]  ADVANCED   - Scan Lanjutan    │")
        print(MAGENTA       + "  └─────────────────────────────────────┘" + RESET)

        print(CYAN + BOLD   + "  ┌─ [ AI TOOLS ] ──────────────────────┐")
        print(CYAN          + "  │  [6]  AI TOOLS   - Fitur AI         │")
        print(CYAN          + "  └─────────────────────────────────────┘" + RESET)

        print(CYAN + "═"*44)
        print(RED + "  [0]  EXIT".center(44))
        print(CYAN + "═"*44 + RESET)

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
            print(ai_color() + "\n[*] VIPER DOWN. Stay safe.\n" + RESET)
            break
        else:
            print(RED + "  [!] Pilihan tidak valid." + RESET)
            time.sleep(0.6)

# ================= MAIN =================
def main():
    clear()
    logo()
    loading("SKYWINGS V1.0 BOOTING")

    while True:
        kali_header("SKYWINGS BY PUTRA")
        print(GREEN + """
help   -> masuk fitur
info   -> system info
clear  -> clear
exit   -> keluar
""" + RESET)

        cmd = input(skywings_codex()).strip()

        if cmd == "help":
            fancy_loading("ENTERING FEATURE MODE")
            main_menu()
        elif cmd == "info":
            system_info()
        elif cmd == "clear":
            clear()
        elif cmd == "exit":
            print(ai_color() + "\n[*] SKYWINGS. Stay safe.\n" + RESET)
            break
        else:
            print(RED + "[-] Command tidak dikenal. Ketik 'help'." + RESET)

if __name__ == "__main__":
    main()
