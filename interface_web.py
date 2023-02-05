import streamlit as st
from Transactions import Transaction
from datetime import date
from Wallet import Wallet
from cryptography.hazmat.primitives.asymmetric import rsa

#create a streamlit app for the blockchain
#first the user will be able to make transactions
#for that, create an interface where he enters public key, amount, receiver 
#lets do this:

st.title("Blockchain Interface")

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
    transaction = Transaction(sender_pk, receiver_pk, amount, date.today())
    st.write("Cheers, transaction validated!")


new_title = '<p style="font-family:sans-serif; color:deeppink; font-size: 30px;">I wish to create a wallet and mine</p>'
st.markdown(new_title, unsafe_allow_html=True)

private_key = private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

if st.button("Let's go for it!"):
    public_key = private_key.public_key()
    wallet = Wallet(public_key, private_key)

    st.write("Congratulations, your wallet has been created!")
    st.write("Your public key is the couple :")
    st.write("e=", public_key.public_numbers().e)
    st.write("n= ... too long to be displayed",)
    st.write("Your private key has been successfully generated too!")

