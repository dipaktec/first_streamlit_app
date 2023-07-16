import streamlit
import snowflake.connector


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

fruit_choice = streamlit.text_input('what fruit would you like information about ' , 'Kiwi')
streamlit.write('user entered '+  fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -this normalizes the json to better readble format 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - shows data in a table/frame
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_lists")
my_data_row = my_cur.fetchone()
streamlit.text("the fruit load list contains:")
streamlit.text(my_data_row) 

