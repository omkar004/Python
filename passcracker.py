#password cracker

import time
import itertools
import math
import threading
import pyfiglet

letters = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@!&")
tries = 0

def cracker(pw, length):
    global tries #doing tries global so we can use it everywhere
    print("Cracking.....")
    startTime = time.time()
    for letter in itertools.product(letters, repeat = length):
        guess = "".join(letter)
        tries += 1
        print(f"[+] {guess}", end = "\r")
        if guess == pw:
            endTime = time.time()
            print("\nPassword cracked.\nPassword Is: {}".format(guess))
            print("Time took to crack the password: {} seconds.".format(math.ceil(endTime - startTime)))
            print("Tries: {}".format(tries))
            print("Tries per second: {}".format(math.ceil(tries / (endTime - startTime))))
            exit()
        
def main():
    pyfiglet.print_figlet("Password  Cracker")
    password = input("Enter your password: ")
    if password != "":
        pwlength = len(password)
        cracker(password, pwlength)

bruteforce = threading.Thread(target=main)
bruteforce.start()
