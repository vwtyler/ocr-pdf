# OCR-PDF Project

## Overview

This project extracts text from PDF files using Tesseract Optical Character Recognition (OCR). It downloads a PDF from a given URL, converts each page into an image, and then extracts the text using Tesseract OCR. The project is deployed on [Replicate](https://replicate.com/vwtyler/ocr-pdf).

## Usage

You can use this model directly on Replicate:

[**Try it on Replicate**](https://replicate.com/vwtyler/ocr-pdf)

### Local Setup (Optional)

If you want to run the project locally:

1. **Install Dependencies:**

   ```bash
   pip install requests pdf2image pytesseract cog
   ```

2. **Run the Predictor:**

   ```python
   from predictor import Predictor

   predictor = Predictor()
   text = predictor.predict(url="https://example.com/your-pdf.pdf")
   print(text)
   ```

   This will download the PDF, convert it to images, and extract the text.

## License

This project is licensed under the MIT License