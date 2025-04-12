import streamlit as st
from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
from langchain_groq import ChatGroq
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler

st.set_page_config(page_title="Chat with SQL DB", page_icon='💻')
st.title('Chat with your SQL DB Dynamically!!')

MYSQL = 'USE_MYSQL'

st.sidebar.header('Database Configuration')
mysql_host = st.sidebar.text_input('Provide Host Name')
mysql_user = st.sidebar.text_input('MySQL Username')
mysql_pass = st.sidebar.text_input('Provide the Password', type='password')
mysql_db = st.sidebar.text_input('MySQL Database Name')

api_key = st.sidebar.text_input(label='Groq API Key', type='password')

if not (mysql_host and mysql_user and mysql_pass and mysql_db):
    st.info('Please enter the MySQL database information')
    st.stop()

if not api_key:
    st.info('Please add the Groq API Key')
    st.stop()

llm = ChatGroq(groq_api_key=api_key, model_name='Llama3-8b-8192', streaming=True)

@st.cache_resource(ttl='2h')
def configure_db(mysql_host, mysql_user, mysql_pass, mysql_db):
    """
    Configures and returns a connection to the MySQL database.

    Args:
        mysql_host (str): The hostname of the MySQL server.
        mysql_user (str): The username for the MySQL database.
        mysql_pass (str): The password for the MySQL database.
        mysql_db (str): The name of the MySQL database.

    Returns:
        SQLDatabase: A configured SQLDatabase instance for the MySQL database.
    """
    return SQLDatabase(create_engine(f'mysql+mysqlconnector://{mysql_user}:{mysql_pass}@{mysql_host}/{mysql_db}'))

db = configure_db(mysql_host, mysql_user, mysql_pass, mysql_db)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    handle_parsing_errors=True,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if 'messages' not in st.session_state or st.sidebar.button('clear message history'):
    st.session_state['messages'] = [{'role': 'assistant', 'content': 'How can I help you?'}]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

user_query = st.chat_input(placeholder='Ask anything from the database')

if user_query:
    st.session_state.messages.append({'role': 'user', 'content': user_query})
    st.chat_message('user').write(user_query)

    with st.chat_message('assistant'):
        streamlit_callback = StreamlitCallbackHandler(st.container())

        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({'role': 'assistant', 'content': response})
        st.write(response)
