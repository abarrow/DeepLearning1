import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv
    #from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import YoutubeAudioLoader, PyPDFLoader
import langchain_community
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers.audio import OpenAIWhisperParser




sys.path.append('../..')

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

url="https://www.youtube.com/watch?v=9b-lYfjJnNo"
save_dir="docs/youtube/"
loader = GenericLoader(
    YoutubeAudioLoader([url],save_dir),
    OpenAIWhisperParser()
)
docs = loader.load()
var = docs[0].page_content[1:1000]
print(var)