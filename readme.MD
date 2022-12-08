# nonebot2调用openai的插件

## 功能:

    艾特bot时并且加上"求助", "请问"的命令头时, bot回复一些调用openai的ai回复(这个ai真他娘的逆天), 具体效果请见下文


安装方式:

    git clone https://github.com/Special-Week/nonebot_plugin_openai.git
    
    Download Zip
 
env配置项:

|config             |type     |default   |example                          |usage                                   |
|-------------------|---------|----------|---------------------------------|----------------------------------------|
| openai_api_key    | string  |寄        |openai_api_key = "aabb114514"    |    openai的api_key, 详细请看下文         |
| openai_max_tokens | int     |1000      |openai_max_tokens = 1500         |    openai的max_tokens, 详细请看下文     |


openai_api_key请在 https://beta.openai.com/account/api-keys 自己获取

openai_max_tokens貌似是ai返回的文本最大多少(根据我自己用的经验)

openai_api_key必须配置, openai_max_tokens随意, 有默认值

bot通过openai模块调用应该不需要科学上网




注意:

    相应器由于使用的是on_command, 请注意用的是否需要带上command_start

    需要安装openai模块 pip install openai

    目前env只提供了api_key和max_tokens的设置, 其他参数你可以自己动源码

    据我个人使用的情况, 总是有群友提问一些引诱犯罪的问题, 如果你遇到这种情况, 你可以考虑自己处理prompt字符串做一些判断

    这个模块貌似不是免费的, 注册的账号只有$18.00的免费额度, 我个人调用了大约1500回, 目前的额度 $7.05 / $18.00


一些具体的实例:

    Q: @bot求助 使用golang定义一个全局变量client, 并让其在init函数内与redis相连接
    A: @USER  
        package main
        import (
            "github.com/go-redis/redis"
        )
        var client *redis.Client
        func init() {
            client = redis.NewClient(&redis.Options{
                Addr:     "localhost:6379",
                Password: "", // no password set
                DB:       0,  // use default DB
            })
        }
        (这ai甚至手撕二叉树, 手撸STL容器, 已经吊打我这个废物了....)


    Q: @bot求助 假如你是李华，今日中国三大运营商——中国联通，中国移动，中国电信，屏蔽了中国境内对 GitHub 的访问，请你使用英语向你的外国笔友Jane写一封信，简要讨论这件事。正文内容要点：（1）对GitHub被封感到震惊、（2）谈论此事对中国开源界的影响、（3）对中国开源界的未来进行探讨。要求：（1）正文要点必须全部包含、（2）词数不少于120词、（3）文中不得出现真实的姓名
    A: @USER 

        Dear Jane,
        I am writing to tell you about a shocking news that three major Chinese operators, China Unicom, China Mobile and China Telecom, have blocked access to GitHub in China.

        This news has caused great concern among Chinese open source communities. On the one hand, the number of people who use GitHub to store and share their codes has decreased dramatically. On the other hand, the development of open source technology in China is facing a great challenge.

        I'm really worried about the future of open source in China. The government should take measures to guarantee the development of open source projects and encourage more people to join in. Moreover, the operators should also consider the interests of users and provide better services.
        
        I hope the situation can be improved soon.

        Yours,
        Li Hua
        (真nm正宗, 薄纱我这个在四六级考试把中国皇帝写成Chinese boss的废物)


