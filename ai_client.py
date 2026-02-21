import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

conversation_history = []

# def ask_ai(prompt):
#     payload = {
#         "model": "mistral",
#         "prompt": f"""
#             You are Jarvis.
#             Answer the user's question directly.
#             Do not greet.
#             Do not introduce yourself.
#             Do not say "Hello".
#             Do not roleplay.
#             Just answer the question clearly and completely.

#             Question: {prompt}
#             Answer:
#             """,
#         "stream": False,
#         "options": {
#             "temperature": 0.5,
#             "num_predict": 80,
#              "top_p": 0.7
#         }
#     }

#     try:
#         response = requests.post(OLLAMA_URL, json=payload, timeout=60)

#         reply = response.json()["response"].strip()

#         if "." in reply:
#             reply = reply[:reply.rfind(".") + 1]

#         if response.status_code != 200:
#             print("Ollama Error:", response.status_code, response.text)
#             return "I am having trouble thinking right now."

        
#         return reply
    
        

#     except requests.exceptions.RequestException:
#         return "I cannot connect to my brain right now."
def ask_ai(prompt):
    global conversation_history

    # Add new user message
    conversation_history.append(f"User: {prompt}")

    # Keep memory limited (last 6 exchanges)
    if len(conversation_history) > 12:
        conversation_history = conversation_history[-12:]

    full_prompt = f"""
You are Jarvis, a helpful and intelligent assistant.
Answer clearly and directly.

{chr(10).join(conversation_history)}
Jarvis:
"""

    payload = {
        "model": "mistral",
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.5,
            "top_p": 0.6,
            "num_predict": 140
        }
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=60)

    if response.status_code != 200:
        return "I am having trouble thinking right now."

    reply = response.json()["response"].strip()

    # Clean ending
    if "." in reply:
        reply = reply[:reply.rfind(".") + 1]

    # Save Jarvis reply to memory
    conversation_history.append(f"Jarvis: {reply}")

    return reply