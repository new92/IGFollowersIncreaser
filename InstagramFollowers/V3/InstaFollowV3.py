"""
Author: new92
Github: @new92

InstaFollowV3: Script for increasing the followers of an Instagram account



*********IMPORTANT*********
User's data (such as: username, password) will not be stored or saved ! 
Will be used only to increase the followers of the user's Instagram account
***************************
"""
try:
    import sys
    import platform
    from os import system
    from time import sleep
    import os
    import instagrapi
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")
banner="""

"""
print(banner)
print("\n")
print("[+] Program for increasing followers on Instagram")
print("\n")
print("[+] Author: new92")
print("[+] Github: @new92")
print("\n")
print("[1] Increase Followers")
print("[2] Exit")
print("\n")
num=int(input("[::] Please enter a number (from the above ones): "))
while num < 0 or num > 2 or num == None:
    print("[!] Invalid number !")
    sleep(1)
    num=int(input("[::] Please enter again the number: "))
if num == 1:
    NAMES = ['Cristiano Ronaldo','Cardi B','Kim Kardashian','Ariana Grande','Nicki Minaj','Beyonce','Katy Perry','Selena Gomez','Justin Bieber','Lionel Messi','Neymar Jr','Kylian Mbappe','Dua Lipa','Billie Eilish','Kylie Jenner','Khloe Kardashian','Kourtney Kardashian','Jennifer Lopez','Shakira','NBA','Instagram','National Geographic','FC Barcelona','Real Madrid','Champions League','Chris Brown','Taylor Swift','Kendall Jenner','Virat Kohli','Zendaya','Marvel','Tom Holland','Emma Watson','Millie Bobby Brown','Shawn Mendes','NASA','Nike']
    users = {
        'Cristiano Ronaldo' : '173560420',
        'Cardi B' : '1436859892',
        'Kim Kardashian': '18428658',
        'Ariana Grande' : '7719696',
        'Nicki Minaj' : '451573056',
        'Beyonce' : '247944034',
        'Katy Perry' : '407964088',
        'Selena Gomez' : '460563723',
        'Justin Bieber' : '6860189',
        'Lionel Messi' : '427553890',
        'Neymar Jr' : '26669533',
        'Kylian Mbappe' : '4213518589',
        'Dua Lipa' : '12331195',
        'Billie Eilish' : '28527810',
        'Kylie Jenner' : '12281817',
        'Khloe Kardashian' : '208560325',
        'Kourtney Kardashian' : '145821237',
        'Jennifer Lopez' : '305701719',
        'Shakira' : '217867189',
        'NBA' : '20824486',
        'Instagram' : '25025320',
        'National Geographic' : '787132',
        'FC Barcelona' : '260375673',
        'Real Madrid' : '290023231',
        'Champions League' : '1269788896',
        'Chris Brown' : '29394004',
        'Taylor Swift' : '11830955',
        'Kendall Jenner' : '6380930',
        'Virat Kohli' : '2094200507',
        'Zendaya' : '9777455',
        'Marvel' : '204633036',
        'Tom Holland' : '176618189',
        'Emma Watson' : '1418652011',
        'Millie Bobby Brown' : '3439002676',
        'Shawn Mendes' : '212742998',
        'Camila Cabello' : '19596899',
        'NASA' : '528817151',
        'Nike' : '13460080'
    }
    sleep(1)
    print("[+] The login credentials will not be stored or saved")
    sleep(2)
    print("-"*20+"login".upper()+"-"*20)
    username=str(input("[::] Please enter your username: "))
    while username == None or len(username) > 30:
        print("[!] Invalid username !")
        sleep(1)
        username=str(input("[::] Please enter again your username: "))
    username=username.lower()
    username=username.strip()
    sleep(1)
    password=input("[::] Please enter your password: ")
    while password == None:
        print("[!] Invalid password !")
        sleep(1)
        password=input("[::] Please enter again your password: ")
    password=password.strip()
    sleep(1)
    clnt=instagrapi.Client()
    try:
        login = clnt.login(username,password)
        if login:
            print("[!] Login successful !")
            sleep(1)
            print("[+] Please wait while the program is increasing your followers...")
            sleep(2)
        else:
            print("[!] Login unsuccessful !")
            sleep(1)
            print("[+] Please check the username and/or the password !")
            sleep(2)
            print("[+] Exiting...")
            quit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        quit(0)
    sleep(2)
    print("[+] To end the process enter Ctrl + C")
    sleep(2)
    f = 0
    x = 0
    for i in range(30):
        for i in range(len(NAMES)-1):
            clnt.user_follow(users[NAMES[i]])
            print(f"[+] Following {NAMES[i]}...")
            sleep(3)
            f += 1
            print(f"[+] Next user to follow: {NAMES[i+1]}...")
            sleep(3)
        for i in range(len(NAMES)-1):
            clnt.user_unfollow(users[NAMES[i]])
            print(f"[+] Unfollowing {NAMES[i]}...")
            sleep(3)
            x += 1
            print(f"[+] Next user to unfollow: {NAMES[i+1]}...")
            sleep(3)
    res = f - x
    if res != 0:
        print(f"[!] Failed to unfollow {res} users !")
        sleep(1)
        print('-'*15+"USERS"+'-'*15)
        print("\n")
        for i in range(res,-1,-1):
            print("[+] User: "+str(NAMES[i]))
    