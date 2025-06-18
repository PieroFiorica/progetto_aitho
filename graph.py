from typing import TypedDict
from typing import Annotated
from operator import add

from langgraph.graph import StateGraph, END
from agent import agent

class State(TypedDict):
    messages : Annotated[list[str], add]

workflow = StateGraph(State)
workflow.add_node("agent", agent)
workflow.set_entry_point("agent")
workflow.add_edge("agent", END)
graph = workflow.compile()