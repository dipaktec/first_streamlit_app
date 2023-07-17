import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title("Mel's streamlit diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index ("Fruit")
fruits_selected = streamlit.multiselect("Pick fruits", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe (fruits_to_show)


def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  # write your own comment -this normalizes the json to better readble format 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # write your own comment - shows data in a table/frame
  return fruityvice_normalized

streamlit.header ('Fruityvice food advice')
try:
  fruit_choice = streamlit.text_input('what fruit would you like information about ' , 'Kiwi')
  if not fruit_choice:
    streamlit.error("Please select fruit to get information")
  else:
    # streamlit.write('user entered '+  fruit_choice)
    fruityvice_normalized = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error();

streamlit.header("the fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()
    
if streamlit.button("Get Fruit List:"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = get_fruit_load_list()
  streamlit.dataframe(my_data_row) 


def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
    return "Thanks for adding "+  new_fruit

fruit_choice_add = streamlit.text_input('what fruit would you like to add ') 
if streamlit.button("Add a fruit to the list:"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(fruit_choice_add)
  streamlit.write(back_from_function)

streamlit.stop()




