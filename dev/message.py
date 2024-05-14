import chainlit as cl

@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()

    # do some work
    await cl.sleep(2)

    msg.content = f"Hello, you just sent: {message.content}!"
    await msg.update()
