# OCR-PDF Project

## Overview

This project extracts text from PDF files using Tesseract Optical Character Recognition (OCR). It downloads a PDF from a given URL, converts each page into an image, and then extracts the text using Tesseract OCR then generates a summary. The project is deployed on [Replicate](https://replicate.com/vwtyler/ocr-pdf).

## Usage

You can use this model directly on Replicate:

[**Try it on Replicate**](https://replicate.com/vwtyler/ocr-pdf)

### Local Setup (Optional)

If you want to run the project locally:

1. **Install Dependencies:**

   ```bash
   pip install requests pdf2image pytesseract transformers cog
   ```

2. **Run the Predictor:**

   ```python
   from predict import Predictor
	import json

	# Instantiate the Predictor class
	predictor = Predictor()

	# Replace with the actual URL of your PDF
	json_output = predictor.predict(url="https://example.com/your-pdf.pdf")

	# Output the full JSON result
	print(json_output)

	# Optionally, parse the JSON to access specific fields
	result = json.loads(json_output)
	print("Summary:", result["summary"])
   ```

   This will download the PDF, convert it to images, extract the text, generate a summary, and return the results in JSON format.

## License

This project is licensed under the MIT License