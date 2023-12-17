import langchain
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI

langchain.verbose = True
langchain.debug = True


def get_chat():
    return ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


if __name__ == "__main__":
    chat = get_chat()
    tools = load_tools(["ddg-search"])
    agent_chain = initialize_agent(tools, chat, agent=AgentType.OPENAI_MULTI_FUNCTIONS)

    result = agent_chain.run("東京と大阪の天気を教えて")
    print(result)
