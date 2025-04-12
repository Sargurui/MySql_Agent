# Chat with SQL DB Dynamically

This application allows users to interact dynamically with a MySQL database using natural language queries. It leverages the power of the `LangChain` framework and the `ChatGroq` language model to process user queries and provide meaningful responses.

## Screen Shot
![image](https://github.com/user-attachments/assets/1d7e262a-d8f2-4afe-a83f-3fb8253f3c04)

## Features

- **Dynamic MySQL Database Interaction**: Query your MySQL database using natural language.
- **Streamlit Interface**: A user-friendly web interface for seamless interaction.
- **Persistent Chat History**: Maintains a session-based chat history for better context.
- **Secure Configuration**: Input sensitive information like database credentials and API keys securely.

## Requirements

- Python 3.8 or higher
- MySQL database
- Groq API Key

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd MySQL_Agent
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your MySQL database is running and accessible.

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser (usually at `http://localhost:8501`).

3. Configure the database connection in the sidebar:
   - Provide the MySQL host, username, password, and database name.
   - Enter your Groq API Key.

4. Start interacting with your database by typing queries in the chat input.

## Example Queries

- "Show me all the records in the `users` table."
- "What is the total revenue for the last quarter?"
- "List the top 5 customers by purchase amount."

## Notes

- Ensure the MySQL user has the necessary permissions to access the database.
- The application uses the `ChatGroq` model for processing queries. Make sure your API key is valid.

## Troubleshooting

- If the application stops unexpectedly, check the Streamlit logs for errors.
- Ensure the database credentials and API key are correct.
- Verify that the required Python packages are installed.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain)
- [Streamlit](https://streamlit.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [ChatGroq](https://groq.com/)

Feel free to contribute to this project by submitting issues or pull requests!
