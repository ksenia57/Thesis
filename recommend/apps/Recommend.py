import streamlit as st
import pickle
import pandas as pd

def app():
    st.title('Рекомендательная система книг')

    def recommend(rusbook):
        rusbook_index = books[books['name'] == rusbook].index[0]
        distances = sorted(list(enumerate(similarity[rusbook_index])), reverse=True, key=lambda x: x[1])

        recommended_book_names = []
        recommended_book_obl = []
        for i in distances[1:9]:
            recommended_book_names.append(books.name[books.iloc[i[0]].name])
            obls = books.cove[books.iloc[i[0]].name]
            if obls[:11] == 'https:https':
                obls = obls[6:]
            recommended_book_obl.append(obls)
        return recommended_book_names, recommended_book_obl

    books_dict = pickle.load(open('books_dict.pkl', 'rb'))
    books = pd.DataFrame(books_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    selected_book_name = st.selectbox(
        'К какой книге вывести рекомендации?', books['name'].values)

    if st.button('Рекомендации'):
        recommended_book_names, recommended_book_obl = recommend(selected_book_name)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.text(recommended_book_names[0])
            st.image(recommended_book_obl[0])
        with col2:
            st.text(recommended_book_names[1])
            st.image(recommended_book_obl[1])
        with col3:
            st.text(recommended_book_names[2])
            st.image(recommended_book_obl[2])
        with col4:
            st.text(recommended_book_names[3])
            st.image(recommended_book_obl[3])
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.text(recommended_book_names[4])
            st.image(recommended_book_obl[4])
        with col2:
            st.text(recommended_book_names[5])
            st.image(recommended_book_obl[5])
        with col3:
            st.text(recommended_book_names[6])
            st.image(recommended_book_obl[6])
        with col4:
            st.text(recommended_book_names[7])
            st.image(recommended_book_obl[7])
