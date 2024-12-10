from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

import os
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key, openai_api_base):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key = openai_api_key, openai_api_base=openai_api_base)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

# openai_api_key="sk-yN6LMdh4613Ka1fbeTWzOiYKiXBSsTGdnOXWBwVX2pVIwVHR"
# openai_api_base="https://api.aigc369.com/v1"
memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory, openai_api_key, openai_api_base))
# print(get_chat_response("我上一个问题是什么？", memory, openai_api_key, openai_api_base))
