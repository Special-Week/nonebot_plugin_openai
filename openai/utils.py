import openai
import nonebot

try:
    api_key = nonebot.get_driver().config.openai_api_key        # 从配置文件中读取api_key
except:
    api_key = '寄'        # 默认值

try:
    max_tokens = nonebot.get_driver().config.openai_max_tokens      # 从配置文件中读取max_tokens
except:
    max_tokens = 1000           # 默认值


def get_openai_reply(prompt:str)->str:
    """获取openai的回复, 传入prompt, 返回回复"""
    openai.api_key = api_key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    res = response.choices[0].text
    # 移除所有开头的\n
    while res.startswith("\n"):
        res = res[1:]
    return res
