import streamlit as st
from Transactions import Transaction
from datetime import datetime, timezone 
from Wallet import Wallet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from Node import SportNode
import time
from Signing import Signing
from hashlib import sha256


filename = "private.txt"
filenamepub = "public.pub"
ipnode = ""
iphost = ""

#create a streamlit app for the blockchain
#first the user will be able to make transactions
#for that, create an interface where he enters public key, amount, receiver 
#lets do this:

st.title("SportBlockchain Interface")

new_title = '<p style="font-family:sans-serif; color:deeppink; font-size: 30px;">I wish to create a wallet and mine</p>'
st.markdown(new_title, unsafe_allow_html=True)

private_key = private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
with open(filename, 'wb') as pem_out:
    pem_out.write(pem)


def gohash(data):
    return sha256(data).hexdigest()

if st.button("Let's go for it!"):
    public_key = private_key.public_key()
    pemb = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(filenamepub, 'wb') as pub:
        pub.write(pemb)
    wallet = Wallet(public_key, private_key)

    st.write("Congratulations, your wallet has been created!")
    st.write("Your public key is the couple :")
    st.write("e=", public_key.public_numbers().e)
    st.write("Your private key has been successfully generated too!")


#create a button "I wish to make a transaction"
#when the user clicks on it, he will a new interface appears where he can enter the transaction details
#write in red "hello"

new_title = '<p style="font-family:sans-serif; color:deeppink; font-size: 30px;">I wish to make a transaction</p>'
st.markdown(new_title, unsafe_allow_html=True)

sender_pk = st.text_input('Enter your public key:')
st.write('Your address is:', sender_pk)

receiver_pk = st.text_input("Enter the receiver's public key")
st.write("The receiver's address is:", receiver_pk)

amount = st.number_input('Insert the amount of the transaction')
st.write('Amount: ', amount)

if st.button("Validate the transaction !"):
    transaction = Transaction(sender_pk, receiver_pk, amount, datetime.now(timezone.etc))
    st.write("Cheers, transaction validated!")


node = SportNode(ipnode, 10002)
node.start()
node.connect_with_node(iphost, 10001)
time.sleep(2)

signature = Signing.sign(transaction)

message = {}
message['_transaction'] = "transaction"
message['_sender'] = transaction.getSender()
message['_receiver'] = transaction.getReceiver()
message['_amount'] = transaction.getAmount()
message['_date'] = transaction.getDate()
message['_signature'] = signature
message['_hash'] = gohash(message)

node.send_message(message)
node.stop()