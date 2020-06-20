import requests
import random
import json
import os
from threading import Thread
from colorama import Fore, init
init()

sayac = 0
aktif_sunucu = 0
sorunsuz_proxy = 0
bozuk_proxy = 0
toplam_proxy = 0





def islem(kod, proxy):
    global toplam_proxy
    global bozuk_proxy
    global sorunsuz_proxy
    global aktif_sunucu
    global sayac
    try:
        s = requests.session()
        s.proxies = proxies()
        r = s.get(f"https://discordapp.com/api/v6/invite/{kod}", timeout=3)
        #print(r.text)
        try:
            #deneme = re.search('"name":(.*)', r.text).group(1)
            veri = r.json()
            sunucu_ad = veri['guild']['name']
            sunucu_davet_linki = "https://discord.gg/" + kod
            sunucu_id = veri['guild']['id']
            sunucu_resmi = "https://cdn.discordapp.com/icons/" + sunucu_id +  "/" + veri['guild']['icon'] + ".png"
            sunucu_dogrulama = veri['guild']['verification_level']
            davet_eden_kullanici = veri['inviter']['username'] + veri['inviter']['discriminator']
            davet_eden_fotograf = "https://cdn.discordapp.com/avatars/" + veri['inviter']['id'] + "/" + veri['inviter']['avatar'] + ".png?size=2048"


            print(Fore.YELLOW + " [ " + Fore.MAGENTA + "?" + Fore.YELLOW + " ] " + Fore.GREEN + f'    {kod} ' + Fore.RESET + '  :  ' + Fore.CYAN + veri['guild']['name'])
            file = open('results/valid.txt', 'a')
            write_code = f"\n ################################### \n\n\n Sunucu Adý: {sunucu_ad} \n Sunucu Davet Linki: {sunucu_davet_linki} \n Sunucu ID: {sunucu_id} \n Sunucu Resmi: {sunucu_resmi} \n Sunucu Doðrulama Seviyesi: {sunucu_dogrulama} \n Davet Eden Kullanýcý: {davet_eden_kullanici} \n Davet Eden Kullanýcýnýn Profil Fotoðrafý: {davet_eden_fotograf}\n\n\n"
            file.write(write_code)
            file.close()
            aktif_sunucu += 1
        except:
            print(Fore.YELLOW + " [ " + Fore.RED + "?" + Fore.YELLOW + " ] " + Fore.RED + f'    {kod}' + Fore.RESET)
            file = open('results/invalid.txt', 'a')
            write_code = kod + "\n"
            file.write(write_code)
            file.close()
            pass
        sorunsuz_proxy += 1
    except:
        bozuk_proxy += 1
        pass
    toplam_proxy += 1
    sayac += 1






while True:
    os.system(f"title Bulunan Sunucu: {aktif_sunucu} Tüm Denemeler: {sayac} Toplam Denenen Proxyler: {toplam_proxy} Sorunsuz Çalýþan Proxyler {sorunsuz_proxy} Bozuk Proxyler {bozuk_proxy}")
    harfler = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rakamlar = '0123456789'
    liste = harfler + rakamlar
    kod = ''
    for i in range(6):
        kod += random.choice(liste)

    proxy_file = open('proxy.txt', "r")
    proxy_text = proxy_file.readlines()


    def proxies():
        line = random.choice(proxy_text)
        ip = line.replace('\n', '')
        if str(ip).startswith('http'):
            pass
        else:
            https = "https://"+ip
            http = "http://"+ip
        proxy = {
            "https":https,
            "http":http
            }
        return proxy
    

    x = Thread(target=islem, args=(kod, proxies(),))
    x.start()