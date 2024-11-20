from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
import os

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Initialize ChatGPT model
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)

# Create conversation memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Create custom prompt template
custom_template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}

Question: {question}

Helpful Answer:"""

QA_PROMPT = PromptTemplate(
    template=custom_template,
    input_variables=["context", "question"]
)

# Initialize retrieval QA chain
qa_chain = ConversationalRetrievalQA.from_llm(
    llm=llm,
    memory=memory,
    chain_type="stuff",
    combine_docs_chain_kwargs={"prompt": QA_PROMPT}
)
