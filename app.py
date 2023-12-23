import streamlit as st
from streamlit.components.v1 import iframe
from bokeh.embed import file_html
from bokeh.resources import CDN

def main():
    st.title("Интрактивная карта загрязнения воздуха.")
    st.subheader("регион: Москва")
    
    if st.button("Текущее значение"):
        display_html("saved/last.html")
        
    if st.button("Предсказание"):
        display_html("saved/predicted.html")

def display_html(path):
    try:
        with open(path, 'r') as file:
            html = file.read()

        html += CDN.render()
        st.components.v1.html(html, width=900, height=700, scrolling=True)
    except Exception as e:
        st.write(f"Возникла ошибка: {str(e)}")
    
if __name__ == "__main__":
    main()