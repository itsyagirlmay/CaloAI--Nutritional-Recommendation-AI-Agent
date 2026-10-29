# CaloAI

CaloAI is a calorie-tracking proof of concept designed to help users record the nutritional information of food and drinks by taking pictures of nutrition labels. The project focuses on using AI-based text extraction and the Open Food Facts database to make nutrition information easier to capture and use.

The project will initially focus on packaged food and drinks, with an emphasis on testing the system using products available in Namibia.

## Project Objectives

- Extract text from photographs of nutrition labels using Florence-2-base.
- Retrieve existing product and nutrition information from the Open Food Facts database where available.
- Allow users to review and correct extracted nutritional values before saving them.
- Calculate calories based on the selected quantity or serving size.
- Record consumed products and display a running daily calorie total.
- Evaluate the accuracy and limitations of AI-based text extraction on nutrition labels from Namibian products.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Florence-2-base | AI model for image-to-text extraction |
| Hugging Face Transformers | Loading and running the AI model |
| Open Food Facts API | Retrieving existing product and nutrition information |
| Pillow | Loading and processing images |
| SQLite | Planned local storage for meal logs and daily totals |
| HTML and CSS | Planned user interface |

The interface and database components are planned parts of the application and are not yet confirmed as fully implemented.

## How It Will Work

The intended workflow is:

1. **Capture an image:** The user uploads or takes a photograph of a product's nutrition label.
2. **Extract text:** Florence-2-base processes the image and attempts to recognise the printed text.
3. **Find product information:** CaloAI uses the Open Food Facts API to search for matching product information when possible.
4. **Review the information:** The user checks the extracted or retrieved values and corrects mistakes before confirming them.
5. **Calculate calories:** The application calculates the calories for the amount consumed, using the correct serving basis and energy unit.
6. **Record consumption:** The confirmed entry is saved and included in the user's daily calorie total.

If a product is not available through Open Food Facts, the application will need to rely on information extracted from its label and verified by the user.

## AI Model Selection

### Florence-2-base

Florence-2-base, developed by Microsoft and available through Hugging Face, is the selected model for the initial image-to-text implementation.

It was selected for its ability to perform optical character recognition (OCR), its relatively compact model size compared with larger vision-language models, and the possibility of running it locally.

The model is being evaluated for its ability to recognise small printed text, numbers, energy units, and serving information on nutrition labels.

**Initial testing status:** The model loaded successfully and processed the available product images. However, the initial results contained significant recognition errors on nutrition panels. Further testing, image preprocessing, and accuracy evaluation are required before the extracted information can be used reliably.

The model's selection does not imply that its accuracy has already been proven suitable for nutrition-label extraction.

## Open Food Facts Integration

Open Food Facts is a collaborative food-product database that provides product information, including ingredients and nutritional values where available.

CaloAI will use its API to look up products and retrieve existing nutrition information. This complements Florence-2-base: the model extracts information from images, while Open Food Facts can provide an alternative or additional source of product data.

Product matching and data completeness will need to be evaluated, particularly for Namibian products that may not be listed in the database.

Open Food Facts data availability and licensing requirements must be considered when using and redistributing its data.

Project resource: https://world.openfoodfacts.org/

API documentation: https://openfoodfacts.github.io/openfoodfacts-server/api/

## Current Development Status

The project is under active development.

- [x] Set up a Python virtual environment.
- [x] Install the initial model dependencies.
- [x] Load Florence-2-base from Hugging Face.
- [x] Run initial image-to-text tests on product photographs.
- [x] Save extracted text to output files.
- [ ] Improve and evaluate nutrition-label text extraction.
- [ ] Establish manually verified ground-truth text and nutrition values.
- [ ] Integrate the Open Food Facts API.
- [ ] Implement product matching and nutrition-data handling.
- [ ] Implement user review and correction of nutrition values.
- [ ] Implement calorie calculations and daily meal logging.
- [ ] Develop and connect the user interface.
- [ ] Test the complete workflow using packaged products available in Namibia.

## Testing and Evaluation

The initial dataset contains photographs of product fronts and nutrition-label sections from selected Namibian products, including milk, drinking yoghurt, and juice.

The model will be evaluated against manually verified label information. Evaluation will consider:

- Text recognition accuracy.
- Correct extraction of energy values and units, such as kcal and kJ.
- Correct interpretation of serving sizes and per-100 g or per-100 ml values.
- Processing time per image.
- Performance on clear, blurry, small, or difficult-to-read labels.

Extracted values will be checked against the original packaging. Incorrect or uncertain results must not be treated as verified nutritional information.

The initial dataset is small and will need to be expanded before drawing conclusions about overall model accuracy.

## Hardware and Development Environment

Initial development and testing are being performed on a Windows 11 laptop with the following specifications:

- Python 3.13.3
- PyTorch CPU build
- 12 GB RAM
- Intel Core i7-11390H processor
- NVIDIA GeForce MX450 graphics card with 2 GB VRAM

The initial implementation runs the model on the CPU. Performance and memory requirements will be monitored as development continues.

## Limitations

- Florence-2-base has not yet demonstrated reliable extraction of the nutrition labels tested.
- Open Food Facts may not contain every product or have complete nutritional information.
- Product matching can fail when product names, packaging, or database records differ.
- Nutrition values extracted from images may contain recognition errors and require user verification.
- The initial product dataset is too small to establish general accuracy.

## Future Improvements

Potential improvements include better image cropping and preprocessing, more representative nutrition-label photographs, additional model benchmarking, improved product matching, and more comprehensive validation of nutritional values.

Future work may also include more detailed nutritional tracking and support for a wider range of packaged products.

## Project Goal

The goal of CaloAI is to demonstrate a practical approach to combining image-to-text extraction with an existing food-product database to support calorie tracking. The proof of concept will prioritise a working end-to-end workflow, transparent evaluation, and user verification of nutritional information.
