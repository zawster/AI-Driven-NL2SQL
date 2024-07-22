import streamlit as st
import pandas as pd
from dbHandler import *
from prompt import SYSTEM_MESSAGE
from openaiHandler import get_completion_from_messages
import json

def clean_dataframe(df):
    """
    Function to clean a DataFrame by:
    - Dropping duplicate rows
    - Dropping nan values
    - Dropping duplicate columns
    """
    try:
        # Remove duplicate rows based on all columns
        df = df.drop_duplicates() # Row duplication
        df = df.dropna()
        df = df.loc[:, ~df.columns.duplicated()] # columns duplication
        # OPTIONAL: Id columns to be removed 
        id_columns = ["Id", "Payment_Id"] 
        columns_to_drop = [col for col in id_columns if col in df.columns]
        # Drop the specified columns
        df_cleaned = df.drop(columns=columns_to_drop)
        return df_cleaned
    except Exception as exp:
        print(f"There is some issue in cleaning dataframe. Issue: {exp}")
        raise




def query_database(query, conn):
    """ Run SQL query and return results in a dataframe """
    try:
        df = pd.read_sql_query(query, conn)
        df = clean_dataframe(df)
        return df
    except Exception as exp:
        print(f"There is some issue in extracting data from database. Issue: {exp}")
        raise
def get_query_dict_from_response(response):
    """
    This method extracts the query from the response from the
    openai.
    """
    try:
        if type(response) == str:
            brack_count = response.count('{')
            brack_two_count = response.count('}')
            if brack_count == brack_two_count == 1:
                start_index = response.index('{')
                end_index = response.index('}') + 1
                return response[start_index:end_index]
        return response
    except Exception as exp:
        print(f"There is some issue dict response. Issue: {exp}")

def main():

    st.set_page_config(page_title="AI Assitant for MySQL Database", page_icon=":bar_chart:", layout="wide")
    st.write("Ask anything about data in SQL database")
    user_message = st.text_input("Enter your question:")
    # Schema Representation for table
    schemas, tables = get_table_schema()

    if user_message:
        try:
            # Format the system message with the schema
            formatted_system_message = SYSTEM_MESSAGE.format(schemas=schemas)
            response = get_completion_from_messages(formatted_system_message, user_message)
            dict_response = get_query_dict_from_response(response)
            json_response = json.loads(dict_response)

            query = json_response['query']
            print(f"SQL: {query}")
            # Display the generated SQL query
            st.write("SQL Query:")
            st.code(query, language="sql")
        except Exception as e:
            st.write(f"------1st Block: An error occurred in crafting SQL: {e}")

        try:
            if(query):
                # Run the SQL query and display the results
                conn = get_db_connection()
                sql_results = query_database(query, conn)
                conn.close()
                st.write("Query Results:")
                st.dataframe(sql_results)
        except Exception as exp:
            st.write(f"------ Last Block: An error occurred in extracting data: {exp}")

if __name__ == "__main__":
    main()
