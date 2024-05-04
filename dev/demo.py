# demo chainlit
import chainlit as cl

@cl.step
def tool():
    return "Response from the tool!"

@cl.on_message # this function is called every time a user inputs a message on UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message on UI.
    It sends back an intermediate response from the tool, followed by the final answer.

    Arg:
        message: The user's message.

    Returns:
        None
    """

    # call the tool
    tool()

    # send the final naswer.
    await cl.Message(content="This is the final answer").send()
