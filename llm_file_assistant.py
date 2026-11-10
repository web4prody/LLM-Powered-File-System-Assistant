import os
import json

from dotenv import load_dotenv
from openai import OpenAI


from fs_tools import (
    read_file,
    list_files,
    write_file,
    search_in_file
)


load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")


if not api_key:
    raise ValueError("OPENROUTER_API_KEY was not found. Check your .env file.")


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)



tools = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the content of a PDF, TXT, or DOCX file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "Path of the file to read"
                    }
                },
                "required": ["filepath"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List files inside a directory. Can optionally filter files by extension.",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "Directory containing the files"
                    },
                    "extension": {
                        "type": "string",
                        "description": "Optional file extension such as .pdf, .txt, or .docx"
                    }
                },
                "required": ["directory"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write text content to a file and create directories if necessary.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "Path where the file should be created"
                    },
                    "content": {
                        "type": "string",
                        "description": "Text content to write into the file"
                    }
                },
                "required": ["filepath", "content"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "search_in_file",
            "description": "Search for a keyword inside a PDF, TXT, or DOCX file. The search is case-insensitive.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "Path of the file to search"
                    },
                    "keyword": {
                        "type": "string",
                        "description": "Keyword or text to search for"
                    }
                },
                "required": ["filepath", "keyword"]
            }
        }
    }
]


available_functions = {
    "read_file": read_file,
    "list_files": list_files,
    "write_file": write_file,
    "search_in_file": search_in_file
}


user_query = input("You: ")


messages = [
    {
        "role": "system",
        "content": (
            "You are a file system assistant. "
            "You have access to tools for reading, listing, writing, "
            "and searching files. "
            "The resumes directory may contain PDF, TXT, and DOCX files. "
            "When the user asks about all resumes, first list all files "
            "without assuming a specific extension. "
            "Use the provided tools whenever you need information from files. "
            "Continue using tools until you have enough information to "
            "answer the user's request."
        )
    },
    {
        "role": "user",
        "content": user_query
    }
]


while True:

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message

    messages.append(assistant_message)

    if not assistant_message.tool_calls:

        print("\nAssistant:")
        print(assistant_message.content)

        break

    for tool_call in assistant_message.tool_calls:

        function_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        print("\nTool requested:", function_name)
        print("Arguments:", arguments)

        function_to_call = available_functions.get(
            function_name
        )

        if function_to_call:

            try:
                result = function_to_call(**arguments)

            except Exception as e:
                result = {
                    "success": False,
                    "error": str(e)
                }

        else:

            result = {
                "success": False,
                "error": f"Unknown tool: {function_name}"
            }

        print("\nTool result:")
        print(result)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })