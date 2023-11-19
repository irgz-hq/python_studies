def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_message):
    while messages:
        message = messages.pop()
        sent_message.append(message)

messages = ["i love you", "lets talk in english now", "say my name"]
sent_messages = []
send_messages(messages, sent_messages)

print(messages)
print(sent_messages)