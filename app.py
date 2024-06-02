import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv
    #from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
import langchain_community



sys.path.append('../..')

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

# this is for loading a pdf document
# loader = PyPDFLoader("docs/retire-off-of-bitcoin-tax-free-wealth_662abb3f.pdf")
# pages = loader.load()
#
# print("number of pages = " + str(len(pages)))
# page = pages[4]
# print(page.page_content[0:500])
# print(page.metadata)

from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

url="https://www.youtube.com/watch?v=9b-lYfjJnNo"
save_dir="docs/youtube/"
loader = GenericLoader(
    YoutubeAudioLoader([url],save_dir),
    OpenAIWhisperParser()
)
docs = loader.load()
var = docs[0].page_content[0:500]