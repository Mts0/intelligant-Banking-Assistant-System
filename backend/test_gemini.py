from backend.services import llm

response = llm.invoke("hello")

print(response)