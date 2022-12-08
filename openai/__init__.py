from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot import on_command
from nonebot.params import CommandArg
from .utils import get_openai_reply,api_key
from nonebot.rule import to_me
import asyncio

openai_text = on_command(
    "求助", aliases={"请问", "帮忙"}, block=True, priority=5, rule=to_me())


@openai_text.handle()
async def _(msg: Message = CommandArg()):
    if api_key == "寄":
        await openai_text.finish("请先配置openai_api_key")
    
    await openai_text.send(MessageSegment.text("让本喵想想吧..."))
    prompt = msg.extract_plain_text()
    if prompt == "" or prompt == None or prompt.isspace():
        await openai_text.finish("需要提供文本prompt")
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, get_openai_reply, prompt)
    await openai_text.finish(MessageSegment.text(res))
