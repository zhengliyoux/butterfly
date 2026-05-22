# 🔥 Phoenix Visions — Network Recon Tool

> Tool recon jaringan serbaguna berbasis Python untuk Termux & Linux.  
> Coded with by **Putra**

---

## 📋 Fitur

| No | Fitur | Keterangan |
|----|-------|------------|
| 1 | 🌐 Website Info | IP, GeoIP, DNS, WHOIS, SSL, CMS Detection |
| 2 | 🔍 Port Scanner | Scan port umum atau custom range (multi-thread) |
| 3 | 🔎 Subdomain Scanner | Cari subdomain via crt.sh & hackertarget |
| 4 | 📡 LAN Host Discovery | Ping scan seluruh subnet lokal |
| 5 | 🔗 URL Extractor | Crawl semua URL dari website target |
| 6 | 🖥️ Network Info Lokal | Info interface, public IP, routing table |
| 7 | 📶 Traceroute | Trace jalur paket ke target |
| 8 | 🛡️ Phishing Detector | Deteksi redirect & URL mencurigakan |

---

## ⚙️ Cara Install & Run di Termux

### 1. Install Termux
Download dari [F-Droid](https://f-droid.org/packages/com.termux/) (disarankan, bukan Play Store).

---

### 2. Update & Install dependensi dasar

```bash
pkg update && pkg upgrade -y
pkg install python git -y
```

---

### 3. Clone repo dari GitHub

```bash
git clone https://github.com/zhengliyoux/butterfly.git
cd butterfly
```

---

### 4. Install library Python

```bash
pip install -r requirements.txt
```

Atau install manual:

```bash
pip install requests colorama dnspython beautifulsoup4
```

---

### 5. Jalankan tool

```bash
python phoenixvision.py
```

---

---

## 🗂️ Struktur Repo

```
phoenix-visions/
├── phoenixvisions.py            # File utama
├── requirements.txt   # Library yang dibutuhkan
└── README.md          # Dokumentasi ini
```

---

## 🔧 Troubleshooting

| Error | Solusi |
|-------|--------|
| `traceroute: not found` | `pkg install traceroute` |
| `ping: not found` | `pkg install inetutils` |
| `dnspython not found` | `pip install dnspython` |
| `bs4 not found` | `pip install beautifulsoup4` |
| Permission error | Jalankan ulang Termux, coba `pip install --user ...` |

---

## ⚠️ Disclaimer

Tool ini dibuat untuk **tujuan edukasi dan riset keamanan** pada sistem yang kamu miliki atau sudah mendapat izin. Penyalahgunaan sepenuhnya tanggung jawab pengguna.

---

## 👤 Author

- **Nama:** Putra  
- **GitHub:** [github.com/zhengliyoux](https://github.com/zhengliyoux)  
- **Tool:** Phoenix Visions v2.0.0
