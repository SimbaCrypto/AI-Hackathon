import google.generativeai as genai

# Set your API key
genai.configure(api_key="")

# Create a model instance
model = genai.GenerativeModel(model_name="gemini-pro")

def custom_gemini_chat(user_input, history):
  """Interacts with the Gemini model to get a response.

  Args:
    user_input: The user's query.
    history: A list of tuples, where each tuple contains the user's query and the model's response.

  Returns:
    The model's response.
  """

  prompt = f"""You are a medical expert specializing in wellness and health improvement. Please provide a helpful and informative response to the following query, taking into account the previous conversation:

{''.join([f'User: {u}\nAI: {a}\n' for u, a in history])}
User: {user_input}'"""

  response = model.generate_content(prompt)
  return response.text

if __name__ == "__main__":
  print("Welcome to Your Well Assistant!")
  history = []  #History initialized

  while True:
    user_input = input("Type your Medical question or topic: ")
    if user_input.lower() == "quit":
      break

    reply = custom_gemini_chat(user_input, history)
    history.append((user_input, reply))
    print("\nWellness's Reply:")
    print(reply)