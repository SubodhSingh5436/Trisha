import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def init():
    load_dotenv()

    #Load the OpenAI API key from the envionment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")    

    st.set_page_config(
        page_title = "Trisha",
        page_icon = "😌",
    )

def main():

    init()

    chat = ChatOpenAI(temperature=0.3)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="Hi, I am Trisha, your personal assistant")
        ]

    st.header("Trisha  😌")

    with st.sidebar:
        user_input = st.text_input("Enter your Question: ", key = "user_input")

        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Thinking 🤔"):
                response = chat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))


    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i%2 == 0:
            message(msg.content, is_user=True, key = str(i) + '_user')
        else:
            message(msg.content, is_user = False, key = str(i) + '_ai')



if __name__ == '__main__':
    main()