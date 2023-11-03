import requests
from Core import nickF
from Core import decor
import os
import sys
from Core import ts
from requests import get
from bs4 import BeautifulSoup
from colorama import Fore, init
from prettytable import PrettyTable
import urllib
import json
import urllib.request
import random
import time
import platform


def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        return 'cls'
    elif system == 'Linux' or system == 'Darwin':
        return 'clear'
    else:
        print(decor.chsystem)
        system = int(input(f"{decor.lye}[Gideon/chooseSystem] >> "))
        if system == 1:
            return 'cls'
        elif system == 2:
            return 'clear'
        else:
            raise Exception("Unknown OS")

clear_command = clear_terminal()
if clear_command:
    os.system(clear_command)


print(decor.banner)
while True:
    print(decor.menu)
    ans = int(input(f"{decor.lye}[Gideon/main] >> {decor.res}"))
    if ans == 1:
        os.system(clear_command)
        nick = input(f"{decor.lye}Enter Nickname >> ")
        print(f"{decor.lye} Messeagers and Soical Networks:")
        nickF.osint(nickF.snm, nick)
        print(f"{decor.lye} Videohostings:")
        nickF.osint(nickF.vh, nick)
        print(f"{decor.lye} Games:")
        nickF.osint(nickF.games, nick)
        print(f"{decor.lye} Forums:")
        nickF.osint(nickF.forums, nick)
        print(f"{decor.lye} Wallets:")
        nickF.osint(nickF.money, nick)
        print(f"{decor.lye} Other:")
        nickF.osint(nickF.other, nick)
        continue

    elif ans == 2:
        os.system(clear_command)
        ip = input(f"{decor.lye}Enter IP >> ")
        url = "https://ipinfo.io/" + ip + "/json"
        info = urllib.request.urlopen(url)
        ls = json.load(info)
        res  = rf'''{Fore.LIGHTGREEN_EX}
        City -> {ls['city']}
        Region -> {ls["region"]}
        Location -> {ls["loc"]}
        Operator -> {ls["org"]}
        '''
        print(res)
        page = get("https://iknowwhatyoudownload.com/en/peer/?ip=" + ip,
                headers=ts.headers)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.find(class_="table").find("tbody")
        torrents = table.find_all("tr")
        output = PrettyTable(["Name", "Category", "Size", "First seen", "Last seen"])
        for torrent in torrents:
            first, last = torrent.find_all(class_="date-column")
            first, last = first.text, last.text
            category = torrent.find(class_="category-column").text
            name = torrent.find(class_="name-column").text.replace("\n", '')
            size = torrent.find(class_="size-column").text
            output.add_row([name, category, size, first, last])

        print(f" {Fore.YELLOW}Found {len(torrents)} torrents... \n{Fore.LIGHTGREEN_EX}{output}{Fore.RESET}")
        continue

    elif ans == 3:
        os.system(clear_command)
        phone = input(f"{decor.lre}Enter Phone Number >> ")
        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
        try:
            infoPhones = urllib.request.urlopen(getInfo)
            infoPhone = json.load(infoPhones)
            print(decor.lye)
            print(u"Country >>", infoPhone["country"]["name"])
            print(u"Region >>", infoPhone["region"]["name"])
            print(u"Operator >>", infoPhone["0"]["oper"])
            print(u"City >>", infoPhone["0"]["name"])
            print(decor.res)
        except:
            print(f"{decor.red}[no result]")

    elif ans == 4:
        car_num = input(f"{decor.lye}Enter Car Number(а111аа77) >> ")
        car_nums = car_num.upper()
        nc = car_num.lower()
        numb_car = nc[:6] + '.' + nc[6:]
        try:
            a_h = requests.get("https://авто-история.рф/num/" + car_nums + "/")
            km = requests.get("https://www.230km.ru/" + numb_car + ".nomer")
            an = requests.get("http://avto-nomer.ru/ru/gallery.php?fastsearch=" + nc)
            if a_h:
                print("https://авто-история.рф/num/" + car_nums + "/")

                if km:
                    print("https://www.230km.ru/" + numb_car + ".nomer")
                else:
                    print(f"{decor.lre}[no result]")
            else:
                print(f"{decor.lre}[no result]")
            if len(nc) < 8:
                print(f"{decor.lre}[no result]")
            else:
                print("http://avto-nomer.ru/ru/gallery.php?fastsearch=" + nc)
        except:
            print(f"{decor.lre}[no result]")

    elif ans == 5:
        break
