import sqlite3
import streamlit as st

def customer_dashboard_page():
    st.title("App Marketplace")
    st.write("Browse and purchase apps")
    
    # Mostrar apps disponibles para comprar
    conn = sqlite3.connect('marketplace.db')
    c = conn.cursor()
    c.execute('SELECT * FROM apps')
    apps = c.fetchall()
    conn.close()

    for app in apps:
        st.subheader(app[1])  # Nombre de la app en la columna 1
        st.write(app[2])  # Descripción de la app en la columna 2
        st.write(f"Price: ${app[3]}")  # Precio en la columna 3
        whatsapp_message = f"Hola, estoy interesado en comprar {app[1]} por ${app[3]}. ¿Podrías proporcionarme los detalles de pago?"
        whatsapp_url = f"https://api.whatsapp.com/send?phone=+5930993513082&text={whatsapp_message}"
        st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button>Buy {app[1]} via WhatsApp</button></a>', unsafe_allow_html=True)
