import google.generativeai as genai

# Set your API key
genai.configure(api_key="")

# Create a model instance
model = genai.GenerativeModel(model_name="gemini-pro")

def custom_gemini_chat(user_input):
  """Interacts with the Gemini model to get a response.

  Args:
    user_input: The user's query.

  Returns:
    The model's response.
  """

  response = model.generate_content(f"You are a medical expert specializing in wellness and health improvement. Please provide a helpful and informative response to the following query: {user_input}")

  return response.text

if __name__ == "__main__":
  print("Welcome to Your Well Assistant!")
  user_input = input("Type your Medical question or topic: ")
  reply = custom_gemini_chat(user_input)
  print("\nGemini's Reply:")
  print(reply)