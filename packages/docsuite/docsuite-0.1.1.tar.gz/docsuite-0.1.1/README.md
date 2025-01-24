# Unified Document Loader

A Python library that automatically detects file types and loads documents using LangChain's powerful document loaders.

## Installation
```bash
pip install docsuite
```

#Usage

```python
from docsuite import UnifiedDocumentLoader

file_path = 'example.pdf'  # Replace with your file path
loader = UnifiedDocumentLoader(file_path)

try:
    documents = loader.load()
    print(documents)
except UnsupportedFileTypeError as e:
    print(e)
```

#Features

-Automatically detects document types (e.g., TXT, PDF, CSV).
-Leverages LangChain's robust document loaders.
-Easy-to-use and extensible.

#License

docsuite is released under the MIT License. You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

