import streamlit as st
from Transactions import Transaction

#create a streamlit app for the blockchain
#first the user will be able to make transactions
#for that, create an interface where he enters public key, amount, receiver 
#lets do this:

st.title("Blockchain Interface")

#create a button "I wish to make a transaction"
#when the user clicks on it, he will a new interface appears where he can enter the transaction details

left_column, right_column = st.columns(2)
left_column.write("I wish to make a transaction")

sender_pk = st.text_input('Enter your public key:')
st.write('Your address is:', sender_pk)

receiver_pk = st.text_input("Enter the receiver's public key")
st.write("The receiver's address is:", receiver_pk)

amount = st.number_input('Insert the amount of the transaction')
st.write('Amount: ', amount)

transaction  =Transaction(sender_pk, receiver_pk, amount)
