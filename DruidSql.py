import ollama
import json

def generate_druid_sql(user_input, model="llama2"): #replace mistral with your model if needed.
    """
    Generates Druid SQL from natural language using an Ollama model.

    Args:
        user_input: The natural language query.
        model: The Ollama model to use.

    Returns:
        The generated Druid SQL query as a string, or None if an error occurs.
    """

    prompt = f"""
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

    


    **Now, generate the Druid SQL query for the following user input:**

    **User Input:** {user_input}
    """

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return response['message']['content'].strip()

    except Exception as e:
        print(f"Error generating Druid SQL: {e}")
        return None

# Example usage:
"""

print("Enter the Text Language :  ")
user_query = input()
druid_sql = generate_druid_sql(user_query)

if druid_sql:
    print(f"User Query: {user_query}")
    print(f"Druid SQL: {druid_sql}")
    
"""   