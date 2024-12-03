from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import google.generativeai as genai

# Initialize Flask and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Set your API key
genai.configure(api_key="")  
# Initialize the Generative AI model
model = genai.GenerativeModel(model_name="gemini-pro")

# Chat history to maintain conversation context
history = []

# Custom function to interact with the AI model
def custom_gemini_chat(user_input, history):
    prompt = f"""
    You are a medical expert specializing in wellness and health improvement. 
    Please provide a helpful and informative response to the following query, 
    taking into account the previous conversation:

    {''.join([f'User: {u}\nAI: {a}\n' for u, a in history])}
    User: {user_input}
    """
    response = model.generate_content(prompt)
    return response.text

# Flask route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# SocketIO event for handling user messages
@socketio.on('message')
def handle_message(message):
    global history
    try:
        # Process the user message and get the AI response
        response = custom_gemini_chat(message, history)
        history.append((message, response))
        emit('response', response)  
    except Exception as e:
        print(f"Error processing request: {e}")
        emit('response', "An error occurred. Please try again later.")

def custom_gemini_chat(user_input, history):
    prompt = f"""
    You are a medical expert specializing in wellness and health improvement. 
    Please provide a helpful and informative response to the following query, 
    taking into account the previous conversation:

    {''.join([f'User: {u}\nAI: {a}\n' for u, a in history])}
    User: {user_input}
    """
    response = model.generate_content(prompt)
    return response.text.strip() 



if __name__ == '__main__':
    socketio.run(app, debug=True)
