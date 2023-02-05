from terra_modules import request_session_google
import os

chaine = "alnaejf"
chaine = "".join([x for x in chaine if x != 'a'])
print(chaine)


def remove_newlines(chain):
    return "".join(chain.splitlines())




print("This program is used to configure your proof-of-workout node and earn money !")
public_key = input("Put your public key from your crypto-wallet : ")
print("authentifiez-vous à l'adresse suivante : {}".format(request_session_google(public_key)))
print("congratulations, you are now a pow miner !")
print("Please run MainNode.py to mine")


