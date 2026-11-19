from langchain.tools import tool

@tool #decorator fro creating a tool
def get_greeting(name : str) -> str: #type hints
    """generate a greeting message for the user"""#docstring
    return f"hello {name}, welcome to the AI world!"

result = get_greeting.invoke({"name": "anushka"})
print(result)

print(get_greeting.name)
print(get_greeting.description)
print(get_greeting.args)