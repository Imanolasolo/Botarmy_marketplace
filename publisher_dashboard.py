import sqlite3
import streamlit as st

def publisher_dashboard_page():
    st.title("Publisher Dashboard")
    st.write("Publish new apps")
    
    # Añadir funcionalidades para publicar apps
    app_name = st.text_input("App Name")
    app_description = st.text_area("App Description")
    app_price = st.number_input("App Price", min_value=0.0, format="%.2f")
    app_link = st.text_input("App Link")
    
    if st.button("Publish App"):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        publisher_id = st.session_state['user'][0]  # El ID del publicador está en la columna 0
        c.execute('INSERT INTO apps (name, description, price, link, publisher_id) VALUES (?, ?, ?, ?, ?)',
                  (app_name, app_description, app_price, app_link, publisher_id))
        conn.commit()
        conn.close()
        st.success("App published successfully")
