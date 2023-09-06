from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import os
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory


load_dotenv()
os.system('cls' if os.name == 'nt' else 'clear')


def dummy(word):
    print(' do nothing')


tools = [
    Tool.from_function(
        func=dummy,
        name="dummy",
        description="do nothing"
    ),
]

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


agent = initialize_agent(
    tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
    agent_kwargs={
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    },
    memory=ConversationBufferMemory(memory_key="memory", return_messages=True)
)

while True:
    question = input("Your question: ")
    if question == 'quit':
        break
    agent.run(question)
