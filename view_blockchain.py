from datetime import date
import streamlit as st
from Block import Block
from Transactions import Transaction

st.title("Blockchain Interface")

trans0 = Transaction("sender", "receiver", 10, date.today())
trans1 = Transaction("sender1", "receiver1", 20, date.today())
block0 = Block(0, [trans0, trans1], "miner")
block1 = Block(1, [trans0, trans1], "miner1")
blocks = [block0, block1] #list of blocks



#creates st.buttons one above each other
for i in range(len(blocks)):

    if st.button("Block " + str(i + 1)):
        st.write("Miner Address: " + str(blocks[i].miner_address))

        all_transactions = blocks[i].transactions
        
        for j in range(len(all_transactions)):
            nb_transaction = "Transaction " + str(j + 1)
            new_title = f'<p style="font-family:sans-serif; color:deeppink; font-size: 20px;">{nb_transaction}</p>'
            st.markdown(new_title, unsafe_allow_html=True)

            st.write("Sender: " + str(all_transactions[j].sender))
            st.write("Receiver: " + str(all_transactions[j].receiver))
            st.write("Amount: " + str(all_transactions[j].amount))
            st.write("Date: " + str(all_transactions[j].date))


# #define the color as red
# color = "#F63366"



