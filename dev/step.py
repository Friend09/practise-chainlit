import chainlit as cl

# using @cl step

@cl.step()
async def tool():
    await cl.sleep(2)

    return "Response from the tool!"

@cl.on_message
async def main(message: cl.Message):
    # call the tool
    tool_res = await tool()

    # send the final answer
    await cl.Message(content="this is the final answer").send()
