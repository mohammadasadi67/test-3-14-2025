import streamlit as st

# Title of the app
st.title("My Streamlit App")

# Using custom CSS for styling
st.markdown("""
    <style>
    .css-1v3nvj4 { 
        color: red;
    }
    </style>
""", unsafe_allow_html=True)

# Adding an image to the app
st.image("path_to_image.png", caption="My Streamlit App", width=200)

# Creating two columns
col1, col2 = st.columns(2)

with col1:
    st.header("Left Column")
    st.write("Content for the left column goes here.")
    user_input = st.text_input("Enter your name:")
    if user_input:
        st.write(f"Hello, {user_input}!")

with col2:
    st.header("Right Column")
    st.write("Content for the right column goes here.")

# Adding an expandable section
with st.beta_expander("Click to expand"):
    st.write("This is a collapsible section with more information.")

# Sidebar with navigation options
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose an option", ["Home", "About", "Contact"])

if option == "Home":
    st.write("This is the Home page.")
elif option == "About":
    st.write("This is the About page.")
elif option == "Contact":
    st.write("This is the Contact page.")

# Displaying a simple interactive widget
age = st.slider("Select your age", 0, 100)
st.write(f"Your age is: {age}")
