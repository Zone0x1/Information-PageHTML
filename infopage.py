#!/usr/bin/python3
"""
--! This Script For Get Information Page HTML
--! My Info
--! Name is : Mahmoud Saber
--! My Age is : 19
--! WHatsApp is : 01117374028

"""
# import module

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import time
import os
import sys

# info Coder
os.system("figlet Info-PageHTML")
time.sleep(2)
print("[*] Cdedd By : Mahmoud S.ALi")
print("[*] Facebook : https://www.facebook.com/mody.saber.96343405")
print("[*] WhatsApp : 01117374028")
time.sleep(2)
os.system("clear")
os.system("figlet Start-GET")
#####################
# def restary


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


curdir = os.getcwd()

# Type From User
try:
    # input("Enter your website Target >> : "))
    url = str(input("Enter your Site For GET info >> : "))
    while url == '':
        print("Please Type your Site !! ")
        url = str(input("Enter your Site For GET info >> : "))

    if_wante = input("""

    1. Type 1 For GET title
    2. Type 2 For GET title text
    3. Type 3 For GET link
    4. Type 4 For GET href on link
    5. Type 5 For GET All Page Code HTML
    6. Type 6 For GET Command in Page

    Type your number >> : """)

    while if_wante == '':
        print("Error .... PLease Enter a NUmber !!")
        if_wante = input("""

        1. Type 1 For GET title
        2. Type 2 For GET title text
        3. Type 3 For GET link
        4. Type 4 For GET href on link
        5. Type 5 For GET All Page Code HTML
        6. Type 6 For GET Command in Page

        Type your number >> :  """)

    # sp = url.split("https://", "")
    operurl = urllib.request.urlopen(url)
    content_url = operurl.read(2000000)
    soup = BeautifulSoup(content_url, 'html.parser')
    # print(soup.prettify())
    time.sleep(2)
    if if_wante == 1:
        print(soup.html.head.title)
    elif if_wante == 2:
        print(soup.html.head.title.text)
    elif if_wante == 3:
        for i in soup.find_all('link'):
            print(i)
    elif if_wante == 4:
        for i in soup.find_all('link'):
            print(i.get("href"))
    elif if_wante == 5:
        print(soup.prettify())
    elif if_wante == 6:
        print(soup.get_text())

    else:
        pass

except TypeError:
    print("[+] string argument without an encoding ")
    print("[+] Try Agian [+]")

print("==================================================")
print(" The connections you requested had finished ")
if __name__ == "__main__":
    answer = input(" Do you want to info more? : Yes Or No > : ")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system("figlet Good Bye")
