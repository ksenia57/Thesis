import streamlit as st
import pickle
import pandas as pd
def app():
    st.title('Список всех книг')
    books_dict = pickle.load(open('books_dict.pkl', 'rb'))
    books = pd.DataFrame(books_dict)

    i = st.selectbox('Страница', list(reversed(range(1,100))))

    for i in books.index[i-1:i+99]:
        col1, col2 = st.columns(2)
        with col1:
            obls = books.cove[books.iloc[i].name]
            if obls[:11] == 'https:https':
                obls = obls[6:]
            st.image(obls)
        with col2:
            st.write(books.name[books.iloc[i].name])
            st.write(books.author[i])
            st.write(books.section[i])
            st.write(books.publish[i])
            st.write(books.age[i])
            st.write(int(books.pages[i]))
            st.write(books.description[i])
