import paperscraper
from paperqa import Docs, Answer, PromptCollection
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.embeddings import OllamaEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from paperqa.contrib import ZoteroDB
from dotenv import load_dotenv
load_dotenv()

my_qaprompt = PromptTemplate(
    input_variables=["context", "question"],
    template="Answer the question '{question}' "
    "Use the context below if helpful. "
    "You can cite the context using the key "
    "like (Example2012). "
    "If there is insufficient context, write a poem "
    "about how you cannot answer.\n\n"
    "Context: {context}\n\n")
prompts=PromptCollection(qa=my_qaprompt)
#docs = Docs(prompts=prompts)

# Make sure the model path is correct for your system!
llm = Ollama(base_url='http://localhost:11434',
    model="llama2:7b", callbacks=[StreamingStdOutCallbackHandler()]
)
embeddings = OllamaEmbeddings(model="llama2:7b")

docs = Docs(llm=llm, embeddings=embeddings, prompts=prompts)

zotero = ZoteroDB(library_type="user")  # "group" if group library

for item in zotero.iterate(tag="bitcoin"):
    print(item.key, item.pdf)
    #if item.num_pages > 30:
    #    print("Skipping long paper")
    #    continue  # skip long papers
    docs.add(item.pdf, docname=item.key)

""" keyword_search = 'bitcoin'
papers = paperscraper.search_papers(keyword_search, limit=2)
for path,data in papers.items():
    try:
        docs.add(path,chunk_chars=500)
    except ValueError as e:
        print('Could not read', path, e)
 """
print("asking questions...")
answer = docs.query("What advantages are unique to bitcoin and how can these advantages help investors?, please cite the sources of your information and create a reference table of sources.")
print(answer.formatted_answer)