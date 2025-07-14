import streamlit as st
from DruidSql import generate_druid_sql  # Import function from DruidSql.py

st.title("Natural Language to SQL Converter")
st.write("Enter a query, and the AI will generate the SQL equivalent.")

# Streamlit input box
user_query = st.text_area("Enter your query:")

if st.button("Convert to SQL"):
    if user_query.strip():
        with st.spinner("Generating SQL query..."):
            try:
                sql_query = generate_druid_sql(user_query)  # Call backend function
                st.success(" SQL Query Generated!")
                st.code(sql_query, language="sql")  # Display SQL
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid query!")
