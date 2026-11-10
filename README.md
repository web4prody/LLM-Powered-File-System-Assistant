# LLM-Powered File System Assistant

## Project Overview

The **LLM-Powered File System Assistant** is a Python project that demonstrates how a Large Language Model (LLM) can use structured tools to interact with files.

The application allows a user to enter natural-language requests such as:

- "Read all resumes in the resumes folder"
- "Find all resumes mentioning Python experience"
- "Read resumes/sarah.pdf and summarize the candidate"
- "Create a summary of resumes/sarah.pdf and save it as output/sarah_summary.txt"

The LLM understands the user's request, selects the appropriate Python tool, executes the tool through the application, receives the result, and produces a final natural-language response.

The project supports resume files in **TXT, PDF, and DOCX** formats.

---

## Learning Objectives

This project demonstrates:

- LLM function calling and tool use
- Structured tool interfaces
- File input/output operations using Python
- Reading TXT, PDF, and DOCX documents
- Searching inside documents
- File metadata handling
- Error handling
- LLM integration using OpenRouter
- Multi-step LLM tool execution

---

## Features

The application provides four core file-system tools:

1. `read_file()`
2. `list_files()`
3. `write_file()`
4. `search_in_file()`

The LLM can decide which tool or combination of tools should be used depending on the user's request.

---

## Core File System Tools

### 1. read_file(filepath)

Reads the contents of a file.

Supported file formats:

- `.txt`
- `.pdf`
- `.docx`

The function returns:

- Success/failure status
- Extracted text content
- File name
- File extension
- File size
- Modified date

Example:

```python
read_file("resumes/john.txt")
```

---

### 2. list_files(directory, extension=None)

Lists files available inside a directory.

It can also optionally filter files by extension.

Example:

```python
list_files("resumes")
```

Example with extension filtering:

```python
list_files("resumes", ".pdf")
```

The function returns file information including:

- File name
- File path
- Extension
- File size
- Modified date

---

### 3. write_file(filepath, content)

Writes text content to a file.

If the destination directory does not exist, the function creates it automatically.

Example:

```python
write_file(
    "output/summary.txt",
    "Candidate summary goes here."
)
```

The function returns a success or failure status.

---

### 4. search_in_file(filepath, keyword)

Searches for a keyword inside a TXT, PDF, or DOCX file.

The search is case-insensitive.

For example, searching for:

```text
python
```

can also match:

```text
Python
PYTHON
```

The function returns:

- Success/failure status
- Keyword
- Number of matches
- Matching lines
- Line numbers
- Surrounding context

Example:

```python
search_in_file(
    "resumes/john.txt",
    "Python"
)
```

---

## Project Structure

```text
LLM-Powered File System Assistant/
│
├── fs_tools.py
├── test_fs_tools.py
├── llm_file_assistant.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── resumes/
│   ├── john.txt
│   ├── priya.txt
│   ├── rahul.txt
│   ├── emily.docx
│   ├── david.docx
│   ├── sarah.pdf
│   └── alex.pdf
│
└── output/
```

> `.env` and `.venv` should not be committed to GitHub.

---

## Sample Resume Data

The `resumes` directory contains dummy resume files for testing.

The sample files use different document formats:

| Candidate | File | Format |
|---|---|---|
| John | john.txt | TXT |
| Priya | priya.txt | TXT |
| Rahul | rahul.txt | TXT |
| Emily | emily.docx | DOCX |
| David | david.docx | DOCX |
| Sarah | sarah.pdf | PDF |
| Alex | alex.pdf | PDF |

The sample data is used only to demonstrate the file-system and LLM tool-calling functionality.

---

## Technologies Used

- Python
- OpenRouter
- OpenAI Python SDK
- PyPDF
- python-docx
- python-dotenv

---

## Requirements

The project requires Python 3.

The required Python packages are listed in `requirements.txt`:

```text
openai
python-dotenv
pypdf
python-docx
```

---

## Installation

### Step 1: Clone or Download the Project

Open the project folder in VS Code or another Python IDE.

---

### Step 2: Create a Virtual Environment

Run:

```bash
python -m venv .venv
```

---

### Step 3: Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

After activation, the terminal should display:

```text
(.venv)
```

---

### Step 4: Install Dependencies

Run:

```bash
python -m pip install -r requirements.txt
```

This installs all Python packages required by the project.

---

## OpenRouter Configuration

This project uses OpenRouter to communicate with an LLM.

Create an OpenRouter API key.

Then create a file named:

```text
.env
```

in the main project directory.

Add:

```text
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Replace:

```text
your_openrouter_api_key_here
```

with your actual OpenRouter API key.

### Important

Never upload the `.env` file or your API key to GitHub.

The `.gitignore` file should contain:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

## Running the File System Tests

The core file-system tools can be tested using:

```bash
python test_fs_tools.py
```

The test file verifies operations such as:

- Listing resume files
- Reading TXT files
- Reading DOCX files
- Reading PDF files
- Searching inside files
- Writing output files

---

## Running the LLM File Assistant

Run:

```bash
python llm_file_assistant.py
```

The application will display:

```text
You:
```

Enter a natural-language request.

---

## Example 1: List Resume Files

Enter:

```text
List all files in the resumes folder
```

The LLM can select the `list_files` tool and return the available resume files.

---

## Example 2: Read a Resume

Enter:

```text
Read resumes/john.txt and tell me about the candidate
```

The LLM selects the `read_file` tool, reads the resume, and provides a natural-language response.

---

## Example 3: Search Resumes

Enter:

```text
Find all resumes mentioning Python experience
```

The LLM can perform multiple tool calls.

For example:

```text
User Request
     |
     v
list_files()
     |
     v
Find available resumes
     |
     v
search_in_file()
     |
     v
Search relevant resume files
     |
     v
LLM combines results
     |
     v
Final Answer
```

The assistant searches TXT, PDF, and DOCX resumes and reports the matching candidates.

---

## Example 4: Read a PDF Resume

Enter:

```text
Read resumes/sarah.pdf and summarize the candidate
```

The assistant uses `read_file()` to extract text from the PDF and then generates a summary.

---

## Example 5: Read a DOCX Resume

Enter:

```text
Read resumes/emily.docx and summarize the candidate
```

The assistant uses `read_file()` to extract the text from the DOCX document and provides a summary.

---

## Example 6: Create a Summary File

Enter:

```text
Create a summary of resumes/sarah.pdf and save it as output/sarah_summary.txt
```

The expected workflow is:

```text
User Request
     |
     v
read_file()
     |
     v
Resume Content
     |
     v
LLM Generates Summary
     |
     v
write_file()
     |
     v
output/sarah_summary.txt
```

This demonstrates multi-step LLM tool calling.

---

## How LLM Tool Calling Works

The LLM does not directly access files on the computer.

Instead, Python provides structured tool definitions to the LLM.

The available tools are:

```text
read_file
list_files
write_file
search_in_file
```

For example, if the user asks:

```text
Find all resumes mentioning Python experience
```

the LLM may first request:

```text
list_files
```

Python executes the function and sends the result back to the LLM.

The LLM can then request:

```text
search_in_file
```

for the relevant resume files.

The tool results are returned to the LLM, which uses them to generate the final response.

---

## Application Workflow

```text
User
 |
 | Natural-language request
 v
LLM
 |
 | Selects appropriate tool
 v
llm_file_assistant.py
 |
 | Executes function
 v
fs_tools.py
 |
 | Reads / Lists / Searches / Writes
 v
Local Files
 |
 | Tool result
 v
LLM
 |
 | More tools if required
 v
Final Answer
```

The tool-calling loop allows the LLM to perform multiple operations before producing its final response.

---

## Error Handling

The application handles common errors gracefully.

Examples include:

- File not found
- Unsupported file type
- Invalid directory
- File read/write errors
- Missing OpenRouter API key
- Unknown tool requests

Instead of crashing unexpectedly, the file-system tools return structured error information where appropriate.

---

## Supported File Types

| File Type | Extension | Supported |
|---|---|---|
| Text | `.txt` | Yes |
| PDF | `.pdf` | Yes |
| Microsoft Word | `.docx` | Yes |

PDF text extraction is performed using PyPDF.

DOCX text extraction is performed using python-docx.

---

## Security

The OpenRouter API key is stored in the `.env` file.

The `.env` file is excluded from Git using `.gitignore`.

API keys should never be hardcoded directly inside Python source files or committed to GitHub.

---

## Deliverables

This project contains:

- Python source code
- `fs_tools.py`
- `llm_file_assistant.py`
- File-system tests
- `requirements.txt`
- Sample dummy resume files
- TXT, PDF, and DOCX examples
- `README.md`
- LLM tool-calling implementation
- Multi-step tool execution support

---

## Conclusion

This project demonstrates how a Large Language Model can interact with a local file system through structured Python tools.

The assistant can understand natural-language requests and dynamically choose tools for reading, listing, searching, and writing files.

It demonstrates the core concepts of LLM function calling, structured tool interfaces, document parsing, file I/O, error handling, and multi-step LLM workflows.




