import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    if submitted := st.form_submit_button("Submit"):
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
