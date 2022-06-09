import streamlit as st
import pickle
import pandas as pd
def app():
    st.title('Поиск книги')
    books_dict = pickle.load(open('books_dict.pkl', 'rb'))
    books = pd.DataFrame(books_dict)

    selectname = st.selectbox(
        'Введите название книги', books['name'])

    if st.button('Поиск'):
        select_ind = [books[books['name'] == selectname].index[0]]
        col1, col2 = st.columns(2)
        with col1:
            obls = books.cove[select_ind[0]]
            if obls[:11] == 'https:https':
                obls = obls[6:]
            st.image(obls)
        with col2:
            st.write(books.name[select_ind[0]])
            st.write(books.author[select_ind[0]])
            st.write(books.section[select_ind[0]])
            st.write(books.publish[select_ind[0]])
            st.write(books.age[select_ind[0]])
            st.write(books.description[select_ind[0]])