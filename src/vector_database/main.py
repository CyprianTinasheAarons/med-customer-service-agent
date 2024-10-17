from utils import PineconeManagment
import os
from dotenv import load_dotenv
import sys

load_dotenv()

WORKDIR = os.getenv("WORKDIR")
os.chdir(WORKDIR)
sys.path.append(WORKDIR)


def deploy_vector_database(index_name: str):
    pinecone_management = PineconeManagment()
    docs = pinecone_management.reading_datasource()
    pinecone_management.creating_index(index_name=index_name, docs=docs)


if __name__ == "__main__":
    deploy_vector_database(index_name="medaiagentvector")
