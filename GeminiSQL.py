# -------------------- Imports --------------------
import streamlit as st
import google.generativeai as genai

# -------------------- Set Page Config FIRST --------------------
st.set_page_config(
    page_title="Gemini NL to Druid SQL",
    page_icon="🧠",
    layout="centered"
)

# -------------------- Title & Description --------------------
st.title("🧠 Gemini NL → Druid SQL Converter")
st.subheader("Convert natural language into accurate Druid SQL queries")

# -------------------- Secure API Key Input --------------------
api_key = st.text_input("🔐 Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.warning("⚠️ Please enter your Gemini API key to continue.")

# -------------------- Prompt --------------------
prompt = [
    """
    You are an expert Druid SQL query generator. Your task is to translate natural language questions into valid Druid SQL queries.

    **Instructions:**

    1.  **Understand the User's Request:** Carefully analyze the user's natural language question to understand their intent and the data they are seeking.
    2.  **Identify Relevant Tables and Columns:** Based on the user's request, determine the necessary tables and columns within the Druid data source. Assume the following table and column information is available. (You may need to adapt/expand these based on your specific Druid instance):
        * **Table:** `studentmemo`
            * **Columns:**
                * "__time" (TIMESTAMP)
                * "S.NO" (INT)
                * "Student Name" (VARCHAR)
                * "ROLL NUMBER" (VARCHAR)
                * "8ECO8_M1" (INT)
                * "8EC08_M2" (INT)
                * "8ECO8_M3" (INT)
                * "8EC08_INT" (INT)
                * "8EC08_M_INT" (INT)
                * "8EC08_EXT" (INT)
                * "8EC08_TOT" (INT)
                * "8EC08_CREDITS" (INT)
                * "8EC08_SECU_CREDITS" (INT)
                * "8EC08_STATUS" (VARCHAR)
                * "8EC08_GRADE" (VARCHAR)
                * "8EC08_POINTS" (INT)
                
                * "8EC19_M1" (INT)
                * "8EC19_M2" (INT)
                * "8EC19_M3" (INT)
                * "8EC19_INT" (INT)
                * "8EC19_M_INT" (INT)
                * "8EC19_EXT" (INT)
                * "8EC19_TOT" (INT)
                * "8EC19_CREDITS" (INT)
                * "8EC19_SECU_CREDITS" (INT)
                * "8EC19_STATUS" (VARCHAR)
                * "8EC19_GRADE" (VARCHAR)
                * "8EC19_POINTS" (INT)
                
                * "8EC30_M1" (INT)
                * "8EC30_M2" (INT)
                * "8EC30_M3" (INT)
                * "8EC30_INT" (INT)
                * "8EC30_M_INT" (INT)
                * "8EC30_EXT" (INT)
                * "8EC30_TOT" (INT)
                * "8EC30_CREDITS" (INT)
                * "8EC30_SECU_CREDITS" (INT)
                * "8EC30_STATUS" (VARCHAR)
                * "8EC30_GRADE" (VARCHAR)
                * "8EC30_POINTS" (INT)

                * "8EC68_M1" (INT)
                * "8EC68_M2" (INT)
                * "8EC68_M3" (INT)
                * "8EC68_INT" (INT)
                * "8EC68_M_INT" (INT)
                * "8EC68_EXT" (INT)
                * "8EC68_TOT" (INT)
                * "8EC68_CREDITS" (INT)
                * "8EC68_SECU_CREDITS" (INT)
                * "8EC68_STATUS" (VARCHAR)
                * "8EC68_GRADE" (VARCHAR)
                * "8EC68_POINTS" (INT)

                * "8F709_M1" (INT)
                * "8F709_M2" (INT)
                * "8F709_M3" (INT)
                * "8F709_INT" (INT)
                * "8F709_M_INT" (INT)
                * "8F709_EXT" (INT)
                * "8F709_TOT" (INT)
                * "8F709_CREDITS" (INT)
                * "8F709_SECU_CREDITS" (INT)
                * "8F709_STATUS" (VARCHAR)
                * "8F709_GRADE" (VARCHAR)
                * "8F709_POINTS" (INT)

                * "Total" (INT)
                * "Total%" (DOUBLE)
                * "BACKLOGS" (INT)
                * "Subjects Registerd" (INT)
                * "APPEARED" (INT)
                * "PASSED" (INT)
                * "TOT_CREDITS" (INT)
                * "SGPA" (DOUBLE)

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

# -------------------- Gemini Query Function --------------------
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content([prompt[0], question])
        return response.text.strip()
    except Exception as e:
        st.error(f"❌ Gemini Error: {e}")
        return None

# -------------------- User Question Input --------------------
question = st.text_input("🗣️ Ask your question (e.g., Show failed students in 8EC08):")

# -------------------- Submit Button --------------------
if st.button("Generate SQL"):
    if not api_key:
        st.warning("⚠️ API key is missing.")
    elif not question:
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("🤖 Generating SQL..."):
            sql = get_gemini_response(question, prompt)
            if sql:
                st.success("✅ Generated SQL:")
                st.code(sql, language="sql")
            else:
                st.warning("⚠️ No SQL generated. Try again.")

# -------------------- Example Prompts --------------------
with st.expander("📌 Example Questions"):
    st.markdown("""
- Show all students with SGPA above 9  
- Show students who failed in 8F709  
- List students who appeared for more than 6 subjects  
- Show total marks greater than 500  
""")
