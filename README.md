# Data-set-processing

For Data set processing.py

Overview

This repository contains a Python script designed to validate task actions extracted from JSONL files. The script classifies tasks based on specific queries, extracts action sequences, and verifies them against predefined valid action sets.

Features

Task Classification: Identifies the task type based on query content.

Action Sequence Extraction: Parses responses to extract action sequences within <Action sequence modeling> tags.

Validation Against Defined Action Sets: Compares extracted actions with predefined valid action sets.

Error Handling: Manages JSON decode errors and provides detailed error messages.

Data Visualization: Displays validation results in a tabular format.

Installation

To run this script, ensure you have Python installed along with the following dependencies:

python script.py

The validation results will be displayed in a tabular format.

JSONL File Format (Example Data set 1. Safety_Assessment_Path_Planning_modified.json)

Each line in the JSONL file should follow this structure:

{
    "query": "<task description>",
    "response": "<action sequence modeling>",
    "images": ["<image_path>"]
}

Task Categories & Valid Actions

Cruise and Image Acquisition Missions

move forward

turn 'left' '90' degrees

turn 'right' '90' degrees

cross 'rock'

cross 'formation'

Sample Grab and Place Task

move to 'place'

grasp 'object'

release 'object' to container

cross 'rock'

cross 'formation'

Locate and Operate Tasks

move to 'place'

write 'char'

cross 'rock'

cross 'formation'


Output

The script generates a DataFrame containing:

image_id: Identifier for the task-related image.

task_type: The classified task type.

valid: Boolean indicating whether all actions are valid.

invalid_actions: List of invalid actions (if any).













For filter.py

Overview

This repository contains a Python script that processes a JSON file containing image-based questions and answers. The script allows users to interactively filter questions based on their content and write the filtered data to a new file.

Features

Interactive Question Filtering: Users can decide whether to retain each question.

Batch Processing: Handles large JSONL datasets efficiently.

Automatic Translation Support (Commented Out): Includes an optional translation function using LangChain (currently disabled).

Progress Bar: Utilizes tqdm to display progress while processing.

Installation

Ensure you have Python installed and install the required dependencies:

pip install tqdm

Usage

Update the input_file and output_file paths in the script.

Run the script:

python script.py

The script will prompt you to decide whether to keep each question. Press:

y (or Enter) to keep

n to discard

JSONL File Format(Example Data set 1. Safety_Assessment_Path_Planning_modified.json)

Each line in the JSONL file should follow this structure:

{
    "img_id": "<image identifier>",
    "qa": [
        {
            "question": "<question text>",
            "answer": "<answer text>"
        }
    ]
}


Output Format

The script generates a new JSONL file with filtered content, retaining only selected questions:

{
    "img_id": "<image identifier>",
    "qa": [
        {
            "question": "<filtered question>",
            "answer": "<corresponding answer>"
        }
    ]
}













