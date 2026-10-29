CaloAI — requirements and design baseline
1. Project definition
Purpose: Build a Namibia-relevant calorie-tracking web application that reads nutritional information from a packaged food label image, lets the user verify the extracted values, calculates calories consumed, and maintains a daily total.

Primary user: A person who wants to track calories from packaged foods without manually transcribing every nutritional label.

Core outcome: Upload a label image → extract text using a Hugging Face model → verify nutritional values → enter the amount consumed → calculate calories → update the daily log.

Design principle: AI extracts the text; ordinary Python code validates data and performs arithmetic. The application must not rely on a language model to guess nutritional values.
2. Scope boundaries
Must have — MVP
- HTML/CSS interface with image upload.
- Hugging Face OCR or vision model for image-to-text extraction.
- Display and allow correction of extracted nutrition values.
- Parse calories, units and serving basis.
- Calculate calories from quantity consumed.
- Record food entries and show the daily calorie total.
- Validate input and handle OCR/API failures.
- Automated tests and documented setup instructions.
Supporting functionality
- Open Food Facts product lookup and cross-checking.
- Testing with real Namibian products.
- A small local dataset of up to two or three products missing from Open Food Facts, if necessary.
Future enhancements
- Barcode scanning as an alternative input route.
- User accounts, cloud synchronization and mobile deployment.
- Food recommendations, meal planning and broader dietary analytics.
- Model serving infrastructure for higher traffic.
For the 13-day deadline, we will prioritize the core workflow and only add enhancements once the end-to-end application works.
3. The README will be our project specification
Before uploading it, we need to make it clear which decisions are final and which still require testing. For example, Florence-2-base is a candidate model, not yet a proven choice. We should record the model evaluation criteria now and fill in the results after testing.

The README will include:
1. Project overview, problem statement, objectives and scope.
2. Stakeholders, assumptions and functional/non-functional requirements.
3. Acceptance criteria and test scenarios.
4. Software architecture and component responsibilities.
5. Data pipeline and activity diagram.
6. Data model and calorie calculation rules.
7. Hugging Face model selection and replacement strategy.
8. Open Food Facts integration and Namibia-specific evaluation.
9. Security, reliability and model risks, with justified mitigations.
10. SDLC plan, milestones and references.
I checked the GitHub repositories accessible through your connected account, and none of the returned repositories is a CaloAI repository. The available GitHub actions let me create files in an existing repository, but not create a new repository itself. I'll prepare the README first; then we can put it in the correct repository without accidentally modifying one of your other projects.
CaloAI
A Namibia-focused calorie tracking proof of concept using image-to-text extraction and nutritional data.

Project status: Requirements and design phase
Development approach: Iterative SDLC
Target platform: Local web application
Primary technologies: Python, Flask, HTML, CSS, Hugging Face Transformers, Open Food Facts and SQLite
1. Project Overview
CaloAI is a calorie-tracking proof of concept designed to help users record calories consumed from packaged foods. The application will accept an image of a food product's nutritional label, extract its text using a pretrained Hugging Face model, identify the relevant nutritional values, and calculate calories based on the quantity consumed.

The application will maintain a daily food log and calculate the running calorie total.

The project will prioritize products available in Namibia. Open Food Facts will provide a supporting source of product and nutritional information, while image-based extraction will allow the application to process labels for products that are not listed in the database.

The initial implementation will run locally to minimize cost and deployment complexity.
2. Problem Statement
Manually recording food intake requires users to read nutritional labels, identify calorie values, calculate the quantity consumed and maintain a record of their daily intake.

This process can be time-consuming and susceptible to transcription and calculation errors. Products available in Namibia may also be missing from online nutritional databases.

CaloAI aims to simplify this process by combining image-to-text extraction, deterministic nutritional calculations and daily food logging in a single application.
3. Project Objectives
1. Develop a web interface for uploading nutritional-label images.
2. Integrate a suitable pretrained Hugging Face model for image-to-text extraction.
3. Extract and validate calorie values, units and serving information.
4. Calculate calories consumed using user-confirmed nutritional values and quantities.
5. Maintain a daily food log and display the running calorie total.
6. Integrate Open Food Facts as a supporting product-data source.
7. Evaluate the system using real packaged-food labels, including Namibian products.
8. Document model selection, limitations, risks and the impact of replacing the model.
4. Scope
4.1 Minimum Viable Product
The following requirements define the initial release.
- Accept an uploaded nutritional-label image.
- Process the image using a pretrained image-to-text model.
- Display the extracted text for inspection.
- Identify nutritional energy values and their associated units and serving basis.
- Allow users to correct extracted values before calculation.
- Accept the quantity consumed.
- Calculate calories consumed.
- Save food entries against a date.
- Display the daily calorie total.
- Handle invalid input, unreadable images, missing values and processing failures.
- Provide automated tests and reproducible setup instructions.
4.2 Supporting functionality
- Retrieve product information from Open Food Facts.
- Cross-check available product information against extracted label values.
- Evaluate the application using Namibian packaged foods.
- Maintain a small local test dataset for up to three Namibian products missing from Open Food Facts, where necessary.
4.3 Out of scope
The initial release will not include:
- Personalized meal plans or dietary recommendations.
- Medical or nutritional diagnosis.
- Automatic estimation of calories from photographs of entire meals.
- User accounts or cloud synchronization.
- A native mobile application.
- Custom model training or fine-tuning.
- Production-scale model serving.
- Mandatory barcode recognition as the primary input route.
These features may be considered in future iterations if time and project requirements permit.
5. Stakeholders and Users
Primary user
An individual who wants to record calorie intake from packaged foods.
Project developer
Responsible for requirements analysis, implementation, testing, documentation and evaluation.
Academic supervisor
Provides feedback on the project scope, technical decisions, evaluation methodology and final deliverables.
6. Functional Requirements
ID	Requirement	Priority
FR-01	The system shall accept an image of a nutritional label in a supported image format.	Must
FR-02	The system shall validate uploaded files before processing.	Must
FR-03	The system shall extract text from the image using a pretrained Hugging Face model.	Must
FR-04	The system shall display the extracted text to the user.	Must
FR-05	The system shall identify candidate calorie values, units and serving bases.	Must
FR-06	The system shall allow the user to review and correct extracted nutritional values.	Must
FR-07	The system shall accept the quantity consumed in a supported unit.	Must
FR-08	The system shall calculate calories using validated nutritional values and quantities.	Must
FR-09	The system shall record confirmed food entries against a date.	Must
FR-10	The system shall calculate and display the total calories recorded for the selected day.	Must
FR-11	The system shall handle unreadable images, missing nutritional values and invalid input without producing an unverified calorie entry.	Must
FR-12	The system should retrieve product information from Open Food Facts when a reliable product identifier or search input is available.	Supporting
FR-13	The system should compare available database information with extracted nutritional values and indicate discrepancies.	Supporting
FR-14	The system may support manual product entry when a product is unavailable in Open Food Facts.	Supporting


7. Non-Functional Requirements
ID	Requirement	Verification
NFR-01	Cost	Core functionality must run locally without requiring paid inference or hosting services.
NFR-02	Accuracy	Critical nutritional values must be evaluated against manually verified label values.
NFR-03	Reliability	Invalid or incomplete nutritional data must not silently enter the daily total.
NFR-04	Maintainability	OCR, parsing, product lookup, calculations and storage must be separated into distinct components.
NFR-05	Usability	The interface must clearly communicate extraction results, validation errors and daily totals.
NFR-06	Performance	Model inference time and resource usage must be measured on the available laptop.
NFR-07	Reproducibility	Dependencies, configuration and setup instructions must be documented.
NFR-08	Security	Uploaded files must be validated, file sizes limited and temporary files handled safely.
NFR-09	Testability	Calculation, parsing, database and integration behaviour must be testable independently.


8. Proposed Technology Stack
Layer	Technology	Purpose
Frontend	HTML	Image upload, nutritional form and daily log
Styling	CSS	Layout and visual presentation
Backend	Python and Flask	Request handling and application logic
OCR	Hugging Face Transformers	Image-to-text extraction
Initial model candidate	Florence-2-base	Evaluation for complete nutrition-label images
Alternative candidate	TrOCR-small-printed	Evaluation for cropped printed-text lines
Supporting data	Open Food Facts API	Product and nutritional information
Data storage	SQLite	Food entries and daily records
Image processing	Pillow	Image loading and preprocessing
Testing	pytest	Unit and integration tests
Version control	Git and GitHub	Source control and project documentation


The final OCR model will be selected after evaluation. Model suitability must be established through observed results rather than assumed from the model name or parameter count.

The initial execution target is local CPU inference. GPU acceleration may be investigated if measurements justify it.
9. Software Architecture
CaloAI will use a modular, layered architecture.
flowchart TD
    U[User] --> UI[HTML and CSS Interface]
    UI --> APP[Flask Application]
    APP --> VALIDATE[Upload Validation]
    VALIDATE --> OCR[OCR Service Interface]
    OCR --> MODEL[Hugging Face Model]
    MODEL --> PARSER[Nutrition Parser]
    PARSER --> REVIEW[User Review and Correction]
    REVIEW --> CALC[Calorie Calculation Service]
    CALC --> DB[(SQLite Database)]
    DB --> LOG[Daily Calorie Summary]
    LOG --> UI
    APP -. Optional lookup .-> OFF[Open Food Facts API]
    OFF --> REVIEW
Component responsibilities
Frontend
- Accept images.
- Display OCR output and candidate nutritional values.
- Collect corrected values and consumed quantities.
- Display food entries, daily totals and validation messages.
Flask application
- Receive requests.
- Validate inputs.
- Coordinate OCR, parsing, product lookup and calculations.
- Return results to the interface.
OCR service
- Load and execute the selected model.
- Receive an image and return extracted text.
- Isolate model-specific code from the rest of the application.
Nutrition parser
- Identify candidate numerical values and associated units.
- Determine whether a value refers to 100 g, 100 ml or a serving.
- Reject ambiguous or incomplete nutritional information.
Calorie calculation service
- Validate quantities and units.
- Normalize energy measurements.
- Calculate calories using deterministic formulas.
Database layer
- Store confirmed food entries.
- Store dates, quantities and nutritional values used for calculations.
- Support daily totals and retrieval of previously recorded entries.
Open Food Facts service
- Retrieve available product data.
- Provide supporting information for product identification and cross-checking.
- Handle unavailable products and API failures independently of OCR.
10. Data Pipeline
The primary data pipeline is:
1. Image input: The user uploads a nutritional-label image.
2. Validation: The backend checks file type, size and image readability.
3. Preprocessing: The image is loaded and optionally resized or otherwise prepared for the model.
4. OCR inference: The Hugging Face model extracts text from the image.
5. Text inspection: The application retains and displays the raw extracted text.
6. Nutrition parsing: The parser identifies candidate energy values, units and serving bases.
7. User verification: The user confirms or corrects the candidate nutritional values.
8. Quantity input: The user enters the amount consumed.
9. Calculation: The calorie service validates units and calculates the estimated energy consumed.
10. Persistence: The confirmed food entry and calculation inputs are saved in SQLite.
11. Daily aggregation: The application sums the entries recorded for the selected date.
12. Presentation: The interface displays the entry and updated daily total.
Open Food Facts is a supporting branch of the pipeline. Its results may be used to identify products or cross-check nutritional information, but an unavailable API must not prevent the primary image-based workflow from operating.
11. Activity Diagram
flowchart TD
    A([Start]) --> B[Upload nutrition label]
    B --> C{Valid image?}
    C -- No --> D[Display validation error]
    D --> B
    C -- Yes --> E[Extract text using OCR model]
    E --> F{Readable text?}
    F -- No --> G[Request clearer image]
    G --> B
    F -- Yes --> H[Parse candidate nutrition values]
    H --> I{Calories and serving basis clear?}
    I -- No --> J[Request manual correction]
    I -- Yes --> K[Display candidate values]
    J --> K
    K --> L[User verifies values]
    L --> M[Enter quantity consumed]
    M --> N{Quantity and units valid?}
    N -- No --> O[Display input error]
    O --> M
    N -- Yes --> P[Calculate calories]
    P --> Q[Save food entry]
    Q --> R[Update daily total]
    R --> S[Display entry and total]
    S --> T([End])
12. Calorie Calculation Rules
Calculations must use validated nutritional values and compatible units.
Calories per 100 grams
If a label specifies calories per 100 g:

\frac{\text{kcal per 100 g}\times\text{grams consumed}}{100}
]

Example:
- Label value: 380 kcal per 100 g.
- Quantity consumed: 45 g.
- Estimated calories: 171 kcal.
Calories per serving
If a label specifies 90 kcal per 30 g serving and the user consumes 60 g:
90\times\frac{60}{30}
180\text{ kcal}
]
Kilojoule conversion
When the source uses kilojoules:

[
\text{kcal}=\frac{\text{kJ}}{4.184}
]

The conversion should only be performed after establishing the correct quantity and serving basis.
Calculation safeguards
- Do not assume every value is per 100 g.
- Do not treat millilitres and grams as interchangeable without a valid conversion.
- Reject missing or ambiguous serving bases.
- Validate positive quantities and supported units.
- Keep unconfirmed values out of the daily total.
- Retain the values and units used for each calculation so results can be audited.
13. Proposed Data Model
The initial database will contain a food-entry table.
Field	Purpose
entry_id	Unique identifier for the entry
product_name	User-confirmed product name, if available
date_consumed	Date associated with the entry
raw_ocr_text	Extracted text retained for troubleshooting and evaluation
energy_value	Confirmed numerical nutritional value
energy_unit	kcal or kJ
nutrition_basis	Per 100 g, per 100 ml or per serving
basis_quantity	Quantity associated with the nutrition value
consumed_quantity	Amount consumed
consumed_unit	g, ml or a supported serving unit
calculated_kcal	Calculated energy consumed
source	OCR/manual entry/Open Food Facts
created_at	Entry creation timestamp


The exact schema may be adjusted during detailed design. Daily totals will initially be calculated by summing the confirmed entries for the selected date.
14. Hugging Face Model Selection
Initial candidates
Florence-2-base

Candidate for evaluating full nutrition-label images. Its vision capabilities make it worth testing, but its accuracy on the project's particular labels has not yet been established.

Model card: https://huggingface.co/microsoft/Florence-2-base

TrOCR-small-printed

Alternative for cropped printed-text lines. Its intended recognition workflow may require preprocessing and line cropping for complete nutrition labels.

Model card: https://huggingface.co/microsoft/trocr-small-printed
Evaluation criteria
The selected model must be evaluated against the same manually verified image set.

Evaluation will measure:
- Exact transcription of critical numerical values.
- Correct extraction of calorie values.
- Correct identification of units and serving bases.
- Frequency of missing or ambiguous outputs.
- Inference time on the target laptop.
- Approximate memory requirements.
- Compatibility with the intended local environment.
- License compatibility with the project's intended use.
The evaluation dataset should include clear labels, small text, angled images, glare and a sample of Namibian products.

Model selection will prioritize reliable extraction of nutritional values rather than general text transcription alone.
15. Model Replacement and Scalability
The application will depend on an OCR service interface rather than directly on one specific model implementation.
class OCRService:
    def extract_text(self, image_path: str) -> str:
        raise NotImplementedError
Concrete model implementations will provide the extraction functionality.

This separation allows the OCR model to change without requiring a redesign of the frontend, nutrition parser, calorie calculations or database.
Model replacement procedure
1. Identify a replacement candidate.
2. Review its intended task, license and resource requirements.
3. Run it against the existing evaluation images.
4. Compare critical-field accuracy and failure rates.
5. Measure inference time and memory usage.
6. Run regression tests against the current implementation.
7. Adopt the replacement only if it meets the acceptance criteria.
8. Document the model version and the reason for the change.
Future scaling
If the project grows, the OCR component could be isolated behind a dedicated inference service. This would allow model inference to scale independently of the web application.

For the initial release, a separate model-serving service is unnecessary overhead. The modular local implementation is sufficient to demonstrate the architecture and replacement strategy.
16. Risk Register
Risk	Potential impact	Mitigation
OCR misreads numerical values	Incorrect calorie totals	Display extracted text, require confirmation and validate critical fields
Serving basis is ambiguous	Incorrect quantity calculations	Require a verified serving basis before calculation
Poor image quality	Missing or inaccurate extraction	Validate image readability and request a clearer image
Open Food Facts record is missing or outdated	Incorrect or unavailable cross-check	Preserve image-based entry and allow manual correction
API is unavailable	Product lookup fails	Keep the OCR and manual-entry workflow independent of the API
Model is too resource-intensive	Slow inference or memory exhaustion	Benchmark locally and evaluate smaller alternatives
Replacement model reduces accuracy	Regressions in nutritional extraction	Maintain a fixed evaluation set and rerun regression tests
Malicious or invalid upload	Application instability or unsafe file handling	Validate file types, limit size and avoid trusting user-supplied filenames
Sensitive information is logged	Unnecessary privacy exposure	Minimize logs and process images locally by default
Dependency incompatibility	Setup failures	Use a virtual environment and document tested dependency versions


Justification for the mitigations
The primary safety concern is that OCR errors can become calculation errors. Displaying and validating critical values provides an opportunity to catch these errors before they affect the daily total.

Separating OCR from deterministic calculations reduces the risk of model output being treated as verified nutritional data. Independent API handling prevents a third-party service failure from disabling the core application.

Regression testing provides evidence that a model replacement improves or preserves performance rather than relying on the assumption that a newer model is better.
17. Acceptance Criteria
The MVP will be considered ready for demonstration when the following criteria have been verified.
- A valid nutrition-label image can be uploaded.
- The selected model produces inspectable text output.
- The application identifies a supported calorie value and its nutritional basis.
- The user can correct extracted values.
- A valid quantity produces the expected calorie calculation.
- Confirmed entries can be stored and retrieved.
- The daily total matches the sum of the stored entries.
- Invalid quantities and ambiguous nutritional data are handled safely.
- Missing Open Food Facts records do not prevent manual label processing.
- Automated tests cover calculation logic, parsing and critical failure cases.
- Setup instructions reproduce the application in a clean environment.
- Model evaluation results and known limitations are documented.
18. Testing Strategy
Unit testing
Test calorie formulas, unit conversions, nutritional parsing and input validation independently.
Integration testing
Test the interaction between image preprocessing, OCR, parsing, calculations and database storage.
API testing
Test valid product lookups, missing products, incomplete responses and network failures.
End-to-end testing
Complete the full workflow from image upload to the updated daily calorie total.
Model evaluation
Compare extracted critical values against manually verified ground truth. Report the number of test images, correct values, failures and limitations. Do not claim accuracy before testing.
19. SDLC and 13-Day Plan
Day	Phase	Deliverable
1	Requirements	Requirements baseline and acceptance criteria
2	Analysis and design	Architecture, diagrams and initial model evaluation
3	Interface	Flask application and image-upload page
4	OCR implementation	Image-to-text extraction
5	Data processing	Nutrition parsing and validation
6	Core logic	Calorie calculations
7	Storage	Daily food log and total
8	Integration	Open Food Facts lookup and cross-checking
9	Local evaluation	Test images, including Namibian products
10	Testing	Unit and integration tests
11	Evaluation	Model results and risk review
12	Documentation	README, setup instructions and project report
13	Release	Clean-start verification and demonstration


The plan is iterative. Critical defects and incomplete core requirements take priority over optional features.
20. Development Principles
- Keep the initial implementation small and testable.
- Prefer local execution and free resources.
- Do not train a model unless evidence shows it is necessary.
- Separate model inference from business logic.
- Never assume extracted nutritional values are correct.
- Record actual evaluation results instead of making unsupported accuracy claims.
- Keep Namibian product testing grounded in real packaging and verified information.
- Document changes to scope and model selection.
21. References
- Hugging Face model hub: https://huggingface.co/models
- Florence-2-base model card: https://huggingface.co/microsoft/Florence-2-base
- TrOCR-small-printed model card: https://huggingface.co/microsoft/trocr-small-printed
- Open Food Facts: https://world.openfoodfacts.org/
- Open Food Facts API documentation: https://openfoodfacts.github.io/documentation/
- Flask documentation: https://flask.palletsprojects.com/
- Python documentation: https://docs.python.org/3/
- SQLite documentation: https://www.sqlite.org/docs.html
The licenses and terms applicable to selected models, datasets, product records and images must be reviewed before reuse.
22. Current Project Status
Area	Status
Project problem and objectives	Drafted
MVP scope	Proposed
Functional requirements	Drafted
Non-functional requirements	Drafted
Software architecture	Proposed
Data pipeline	Proposed
Activity diagram	Proposed
Data model	Proposed
Model selection	Pending empirical evaluation
Risk analysis	Initial draft
Acceptance criteria	Drafted
Implementation	Not started
Model evaluation results	Not available
Supervisor review	Pending confirmation
