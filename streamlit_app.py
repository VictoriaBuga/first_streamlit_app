import streamlit
import pandas

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect('Pick some fruits: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#streamlit.dataframe(my_fruit_list)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cursor = my_cnx.cursor()
my_cursor.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cursor.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_rows)
my_cursor.execute("insert into fruit_load_list values ('from streamlit')")

my_cnx1 = snowflake.connector.connect(**streamlit.secrets["snowflake"])

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('The user entered', add_my_fruit)
my_cursor = my_cnx.cursor()
sql = "insert into pc_rivery_db.public.fruit_load_list values(%s)"
my_cursor.execute(sql, add_my_fruit)
my_data_rows = my_cursor.fetchall()
  

