from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
import os

load_dotenv()


def buildAgentChain(llm):
    with open('story.md', 'r') as file:
        # Read the entire contents of the file into a string
        prompt = file.read()
        template = PromptTemplate(
            template=prompt,
            input_variables=[
                'salesperson_name',
                'conversation_hisotry'
            ],
        )
        return LLMChain(prompt=template, llm=llm, verbose=False)


def extract(llm, history):
    template = PromptTemplate(
        template="""
            The history below included contains a user's id and its choice of subscription plan and its start date.
            Please extract the id, the chozen plan and the start date. 
            {conversation_hisotry}
            """,
        input_variables=['conversation_hisotry'],
    )
    chain = LLMChain(prompt=template, llm=llm)
    aiMessage = chain.__call__(inputs={
            'conversation_hisotry': history
    })
    print(aiMessage["text"])


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    llm = ChatOpenAI(model="gpt-3.5-turbo")
    agentChain = buildAgentChain(llm)
    conversationHisotry = []

    while True:
        aiMessage = agentChain.__call__(inputs={
            'salesperson_name': 'Ted Lasso',
            'conversation_hisotry': '\n'.join(conversationHisotry)
        })
        conversationHisotry.append(aiMessage["text"])
        print('\x1b[35m')
        print(aiMessage["text"].replace("<END_OF_TURN>", ""))
        print('\x1b[0m')

        if '<END_OF_CALL>' in aiMessage["text"]:
            break

        userMessage = input("Your response: ")
        conversationHisotry.append(f'User: {userMessage} <END_OF_TURN>')

    extract(llm, '\n'.join(conversationHisotry))
