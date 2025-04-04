from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

# Define colors for console output
n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # Fancy logo
    b = [
    '░██████╗███████╗████████╗██╗░░░██╗██████╗░',
    '██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗',
    '╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝',
    '░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░',
    '██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░',
    '╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░'
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    print('Contact below address for get premium script')
    print(f'{lg}Version: {w}2.6.82{lg} | GitHub: {w}@garud_owner{n}')
    print(f'{lg}Telegram: {w}@GARUD_OWNER{lg} | Instagram: {w}www.instagram.com/saifaliopp{n}')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add_new_accounts():
    new_accs = []
    with open('vars.txt', 'ab') as g:
        number_to_add = int(input(f'\n{lg} [~] Enter How Many Accounts You Want To Add: {r}'))
        for _ in range(number_to_add):
            phone_number = str(input(f'\n{lg} [~] Enter Phone Number With Country Code: {r}'))
            parsed_number = ''.join(phone_number.split())
            pickle.dump([parsed_number], g)
            new_accs.append(parsed_number)
        print(f'\n{lg} [i] Saved all accounts in vars.txt')
        clr()
        print(f'\n{lg} [*] Logging in from new accounts\n')
        for number in new_accs:
            c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            c.start(number)
            print(f'{lg}[+] Login successful')
            c.disconnect()
        input(f'\n Press enter to goto main menu...')

def filter_banned_accounts():
    accounts = []
    banned_accs = []
    with open('vars.txt', 'rb') as h:
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
    if not accounts:
        print(f'{r}[!] There are no accounts! Please add some and retry')
        sleep(3)
    else:
        for account in accounts:
            phone = str(account[0])
            client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            client.connect()
            if not client.is_user_authorized():
                try:
                    client.send_code_request(phone)
                    print(f'{lg}[+] {phone} is not banned{n}')
                except PhoneNumberBannedError:
                    print(r + phone + ' is banned!' + n)
                    banned_accs.append(account)
            client.disconnect()
        if not banned_accs:
            print(f'{lg}Congrats! No banned accounts')
        else:
            for m in banned_accs:
                accounts.remove(m)
            with open('vars.txt', 'wb') as k:
                for a in accounts:
                    Phone = a[0]
                    pickle.dump([Phone], k)
            print(f'{lg}[i] All banned accounts removed{n}')
        input('\nPress enter to goto main menu...')

def delete_specific_account():
    accs = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
    print(f'{lg}[i] Choose an account to delete\n')
    for i, acc in enumerate(accs):
        print(f'{lg}[{i}] {acc[0]}{n}')
    index = int(input(f'\n{lg}[+] Enter a choice: {n}'))
    phone = str(accs[index][0])
    session_file = f'{phone}.session'
    if os.name == 'nt':
        os.system(f'del sessions\\{session_file}')
    else:
        os.system(f'rm sessions/{session_file}')
    del accs[index]
    with open('vars.txt', 'wb') as f:
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Account Deleted{n}')
        input(f'\nPress enter to goto main menu...')

def update_script():
    print(f'\n{lg}[i] Checking for updates...')
    try:
        version = requests.get('https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/version.txt')
    except:
        print(f'{r} You are not connected to the internet')
        print(f'{r} Please connect to the internet and retry')
        exit()
    if float(version.text) > 2.0:
        prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
        if prompt in {'y', 'yes', 'Y'}:
            print(f'{lg}[i] Downloading updates...')
            if os.name == 'nt':
                os.system('del add.py')
                os.system('del manager.py')
            else:
                os.system('rm add.py')
                os.system('rm manager.py')
            os.system('curl -l -O https://raw.githubusercontent.com/FantasticSukhi/Member-Adder/main/add.py')
            os.system('curl -l -O https://raw.githubusercontent.com/FantasticSukhi/Member-Adder/main/manager.py')
            print(f'{lg}[*] Updated to version: {version.text}')
            input('Press enter to exit...')
            exit()
        else:
            print(f'{lg}[!] Update aborted.')
            input('Press enter to goto main menu...')
    else:
        print(f'{lg}[i] Your Telegram-Members-Adder is already up to date')
        input('Press enter to goto main menu...')

def display_all_accounts():
    accs = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
    print(f'\n{cy}')
    print(f'\tList Of Phone Numbers Are')
    print('==========================================================')
    for z in accs:
        print(f'\t{z[0]}')
    print('==========================================================')
    input('\nPress enter to goto main menu')

while True:
    clr()
    banner()
    print(f'{lg}[1] Add new accounts{n}')
    print(f'{lg}[2] Filter all banned accounts{n}')
    print(f'{lg}[3] Delete specific accounts{n}')
    print(f'{lg}[4] Update your Script{n}')
    print(f'{lg}[5] Display All Accounts{n}')
    print(f'{lg}[6] Quit{n}')
    a = int(input('\nEnter your choice: '))
    if a == 1:
        add_new_accounts()
    elif a == 2:
        filter_banned_accounts()
    elif a == 3:
        delete_specific_account()
    elif a == 4:
        update_script()
    elif a == 5:
        display_all_accounts()
    elif a == 6:
        clr()
        banner()
        exit()
