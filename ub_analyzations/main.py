import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["username"])
st.write("DB password:", st.secrets["password"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)

# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from master_recomm;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")


tbl=pd.DataFrame({"colmn 1":[1,2,3,4,5], "colmn2":[6,7,8,9,0]})
st.title('Hi i am streamlit web app!!!!!!')
st.subheader('I am subheader')
st.header('I am header')
st.text('I am text function')
st.write(" ## this is markdown header ")
st.write(" ### below is an example of dataframe ")
st.table(tbl)
st.dataframe(tbl)

## example for matpotlib

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

### example from https://towardsdatascience.com/streamlit-from-scratch-presenting-data-d5b0c77f9622
## another example of graphs
# Crypto monthly data
d = {'Month':[1,2,3,4,5,6,7,8,9,10,11],
     'Bitcoin':[47733,38777,44404,46296,38471,29788,19247,23273,20146,19315,20481],
     'Ethereum':[3767,2796,2973,3448,2824,1816,1057,1630,1587,1311,1579]}

cryptodf = pd.DataFrame(data = d)

# The Incredible Widget Company
d = {'Quarter':[1,2,3,4],
     'Widgets':[100,110,112,120],
     'Wodgets':[50,100,120, 125],
     'Wudgets':[200,150,100,90]}
     
salesdf = pd.DataFrame(d)

#st.bar_chart(df, y = 'Bitcoin', x='Month')

btcCurrent = 16080
btcYrBeg = 47733
btcdelta = btcCurrent - btcYrBeg

st.metric("Bitcoin", btcCurrent, delta=btcdelta, delta_color="normal", 
          help="Change in Bitcoin dollar value since the year beginning")

#####
ethCurrent = 1225
ethYrBeg = 3767
ethdelta = ethCurrent - ethYrBeg

# Use columns to display them together
col1, col2, col3 = st.columns([50,25,25])
col1.write("The value of crytocurrencies has dropped considerably since the beginning of the year")
col2.metric("Bitcoin", btcCurrent, delta=btcdelta, delta_color="normal", 
            help="Change in Bitcoin dollar value since the year beginning")
col3.metric("Ethereum", ethCurrent, delta=ethdelta, delta_color="normal", 
            help="Change in Ethereum dollar value since the year beginning")

#######


st.table(cryptodf)

st.dataframe(cryptodf, use_container_width=True)

st.line_chart(cryptodf, x='Month')

st.bar_chart(cryptodf, y = 'Bitcoin', x='Month')

st.bar_chart(salesdf, x='Quarter')

st.area_chart(salesdf, x='Quarter')

fig, ax = plt.subplots()
plt.plot(cryptodf['Bitcoin'])
st.pyplot(fig)

# Pyplot charts are customizable
fig, ax = plt.subplots()
plt.bar(cryptodf.Month, cryptodf.Bitcoin)
ax.set_ylabel("Value in dollars")
ax.set_xlabel("Month 2022")
ax.set_title("Bitcoin")
plt.grid(axis='y')
st.pyplot(fig)

fig, ax = plt.subplots()
cryptodf.plot.bar(x = 'Month', y=['Bitcoin','Ethereum'],ax=ax)
st.pyplot(fig)
