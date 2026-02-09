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
    
tools = [update, save]
    
llm_model = ChatOllama(model="llama3.2:1b").bind_tools(tools)

def agent(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(
        content = f"""
    You are a Drafter, a helpful writing assistant. You are going to help the user update and modify documents.

    - If the user wants to update or modify content, use the 'update' tool with the complete updated content.
    - If the user wants to save and finish, you need to use the 'save' tool.
    - Make sure to always show the current document state after modifications.

    The current document content is : {document_content}
"""
    )

    if not state['messages']:
        user_input = "I'm ready to help you update a document. What would you like to create?"
        user_msg = HumanMessage(content=user_input)
    else:
        user_input = input("\nWhat would you like to do with the documents? ")
        print(f"\nUser : {user_input}")
        user_msg = HumanMessage(content=user_msg)

    zembu_msg = [system_prompt] + list(state['messages']) + [user_msg]

    response = llm_model.invoke(zembu_msg)

    print(f"\nAI : {response.content}")
    if hasattr(response, "tool_calls") and response.tool_calls:
        print(f"USING TOOLS : {[tc['name'] for tc in response.tool_calls]}")

    return {"messages" : list(state['messages']) +  [user_msg, response]}