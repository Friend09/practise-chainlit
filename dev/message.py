# use this to practise message The Message class is designed to send, stream, update or remove messages. https://docs.chainlit.io/api-reference/message


import chainlit as cl

# send a new message
@cl.on_message
async def main(message: cl.Message):
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()


# update a message
import chainlit as cl

@cl.on_chat_start
async def main():
    msg = cl.Message(content="Hello!")
    await msg.send()

    await cl.sleep(3)

    msg.content = "Hello again after 3 seconds" # this is where the new info should be sent
    await msg.update()

# remove a message
import chainlit as cl

@cl.on_chat_start
async def main():
    msg = cl.Message(content="Message 1")
    await msg.send() # shown on UI
    await cl.sleep(2) # wait for 2 seconds
    await msg.remove() # remove the message
