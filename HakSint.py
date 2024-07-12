# Coded By Haket
# Owned By Haket
# ©Haket
# This Tools For Osint
import os
import sys
import time
import pytz
import whois
import socket
import requests
import colorama
import pycountry
import subprocess
import phonenumbers
from geopy.geocoders import Nominatim
from colorama import Fore, Back, Style
from phonenumbers import geocoder, carrier, timezone


# Menu
def menu():
    
    print(Style.BRIGHT, Fore.BLUE + """
__________(█)
_______██████
_____ ████████	    [+] Note   : Welcome in HakSint
___███████████      [+] Author : Haket
___ (░░░░░░░)░░░)   [+] Name-T : HakSint
___(░(░█░░█░)░░░)   [+] Type   : White-Hat
__ (░░(░░●░░░)░░░)
__ (░░░░◡░░)░░░░)
_██(░░░░░░░░░░)██
_███(░░░░░░░░░)███
████ ██(░░░)██ ████
████ █████████ ███
████ ████░████ ███
(░░)_ ▓▓▓▓▌▓▐▓▓▓_(░░)
(██) ███████████ (██)
_____█████░█████_▓▓▓)
_____█████-,█████▓▓▓▓▓)
_____█████-,█████▓▓▓▓▓)
___(░░░░░░)(░░░░░) ▓▓▓▓)
______(███)_(███)▓▓▓▓▓▓)
____ (████)_(████)▓▓▓▓▓)""")
    # Teks Haket
    text = "[Owned By Haket]"

    text1 = "[Welcome To Haksint]"
    # Format Text
    Format = f"{Style.BRIGHT}{Back.GREEN}{Fore.WHITE}{text}{Style.RESET_ALL}"
    # Format Text1
    Format1 = f"{Back.BLUE}{Fore.WHITE}{text1}{Style.RESET_ALL}"
    # Panjang Text
    Panjang = 42
    # Panjang Text1
    Panjang1 = 38
    # Text Ditengah
    text_tengah = Format.center(Panjang)
    # Text1 Ditengah
    text1_tengah = Format1.center(Panjang1)
    print(text_tengah)
    print(text1_tengah)
    print(Style.BRIGHT, Fore.GREEN)
    print("[1].Phone Number Osint")
    print("[2].IP Osint")
    print("[3].Website Osint")
    print("[4].About")
    print("[5].Exit")

# Aksi Pemilihan Menu
def aksi():
    while True:
        os.system("clear")
        menu()
        pilih = int(input("Select Choice: "))
        if pilih == 1:
            fit1()
            Cb()

        elif pilih == 2:
            fit2()
            Cb()
        elif pilih == 3:
            fit3()
            Cb()

        elif pilih == 4:
            fit4()
            Cb()

        elif pilih == 5:
            fit5()

        else:
            os.system("clear")
            print("ERROR 404 PAGE NOT FOUND :(")
            time.sleep(2)

# Menu Settings:

# Koordinat Ibukota
zonawaktu_kordinat = {
    "Pacific/Midway": {"ibukota": "Midway", "latitude": -11.55, "longitude": -177.3667},
    "Pacific/Honolulu": {"ibukota": "Honolulu", "latitude": 21.3069, "longitude": -157.8583},
    "America/Anchorage": {"ibukota": "Anchorage", "latitude": 61.2181, "longitude": -149.9003},
    "America/Los_Angeles": {"ibukota": "Los Angeles", "latitude": 34.0522, "longitude": -118.2437},
    "America/Denver": {"ibukota": "Denver", "latitude": 39.7392, "longitude": -104.9903},
    "America/Chicago": {"ibukota": "Chicago", "latitude": 41.8781, "longitude": -87.6298},
    "America/New_York": {"ibukota": "New York", "latitude": 40.7128, "longitude": -74.0060},
    "Europe/London": {"ibukota": "London", "latitude": 51.5074, "longitude": -0.1278},
    "Europe/Berlin": {"ibukota": "Berlin", "latitude": 52.52, "longitude": 13.405},
    "Asia/Jakarta": {"ibukota": "Jakarta", "latitude": -6.2088, "longitude": 106.8456},
    "Asia/Tokyo": {"ibukota": "Tokyo", "latitude": 35.6895, "longitude": 139.6917},
    "Australia/Sydney": {"ibukota": "Sydney", "latitude": -33.8688, "longitude": 151.2093},
    "Asia/Jerusalem": {"ibukota": "Neraka", "latitude": 31.7683, "longitude": 35.2137},
}

# Nama Wilayah
wilayah_negara = {
    "AF": "Asia",
    "AL": "Europe",
    "DZ": "Africa",
    "AS": "Oceania",
    "AD": "Europe",
    "AO": "Africa",
    "AI": "North America",
    "AQ": "Antarctica",
    "AG": "North America",
    "AR": "South America",
    "AM": "Asia",
    "AW": "North America",
    "AU": "Oceania",
    "AT": "Europe",
    "AZ": "Asia",
    "BS": "North America",
    "BH": "Asia",
    "BD": "Asia",
    "BB": "North America",
    "BY": "Europe",
    "BE": "Europe",
    "BZ": "North America",
    "BJ": "Africa",
    "BM": "North America",
    "BT": "Asia",
    "BO": "South America",
    "BA": "Europe",
    "BW": "Africa",
    "BR": "South America",
    "IO": "Asia",
    "BN": "Asia",
    "BG": "Europe",
    "BF": "Africa",
    "BI": "Africa",
    "CV": "Africa",
    "KH": "Asia",
    "CM": "Africa",
    "CA": "North America",
    "KY": "North America",
    "CF": "Africa",
    "TD": "Africa",
    "CL": "South America",
    "CN": "Asia",
    "CX": "Asia",
    "CC": "Asia",
    "CO": "South America",
    "KM": "Africa",
    "CD": "Africa",
    "CG": "Africa",
    "CK": "Oceania",
    "CR": "North America",
    "CI": "Africa",
    "HR": "Europe",
    "CU": "North America",
    "CY": "Asia",
    "CZ": "Europe",
    "DK": "Europe",
    "DJ": "Africa",
    "DM": "North America",
    "DO": "North America",
    "EC": "South America",
    "EG": "Africa",
    "SV": "North America",
    "GQ": "Africa",
    "ER": "Africa",
    "EE": "Europe",
    "ET": "Africa",
    "FK": "South America",
    "FO": "Europe",
    "FJ": "Oceania",
    "FI": "Europe",
    "FR": "Europe",
    "GF": "South America",
    "PF": "Oceania",
    "GA": "Africa",
    "GM": "Africa",
    "GE": "Asia",
    "DE": "Europe",
    "GH": "Africa",
    "GI": "Europe",
    "GR": "Europe",
    "GL": "North America",
    "GD": "North America",
    "GP": "North America",
    "GU": "Oceania",
    "GT": "North America",
    "GG": "Europe",
    "GN": "Africa",
    "GW": "Africa",
    "GY": "South America",
    "HT": "North America",
    "VA": "Europe",
    "HN": "North America",
    "HK": "Asia",
    "HU": "Europe",
    "IS": "Europe",
    "IN": "Asia",
    "ID": "Asia",
    "IR": "Asia",
    "IQ": "Asia",
    "IE": "Europe",
    "IM": "Europe",
    "IL": "Asia",
    "IT": "Europe",
    "JM": "North America",
    "JP": "Asia",
    "JE": "Europe",
    "JO": "Asia",
    "KZ": "Asia",
    "KE": "Africa",
    "KI": "Oceania",
    "KP": "Asia",
    "KR": "Asia",
    "KW": "Asia",
    "KG": "Asia",
    "LA": "Asia",
    "LV": "Europe",
    "LB": "Asia",
    "LS": "Africa",
    "LR": "Africa",
    "LY": "Africa",
    "LI": "Europe",
    "LT": "Europe",
    "LU": "Europe",
    "MO": "Asia",
    "MG": "Africa",
    "MW": "Africa",
    "MY": "Asia",
    "MV": "Asia",
    "ML": "Africa",
    "MT": "Europe",
    "MH": "Oceania",
    "MQ": "North America",
    "MR": "Africa",
    "MU": "Africa",
    "YT": "Africa",
    "MX": "North America",
    "FM": "Oceania",
    "MD": "Europe",
    "MC": "Europe",
    "MN": "Asia",
    "ME": "Europe",
    "MS": "North America",
    "MA": "Africa",
    "MZ": "Africa",
    "MM": "Asia",
    "NA": "Africa",
    "NR": "Oceania",
    "NP": "Asia",
    "NL": "Europe",
    "NC": "Oceania",
    "NZ": "Oceania",
    "NI": "North America",
    "NE": "Africa",
    "NG": "Africa",
    "NU": "Oceania",
    "NF": "Oceania",
    "MK": "Europe",
    "MP": "Oceania",
    "NO": "Europe",
    "OM": "Asia",
    "PK": "Asia",
    "PW": "Oceania",
    "PA": "North America",
    "PG": "Oceania",
    "PY": "South America",
    "PE": "South America",
    "PH": "Asia",
    "PL": "Europe",
    "PT": "Europe",
    "PR": "North America",
    "QA": "Asia",
    "RE": "Africa",
    "RO": "Europe",
    "RU": "Europe",
    "RW": "Africa",
    "BL": "North America",
    "SH": "Africa",
    "KN": "North America",
    "LC": "North America",
    "MF": "North America",
    "PM": "North America",
    "VC": "North America",
    "WS": "Oceania",
    "SM": "Europe",
    "ST": "Africa",
    "SA": "Asia",
    "SN": "Africa",
    "RS": "Europe",
    "SC": "Africa",
    "SL": "Africa",
    "SG": "Asia",
    "SX": "North America",
    "SK": "Europe",
    "SI": "Europe",
    "SB": "Oceania",
    "SO": "Africa",
    "ZA": "Africa",
    "SS": "Africa",
    "ES": "Europe",
    "LK": "Asia",
    "SD": "Africa",
    "SR": "South America",
    "SJ": "Europe",
    "SZ": "Africa",
    "SE": "Europe",
    "CH": "Europe",
    "SY": "Asia",
    "TW": "Asia",
    "TJ": "Asia",
    "TZ": "Africa",
    "TH": "Asia",
    "TL": "Asia",
    "TG": "Africa",
    "TK": "Oceania",
    "TO": "Oceania",
    "TT": "North America",
    "TN": "Africa",
    "TR": "Asia",
    "TM": "Asia",
    "TC": "North America",
    "TV": "Oceania",
    "UG": "Africa",
    "UA": "Europe",
    "AE": "Asia",
    "GB": "Europe",
    "US": "North America",
    "UY": "South America",
    "UZ": "Asia",
    "VU": "Oceania",
    "VE": "South America",
    "VN": "Asia",
    "VG": "North America",
    "VI": "North America",
    "EH": "Africa",
    "YE": "Asia",
    "ZM": "Africa",
    "ZW": "Africa",
}

# Settings Untuk Fitur 1
def info_nomor(nomor_telpon):
    try:
        # pemanggilan nomor handphone
        parse_nomor = phonenumbers.parse(nomor_telpon)

        # kode negara
        kode_negara = phonenumbers.region_code_for_number(parse_nomor)

        # nomor negara
        nomor_negara = parse_nomor.country_code

        # mengambil info negara dari nomor
        negara = geocoder.country_name_for_number(parse_nomor, "en")

        # mengambil info wilayah negara
        wilayah = wilayah_negara.get(kode_negara, "Unknown")

        # mengambil info kartu sim nomor
        kartu_sim = carrier.name_for_number(parse_nomor, "en")

        # mengambil info zona waktu nomor
        zona_waktu = timezone.time_zones_for_number(parse_nomor)

        # mengambil format nomor internasional
        nomor_internasional = phonenumbers.format_number(parse_nomor, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        # mengambil format nomor nasional
        nomor_nasional = phonenumbers.format_number(parse_nomor, phonenumbers.PhoneNumberFormat.NATIONAL)

        # menghapus hal-hal yang ada di format nasional
        nomor_nasional = ''.join(filter(str.isdigit, nomor_nasional))

        # cek nomornya valid
        nomor_valid = phonenumbers.is_valid_number(parse_nomor)

        # cek tipe nomor
        tipe_line = phonenumbers.number_type(parse_nomor)
        if tipe_line == phonenumbers.PhoneNumberType.MOBILE:
            tipe_line_str = "mobile"
        elif tipe_line == phonenumbers.PhoneNumberType.FIXED_LINE:
            tipe_line_str = "fixed line"
        elif tipe_line == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
            tipe_line_str = "fixed line or mobile"
        elif tipe_line == phonenumbers.PhoneNumberType.TOLL_FREE:
            tipe_line_str = "toll free"
        elif tipe_line == phonenumbers.PhoneNumberType.VOIP:
            tipe_line_str = "voip"
        else:
            tipe_line_str = "unknown"

        # mengambil nama ibukota dan koordinatnya
        ibukota_zonawaktu = [zonawaktu_kordinat[tz]["ibukota"] for tz in zona_waktu if tz in zonawaktu_kordinat]
        kordinat_zonawaktu = [{"latitude": zonawaktu_kordinat[tz]["latitude"], "longitude": zonawaktu_kordinat[tz]["longitude"]} for tz in zona_waktu if tz in zonawaktu_kordinat]

        return {
            "[+]Nomor Target": nomor_telpon,
            "[+]Format Internasional": nomor_internasional,
            "[+]Format nasional": nomor_nasional,
            "[+]Nomor Negara": nomor_negara,
            "valid": nomor_valid,
            "[+]Negara": negara,
            "[+]Kode Negara": kode_negara,
            "[+]Wilayah": wilayah,
            "nama ibukota": ibukota_zonawaktu,
            "koordinat ibukota": kordinat_zonawaktu,
            "[+]Kartu Sim": kartu_sim,
            "[+]Tipe Line": tipe_line_str
        }

    except phonenumbers.NumberParseException:
        return {"Valid": False, "error": "invalid format nomor handphone"}

# Fitur 1 Settings
def fit1():
    os.system("clear")
    print("""
             ⬛⬛⬛⬛⬛⬛
           ⬛⬛⬛⬛⬛⬛⬛⬛
           ⬛⬛⬛⬛⬛⬛⬛⬛
         ⬛⬛🟥🟥⬛⬛🟥🟥⬛⬛
         ⬛⬛🟥🟥⬛⬛🟥🟥⬛⬛
         ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
         ⬛⬛⬛🟥🟥🟥🟥⬛⬛⬛
           ⬛⬛⬛🟥🟥⬛⬛⬛
             ⬛⬛⬛⬛⬛⬛
               ⬛⬛⬛⬛""" + Style.BRIGHT, Fore.YELLOW)
    print("|—————————Phone–Number–Osint—————————|")
    print("|____________________________________|")
    print("|masukkan nomor telepon dengan format|")
    print("|negara, contoh: +6212345678910      |")
    print("|__________Coded_By:[Haket]__________|")
    print(Style.BRIGHT, Fore.BLUE)
    nomor_telpon = input("[?] Enter Target Number: ")
    print(Style.BRIGHT, Fore.GREEN)
    info = info_nomor(nomor_telpon)
    if info["valid"]:
        print("Hasil Osint Target: ")
        for key, value in info.items():
            if key not in ["valid", "nama ibukota", "koordinat ibukota"]:
                print(f"{key}: {value}")
        for i in range(len(info["nama ibukota"])):
            print(f"[+]Nama Ibukota {i+1}: {info['nama ibukota'][i]}")
            print(f"[+]Koordinat Ibukota {i+1}: Latitude: {info['koordinat ibukota'][i]['latitude']}, Longitude: {info['koordinat ibukota'][i]['longitude']}")
        print(f"[+]Valid: {info['valid']}")
    else:
        print(f"Error: {info['error']}")



# Settings Untuk Fitur 2
def ambil_ip():
    try:
      response = requests.get("https://api.ipify.org?format=json")
      info_ip = response.json()
      return info_ip['ip']
    except Exception as e:
      print(f"Gagal mendapatkan IP. Error: {e}")
      return None

def mengambil_lokasi(ip):
    try:
       response = requests.get(f"https://ipinfo.io/{ip}/json")
       info_lokasi = response.json()
       return info_lokasi
    except Exception as e:
      print(f"Gagal mendapatkan lokasi IP. Error: {e}")
      return None

def format_lokasi(info_lokasi):
    formasi_info = "\n".join(f"{key}: {value}" for key, value in info_lokasi.items())
    return formasi_info

def log_ip_lokasi(ip, info_lokasi, log_filename):
    with open(log_filename, "a") as log_file:
         log_file.write(f"{time.ctime()}: IP:{ip}\n")
         log_file.write(format_lokasi(info_lokasi))
         log_file.write("\n\n")

def lacak_ip(interval, log_filename):
    while True:
       ip = ambil_ip()
       if ip:
          info_lokasi = mengambil_lokasi(ip)
          if info_lokasi:
             log_ip_lokasi(ip, info_lokasi, log_filename)
             print(f"IP: {ip}")
             print(format_lokasi(info_lokasi))
          else:
              print("Gagal mengambil IP")
       else:
           print("Gagal mengambil IP")
       time.sleep(interval)

# Fitur 2 Settings
def fit2():
    os.system("clear")
    print(Fore.WHITE + """
                      ..
              .:lllodxkOkxdool:'
          .:odxxc;dd;0NWMMMNKOOOxdl.
        ;oo;co0lxlo0:lllodxxdoldM0kkxc.
      ;xo,dd,:dKXXNNc...........NMMW0xkl
    .kocod;ckKNWWMWK:...........xMMMMM0d0'
   ,OckdloKXNWWMMW0;.............;:lKMMWd0:
  '0ckc,xXNWWWMkoll,............lWWMMMMMMx0c
  K;xkdcXNWWWWKXOWMd............xWWMWMMMMWlX.
 cdcx;,loXWWWdXkXMMo............:oxOWMMMMMXox
 O:dxddOOloWWKKoNMNk;..............,MWMMMMWcN
 KcNNNWWXKk;KMMNNkOWN..............;WWWMWWWcW
 0cWWMMMMMX0.KMMMMMMMk...............kMMMMMcN
 lkOMMWWWMMM0,c0WMMMd.................;NMMXox
  XcNWWWWMMMKOc..oMk....................MMlN.
  'KlWWWWWM00;....xW'...................Kd0:
   'KoNWWWMK;......l....................,O:
     OdOMMMMWk............................
      ,kxOWMMM0.......................
        .xxkOWM0....................
           .dxkO,................
                .   .........""" + Style.BRIGHT, Fore.BLUE)
    print("            [HakSint: Author: Haket]")
    print("            [Track IP Lokal/Pribadi]" + Style.BRIGHT, Fore.GREEN)
    print("""
__________________________________________________
[Cara Pemakaian: Buat File Yang Berisi Target.txt]
|Contoh        : [$] Waktu Pergerakan: 60        |
|Contoh        : [#] Nama File Lacak : target.txt|
|Contoh        : Tekan ctrl + z Untuk Berhenti   |
__________________________________________________""")
    print()
    interval = int(input(Fore.YELLOW + "[$] Waktu Pergerakan: "))
    log_filename = input(Fore.GREEN + "[#] Nama File Lacak : ")
    print(Fore.WHITE + "[+]Hasil Lacak Target[+]" + Fore.YELLOW)
    print()
    lacak_ip(interval, log_filename)



# Settings Untuk Fitur 3
def web_ip(domain):
    try:
       alamat_ip = socket.gethostbyname(domain)
       return alamat_ip
    except socket.error as err:
       return f"Error: {err}"

def info_whois(domain):
    try:
       w = whois.whois(domain)
       return w
    except Exception as err:
       return f"Error: {err}"

# Fitur 3 Settings
def fit3():
    os.system("clear")
    print(Style.RESET_ALL, Fore.BLUE + """
               .........',
            .,:c......'dkxl,...
        .:oooc;'.......;xkoooc,...
      ,oo:'......;,';';'.:o.';odc'..
    ,xl'.......;o;.;o.'lc......':xl'..
   do'........lc...;o...;d'......'lx;..
  x:.........lc,;;:ld:;;,,d'.......;k:..
 xc......':codc;;,':o',,;:lxcc,..,'.,k;..
,x....,cc:,.x,.....;o......x,'cl:cc:;lx...
kc...;:'...'x......;o.....,ccccoxOkdlcc:,'
O;...;ccccclxcccccclxcccccccdkOOOOOOOOxocc
l:...,'....,x......;o....'ccOOOOOOOOokOkc;
.o...'cc:'..k'.....;o....'ccOOd:Od;,lOOkc.
 c,.....,cccdl'....;o....'ccOOO.':xOOOOx,
  c,........'xlcccclxccccclcoOOOOOOOOOk:
   ,:........'d,...;o...'o:;ccdkOOOOkd.
     o,.......'lc..;o..;o,..';ccloolc
       c:'..o:..,c,,c'::......;dl;,
          oc:xo'..........,:odl,
              ,o.......:ool.
                    ..""" + Style.BRIGHT, Fore.BLUE)
    print("    [HakSint: Author: [Haket]: WebSint]")
    print(" [Contoh: [T] Target Website: github.com]")
    print(Style.BRIGHT, Fore.GREEN)
    target_website = input("[T] Target Website: ")
    if target_website == "Cb":
       Cb()
    print(Fore.WHITE + "\n[+]--- Proses Osint Target ---[+]" + Style.RESET_ALL, Fore.BLUE)
    alamat_ip = web_ip(target_website)
    print(f"IP Address: {alamat_ip}" + Style.BRIGHT, Fore.GREEN)

    whois = info_whois(target_website)

    print(Fore.WHITE + "\n[+]--- Hasil Osint Target ---[+]" + Fore.GREEN)
    if isinstance(info_whois, str):
       print(info_whois)
    else:
       for key, value in whois.items():
           if value is None:
              value = "N/A"
           print(f"[+] {key}: {value}\n")
    print()
    # Jalanin Printah Whois
    hasil = subprocess.run(['whois',target_website], capture_output=True, text=True)
    # Memproses Hasil
    format_hasil = "\n\n".join(f"[+] {line}" for line in hasil.stdout.splitlines())
    print(format_hasil)

# Fitur 4 Settings
def fit4():
    os.system("clear")
    print(Style.BRIGHT, Fore.YELLOW + """[+]=============================================[+]""" + Style.BRIGHT)
    print(Fore.GREEN + "List Author: " + Fore.WHITE, Style.BRIGHT)
    print("[+] Category   : White-Hat")
    print("[+] Name Tools : HakSint")
    print("[+] Author Name: Haket")
    print("[-] Locate     : N/a")
    print("[-] Region     : N/a")
    print("[+] TimeCreate : 4/7/24")
    print("[+] Massage    : Halo 三三ᕕ( ᐛ )ᕗ")
    print(Style.BRIGHT, Fore.YELLOW + """[+]=============================================[+]""" + Style.BRIGHT)
    print(Fore.BLUE + "[#] Description:")
    print(Fore.GREEN + """Tools Ini Dibuat Hanya Untuk Edukasi Osint
Tanpa Apikey Menggunakan Bahasa Python Untuk 
Pembelajaran Bersama,
Gunakan Tools Ini Dengan Bijak Dan Untuk 
Tujuan Kebaikan.""")
    print(Style.BRIGHT, Fore.YELLOW + """[+]=============================================[+]""" + Style.BRIGHT)


# Fitur 5 Settings
def fit5():
    os.system("clear")
    print(Style.BRIGHT)
    print(Fore.YELLOW + """
────────────────████
───────────────█░░███
───────────────█░░████
────────────────███▒██─────████████
──────████████─────█▒█──████▒▒▒▒▒▒████
────███▒▒▒▒▒▒████████████░░████▒▒▒▒▒███     [+] H
──██▒▒▒▒░▒▒████░░██░░░░██░░░░░█▒▒▒▒▒▒▒███   [+] A
─██▒▒░░░░▒██░░░░░█▒░░░░░██▒░░░░░░░▒▒▒▒▒▒█   [+] K
██▒░░░░░▒░░░░░░░░░▒░░░░░░░▒▒░░░░░░░▒▒▒▒▒██  [+] S
█░░░░░░▒░░░██░░░░░░░░░░░░░██░░░░░░░░▒▒▒▒▒█  [+] I
█░░░░░░░░█▒▒███░░░░░░░░░█▒▒███░░░░░░░▒▒▒▒█  [+] N
█░░░░░░░████████░░░░░░░████████░░░░░░▒▒▒▒█  [+] T
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█
██░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░▒▒▒▒█  [+] E
─█░░░░██░█░░░░░░░░░░░░░░░░░░░░░░░███▒▒▒▒▒█  [+] X
─█▒▒░░░░█████░░░█░░░░██░░░██░░████░▒▒▒▒▒▒█  [+] I
─██▒▒░░░░░█████████████████████░░░▒▒▒▒▒▒██  [+] T
──██▒▒▒▒░░░░░██░░░███░░░██░░░█░░░▒▒▒▒▒▒██
───███▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█████
─────███▒▒▒▒▒▒░░░░░░░░░░░░░▒▒▒▒▒▒████
────────██████████████████████████
""")
    print(Fore.WHITE + "        Thanks For View This Tools")
    sys.exit()

# Callback Setting
def Cb():
    again = input(Fore.WHITE + "Comeback? [Y/n]:")
    if again == "Y":
        aksi()
    elif again == "n":
        fit5()
    else:
        fit5()

# Menu utama aksi
aksi()

# ©Haket
# Knowledge Is Free
# We Are Anonymous
# We Are Legion
# We Do Not Forgive
# We Do Not Forget
# Expect Us
