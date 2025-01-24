from docsuite import UnifiedDocumentLoader, UnsupportedFileTypeError


loader = UnifiedDocumentLoader("test/pdf/artificial_intelligence_tutorial.pdf")
documents = loader.load()
print(documents) 
print("\n Number of the document:",len(documents))