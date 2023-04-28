from langchain import HuggingFaceHub, PromptTemplate, LLMChain, OpenAI
from langchain.chains import SimpleSequentialChain
from langchain import SQLDatabase, SQLDatabaseChain

from dotenv import load_dotenv

load_dotenv()

def translate_to_english():
    llm = HuggingFaceHub(repo_id="bigscience/bloomz")
    template = "Translate Indonesian to English: {input}"
    prompt = PromptTemplate(template=template, input_variables=["input"])
    return LLMChain(llm=llm, prompt=prompt, verbose=True)

def translate_to_sql():
    db = SQLDatabase.from_uri("sqlite:///chinook.db")
    llm = OpenAI(model_name="gpt-3.5-turbo")
    return SQLDatabaseChain(llm=llm, database=db, verbose=True)

def main():
    chain = SimpleSequentialChain(chains=[translate_to_english(), translate_to_sql()], verbose=True)
    response = chain.run("Berapa banyak karyawan yang ada?")
    print(response)

if __name__ == "__main__":
    main()