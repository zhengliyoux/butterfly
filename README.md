<div align="center">

```
 ____  _           __        ___                 
/ ___|| | ___   _ _\ \      / (_)_ __   __ _ ___ 
\___ \| |/ / | | \ \ \ /\ / /| | '_ \ / _` / __|
 ___) |   <| |_| |\ \ V  V / | | | | | (_| \__ \
|____/|_|\_\\__, | \_\_/\_/  |_|_| |_|\__, |___/
            |___/                      |___/     
```

**Network Intelligence Suite for Termux**

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-black?style=flat-square&logo=linux&logoColor=white)](https://termux.dev)
[![Version](https://img.shields.io/badge/Version-2.0-cyan?style=flat-square)](.)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](.)
[![Stars](https://img.shields.io/github/stars/zhengliyoux/skywings?style=flat-square&color=yellow)](.)

</div>

---

## ✦ Tentang SkyWings

**SkyWings** adalah toolkit intelijen jaringan berbasis CLI yang dirancang untuk Termux dan Linux.  
Ringan, cepat, dan dilengkapi tampilan terminal bergaya hacker — cocok untuk recon, audit, dan monitoring jaringan.

---

## ⚡ Fitur Utama

| Kategori | Tools |
|---|---|
| 🌐 **Network** | Quick Info, Multi Scan, Ping, Port Scan, Traceroute |
| 🌍 **Web Intel** | HTTP Header, Dir Scan, Subdomain, SSL Check |
| 🕵️ **OSINT** | WHOIS, Geo IP, DNS Lookup |
| 💻 **System** | System Info, Firewall Check |
| 🗡️ **Advanced** | Nmap Scanner, Full Security Report, Save Output |
| 🤖 **AI Tools** | Fast Scan, AI Voice Mode |

---

## 📦 Instalasi

### 1 · Update & Install Dependensi

```bash
pkg update && pkg upgrade -y
pkg install git python -y
```

### 2 · Clone Repository

```bash
git clone https://github.com/zhengliyoux/butterfly.git
```

### 3 · Masuk ke Direktori

```bash
cd butterfly
```

### 4 · Jalankan Tool

```bash
python butterfly.py
```

---

## 🔄 Update Tool

Untuk mendapatkan versi terbaru:

```bash
git pull origin main
```

> **Catatan:** Pastikan kamu sudah berada di dalam folder repo hasil `git clone` sebelum menjalankan perintah di atas.

---

## 🛠️ Dependensi Opsional

| Tool | Kegunaan | Install |
|---|---|---|
| `nmap` | Advanced port scan | `pkg install nmap` |
| `whois` | WHOIS lookup | `pkg install whois` |
| `curl` | HTTP header, GeoIP | `pkg install curl` |
| `openssl` | SSL/TLS check | `pkg install openssl` |
| `dig` | DNS records | `pkg install dnsutils` |
| `traceroute` | Trace route | `pkg install traceroute` |

---

## 📋 Cara Pakai

Setelah tool berjalan, ketik salah satu perintah berikut di prompt:

```
SkyWings@root ❯ help     → masuk menu fitur
SkyWings@root ❯ info     → system info
SkyWings@root ❯ clear    → bersihkan layar
SkyWings@root ❯ exit     → keluar
```

Dari menu utama, pilih kategori tool yang ingin digunakan dengan mengetik angkanya.

---

## ⚠️ Disclaimer

> Tool ini dibuat **untuk keperluan edukasi, audit mandiri, dan riset keamanan jaringan**.  
> Penggunaan terhadap sistem yang bukan milik kamu **tanpa izin adalah ilegal**.  
> Developer tidak bertanggung jawab atas penyalahgunaan tool ini.

---

## 👤 Developer

<div align="center">

**Ganz SyahPutra**  
*Script by SkyWings · v2.0 · Codename: Wings Point O*

[![GitHub](https://img.shields.io/badge/GitHub-zhengliyoux-black?style=flat-square&logo=github)](https://github.com/zhengliyoux)

---

⭐ **Kalau tool ini bermanfaat, kasih bintang di GitHub ya!**

</div>
