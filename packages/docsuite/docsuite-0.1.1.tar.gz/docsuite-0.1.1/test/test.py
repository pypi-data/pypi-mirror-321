import unittest
from docsuite import UnifiedDocumentLoader
from docsuite.loader import UnsupportedFileTypeError

class TestUnifiedDocumentLoader(unittest.TestCase):
    def setUp(self):
        """Set up test paths."""
        self.valid_pdf_path = "test/pdf/artificial_intelligence_tutorial.pdf"
        self.invalid_path = "test/pdf/non_existent_file.pdf"

    def test_load_valid_pdf(self):
        """Test loading a valid PDF document."""
        loader = UnifiedDocumentLoader(self.valid_pdf_path)
        documents = loader.load()
        self.assertTrue(
            all(isinstance(doc.page_content, str) for doc in documents),
            "Each document should have its page content as a string."
        )

    def test_load_invalid_path(self):
        """Test loading a document from an invalid file path."""
        with self.assertRaises(ValueError) as context:
            loader = UnifiedDocumentLoader(self.invalid_path)
            loader.load()
        self.assertIn("is not a valid file or url", str(context.exception))

    def test_load_unsupported_extension(self):
        """Test loading a file with an unsupported extension."""
        unsupported_path = "test/file.xyz"
        with self.assertRaises(UnsupportedFileTypeError) as context:
            loader = UnifiedDocumentLoader(unsupported_path)
            loader.load()
        self.assertIn("Unsupported file type", str(context.exception))


if __name__ == "__main__":
    unittest.main()
