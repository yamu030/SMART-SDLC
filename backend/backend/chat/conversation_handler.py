from langchain.llms import OpenAI
from langchain.chains import ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm)

def ask_ai(question: str) -> str:
    return conversation.predict(input=question)
