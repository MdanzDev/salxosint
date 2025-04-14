import os
import time
import requests

# Membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menampilkan logo
def display_logo():
    clear_screen()
    print("""
\033[1;31m███████╗ █████╗ ██╗     ██╗  ██╗    ██████╗  ██████╗ ██╗  ██╗
\033[1;31m██╔════╝██╔══██╗██║     ╚██╗██╔╝    ██╔══██╗██╔═══██╗╚██╗██╔╝
\033[1;31m███████╗███████║██║      ╚███╔╝     ██║  ██║██║   ██║ ╚███╔╝ 
\033[1;31m╚════██║██╔══██║██║      ██╔██╗     ██║  ██║██║   ██║ ██╔██╗ 
\033[1;31m███████║██║  ██║███████╗██╔╝ ██╗    ██████╔╝╚██████╔╝██╔╝ ██╗
\033[1;31m╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
\033[1;35m                OSINT TOOL BY SALX | Version 1.0
    """)

# Fungsi pencarian OSINT berdasarkan nama
def search_by_name():
    clear_screen()
    display_logo()
    name = input("\n\033[1;35mMasukkan Nama:\033[1;m ")
    print("\n\033[1;33m[INFO]\033[1;m Mencari informasi dari sumber...\n")
    time.sleep(2)

    sources = [
          f"https://pipl.com/search/?q={name}",
        f"https://www.facebook.com/search/top/?q={name}",
        f"https://www.spokeo.com/{name}",
        f"https://www.peekyou.com/{name}",
        f"https://twitter.com/search?q={name}",
        f"https://instagram.com/{name}",
        f"https://www.linkedin.com/search/results/people/?keywords={name}",
        f"https://www.truepeoplesearch.com/results?name={name}",
        f"https://www.zabasearch.com/people/{name}/",
        f"https://www.thatsthem.com/name/{name}"
    ]

    for source in sources:
        print(f"\033[1;32m[+] {source}\033[1;m")

    input("\n\033[1;32mTekan Enter untuk kembali ke menu utama...\033[1;m")
    main_menu()

# Fungsi pencarian OSINT berdasarkan nombor telefon
def search_by_phone():
    clear_screen()
    display_logo()
    phone_number = input("\n\033[1;35mMasukkan Nombor Telefon (Dengan Kod Negara):\033[1;m ")
    print("\n\033[1;33m[INFO]\033[1;m Mengambil informasi, sila tunggu...\n")
    time.sleep(2)

    sources = [
        f"http://www.okcaller.com/{phone_number}",
        f"https://www.facebook.com/search/top/?q={phone_number}",
        f"https://www.truecaller.com/search/global/{phone_number}",
        f"https://www.whitepages.com/phone/{phone_number}",
        f"https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui={phone_number}",
        f"https://whocallsme.com/Phone-Number.aspx/{phone_number}",
        f"https://www.sync.me/search/?number={phone_number}",
        f"https://www.411.com/phone/{phone_number}",
        f"https://calleridtest.com/{phone_number}",
        f"https://numlookup.com/{phone_number}",
        f"https://wa.me/{phone_number}",
        f"https://t.me/{phone_number}"
    ]

    for source in sources:
        print(f"\033[1;32m[+] {source}\033[1;m")

    input("\n\033[1;32mTekan Enter untuk kembali ke menu utama...\033[1;m")
    main_menu()

# Fungsi pencarian maklumat berdasarkan IP Address
def search_by_ip():
    clear_screen()
    display_logo()
    ip_address = input("\n\033[1;35mMasukkan IP Address:\033[1;m ")

    print("\n\033[1;33m[INFO]\033[1;m Mengambil data, sila tunggu...\n")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}?fields=66846719")
        data = response.json()

        if data["status"] == "fail":
            print("\033[1;31m[ERROR]\033[1;m IP Address tidak valid!")
            time.sleep(2)
            return

        # Menampilkan data IP Address
        print("\033[1;32m══════════════════════════════════════════\033[1;m")
        print(f"\033[1;35m🌍 Negara      :\033[1;m {data['country']} ({data['countryCode']})")
        print(f"\033[1;35m📍 Wilayah     :\033[1;m {data['regionName']}")
        print(f"\033[1;35m🏙️  Kota        :\033[1;m {data['city']}")
        print(f"\033[1;35m⏱️  Timezone    :\033[1;m {data['timezone']}")
        print(f"\033[1;35m📡 ISP         :\033[1;m {data['isp']}")
        print(f"\033[1;35m🌐 ASN         :\033[1;m {data['as']}")
        print(f"\033[1;35m🕵️  Tipe Jaringan :\033[1;m {data['mobile'] and 'Mobile' or 'Fixed-line'}")
        print(f"\033[1;35m📍 Koordinat   :\033[1;m {data['lat']}, {data['lon']}")
        print("\033[1;32m══════════════════════════════════════════\033[1;m")

        # Cek apakah IP ada dalam database AbuseIPDB (Blacklist Check)
        check_blacklist(ip_address)

    except requests.exceptions.RequestException:
        print("\033[1;31m[ERROR]\033[1;m Tidak dapat menghubungi server!")

    input("\n\033[1;32mTekan Enter untuk kembali ke menu utama...\033[1;m")
    main_menu()

# Fungsi untuk cek apakah IP masuk dalam blacklist
def check_blacklist(ip):
    print("\n\033[1;33m[CHECK]\033[1;m Mengecek blacklist database...\n")
    try:
        response = requests.get(f"https://www.abuseipdb.com/check/{ip}")
        if response.status_code == 200:
            print(f"\033[1;31m🚨 IP {ip} mungkin telah dilaporkan sebagai berbahaya!\033[1;m")
            print(f"🔗 Lihat detail: https://www.abuseipdb.com/check/{ip}")
        else:
            print(f"\033[1;32m✅ IP {ip} tidak ditemukan dalam database blacklist.\033[1;m")
    except:
        print("\033[1;31m[ERROR]\033[1;m Tidak dapat mengambil data blacklist.")

# Fungsi untuk menampilkan menu utama
def main_menu():
    while True:
        display_logo()
        print("\033[1;32m╔════════════════════════════════════╗")
        print("║           \033[1;31mSALX OSINT MENU\033[1;32m            ║")
        print("╠════════════════════════════════════╣")
        print("║  \033[1;33m1. OSINT by Name\033[1;32m                       ║")
        print("║  \033[1;33m2. OSINT by Number\033[1;32m                     ║")
        print("║  \033[1;33m3. IP Address Detail\033[1;32m                    ║")
        print("║  \033[1;31m0. Exit\033[1;32m                               ║")
        print("╚════════════════════════════════════╝\033[1;m")

        option = input("\033[1;35m  Pilih opsi:\033[1;m ")
        menu_actions = {
            "1": search_by_name,
            "2": search_by_phone,
            "3": search_by_ip,
            "0": exit
        }

        action = menu_actions.get(option)
        if action:
            action()
        else:
            print("\033[1;31m[ERROR]\033[1;m Pilihan tidak valid!")
            time.sleep(2)

# Jalankan program
if __name__ == "__main__":
    main_menu()
