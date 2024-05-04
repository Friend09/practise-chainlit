import chainlit as cl

@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")

@cl.on_message
async def main(message: cl.Message):
    # custom logic go here

    # Send a message to the user
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()
