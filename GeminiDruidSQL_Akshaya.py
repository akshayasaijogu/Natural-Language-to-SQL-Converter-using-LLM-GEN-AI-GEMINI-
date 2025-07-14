import streamlit as st
import google.generativeai as genai
import requests
import pandas as pd


# Druid SQL Broker URL
DRUID_BROKER_URL = "http://localhost:8888/unified-console.html"

## Configure Genai Key
## api_key = "AIzaSyBvtPP-kQu_c_R_zEHW3Gajt56LXUkH1GM"
genai.configure(api_key= "AIzaSyBvtPP-kQu_c_R_zEHW3Gajt56LXUkH1GM")



## Define Your Prompt
prompt=[
    """
    You are an expert Druid SQL query generator. Your task is to translate natural language questions into valid Druid SQL queries.

    **Instructions:**

    1.  **Understand the User's Request:** Carefully analyze the user's natural language question to understand their intent and the data they are seeking.
    2.  **Identify Relevant Tables and Columns:** Based on the user's request, determine the necessary tables and columns within the Druid data source. Assume the following table and column information is available. (You may need to adapt/expand these based on your specific Druid instance):
        * **Table:** `studentmemo`
            * **Columns:**
                * "__time"(TIMESTAMP) — Record timestamp in UTC.
                * "S.NO" (INT) — Serial number of the record.
                * "Student Name" (VARCHAR) — Name of the student.
                * "ROLL NUMBER" (VARCHAR) — Unique roll number for each student.

                * "8EC08_M1" (INT) — Midterm 1 marks for the subject 8EC08.
                * "8EC08_M2"(INT) — Midterm 2 marks for subject 8EC08.
                * "8EC08_M3" (INT) — Midterm 3 marks for subject 8EC08.
                * "8EC08_INT" (INT) — Total Internal marks (the average of midterms) for subject 8EC08.
                * "8EC08_EXT" (INT) — External exam marks for subject 8EC08.
                * "8EC08_TOT" (INT) — Total marks for subject 8EC08 (INT + EXT).
                * "8EC08_CREDITS" (INT) — Credits obtained for subject 8EC08.
                * "8EC08_STATUS" (VARCHAR) — Status of passing (P/F) for subject 8EC08.
                * "8EC08_GRADE" (VARCHAR) — Grade awarded (O,A+,A,B+,B,C,F) for subject 8EC08.
                * "8EC08_POINTS" (INT) — Points scored (Range of 0 to 10) for subject 8EC08
                
                * "8EC19_M1" (INT) — Midterm 1 marks for the subject 8EC19.
                * "8EC19_M2" (INT) — Midterm 2 marks for subject 8EC19.
                * "8EC19_M3" (INT) — Midterm 3 marks for subject 8EC19.
                * "8EC19_INT" (INT) — Total Internal marks (the average of midterms) for subject 8EC19.
                * "8EC19_EXT" (INT) — External exam marks for subject 8EC19.
                * "8EC19_TOT" (INT) — Total marks for subject 8EC19 (INT + EXT).
                * "8EC19_CREDITS" (INT) — Credits obtained for subject 8EC19.
                * "8EC19_STATUS" (VARCHAR) — Status of passing (P/F) for subject 8EC19.
                * "8EC19_GRADE" (VARCHAR) — Grade awarded (O,A+,A,B+,B,C,F) for subject 8EC19.
                * "8EC19_POINTS" (INT) — Points scored (Range of 0 to 10) for subject 8EC19.

                
                * "8EC30_M1" (INT) — Midterm 1 marks for the subject 8EC30.
                * "8EC30_M2" (INT) — Midterm 2 marks for subject 8EC30.
                * "8EC30_M3" (INT) — Midterm 3 marks for subject 8EC30.
                * "8EC30_INT" (INT) — Total Internal marks (the average of midterms) for subject 8EC30.
                * "8EC30_EXT" (INT) — External exam marks for subject 8EC30.
                * "8EC30_TOT" (INT) — Total marks for subject 8EC30 (INT + EXT).
                * "8EC30_CREDITS" (INT) — Credits obtained for subject 8EC30.
                * "8EC30_STATUS" (VARCHAR) — Status of passing (P/F) for subject 8EC30.
                * "8EC30_GRADE" (VARCHAR) — Grade awarded (O,A+,A,B+,B,C,F) for subject 8EC30.
                * "8EC30_POINTS" (INT) — Points scored (Range of 0 to 10) for subject 8EC30.


                * "8EC68_M1" (INT) — Midterm 1 marks for the subject 8EC68.
                * "8EC68_M2" (INT) — Midterm 2 marks for subject 8EC68.
                * "8EC68_M3" (INT) — Midterm 3 marks for subject 8EC68.
                * "8EC68_INT" (INT) — Total Internal marks (the average of midterms) for subject 8EC68.
                * "8EC68_EXT" (INT) — External exam marks for subject 8EC68.
                * "8EC68_TOT" (INT) — Total marks for subject 8EC68 (INT + EXT).
                * "8EC68_CREDITS" (INT) — Credits obtained for subject 8EC68.
                * "8EC68_STATUS" (VARCHAR) — Status of passing (P/F) for subject 8EC68.
                * "8EC68_GRADE" (VARCHAR) — Grade awarded (O,A+,A,B+,B,C,F) for subject 8EC68.
                * "8EC68_POINTS" (INT) — Points scored (Range of 0 to 10) for subject 8EC68.

                * "8F709_M1" (INT) — Midterm 1 marks for the subject 8F709.
                * "8F709_M2" (INT) — Midterm 2 marks for subject 8F709.
                * "8F709_M3" (INT) — Midterm 3 marks for subject 8F709.
                * "8F709_INT" (INT) — Total Internal marks (the average of midterms) for subject 8F709.
                * "8F709_EXT" (INT) — External exam marks for subject 8F709.
                * "8F709_TOT" (INT) — Total marks for subject 8F709 (INT + EXT).
                * "8F709_CREDITS"(INT) — Credits obtained for subject 8F709.
                * "8F709_STATUS" (VARCHAR) — Status of passing (P/F) for subject 8F709.
                * "8F709_GRADE" (VARCHAR) — Grade awarded (O,A+,A,B+,B,C,F) for subject 8F709.
                * "8F709_POINTS" (INT) — Points scored (Range of 0 to 10) for subject 8F709.


                * "Total" (INT) — Sum of all marks across subjects.
                * "Total%" (DOUBLE) — Percentage calculated from the total marks.
                * "BACKLOGS" (INT) — Number of backlogs the student has.
                * "Subjects Registerd" (INT) — Count of subjects registered by the student.
                * "APPEARED" (INT) — Number of subjects appeared for.
                * "PASSED" (INT) — Number of subjects passed.
                * "TOT_CREDITS" (INT) — Total credits earned across all subjects.
                * "SGPA" (DOUBLE) — Semester Grade Point Average.



    3.  **Generate Accurate Druid SQL:** Construct a valid Druid SQL query that accurately reflects the user's request.
    4.  **Handle Aggregations and Filtering:** Use appropriate Druid SQL functions for aggregations (e.g., `SUM`, `COUNT`, `AVG`, `MIN`, `MAX`) and filtering (e.g., `WHERE`, `AND`, `OR`, `LIKE`, `=`).
    5.  **Time-Based Filtering:** If the user's request involves time-based filtering, use the `__time` column and appropriate Druid time functions (e.g., `TIME_FLOOR`, `TIME_PARSE`).
    6.  **Grouping and Ordering:** Use `GROUP BY` and `ORDER BY` clauses as needed to organize and present the results.
    8.  **Output Druid SQL Only:** Provide only the generated Druid SQL query as the output and Donot include semicolon at end of output query and  Do not include any explanations or other text.
    9. **Assume UTC Timezone.**
    10. **Use double quotes for identifiers **.
    11. **Use double quotes for column and tables**.

    *Example:*

    *User Input:* "Show me data for studentmemo table"

    *Your Output:*
    Druid sql
    SELECT * from "studentsmemo" 

    
    """
]

    
## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-1.5-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function to generate query output from Druid Database

def query_druid(sql_query):
    """Executes Druid SQL and returns the results"""
    headers = {"Content-Type": "application/json"}
    payload = {"query": sql_query}
    
    response = requests.post(DRUID_BROKER_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return pd.DataFrame(response.json())  # Convert to DataFrame for better handling
    else:
        st.error(f"Error querying Druid: {response.text}")
        return None


## Streamlit App
st.set_page_config(page_title="English questions to Druid SQL query")
st.header("Gemini App To Retrieve Druid SQL Data")

question=st.text_input("Input: ",key="input")

# The content of the Submit button
submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    st.success("Druid SQL Query Generated!")
    st.code(response, language="DruidSql")
    print(response)
    with st.spinner("Querying Apache Druid..."):
        results = query_druid(response)
        
        if results is not None and not results.empty:
            st.success("Query Results:")
            st.dataframe(results)
        else:
            st.warning("No results found or query failed.")
    