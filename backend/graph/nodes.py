from backend.services import llm


VALID_ROUTES = {
    "account",
    "loan",
    "card",
    "policy",
    "general"
}


def classifier_node(state):
    """
    Determines which department should handle the question
    """

    question = state["question"]

    prompt = f"""
أنت نظام تصنيف داخل بنك.

صنف السؤال التالي إلى واحدة فقط من الفئات:

account
loan
card
policy
general

السؤال:
{question}

أعد فقط اسم الفئة بدون أي شرح أو علامات إضافية.
"""

    try:
        response = llm.invoke(prompt)

        print("=" * 50)
        print("CLASSIFIER RAW RESPONSE:")
        print(response)
        print("=" * 50)

        route = str(response).strip().lower()

        # تنظيف الردود المحتملة
        route = route.replace(".", "")
        route = route.replace('"', "")
        route = route.replace("'", "")

        if route not in VALID_ROUTES:
            print(f"INVALID ROUTE RECEIVED: {route}")
            route = "general"

        print(f"FINAL ROUTE: {route}")

        return {
            "route": route
        }

    except Exception as e:
        print(f"CLASSIFIER ERROR: {e}")

        return {
            "route": "general"
        }


def account_agent(state):
    q = state["question"]

    return {
        "answer": f"[ACCOUNT AGENT] {q}"
    }


def loan_agent(state):
    q = state["question"]

    return {
        "answer": f"[LOAN AGENT] {q}"
    }


def card_agent(state):
    q = state["question"]

    return {
        "answer": f"[CARD AGENT] {q}"
    }


def policy_agent(state):
    q = state["question"]

    return {
        "answer": f"[POLICY AGENT - RAG LATER] {q}"
    }


def general_agent(state):
    q = state["question"]

    try:
        response = llm.invoke(q)

        return {
            "answer": str(response)
        }

    except Exception as e:
        return {
            "answer": f"Error: {str(e)}"
        }