import os
from pathlib import Path
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    UnstructuredHTMLLoader,
    JSONLoader,
    UnstructuredMarkdownLoader,
    UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredImageLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader,
    Docx2txtLoader,
    UnstructuredODTLoader,
    UnstructuredXMLLoader
)
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.recursive_url_loader import RecursiveUrlLoader


class UnsupportedFileTypeError(Exception):
    pass

class UnifiedDocumentLoader:
    def __init__(self, file_path):
        self.original_path = file_path
        self.file_path = self._resolve_path(file_path)
        self.loader = self._select_loader()
    
    def _resolve_path(self, file_path):
        """
        Resolve the file path to handle both relative and absolute paths.
        """
        try:
            # Convert to Path object
            path = Path(file_path)
            
            # If path is absolute and exists, use it
            if path.is_absolute() and path.exists():
                return str(path)

            # If the original path exists relative to current directory, use it
            if Path(self.original_path).exists():
                return str(Path(self.original_path).absolute())
            
            # Remove duplicate 'test' in path if present
            parts = path.parts
            if parts.count('test') > 1:
                # Remove duplicate 'test' occurrences
                new_parts = []
                test_found = False
                for part in parts:
                    if part == 'test' and not test_found:
                        new_parts.append(part)
                        test_found = True
                    elif part != 'test':
                        new_parts.append(part)
                path = Path(*new_parts)
            
            # Try with current working directory
            full_path = Path.cwd() / path
            if full_path.exists():
                return str(full_path.absolute())
            
            # If that doesn't work, try without 'test' prefix if it exists
            if 'test' in str(path):
                no_test_path = Path(*[p for p in path.parts if p != 'test'])
                full_path = Path.cwd() / no_test_path
                if full_path.exists():
                    return str(full_path.absolute())
            
            # If all attempts fail, raise an error
            raise FileNotFoundError(f"Could not find file: {file_path}")
            
        except Exception as e:
            raise FileNotFoundError(f"Error resolving path '{file_path}': {str(e)}")
    
    def _select_loader(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        _, file_extension = os.path.splitext(self.file_path)
        file_extension = file_extension.lower()

        if file_extension == '.txt':
            return TextLoader(self.file_path)
        elif file_extension == '.pdf':
            return PyPDFLoader(self.file_path)
        elif file_extension == '.csv':
            return CSVLoader(self.file_path)
        elif file_extension == '.html':
            return UnstructuredHTMLLoader(self.file_path)
        elif file_extension == '.json':
            return JSONLoader(self.file_path)
        elif file_extension == '.md':
            return UnstructuredMarkdownLoader(self.file_path)
        elif file_extension == '.eml':
            return UnstructuredEmailLoader(self.file_path)
        elif file_extension == '.epub':
            return UnstructuredEPubLoader(self.file_path)
        elif file_extension in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
            return UnstructuredImageLoader(self.file_path)
        elif file_extension == '.xls':
            return UnstructuredExcelLoader(self.file_path)
        elif file_extension == '.xlsx':
            return UnstructuredExcelLoader(self.file_path)
        elif file_extension == '.ppt':
            return UnstructuredPowerPointLoader(self.file_path)
        elif file_extension == '.pptx':
            return UnstructuredPowerPointLoader(self.file_path)
        elif file_extension == '.docx':
            return Docx2txtLoader(self.file_path)
        elif file_extension == '.odt':
            return UnstructuredODTLoader(self.file_path)
        elif file_extension == '.xml':
            return UnstructuredXMLLoader(self.file_path)
        else:
            raise UnsupportedFileTypeError(f"Unsupported file type: {file_extension}")

    def load(self):
        return self.loader.load()
    
class RecursiveUrlLoader:
    def __init__(self, url: str):
            """
            Initializes the RecursiveUrlLoaderWrapper with the given URL.
            
            Args:
            - url (str): The URL to load documents from recursively.
            """
            self.url = url
            self.loader = RecursiveUrlLoader(url=self.url)

    def load(self):
        """
        Loads the documents recursively from the provided URL.
        
        Returns:
        - List: A list of documents extracted from the URL.
        
        Raises:
        - Exception: If the loading fails.
        """
        try:
            # Load the documents using the RecursiveUrlLoader
            return self.loader.load()
        except Exception as e:
            raise ValueError(f"Failed to load documents from URL: {self.url}. Error: {str(e)}")
    

