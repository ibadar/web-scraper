import streamlit as st 
from scrape import grab_data, extract_body_content, remove_body_content, split_all_content
from parse import parse_data

st.title("Webscraper")
url = st.text_input("Enter web URL: ")

if st.button("Run"):
    st.write("Buttom pressed")
    
    result = grab_data(url)
    body_content = extract_body_content(result)
    clean_content = remove_body_content(body_content)
    
    st.session_state.dom_content = clean_content
    
    with st.expander("View Content"):
        st.text_area("Content", clean_content, height=300)

if "dom_content" in st.session_state:
    usr_input = st.text_area("What would you like to know? ")
    
    if st.button("Send"):
        if usr_input:
            st.write("Sending content")
        
            chunks = split_all_content(st.session_state.dom_content)
            ran = parse_data(chunks, usr_input)
            st.write(ran)
    