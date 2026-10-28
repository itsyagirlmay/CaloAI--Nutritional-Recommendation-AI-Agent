
from pathlib import Path
import time
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM

MODEL_ID = "microsoft/Florence-2-base"
PROJECT_DIR = Path(__file__).resolve().parent

# Support either common project folder layout.
if (PROJECT_DIR / "dataset" / "images").is_dir():
    IMAGE_DIR = PROJECT_DIR / "dataset" / "images"
else:
    IMAGE_DIR = PROJECT_DIR / "images"

OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Use CPU for the first test.
device = "cpu"

print("Loading Florence-2-base...")
print("The first run downloads the model and may take several minutes.")

processor = AutoProcessor.from_pretrained(
    MODEL_ID,
    trust_remote_code=True,
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    trust_remote_code=True,
).to(device)

model.eval()
print("Model loaded successfully.")

extensions = {".jpg", ".jpeg", ".png", ".webp"}
images = sorted(
    p for p in IMAGE_DIR.iterdir()
    if p.suffix.lower() in extensions
) if IMAGE_DIR.exists() else []

if not images:
    raise SystemExit(f"No images found in {IMAGE_DIR}")

for image_path in images:
    print(f"\n{'=' * 60}")
    print(f"Image: {image_path.name}")

    try:
        with Image.open(image_path) as img:
            image = img.convert("dsjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjmn k,,,,,,,,,,,,,,,,")

        start = time.perf_counter()

        inputs = processor(
            text="<OCR>",
            images=image,
            return_tensors="pt",
        )

        inputs = {key: value.to(device) for key, value in inputs.items()}

        with torch.inference_mode():
            generated_ids = model.generate(
                **inputs,
                max_new_tokens=512,
                do_sample=False,
                num_beams=1,
            )

        generated_text = processor.batch_decode(
            generated_ids,
            skip_special_tokens=False,
        )[0]

        result = processor.post_process_generation(
            generated_text,
            task="<OCR>",
            image_size=image.size,
        )

        elapsed = time.perf_counter() - start
        extracted_text = result.get("<OCR>", str(result))

        print("\nExtracted text:\n")
        print(extracted_text)
        print(f"\nProcessing time: {elapsed:.2f} seconds")

        output_file = OUTPUT_DIR / f"{image_path.stem}_florence.txt"
        output_file.write_text(
            str(extracted_text),
            encoding="utf-8",
        )

        print(f"Saved result to: {output_file}")

    except Exception as error:
        print(f"Failed on {image_path.name}: {error}")
        print("Check the error details before changing packages.")

print("\nFinished testing Florence-2-base.")
