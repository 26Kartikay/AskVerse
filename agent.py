from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader("496.pdf")
docs=loader.load()
docs
