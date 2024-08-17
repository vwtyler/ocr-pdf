import requests
from io import BytesIO
from pdf2image import convert_from_bytes
import pytesseract
from cog import BasePredictor, Input

class Predictor(BasePredictor):
    def predict(self, url: str = Input(description="URL of the PDF to extract text from")) -> str:
        try:
            pdf_file = self.download_pdf(url)
            images = self.pdf_to_images(pdf_file)
            text = self.ocr_images(images)
            return text
        except Exception as e:
            return f"An error occurred: {e}"

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
