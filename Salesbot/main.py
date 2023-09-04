from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
import productbase
import prompts
import example
import os

load_dotenv()


def buildChain(llm):
    template = PromptTemplate(
        template=prompts.SALES_AGENT_TOOLS_PROMPT,
        input_variables=[
            "salesperson_name",
            "salesperson_role",
            "company_name",
            "company_business",
            "company_values",
            "conversation_purpose",
            "conversation_type",
            "conversation_history",
        ],
    )
    return LLMChain(prompt=template, llm=llm, verbose=False)


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    llm = ChatOpenAI(model="gpt-3.5-turbo")
    chain = buildChain(llm)
    stage = '1'
    conversationHisotry = []

    while True:
        prompt = example.ExampleSales.copy()
        prompt['conversation_history'] = "\n".join(conversationHisotry)
        
        aiMessage = chain.__call__(inputs=prompt)
        output = f'{example.ExampleSales["salesperson_name"]}: {aiMessage["text"]}'
        conversationHisotry.append(output)
        print('\x1b[35m')
        print(output.replace("<END_OF_TURN>", ""))
        print('\x1b[0m')

        userMessage = input("Your response: ")
        conversationHisotry.append(f'User: {userMessage} <END_OF_TURN>')


