from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import google.generativeai as genai

# Set your API key
genai.configure(api_key="")

# ... Your chatbot logic ...

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    try:
        response = custom_gemini_chat(message, history)
        emit('response', response)
    except Exception as e:
        print(f"Error processing request: {e}")
        emit('response', "An error occurred. Please try again later.")

if __name__ == '__main__':
    socketio.run(app)