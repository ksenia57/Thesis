import streamlit as st

def app():
    st.title('Главная страница')

    st.image('https://readrate.com/img/pictures/rating/364/36418/36418/w816h301-crop-stretch-daa78d98.jpg')


    st.markdown("""
    * **Что это**
    Веб-приложение, для демонстрирования работы рекомендательной системы.
    * **Для чего**
    Пользователь может получить рекомендации русскоязычной художественной литературы. Система основана на методе 
    content-base, то есть строится исключительно на данных книг.
    * **Разработчик**
    ИУ5-82Б Рабцевич Ксения Руслановна
    """)
    if st.button('Связаться'):
        st.write('ksyunya_rabcevich@mail.ru')