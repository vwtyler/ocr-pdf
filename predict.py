import requests
from io import BytesIO
from pdf2image import convert_from_bytes
import pytesseract
from cog import BasePredictor, Input

class Predictor(BasePredictor):
def setup(self):
        # Initialize the summarization pipeline
        self.summarizer = pipeline("summarization")

    def predict(self, url: str = Input(description="URL of the PDF to extract text from")) -> str:
        try:
            # Download and process the PDF
            pdf_file = self.download_pdf(url)
            images = self.pdf_to_images(pdf_file)
            text = self.ocr_images(images)

            # Generate a summary of the extracted text
            summary = self.generate_summary(text)

            # Create a structured JSON response
            result = {
                "url": url,
                "extracted_text": text,
                "summary": summary
            }
            
            return json.dumps(result, indent=4)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=4)

    def download_pdf(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return BytesIO(response.content)

    def pdf_to_images(self, pdf_file):
        return convert_from_bytes(pdf_file.read())

    def ocr_images(self, images):
        text = ""
        for i, image in enumerate(images):
            page_text = pytesseract.image_to_string(image)
            text += f"\n--- Page {i + 1} ---\n{page_text}"
        return text

    def generate_summary(self, text):
        # Generate a summary using the summarization model
        max_chunk_size = 1000
        text_chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
        summaries = [self.summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text'] for chunk in text_chunks]
        return " ".join(summaries)
