import random
import string
from os import system
import requests
import time
from colorama import Fore
system("title " + "github.com/screamz2k")
webhook = input(Fore.BLUE + ">>Please enter the Webhook: ")
try:
    amount = int(input(">>How many codes do you want to generate: "))
except ValueError:
    print("Need to input a number!")
    amount = int(input(">>How many codes do you want to generate: "))

codes = ""
for i in range(amount):  # Loop the amount of codes to generate
    code = "".join(random.choices(
        string.ascii_uppercase + string.digits + string.ascii_lowercase,
        k=16))
    start = "https://discord.gift/{code}\n"
    codes += start


def send():
    res = requests.post(webhook, data=data)
    try:
        print(Fore.RED + 'getting ratelimited, waiting ' + str(res.json()["retry_after"]) + 'ms.')
        time.sleep(res.json()["retry_after"] / 1000)
        res = 'waited ' + Fore.RED + str(res.json()["retry_after"]) + 'ms.'
    except:
        pass
    print(Fore.CYAN + "Successfully sent code!")
    return


for i in range(amount):
    code_gen = (random.choices(
        string.ascii_uppercase + string.digits + string.ascii_lowercase,
        k=16))
    code = ""
    for char in code_gen:
        code += char
    start = "https://discord.gift/" + code + "\n"

    data = {
        "content": start
    }
    send()
