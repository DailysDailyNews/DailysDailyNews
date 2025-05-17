def chatbot():
  knowledge = {
    "hello": "Hi there!",
    "how are you": "i'm doing well, thank you!",
    "What is your name?": "I am a chatbot created by Daily Investors",
    "What is your purpose?": "To help you better understand",
    "What is your investment strategy?": "I don't have a specific investment strategy, but I can provide information on various techniques.",
    "Help": "I can help, with future funds the News will continue in the future.",
    "Bye": "Goodbye!"
  }
  
def respond(message):
  message = message.lower()
  if message in knowledge:
    return knowledge[message]
  else:
    return "I'm sorry, havnt been sponsored yet. Will be soon!"
  
  def learn(question, answer):
    knowledge[question.lower()] = answer
    print(f"Thanks! I've learned that when you say '{question}', I should respond with '{answer}'.")

    print("Hello! I', a simple learning chatbot. Type 'bye' to exit.")
    while True:
      user_input = input(".")
      if user_input.lower() == 'bye':
        print(respond(user_input))
        break
      else:
        response = respond(user_input)
        break
    else:
      response = respond(user_input)
      print(response)
      if "Learn": in user_input:
question = input("What would you like to teach me?")
      answer = input("Stock Market Strategies, Updated News, Future Picks")
      learn(question, answer)
      print("Thank You, we value education and will continue to learn.")
    else:
      new_answere = input("What should I say?")
      learn(user_input, new_answer)
      

if __name__ == "__main__":
   chatbot()
