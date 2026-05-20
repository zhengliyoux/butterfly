import socket
import requests
import json
import re
import os
import sys
import time
import threading
import ipaddress
import subprocess
from datetime import datetime
from urllib.parse import urljoin, urlparse

try:
    import dns.resolver
    HAS_DNS = True
except ImportError:
    HAS_DNS = False

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama -q")
    from colorama import Fore, Back, Style, init
    init(autoreset=True)

# ══════════════════════════════════════
#              COLORS
# ══════════════════════════════════════
R  = Fore.RED
G  = Fore.GREEN
Y  = Fore.YELLOW
C  = Fore.CYAN
M  = Fore.MAGENTA
W  = Fore.WHITE
B  = Fore.BLUE
LR = Fore.LIGHTRED_EX
LG = Fore.LIGHTGREEN_EX
LY = Fore.LIGHTYELLOW_EX
LC = Fore.LIGHTCYAN_EX
LM = Fore.LIGHTMAGENTA_EX
LW = Fore.LIGHTWHITE_EX
RS = Style.RESET_ALL
DIM = Style.DIM
BRT = Style.BRIGHT
# ══════════════════════════════════════
#              HELPERS
# ══════════════════════════════════════

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def sep(char="─", color=C, length=55):
    print(color + char * length)

def title(text, color=LM):
    sep("═", color)
    print(color + BRT + f"  {text}")
    sep("═", color)

def info(text):  print(LC + " ◆ " + W + text)
def ok(text):    print(LG + " ✔ " + W + text)
def err(text):   print(LR + " ✘ " + W + text)
def warn(text):  print(LY + " ⚠ " + W + text)
def data(k, v):  print(C + f"   {'':>1}▸ " + LW + f"{k}: " + G + str(v))

def loading(text, duration=1.2):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{LM}  {frames[i % len(frames)]}  {W}{text}", end="", flush=True)
        time.sleep(0.08)
        i += 1
    print("\r" + " " * 50 + "\r", end="")

def prompt(text):
    return input(LM + "\n  ➤ " + LW + text + C + " : " + G).strip()

def pause():
    input(DIM + C + "\n  [ tekan ENTER untuk lanjut ]")

# ══════════════════════════════════════
#              BANNER
# ══════════════════════════════════════

def banner():
    clear()
    print(M + BRT + """
  ██████╗ ██╗  ██╗ ██████╗ ███████╗███╗   ██╗██╗██╗  ██╗
  ██╔══██╗██║  ██║██╔═══██╗██╔════╝████╗  ██║██║╚██╗██╔╝
  ██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║██║ ╚███╔╝ 
  ██╔═══╝ ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║██║ ██╔██╗ 
  ██║     ██║  ██║╚██████╔╝███████╗██║ ╚████║██║██╔╝ ██╗
  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝""")
    print(C + "        ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗███████╗")
    print(C + "        ██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║██╔════╝")
    print(C + "        ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║███████╗")
    print(C + "        ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║╚════██║")
    print(C + "         ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║███████║")
    print(C + "          ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝")
    print()
    sep("─", M)
    print(M + "  ⚡ " + LW + "Phoenix Visions Network Recon Tool" + M + "  ⚡")
    print(C + "  👤 Coded by  : " + G + BRT + "Putra")
    print(C + "  🌐 GitHub    : " + G + "github.com/zhengliyoux")
    print(C + "  📅 Date      : " + G + datetime.now().strftime("%d %B %Y  %H:%M:%S"))
    print(C + "  ⚙️  Version   : " + G + "v2.0.0")
    sep("─", M)
    print()

# ══════════════════════════════════════
#         1. WEBSITE INFO
# ══════════════════════════════════════

def get_info(domain):
    title("🌐  WEBSITE INFO")
    loading("Mengambil informasi domain...")

    # IP Address
    try:
        ip = socket.gethostbyname(domain)
        ok(f"IP Address    : {G}{ip}")
    except Exception as e:
        err(f"Gagal resolve IP: {e}")
        return

    # HTTP Headers
    try:
        resp = requests.get("http://" + domain, timeout=6)
        info("Server Headers:")
        for k, v in resp.headers.items():
            data(k, v)
    except Exception:
        warn("Tidak bisa mengambil HTTP headers.")

    # GeoIP
    try:
        geo = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5).json()
        info("GeoIP Info:")
        data("City/Region", f"{geo.get('city', '-')}, {geo.get('region', '-')}")
        data("Country", geo.get('country', '-'))
        data("Org/ISP", geo.get('org', '-'))
        data("Timezone", geo.get('timezone', '-'))
        data("Hostname", geo.get('hostname', '-'))
    except Exception:
        warn("GeoIP gagal diambil.")

    # Reverse DNS
    try:
        rev = socket.gethostbyaddr(ip)[0]
        data("Reverse DNS", rev)
    except Exception:
        warn("Reverse DNS tidak ditemukan.")
        # DNS Records
    if HAS_DNS:
        info("DNS Records:")
        for rtype in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']:
            try:
                answers = dns.resolver.resolve(domain, rtype)
                for rd in answers:
                    data(rtype, rd.to_text())
            except Exception:
                pass
    else:
        warn("dnspython tidak terinstall. Jalankan: pip install dnspython")

    # WHOIS via RDAP
    try:
        rdap = requests.get(f"https://rdap.org/domain/{domain}", timeout=6).json()
        info("WHOIS (RDAP):")
        events = {e.get('eventAction'): e.get('eventDate') for e in rdap.get('events', [])}
        data("Registrar", rdap.get('registrar', {}).get('name', '-') if isinstance(rdap.get('registrar'), dict) else '-')
        data("Created", events.get('registration', '-'))
        data("Expires", events.get('expiration', '-'))
        data("Updated", events.get('last changed', '-'))
    except Exception:
        warn("Gagal mengambil WHOIS RDAP.")

    # SSL Info
    try:
        import ssl
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as ssock:
            ssock.settimeout(5)
            ssock.connect((domain, 443))
            cert = ssock.getpeercert()
            info("SSL Certificate:")
            data("Issuer", dict(x[0] for x in cert['issuer']).get('organizationName', '-'))
            data("Valid From", cert.get('notBefore', '-'))
            data("Valid Until", cert.get('notAfter', '-'))
            data("Subject", dict(x[0] for x in cert['subject']).get('commonName', '-'))
    except Exception:
        warn("SSL info tidak bisa diambil atau tidak support HTTPS.")

    # CMS & Tech Detection
    try:
        resp = requests.get("http://" + domain, timeout=6)
        html = resp.text
        powered = resp.headers.get('X-Powered-By', '')
        server = resp.headers.get('Server', '')
        info("Tech Stack Detection:")
        data("Server", server if server else '-')
        data("X-Powered-By", powered if powered else '-')
        cms = "Unknown"
        if 'wp-content' in html or 'wp-includes' in html:
            cms = "WordPress"
        elif 'Joomla' in html:
            cms = "Joomla"
        elif 'Drupal' in html:
            cms = "Drupal"
        elif 'Laravel' in html or 'laravel' in html:
            cms = "Laravel"
        elif 'Next.js' in html or '__NEXT_DATA__' in html:
            cms = "Next.js"
        data("CMS Detected", cms)
    except Exception:
        pass

    pause()

# ══════════════════════════════════════
#         2. PORT SCANNER
# ══════════════════════════════════════

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 6379: "Redis", 8080: "HTTP-Alt",
    8443: "HTTPS-Alt", 8888: "Jupyter", 27017: "MongoDB",
    9200: "Elasticsearch", 5000: "Flask/Dev"
}

open_ports = []
lock = threading.Lock()

def scan_port(ip, port, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((ip, port))
        s.close()
        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            banner_txt = ""
            try:
                s2 = socket.socket()
                s2.settimeout(1)
                s2.connect((ip, port))
                s2.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner_txt = s2.recv(128).decode(errors='ignore').split('\n')[0].strip()
                s2.close()
            except Exception:
                pass
            with lock:
                open_ports.append((port, service, banner_txt))
    except Exception:
        pass

def port_scanner():
    title("🔍  PORT SCANNER")
    target = prompt("Masukkan IP/Domain target")
    mode = prompt("Mode scan? [1] Common Ports  [2] Custom Range")

    try:
        ip = socket.gethostbyname(target)
    except Exception:
        err("Gagal resolve host!")
        pause()
        return

    open_ports.clear()
    ports = []

    if mode == "2":
        try:
            start = int(prompt("Port awal"))
            end = int(prompt("Port akhir"))
            ports = list(range(start, end + 1))
        except Exception:
            err("Input tidak valid.")
            pause()
            return
    else:
        ports = list(COMMON_PORTS.keys())

    info(f"Scanning {ip} — {len(ports)} port...")
    sep()

    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
        if len(threads) >= 100:
            for th in threads:
                th.join()
            threads = []

    for th in threads:
        th.join()

    if open_ports:
        ok(f"{len(open_ports)} port terbuka ditemukan:\n")
        print(C + f"  {'PORT':<8} {'SERVICE':<16} {'BANNER'}")
        sep("─", C, 55)
        for port, svc, bnr in sorted(open_ports):
            print(G + f"  {port:<8}" + LW + f"{svc:<16}" + DIM + W + bnr[:30])
    else:
        warn("Tidak ada port terbuka ditemukan.")

    pause()
    
# ══════════════════════════════════════
#         3. SUBDOMAIN SCANNER
# ══════════════════════════════════════

def extract_subdomains():
    title("🔎  SUBDOMAIN SCANNER")
    domain = prompt("Masukkan domain target")
    loading("Mencari subdomain dari crt.sh & hackertarget...")

    found = set()

    try:
        crt = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json", timeout=10).json()
        for entry in crt:
            for sub in entry.get('name_value', '').split('\n'):
                sub = sub.strip().lstrip('*.')
                if domain in sub:
                    found.add(sub)
        ok(f"crt.sh → {len(found)} subdomain")
    except Exception:
        err("Gagal dari crt.sh")

    try:
        ht = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", timeout=10).text
        for line in ht.strip().splitlines():
            sub = line.split(',')[0].strip()
            if domain in sub:
                found.add(sub)
        ok(f"hackertarget → total {len(found)} subdomain")
    except Exception:
        err("Gagal dari hackertarget")

    sep()
    if found:
        ok(f"Total {len(found)} subdomain ditemukan:\n")
        for i, sub in enumerate(sorted(found), 1):
            try:
                ip = socket.gethostbyname(sub)
                status = G + "✔ LIVE"
            except Exception:
                ip = "-"
                status = R + "✘ DOWN"
            print(C + f"  [{i:>3}] " + LW + f"{sub:<40}" + status + W + f"  {ip}")
    else:
        warn("Tidak ada subdomain ditemukan.")

    pause()

# ══════════════════════════════════════
#         4. NETWORK SCAN (LAN)
# ══════════════════════════════════════

alive_hosts = []
lock2 = threading.Lock()

def ping_host(ip_str):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip_str],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(ip_str)[0]
            except Exception:
                hostname = "-"
            with lock2:
                alive_hosts.append((ip_str, hostname))
    except Exception:
        pass

def network_scan():
    title("📡  LAN HOST DISCOVERY")

    # Detect local IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        local_ip = "192.168.1.1"

    info(f"IP Lokal terdeteksi: {G}{local_ip}")
    subnet = prompt(f"Masukkan subnet [default: {local_ip.rsplit('.', 1)[0]}.0/24]")

    if not subnet:
        subnet = local_ip.rsplit('.', 1)[0] + ".0/24"

    try:
        network = ipaddress.ip_network(subnet, strict=False)
    except Exception:
        err("Subnet tidak valid!")
        pause()
        return

    alive_hosts.clear()
    hosts = list(network.hosts())
    info(f"Scanning {len(hosts)} host di {subnet}...")
    sep()

    threads = []
    for host in hosts:
        t = threading.Thread(target=ping_host, args=(str(host),))
        threads.append(t)
        t.start()
        if len(threads) >= 50:
            for th in threads:
                th.join()
            threads = []
    for th in threads:
        th.join()

    sep()
    if alive_hosts:
        ok(f"{len(alive_hosts)} host aktif ditemukan:\n")
        print(C + f"  {'NO':<5} {'IP ADDRESS':<18} {'HOSTNAME'}")
        sep("─", C, 50)
        for i, (ip, hn) in enumerate(sorted(alive_hosts), 1):
            print(G + f"  {i:<5}" + LW + f"{ip:<18}" + DIM + W + hn)
    else:
        warn("Tidak ada host aktif ditemukan. Pastikan di jaringan yang sama.")

    pause()
    # ══════════════════════════════════════
#         5. URL EXTRACTOR
# ══════════════════════════════════════

def extract_urls():
    title("🔗  URL EXTRACTOR")
    if not HAS_BS4:
        err("BeautifulSoup tidak terinstall. Jalankan: pip install beautifulsoup4")
        pause()
        return

    domain = prompt("Masukkan domain target")
    loading("Crawling URL dari halaman...")

    seen = set()
    all_urls = set()
    social_domains = ['facebook.com', 'twitter.com', 'instagram.com', 'youtube.com', 'tiktok.com', 'linkedin.com']

    def crawl(url, base):
        if url in seen or len(seen) > 80:
            return
        seen.add(url)
        try:
            r = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(r.text, 'html.parser')
            for tag in soup.find_all(['a', 'script', 'link', 'iframe', 'img']):
                attr = tag.get('href') or tag.get('src')
                if attr:
                    full = urljoin(base, attr)
                    if re.match(r'^https?://', full):
                        all_urls.add(full)
            for script in soup.find_all("script"):
                if script.string:
                    for u in re.findall(r'https?://[^\s\'"<>]+', script.string):
                        all_urls.add(u)
        except Exception:
            pass

    crawl(f"http://{domain}", f"http://{domain}")

    internal = [u for u in all_urls if domain in u]
    external = [u for u in all_urls if domain not in u]
    social = [u for u in all_urls if any(s in u for s in social_domains)]

    sep()
    ok(f"Total URL   : {len(all_urls)}")
    data("Internal", len(internal))
    data("External", len(external))
    data("Sosial Media", len(social))
    sep()

    show = prompt("Tampilkan semua URL? [y/n]")
    if show.lower() == 'y':
        for url in sorted(all_urls):
            color = LG if domain in url else (LM if any(s in url for s in social_domains) else LC)
            print(color + "  → " + W + url)

    pause()

# ══════════════════════════════════════
#         6. NETWORK INFO (LOKAL)
# ══════════════════════════════════════

def network_info():
    title("🖥️   NETWORK INTERFACE INFO")
    loading("Mengambil info jaringan lokal...")

    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        data("Hostname", hostname)
        data("Local IP", local_ip)
    except Exception:
        warn("Gagal mengambil hostname/IP lokal.")

    try:
        pub_ip = requests.get("https://api.ipify.org", timeout=5).text.strip()
        data("Public IP", pub_ip)
        geo = requests.get(f"https://ipinfo.io/{pub_ip}/json", timeout=5).json()
        data("ISP/Org", geo.get('org', '-'))
        data("City", f"{geo.get('city', '-')}, {geo.get('country', '-')}")
        data("Timezone", geo.get('timezone', '-'))
    except Exception:
        warn("Gagal mengambil public IP / GeoIP.")

    try:
        result = subprocess.run(["ip", "route"], capture_output=True, text=True)
        info("Routing Table:")
        for line in result.stdout.strip().splitlines()[:8]:
            print(DIM + "   " + line)
    except Exception:
        pass

    try:
        result = subprocess.run(["ifconfig"], capture_output=True, text=True)
        if result.returncode == 0:
            info("Network Interfaces (ifconfig):")
            for line in result.stdout.strip().splitlines()[:20]:
                print(DIM + "   " + line)
    except Exception:
        pass

    pause()

# ══════════════════════════════════════
#         7. TRACEROUTE
# ══════════════════════════════════════

def traceroute():
    title("📶  TRACEROUTE")
    target = prompt("Masukkan IP/Domain target")
    info(f"Tracing route ke {target}...\n")
    sep()
    try:
        result = subprocess.run(
            ["traceroute", "-m", "20", target],
            capture_output=True, text=True, timeout=60
        )
        for line in result.stdout.splitlines():
            print(C + "  " + W + line)
    except FileNotFoundError:
        try:
            result = subprocess.run(
                ["tracepath", target],
                capture_output=True, text=True, timeout=60
            )
            for line in result.stdout.splitlines():
                print(C + "  " + W + line)
        except Exception:
            err("traceroute/tracepath tidak tersedia.")
    except Exception as e:
        err(f"Error: {e}")

    pause()

# ══════════════════════════════════════
#         8. PHISHING DETECTOR
# ══════════════════════════════════════

def phishing_detector():
    title("🛡️   PHISHING & REDIRECT DETECTOR")
    if not HAS_BS4:
        err("BeautifulSoup tidak terinstall. Jalankan: pip install beautifulsoup4")
        pause()
        return

    domain = prompt("Masukkan domain target")
    loading("Menganalisa link dan redirect...")

    phishing_keywords = ['login', 'verify', 'secure', 'account', 'bank', 'update', 'signin', 'reset', 'confirm', 'credential']
    urls = set()
    redirect_links = []
    suspicious = []

    try:
        r = requests.get(f"http://{domain}", timeout=6, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup.find_all(['a', 'script', 'iframe', 'link']):
            attr = tag.get('href') or tag.get('src')
            if attr and attr.startswith('http'):
                urls.add(attr)
    except Exception:
        warn("Gagal crawl halaman utama.")

    checked = set()
    for url in urls:
        if url in checked:
            continue
        checked.add(url)
        try:
            resp = requests.get(url, timeout=5, allow_redirects=True)
            if resp.history:
                final = resp.url
                if domain not in final:
                    redirect_links.append((url, final))
            for kw in phishing_keywords:
                if kw in url.lower():
                    parsed = urlparse(url)
                    if domain not in parsed.netloc:
                        suspicious.append(url)
        except Exception:
            pass

    sep()
    ok(f"Redirect terdeteksi: {len(redirect_links)}")
    for src, dst in redirect_links:
        print(Y + f"  ↳ {src[:40]}...")
        print(R + f"    → {dst}")

    print()
    ok(f"Potensi phishing URL: {len(suspicious)}")
    for s in suspicious:
        print(R + "  ⚠️  " + s)

    if not redirect_links and not suspicious:
        ok("Tidak ada redirect mencurigakan atau phishing URL ditemukan.")

    pause()

# ══════════════════════════════════════
#              MAIN MENU
# ══════════════════════════════════════

def menu():
    while True:
        banner()
        print(M + "  ╔══════════════════════════════════╗")
        print(M + "  ║" + LW + "         PILIH MENU UTAMA        " + M + "║")
        print(M + "  ╠══════════════════════════════════╣")
        print(M + "  ║  " + LC + "[1]" + W + " 🌐  Website Info           " + M + "║")
        print(M + "  ║  " + LC + "[2]" + W + " 🔍  Port Scanner           " + M + "║")
        print(M + "  ║  " + LC + "[3]" + W + " 🔎  Subdomain Scanner      " + M + "║")
        print(M + "  ║  " + LC + "[4]" + W + " 📡  LAN Host Discovery     " + M + "║")
        print(M + "  ║  " + LC + "[5]" + W + " 🔗  URL Extractor          " + M + "║")
        print(M + "  ║  " + LC + "[6]" + W + " 🖥️   Network Info Lokal     " + M + "║")
        print(M + "  ║  " + LC + "[7]" + W + " 📶  Traceroute             " + M + "║")
        print(M + "  ║  " + LC + "[8]" + W + " 🛡️   Phishing Detector      " + M + "║")
        print(M + "  ║  " + LR + "[0]" + W + " ❌  Keluar                 " + M + "║")
        print(M + "  ╚══════════════════════════════════╝")

        choice = prompt("Pilihan kamu")

        if choice == "1":
            domain = prompt("Masukkan domain target (contoh: google.com)")
            get_info(domain)
        elif choice == "2":
            port_scanner()
        elif choice == "3":
            extract_subdomains()
        elif choice == "4":
            network_scan()
        elif choice == "5":
            extract_urls()
        elif choice == "6":
            network_info()
        elif choice == "7":
            traceroute()
        elif choice == "8":
            phishing_detector()
        elif choice == "0":
            clear()
            print(M + BRT + "\n  Phoenix Visions — sampai jumpa! 👋\n")
            print(C + "  Coded with ❤️  by Putra\n")
            sys.exit(0)
        else:
            warn("Pilihan tidak valid! Coba lagi.")
            time.sleep(0.8)

# ══════════════════════════════════════
#              ENTRY POINT
# ══════════════════════════════════════

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(R + BRT + "\n\n  [!] Dihentikan paksa. Sampai jumpa!\n")
        sys.exit(0)