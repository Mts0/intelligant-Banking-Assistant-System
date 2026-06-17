from langgraph.graph import StateGraph
from langgraph.graph import START, END

from backend.graph.state import BankState
from backend.graph.nodes import (
    classifier_node,
    account_agent,
    loan_agent,
    card_agent,
    policy_agent,
    general_agent
)


builder = StateGraph(BankState)

builder.add_node("classifier", classifier_node)
builder.add_node("account", account_agent)
builder.add_node("loan", loan_agent)
builder.add_node("card", card_agent)
builder.add_node("policy", policy_agent)
builder.add_node("general", general_agent)

builder.add_edge(START, "classifier")


def route_selector(state):
    return state["route"]

builder.add_conditional_edges(
    "classifier",
    route_selector,
    {
        "account": "account",
        "loan": "loan",
        "card": "card",
        "policy": "policy",
        "general": "general"
    }
)

builder.add_edge("account", END)
builder.add_edge("loan", END)
builder.add_edge("card", END)
builder.add_edge("policy", END)
builder.add_edge("general", END)

graph = builder.compile()