faqs = {
    ("hello", "hi", "hey"): "Hello! How can I assist you today?",
    ("whats your name",): "I'm a ChatBot built with Python. How can I help you?",
    ("when you avalaible?", "open", "timing"): "I'm avalaible from 9 AM to 6 PM, Monday through Friday.",
    ("can you tell me about your location", "address", "where"): "We are located at 123 Main Street, karachi",
    ("services", "offerings", "what do you provide"): "We offer a variety of services including web development, digital marketing, and IT consulting.",
    ("contact", "phone", "email"): "You can reach us at chatbot@gmail.com or call 4213982467.",
    ("price", "cost", "fee","how much you charge"): "Our prices vary depending on the service and complexity. Please contact us for a customized quote.",
    ("refund", "return"): "Refunds are processed within 5-7 buisness days of request.",
    ("bye", "exit", "quit"): "Goodbye! Have a good day!",    
}

def get_response(user_input):
    user_input_lower = user_input.lower()
    for keywords, response in faqs.items():
        if any(keyword in user_input_lower for keyword in keywords):
            return response
    return "I'm sorry, I don't understand. Please contact me for further help."
def run_chatbot():
    print("FAQ Chatbot: Ask me a question (type 'bye' to exit)\n")
    
    while True:
        user_input =input("You: ")
        response = get_response(user_input)
        print(f"Bot:{response}")
        
        if user_input.lower() in ("bye", "exit", "quit"):
            break
        
if __name__ == "__main__":
    run_chatbot()