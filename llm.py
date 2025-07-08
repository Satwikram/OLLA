from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.output_parsers import JsonOutputToolsParser
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


print("Loading LLM...")