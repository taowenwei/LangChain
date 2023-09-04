from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
import productbase
import prompts
import example
import os

load_dotenv()


def buildAgentChain(llm):
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

def buildAssitantChain(llm):
    template = PromptTemplate(
        template=prompts.STAGE_ANALYZER_INCEPTION_PROMPT,
        input_variables=[
            "conversation_history",
            "conversation_stage_id",
            "conversation_stages",
        ],
    )
    chain = LLMChain(prompt=template, llm=llm)
    stages = list(map(lambda item: f'{item[0]}: {item[1]}', prompts.CONVERSATION_STAGES.items()))
    return (chain, stages)


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    llm = ChatOpenAI(model="gpt-3.5-turbo")
    agentChain = buildAgentChain(llm)
    assistantChain, stages = buildAssitantChain(llm)
    currentSalesStage = '1'
    conversationHisotry = []

    while True:
        prompt = example.ExampleSales.copy()
        prompt['conversation_history'] = "\n".join(conversationHisotry)
        
        aiMessage = agentChain.__call__(inputs=prompt)
        conversationHisotry.append(aiMessage["text"])
        print('\x1b[35m')
        print(aiMessage["text"].replace("<END_OF_TURN>", ""))
        print('\x1b[0m')

        if '<END_OF_CALL>' in aiMessage["text"]:
            break

        userMessage = input("Your response: ")
        conversationHisotry.append(f'User: {userMessage} <END_OF_TURN>')

        conversationStage = assistantChain.run(
            conversation_history="\n".join(conversationHisotry).rstrip("\n"),
            conversation_stage_id=currentSalesStage,
            conversation_stages="\n".join(stages),
        )
        print('\x1b[34m')
        print(conversationStage)
        print('\x1b[0m')


