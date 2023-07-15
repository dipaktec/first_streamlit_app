import streamlit


streamlit.title("Mel's streamlit diner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index ("Fruit")

fruits_selected = streamlit.multiselect("Pick fruits", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe (fruits_to_show)

streamlit.header ('Fruityvice food advice')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# write your own comment -this normalizes the json to better readble format 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - shows data in a table/frame
streamlit.dataframe(fruityvice_normalized)

