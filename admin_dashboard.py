import streamlit as st
import sqlite3
from auth import hash_password

def admin_dashboard_page():
    st.title("Administrator Dashboard")

    # Tablero de gestión
    tab = st.sidebar.selectbox("Select Action", ["Manage Apps", "Manage Users"])

    if tab == "Manage Apps":
        manage_apps()
    elif tab == "Manage Users":
        manage_users()

def manage_apps():
    st.header("Manage Apps")

    action = st.selectbox("Select Action", ["Create App", "Edit App", "Delete App"])

    if action == "Create App":
        create_app()
    elif action == "Edit App":
        edit_app()
    elif action == "Delete App":
        delete_app()

def create_app():
    st.subheader("Create New App")

    app_name = st.text_input("App Name")
    app_description = st.text_area("App Description")
    app_price = st.number_input("App Price", min_value=0.0, format="%.2f")
    app_link = st.text_input("App Link")

    if st.button("Create App"):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        publisher_id = st.session_state['user'][0]
        c.execute('INSERT INTO apps (name, description, price, link, publisher_id) VALUES (?, ?, ?, ?, ?)',
                  (app_name, app_description, app_price, app_link, publisher_id))
        conn.commit()
        conn.close()
        st.success("App created successfully")

def edit_app():
    st.subheader("Edit App")

    conn = sqlite3.connect('marketplace.db')
    c = conn.cursor()
    c.execute('SELECT * FROM apps')
    apps = c.fetchall()
    conn.close()

    app_names = [app[1] for app in apps]
    selected_app = st.selectbox("Select App to Edit", app_names)

    if selected_app:
        app = next(app for app in apps if app[1] == selected_app)
        new_name = st.text_input("New Name", value=app[1])
        new_description = st.text_area("New Description", value=app[2])
        new_price = st.number_input("New Price", min_value=0.0, format="%.2f", value=app[3])
        new_link = st.text_input("New Link", value=app[4])

        if st.button("Save Changes"):
            conn = sqlite3.connect('marketplace.db')
            c = conn.cursor()
            c.execute('UPDATE apps SET name=?, description=?, price=?, link=? WHERE id=?',
                      (new_name, new_description, new_price, new_link, app[0]))
            conn.commit()
            conn.close()
            st.success("App updated successfully")

def delete_app():
    st.subheader("Delete App")

    conn = sqlite3.connect('marketplace.db')
    c = conn.cursor()
    c.execute('SELECT * FROM apps')
    apps = c.fetchall()
    conn.close()

    app_names = [app[1] for app in apps]
    selected_app = st.selectbox("Select App to Delete", app_names)

    if selected_app:
        if st.button("Delete App"):
            conn = sqlite3.connect('marketplace.db')
            c = conn.cursor()
            app_id = next(app[0] for app in apps if app[1] == selected_app)
            c.execute('DELETE FROM apps WHERE id=?', (app_id,))
            conn.commit()
            conn.close()
            st.success("App deleted successfully")

def manage_users():
    st.header("Manage Users")

    action = st.selectbox("Select Action", ["Create User", "Edit User", "Delete User"])

    if action == "Create User":
        create_user()
    elif action == "Edit User":
        edit_user()
    elif action == "Delete User":
        delete_user()

def create_user():
    st.subheader("Create New User")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["publisher", "customer"])

    if st.button("Create User"):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        hashed_password = hash_password(password)
        try:
            c.execute('INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)',
                      (username, email, hashed_password, role))
            conn.commit()
            st.success("User created successfully")
        except sqlite3.IntegrityError:
            st.error("Username or email already exists")
        conn.close()

def edit_user():
    st.subheader("Edit User")

    conn = sqlite3.connect('marketplace.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()

    usernames = [user[1] for user in users]
    selected_user = st.selectbox("Select User to Edit", usernames)

    if selected_user:
        user = next(user for user in users if user[1] == selected_user)
        new_username = st.text_input("New Username", value=user[1])
        new_email = st.text_input("New Email", value=user[2])
        new_password = st.text_input("New Password", type="password")
        new_role = st.selectbox("New Role", ["publisher", "customer"], index=["publisher", "customer"].index(user[3]))

        if st.button("Save Changes"):
            conn = sqlite3.connect('marketplace.db')
            c = conn.cursor()
            if new_password:
                new_password = hash_password(new_password)
            else:
                new_password = user[2]  # Keep the old password if not provided
            c.execute('UPDATE users SET username=?, email=?, password=?, role=? WHERE id=?',
                      (new_username, new_email, new_password, new_role, user[0]))
            conn.commit()
            conn.close()
            st.success("User updated successfully")

def delete_user():
    st.subheader("Delete User")

    conn = sqlite3.connect('marketplace.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()

    usernames = [user[1] for user in users]
    selected_user = st.selectbox("Select User to Delete", usernames)

    if selected_user:
        if st.button("Delete User"):
            conn = sqlite3.connect('marketplace.db')
            c = conn.cursor()
            user_id = next(user[0] for user in users if user[1] == selected_user)
            c.execute('DELETE FROM users WHERE id=?', (user_id,))
            conn.commit()
            conn.close()
            st.success("User deleted successfully")

