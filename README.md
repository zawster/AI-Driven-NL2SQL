# AI-Driven-NL2SQL

This repository contains a project that leverages OpenAI's natural language processing capabilities to convert natural language queries into SQL commands, which are then used to query a MySQL database. The goal of this project is to simplify database querying by allowing users to interact with the database using plain English, eliminating the need for extensive SQL knowledge.

### Features

- **Natural Language to SQL Conversion**: Utilizes OpenAI to translate user input in natural language into SQL commands.
- **MySQL Database Integration**: Executes the generated SQL commands on a MySQL database.
- **Streamlit Interface**: Provides an intuitive web interface using Streamlit for users to input their queries, view the generated SQL, and see the query results from the database.
- **Dynamic Querying**: Supports a wide range of SQL queries based on natural language input.

### Technologies Used

- **OpenAI API**: For natural language processing and SQL generation.
- **MySQL**: Database management system.
- **Python**: Core programming language for backend logic.
- **Streamlit**: Web framework for building the user interface.

### Setup and Installation

1. Clone the repository: `git clone https://github.com/zawster/AI-Driven-NL2SQL.git`
2. Navigate to the project directory: `cd AI-Driven-NL2SQL`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Configure the MySQL database and Openai API Key settings in `config.py`.
5. Set the permission of the automation script: `chmod +x entrypoint.sh`
6. Run the application: `./entrypoint.sh`
7. Open your browser and navigate to `http://localhost:8501` to use the interface.

### Usage

1. Enter your query in natural language in the provided text box.
2. Press Enter key to complete the NL2SQL process.
3. View the generated SQL command and the results from the MySQL database.

### Contributing

Contributions are welcome! Please create a pull request with detailed descriptions of your changes.

### License

This project is licensed under the Apache-2.0 License.
