import streamlit as st
import pandas as pd
import json
import openai
import os
import re
import matplotlib.pyplot as plt
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv


def csv_agent_func(file_path, user_message):
    """Run the CSV agent with the given file path and user message."""
    agent = create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
        file_path,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    try:
        # Properly format the user's input and wrap it with the required "input" key
        tool_input = {
            "input": {
                "name": "python",
                "arguments": user_message
            }
        }

        response = agent.run(tool_input)
        return response
    except Exception as e:
        st.write(f"Error: {e}")
        return None


def extract_code_from_response(response):
    """Extracts Python code from a string response."""
    # Use a regex pattern to match content between triple backticks
    code_pattern = r"```python(.*?)```"
    match = re.search(code_pattern, response, re.DOTALL)

    if match:
        # Extract the matched code and strip any leading/trailing whitespaces
        return match.group(1).strip()
    return None


def csv_analyzer_app():
    """Main Streamlit application for CSV analysis."""

    st.title('CSV Assistant')
    st.write('Please upload your CSV file and enter your query below:')

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name,
                        "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)

        # Save the uploaded file to disk
        file_path = os.path.join("tmp", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        df = pd.read_csv(file_path)
        st.dataframe(df)

        user_input = st.text_input("Your query")
        if st.button('Run'):
            response = csv_agent_func(file_path, user_input)

            # Extracting code from the response
            code_to_execute = extract_code_from_response(response)

            if code_to_execute:
                try:
                    # Making df available for execution in the context
                    exec(code_to_execute, globals(), {"df": df, "plt": plt})
                    fig = plt.gcf()  # Get current figure
                    st.pyplot(fig)  # Display using Streamlit
                except Exception as e:
                    st.write(f"Error executing code: {e}")
            else:
                st.write(response)

    st.divider()


def main():
    load_dotenv()
    csv_analyzer_app()


if __name__ == '__main__':
    main()
