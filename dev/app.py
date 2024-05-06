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

@cl.on_stop
def on_stop():
    print("The user wants to step the task!")

@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")

from chainlit.types import ThreadDict
@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    print("The user resumed a previous chat session!")
