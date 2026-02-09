from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage, ToolMessage
from langchain_ollama import ChatOllama
from typing import Annotated, Sequence, TypedDict
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages


# This global variable will store document content
document_content = ""

class AgentState(TypedDict):
    messages : Annotated[Sequence[BaseMessage], add_messages]
    

@tool
def update(content: str) -> str:
    """Updates the content with the provided content."""
    global document_content
    document_content = content

    return f"Document has been updated successfully! The current content is : \n{document_content}"

@tool
def save(filename: str) -> str:
    """Save the current document to a text file and finish the process.
    
    Args : 
        filename : Name for the text file."""
    
    global document_content
    
    if not filename.endswith('.txt'):
        filename = f"{filename}.txt"

    try:
        with open(filename, "w") as file:
            file.write(document_content)
        print(f"\nDocument has been saved to : {filename}")

        return f"Document has been saved successfully to {filename}."
    except Exception as e:
        return f"Error saving document {str(e)}"