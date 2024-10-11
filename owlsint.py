import time
import os
import sys
import requests
import re
import json
import urllib
import colorama
import instaloader
from time import sleep
from datetime import datetime
import phonenumbers as pnumb
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from instaloader import instaloader
from phonenumbers import parse, PhoneNumber, PhoneNumberType, PhoneNumberFormat

### colors
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[1;93m"
WHITE = "\033[1;97m"
NORMAL = "\033[0;37m"

OKGREEN = '\033[92m'
WARNING = '\033[93m'
YE = '\033[1;33m'
BOLD = '\033[1m'
ENDC = '\033[0m'

CRED2 = "\33[91m"
CBLUE2 = "\33[94m"
ENDC = "\033[0m"

shaded_light_square = "\u2591"
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
### animation
def animation(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0025)
     
### banner
def banner():
    animation(f"""
    {BLUE}░█████╗░░██╗░░░░░░░██╗██╗░░░░░░██████╗██╗███╗░░██╗████████╗   
    ██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██║████╗░██║╚══██╔══╝          
    ██║░░██║░╚██╗████╗██╔╝██║░░░░░╚█████╗░██║██╔██╗██║░░░██║░░░             
    ██║░░██║░░████╔═████║░██║░░░░░░╚═══██╗██║██║╚████║░░░██║░░░               
    ╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██████╔╝██║██║░╚███║░░░██║░░░                  
    ░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░                   
    Version 1.2 - 2023 coded by Mr,Saya_IB

    \033[91m[??] Choose an option:
    \033[91m[\033[93m1\033[91m] \033[1;97mPhone Number Information
    \033[91m[\033[93m2\033[91m] \033[1;97mTrack IP
    \033[91m[\033[93m3\033[91m] \033[1;97mInstagram User Information
    \033[91m[\033[93mA\033[91m] \033[1;97mAbout""")

def start():
    os.system("cls")  # Clear screen in Windows
    banner()
    chose = input("           \033[94mChoose\033[0m: ")
    if chose == "1":  ## MENU 1
        sleep(1)
        print(f"""
        \033[91m[\033[93m1\033[91m] \033[1;97mTrack Number V1
        \033[91m[\033[93m2\033[91m] \033[1;97mTrack Number V2
        \033[91m[\033[93m3\033[91m] \033[1;97mTrack Number V3""")
        V = input(f"      {BLUE}Choose\033[0m: ")
        if V == "1":  ### chose 1
            number = input(f"{WHITE}Enter Number {NORMAL}({GREEN}Without +){WHITE} :{CRED2}➤ ")
            
            # Set default region explicitly
            default_region = "ID"  # Change this to the appropriate country code
            
            parsing = parse(number, default_region)
            loc = geocoder.description_for_number(parsing, "id")
            isp = carrier.name_for_number(parsing, "id")
            tz = timezone.time_zones_for_number(parsing)
            ### track number v1
            print()
            sleep(0.1)
            print(f"{YELLOW}International Format          {NORMAL}:", pnumb.normalize_digits_only(parsing))
            sleep(0.1)
            print(f"{YELLOW}National Format               {NORMAL}:", pnumb.format_number(parsing, PhoneNumberFormat.NATIONAL))
            sleep(0.1)
            print(f"{YELLOW}Valid Number                  {NORMAL}:", pnumb.is_valid_number(parsing))
            sleep(0.1)
            print(f"{YELLOW}Can Be Internatioally Dialled {NORMAL}:", pnumb.can_be_internationally_dialled(parsing))
            sleep(0.1)
            print(f"{YELLOW}Location                      {NORMAL}:", loc)
            sleep(0.1)
            print(f"{YELLOW}Region Code For Number        {NORMAL}:", pnumb.region_code_for_number(parsing))
            sleep(0.1)
            print(f"{YELLOW}Number Type                   {NORMAL}:", pnumb.number_type(parsing))
            sleep(0.1)
            print(f"{YELLOW}Is Carrier Specific           {NORMAL}:", pnumb.is_carrier_specific(parsing))
            sleep(0.1)
            print(f"{YELLOW}ISP                           {NORMAL}:", isp)
            sleep(0.1)
            print(f"{YELLOW}Time Zone                     {NORMAL}:", tz)
            sleep(0.1)
            print('\n\033[1;93mWhatsApp Number               \033[0m: wa.me/' + number + ' \n')
            sleep(0.1)
            print(f"{YELLOW}Is Number Geographical        {NORMAL}:", pnumb.is_number_geographical(parsing))
            print("")
            sleep(1)
            open = input(f"{WHITE}TYPE 1 To Open Chat Target on WhatsApp or press ENTER to next: ")
            if open == "1":
                sleep(1)
                print(f"{WHITE}Openned WhatsApp")
                sleep(1)
                sleep(1)
                print(f"{NORMAL}Done")
                sleep(0.50)
                os.system('\nxdg-open http://wa.me/' + number + ' \n')
                sleep(0.30)
                print("")
            elif open == "":
                print("")
                sys.exit(1)

    elif chose == "2":  ## MENU 2
        try:
            def IP_Track():
                sleep(1)
                ip = input(f"{WHITE}\n Enter IP target :{CRED2}➤ ")  # INPUT IP ADDRESS
                print()
                print(f' {NORMAL}============= {YELLOW}SHOW INFORMATION IP ADDRESS {NORMAL}=============')
                req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
                ip_data = json.loads(req_api.text)
                time.sleep(2)
                print(f"{NORMAL}\n IP target       :{YELLOW}", ip)
                sleep(0.1)
                print(f"{NORMAL} Type IP         :{YELLOW}", ip_data["type"])
                sleep(0.1)
                print(f"{NORMAL} Country         :{YELLOW}", ip_data["country"])
                sleep(0.1)
                print(f"{NORMAL} Country Code    :{YELLOW}", ip_data["country_code"])
                sleep(0.1)
                print(f"{NORMAL} City            :{YELLOW}", ip_data["city"])
                sleep(0.1)
                print(f"{NORMAL} Continent       :{YELLOW}", ip_data["continent"])
                sleep(0.1)
                print(f"{NORMAL} Continent Code  :{YELLOW}", ip_data["continent_code"])
                sleep(0.1)
                print(f"{NORMAL} Region          :{YELLOW}", ip_data["region"])
                sleep(0.1)
                print(f"{NORMAL} Region Code     :{YELLOW}", ip_data["region_code"])
                sleep(0.1)
                print(f"{NORMAL} Latitude        :{YELLOW}", ip_data["latitude"])
                sleep(0.1)
                print(f"{NORMAL} Longitude       :{YELLOW}", ip_data["longitude"])
                sleep(0.1)
                lat = int(ip_data['latitude'])
                lon = int(ip_data['longitude'])
                sleep(0.1)
                print(f"{NORMAL} Maps            :{YELLOW}", f"https://www.google.com/maps/@{lat},{lon},8z")
                sleep(0.1)
                print(f"{NORMAL} EU              :{YELLOW}", ip_data["is_eu"])
                sleep(0.1)
                print(f"{NORMAL} Postal          :{YELLOW}", ip_data["postal"])
                sleep(0.1)
                print(f"{NORMAL} Calling Code    :{YELLOW}", ip_data["calling_code"])
                sleep(0.1)
                print(f"{NORMAL} Capital         :{YELLOW}", ip_data["capital"])
                sleep(0.1)
                print(f"{NORMAL} Borders         :{YELLOW}", ip_data["borders"])
                sleep(0.1)
                print(f"{NORMAL} Country Flag    :{YELLOW}", ip_data["flag"]["emoji"])
                sleep(0.1)
                print(f"{NORMAL} ASN             :{YELLOW}", ip_data["connection"]["asn"])
                sleep(0.1)
                print(f"{NORMAL} ORG             :{YELLOW}", ip_data["connection"]["org"])
                sleep(0.1)
                print(f"{NORMAL} ISP             :{YELLOW}", ip_data["connection"]["isp"])
                sleep(0.1)
                print(f"{NORMAL} Domain          :{YELLOW}", ip_data["connection"]["domain"])
                sleep(0.1)
                print(f"{NORMAL} ID              :{YELLOW}", ip_data["timezone"]["id"])
                sleep(0.1)
                print(f"{NORMAL} ABBR            :{YELLOW}", ip_data["timezone"]["abbr"])
                sleep(0.1)
                print(f"{NORMAL} DST             :{YELLOW}", ip_data["timezone"]["is_dst"])
                sleep(0.1)
                print(f"{NORMAL} Offset          :{YELLOW}", ip_data["timezone"]["offset"])
                sleep(0.1)
                print(f"{NORMAL} UTC             :{YELLOW}", ip_data["timezone"]["utc"])
                sleep(0.1)
                print(f"{NORMAL} Current Time    :{YELLOW}", ip_data["timezone"]["current_time"])
                print()
                sleep(0.1)

            if __name__ == '__main__':
                IP_Track()
        except KeyboardInterrupt:
            print(f" {NORMAL}[{YE}!{NORMAL}] {YE}PROGRAM STOPPED...")

    elif chose == "3":
        def instagram():
            import instaloader, sys
            from instaloader import instaloader
            # 2 MODULE

            x = instaloader.Instaloader()

            try:
                print()
                sleep(1)
                uname = input(f"\033[36mEnter a username \033[0m:{CRED2}➤ \033[36m")  # INPUT USER
                if uname == "":
                    print("\033[33mUnknown command!")
                    sys.exit()

                f = instaloader.Profile.from_username(x.context, uname)

                print("\033[32mUsername\033[0m :", f.username)
                print("\033[32mID\033[0m :", f.userid)
                print("\033[32mNama lengkap\033[0m :", f.full_name)
                print("\033[32mBiografi\033[0m :", f.biography)
                print("\033[32mNama kategori bisnis\033[0m :", f.business_category_name)
                print("\033[32mURL eksternal\033[0m :", f.external_url)
                print("\033[32mDiikuti orang\033[0m :", f.followed_by_viewer)
                print("\033[32mMengikuti\033[0m :", f.followees)
                print("\033[32mPengikut\033[0m :", f.followers)
                print("\033[32mMengikuti orang\033[0m :", f.follows_viewer)
                print("\033[32mDiblokir orang\033[0m :", f.is_blocked)
                print("\033[32mHanya untuk pengguna terverifikasi\033[0m :", f.is_verified)
                print("\033[32mBisnis akun\033[0m :", f.is_business_account)
                print("\033[32mTertutup\033[0m :", f.is_private)
                print("\033[32mTipe akun\033[0m :", f.is_type_private)
                print("\033[32mIGTV\033[0m :", f.igtv_count)
                print("\033[32mJumlah pos\033[0m :", f.mediacount)
                print("\033[32mTotal pemberian tanda suka\033[0m :", f.total_igtv_series)
                print("\033[32mDitautkan FB\033[0m :", f.connected_fb_page)
                print("\033[32mJumlah unduhan\033[0m :", f.mutual_followers)
                print("\033[32mNama pengguna lain\033[0m :", f.other_usernames)
                print("\033[32mPronouns\033[0m :", f.pronouns)
                print("\033[32mTagline\033[0m :", f.tagline)
                print("\033[32mIklan politik atau berpihak\033[0m :", f.has_anonymous_profile_picture)
                print("\033[32mDilaporkan\033[0m :", f.is_business)
                print("\033[32mMengikuti \033[0m:", f.has_chaining)
                print("\033[32mTelepon\033[0m :", f.has_highlight_reels)
                print("\033[32mRekaman\033[0m :", f.has_public_story)
                print("\033[32mArchive\033[0m :", f.has_saved_media)
                print("\033[32mPengguna\nmenandai saya\033[0m :", f.has_viewer_archived_media)
                print("\033[32mMengikuti tautan\033[0m :", f.external_url_linkshimmed)
                print("\033[32mBIPOC\033[0m :", f.is_eligible_for_school)
                print("\033[32mEmail\033[0m :", f.is_favorite)
                print("\033[32mURL eksternal\033[0m :", f.is_interest_account)
                print("\033[32mMenghubungkan ke produk\033[0m :", f.is_meme_page)
                print("\033[32mBukti status\nkepegawaian\033[0m :", f.is_using_app)
                print("\033[32mKonon\033[0m :", f.can_link_entities_in_bio)
                print("\033[32mIGTV  \nCTA=    \033[0m :", f.can_see_organic_insights)
                print("\033[32mNama alternatif\033[0m :", f.can_follow_hashtags)
                print("\033[32mAktor atau\naktris\033[0m :", f.is_potentially_business)
                print("\033[32mProgram TV atau\nkesayangan\norang lain\033[0m :", f.is_private)
                print("\033[32mHasil tanaman\033[0m :", f.blocked_by_viewer)
                print("\033[32mIGTV  \nCTA  \nlink\033[0m :", f.is_viewer)
                print("\033[32mMeningkatkan tampilan\033[0m :", f.has_blocked_viewer)
                print("\033[32mSaran\033[0m :", f.has_requested_viewer)
                print("\033[32mTersedia untuk\ndiketahui pihak\nketiga\033[0m :", f.requested_by_viewer)
                print("\033[32mDiketahui pihak\nketiga\033[0m :", f.restricted_by_viewer)
                print("\033[32mTautan biografi\033[0m :", f.follows_count)
                print("\033[32mLink biografi\033[0m :", f.following_tagged_count)
                print("\033[32mDilaporkan\033[0m :", f.edge_owner_to_timeline_media)
                print("\033[32mTerbuka peta\033[0m :", f.highlight_reel_count)
                print("\033[32mTautan biografi\033[0m :", f.edge_felix_video_timeline)
                print("\033[32mPeta terbuka\033[0m :", f.edge_saved_media)
                print("\033[32mIklan yang\nditautkan\033[0m :", f.edge_media_collections)
                print("\033[32mHasil tanaman\033[0m :", f.edge_related_profiles)
                print("\033[32mTersedia untuk\ndiketahui pihak\nketiga\033[0m :", f.edge_mutual_followed_by)
                print("\033[32mRequest\033[0m :", f.edge_user_to_photos_of_you)
                print("\033[32mTerbuka untuk\ndiketahui pihak\nketiga\033[0m :", f.edge_blocked_by_viewer)
                print("\033[32mDiketahui pihak\nketiga\033[0m :", f.edge_restrictions)
                print("\033[32mTersedia untuk\ndiketahui pihak\nketiga\033[0m :", f.edge_user_to_mutual_followed_by)
                print("\033[32mDalam proses\033[0m :", f.edge_highlighted_profile)
                print("\033[32mAlamat email\033[0m :", f.edge_latest_reel_media)
                print("\033[32mDalam proses\033[0m :", f.edge_felix_video_timeline)
                print("\033[32mDalam proses\033[0m :", f.edge_saved_media)
                print("\033[32mDalam proses\033[0m :", f.edge_media_collections)
                print("\033[32mDalam proses\033[0m :", f.edge_related_profiles)
                print("\033[32mDalam proses\033[0m :", f.edge_mutual_followed_by)
                print("\033[32mDalam proses\033[0m :", f.edge_user_to_photos_of_you)
                print("\033[32mDalam proses\033[0m :", f.edge_blocked_by_viewer)
                print("\033[32mDalam proses\033[0m :", f.edge_restrictions)
                print("\033[32mDalam proses\033[0m :", f.edge_user_to_mutual_followed_by)
                print("\033[32mDalam proses\033[0m :", f.edge_highlighted_profile)
                print("\033[32mDalam proses\033[0m :", f.edge_latest_reel_media)
                print("\033[32mDalam proses\033[0m :", f.edge_felix_video_timeline)
                print("\033[32mDalam proses\033[0m :", f.edge_saved_media)
                print("\033[32mDalam proses\033[0m :", f.edge_media_collections)
                print("\033[32mDalam proses\033[0m :", f.edge_related_profiles)
                print("\033[32mDalam proses\033[0m :", f.edge_mutual_followed_by)
                print("\033[32mDalam proses\033[0m :", f.edge_user_to_photos_of_you)
                print("\033[32mDalam proses\033[0m :", f.edge_blocked_by_viewer)
                print("\033[32mDalam proses\033[0m :", f.edge_restrictions)
                print("\033[32mDalam proses\033[0m :", f.edge_user_to_mutual_followed_by)
                print("\033[32mDalam proses\033[0m :", f.edge_highlighted_profile)
                print("\033[32mDalam proses\033[0m :", f.edge_latest_reel_media)
                print()
                print(f"\033[32mUser ID\033[0m        : {f.userid}")
                print(f"\033[32mFollowers\033[0m      : {f.followers}")
                print(f"\033[32mFollowing\033[0m      : {f.followees}")
                print(f"\033[32mBio\033[0m            : {f.biography}")
                print(f"\033[32mExternal URL\033[0m   : {f.external_url}")
                print(f"\033[32mBusiness Category\033[0m: {f.business_category_name}")
                print(f"\033[32mIs Business Account\033[0m: {f.is_business_account}")
                print(f"\033[32mIs Private\033[0m      : {f.is_private}")
                print(f"\033[32mIs Verified\033[0m     : {f.is_verified}")
                print(f"\033[32mIs Blocked\033[0m      : {f.blocked_by_viewer}")
                print(f"\033[32mHas Highlight Reels\033[0m: {f.has_highlight_reels}")
                print(f"\033[32mProfile Pic URL\033[0m : {f.profile_pic_url}")
                print()
                sleep(1)
                print()
                sleep(0.1)

            except Exception as e:
                print("\033[31m", str(e))
                pass

        if __name__ == '__main__':
            instagram()

    elif chose == "A" or chose == "a":
        sleep(1)
        print("\n")
        print(f"\033[36mCoded by Mr,OwlBird05\033[0m")
        sleep(1)
        print(f"\033[36mGitHub : \033[0mhttps://github.com/404rgr")
        print()
        sleep(1)
        print("\033[31mThanks to everyone who supported me\033[0m")
        print()
        sleep(1)
        print(f"\033[31mWith LOVE! \033[0m<3")
        print()
        sleep(1)
        print(f"\033[31mDont forget to visit my repository on GitHub!!\033[0m")
        print("\n")
        sleep(1)
    else:
        print("\033[33mUnknown command!")

if __name__ == "__main__":
    try :
        start()
    except UnicodeDecodeError :
        print("eror charmap")
