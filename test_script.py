from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

# Configurations
username = "***"
password = "*****"
host = "***********.ondigitalocean.com"
port = 24075
mydatabase = "maindb"
openai_key = "sk-************************************"

mysql_uri = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{mydatabase}'
# postgres_uri = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{mydatabase}"
# sql_database_uri = ""
# engine = create_engine(sql_database_uri)
# allowed_tables = ["CustomerInformation", "InvoiceInformation", "AccountInformation"]

print("### Creating connection with database...")
# sql_database = SQLDatabase(engine, include_tables=allowed_tables)
sql_database = SQLDatabase.from_uri(mysql_uri)
print("### DB connection got ctreated...")

### Configuring OpenAI API
llm = ChatOpenAI(api_key=openai_key, model="gpt-3.5-turbo")
print("Creating SQL Query Chain...")
generate_query = create_sql_query_chain(llm, sql_database)
print("SQL Query Chain Created...\n\n")

# Querying db
print("Generating SQL Query...")
question = "What is the total payment of Alexander?"
print(f"Question: {question}")
query = generate_query.invoke({"question": question})
print(f"SQL Query: {query}")
