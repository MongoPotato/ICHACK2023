import streamlit as st

#create a streamlit app for the blockchain
#first the user will be able to make transactions
#for that, create an interface where he enters public key, amount, receiver 
#lets do this:

st.title("Blockchain Interface")

#create a button "I wish to make a transaction"
#when the user clicks on it, he will a new interface appears where he can enter the transaction details

left_column, right_column = st.columns(2)
left_column.write("I wish to make a transaction")

sender_address = st.text_input('Enter your address:')
st.write('Your address is:', sender_address)

receiver_address = st.text_input("Enter the receiver's address")
st.write("The receiver's address is:", receiver_address)

amout = st.number_input('Insert the amount of the transaction')
st.write('Amount: ', amout)


