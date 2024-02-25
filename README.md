# Text Extraction and Analysis

This project provides a command line app and a Flask web app for extracting and analyzing text from PDF or image files. The extracted text is processed to identify key-value pairs, which can be useful for various applications.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/abrhamgg/data_extraction
   ```

2. Navigate to the project directory:

   ```shell
   cd text-extraction
   ```

3. Create a virtual environment:

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Command Line App

The command line app allows you to extract and analyze text from PDF or image files. To use the command line app, follow these steps:

1. Open a terminal.

2. Navigate to the project directory.

3. Run the following command:

   ```shell
   python extract.py [file_path]
   ```

   Replace `[file_path]` with the path to the input file (PDF or image) that you want to analyze.

4. The app will extract the text from the file, analyze the key-value pairs, and save the analyzed text as a CSV file.

5. The CSV file will be saved in the same directory as the input file, with the same name and the `.csv` extension.

## Flask Web App

The Flask web app provides a user-friendly interface for uploading files and extracting key-value pairs. To use the web app, follow these steps:

1. Make sure you have activated the virtual environment.

2. Start the Flask development server:

   ```shell
   python app.py
   ```

3. Open a web browser and navigate to `http://localhost:5000`.

4. Click on the "Choose File" button and select the PDF or image file that you want to analyze.

5. Click the "Submit" button to upload the file and extract the key-value pairs.

6. The web app will display the extracted key-value pairs on the results page.

7. You can repeat the process to upload and analyze additional files.

## License

This project is licensed under the [MIT License](LICENSE).
