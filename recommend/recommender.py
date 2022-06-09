import streamlit as st
from multiapp import MultiApp
from apps import Home, Books, Recommend, search # import your app modules here

app = MultiApp()


# Add all your application here
app.add_app("Главная страница", Home.app)
app.add_app("Список всех книг", Books.app)
app.add_app("Поиск книги", search.app)
app.add_app("Рекомендательная система книг", Recommend.app)
# The main app
app.run()


