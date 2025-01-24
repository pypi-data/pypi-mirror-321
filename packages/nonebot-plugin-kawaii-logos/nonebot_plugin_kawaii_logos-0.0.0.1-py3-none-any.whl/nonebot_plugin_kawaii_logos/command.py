# coding=utf-8
from nonebot import logger
from .draw import template_1


async def command_kawaii_logos(args: str):
    # 解析
    args = args.split(" ")
    if len(args) == 0:
        return "请添加要生成logo的文字"
    elif len(args) == 1:
        logo_data: dict = {"标题": args[0], "副标题": None, "下": None,"上": None}
    elif len(args) == 2:
        logo_data: dict = {"标题": args[0], "副标题": args[1], "下": None,"上": None}
    elif len(args) == 3:
        logo_data: dict = {"标题": args[0], "副标题": args[1], "下": args[2],"上": None}
    elif len(args) == 4:
        logo_data: dict = {"标题": args[0], "副标题": args[1], "下": args[2],"上": args[3]}
    else:
        return "文字参数过多，最多包含4段文字"

    # 检查内容长度
    if not 3 <= len(logo_data["标题"]):
        return "第1段文字过短"
    if not len(logo_data["标题"]) <= 10:
        return "第1段文字过长"
    if not 3 <= len(logo_data["副标题"]):
        return "第2段文字过短"
    if not len(logo_data["副标题"]) <= 10:
        return "第2段文字过长"
    if not 3 <= len(logo_data["下"]):
        return "第3段文字过短"
    if not len(logo_data["下"]) <= 15:
        return "第3段文字过长"
    if not 3 <= len(logo_data["上"]):
        return "第4段文字过短"
    if not len(logo_data["上"]) <= 15:
        return "第4段文字过长"

    image = await template_1(logo_data=logo_data)

    return image

