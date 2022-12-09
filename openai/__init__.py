from nonebot.adapters.onebot.v11 import Message, MessageSegment,MessageEvent
from nonebot import on_command
from nonebot.params import CommandArg
from .utils import get_openai_reply,api_key
from nonebot.rule import to_me
import asyncio
import nonebot

try:
    cd_time = nonebot.get_driver().config.openai_cd_time        # 从配置文件中读取cd_time
except:
    cd_time = 60       # 默认值
    
openai_cd_dir = {}  # 记录cd的字典


# 响应器
openai_text = on_command(
    "求助", aliases={"请问", "帮忙"}, block=True, priority=5, rule=to_me()) 


@openai_text.handle()
async def _(event: MessageEvent, msg: Message = CommandArg()):
    if api_key == "寄":                                                      # 没有配置api_key
        await openai_text.finish("请先配置openai_api_key")                    # finish提示配置api_key
    prompt = msg.extract_plain_text()                                        # 提取文本
    if prompt == "" or prompt == None or prompt.isspace():                   # 没有提供文本
        await openai_text.finish("需要提供文本prompt")                        # finish提示提供文本

    qid = event.get_user_id()                                                # 获取用户id
    try:
        cd = event.time - openai_cd_dir[qid]                                 # 计算cd
    except KeyError:
        cd = cd_time + 1                                                     # 没有记录则cd为cd_time+1
    if (
        cd > cd_time    
        or event.get_user_id() in nonebot.get_driver().config.superusers
    ):                                                                       # 判断cd

        # 记录cd    
        openai_cd_dir.update({qid: event.time})
        await openai_text.send(MessageSegment.text("让本喵想想吧..."))        # 发送提示
        loop = asyncio.get_event_loop()                                      # 获取事件循环
        try:
            res = await loop.run_in_executor(None, get_openai_reply, prompt)    # 开一个不会阻塞asyncio的线程调用get_openai_reply函数
        except Exception as e:
            await openai_text.finish(str(e))                                    # 出错则finish
        await openai_text.finish(MessageSegment.text(res),at_sender=True)       # finish回复
    else:
        await openai_text.finish(
            MessageSegment.text(f"让本喵的脑子休息一下好不好喵, {cd_time - cd:.0f}秒后才能再次使用"),   # finish提示cd
            at_sender=True
        )
