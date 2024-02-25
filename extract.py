import argparse
import pytesseract
from pdf2image import convert_from_path
import csv
import re
from PIL import Image
import os


def extract_text_from_pdf_images(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path)

    text = ""
    # Extract text from each image using OCR
    for img in images:
        text += pytesseract.image_to_string(img)

    return text


def save_text_to_csv(text, csv_file):
    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write each key-value pair as a row in the CSV file
        for key, value in text.items():
            csv_writer.writerow([key, value])


def extract_key_value_pairs(text):
    key_value_pairs = {}
    current_key = None
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line:
            # Check if the line ends with a colon, indicating a key
            if line.endswith(':'):
                current_key = line[:-1].strip()
            else:
                # If not a key, assume it's part of the value
                # Append to the value of the current key
                if current_key:
                    key_value_pairs[current_key] = key_value_pairs.get(
                        current_key, "") + " " + line.strip()
    return key_value_pairs


def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(img)
    return text


def analyze_key_value_pairs(text):
    """
    Analyzes key-value pairs from a string.

    Args:
      text: The string to analyze.

    Returns:
      A dictionary containing the key-value pairs found in the text.
    """

    # Define a regular expression to match key-value pairs.
    pattern = r"(?P<key>\w+)\s*:\s*(?P<value>.*)"

    # Use the regular expression to find all key-value pairs in the text.
    matches = re.findall(pattern, text)

    # Create a dictionary to store the key-value pairs.
    key_value_pairs = {}
    for match in matches:
        key, value = match
        key_value_pairs[key] = value

    return key_value_pairs


def main():
    parser = argparse.ArgumentParser(
        description='Extract and analyze text from PDF or image files.')
    parser.add_argument('file_path', type=str,
                        help='Path to the input file (PDF or image).')

    args = parser.parse_args()
    file_path = args.file_path

    # Extract text based on file type
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf_images(file_path)
    elif file_path.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        text = extract_text_from_image(file_path)
    else:
        print("Unsupported file format. Please provide a PDF or image file.")
        return

    # Analyze key-value pairs in the extracted text
    analyzed_text = analyze_key_value_pairs(text)

    # Save the analyzed text as a CSV file
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    csv_file = file_name + '.csv'
    save_text_to_csv(analyzed_text, csv_file)

    print(f"Text extracted and saved to {csv_file}.")


if __name__ == '__main__':
    main()
