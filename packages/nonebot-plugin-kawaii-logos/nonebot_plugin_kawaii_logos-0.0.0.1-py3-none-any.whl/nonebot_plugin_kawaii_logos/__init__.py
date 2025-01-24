# coding=utf-8
import html
from PIL import Image
from nonebot import logger, require, on_command
from nonebot.plugin import PluginMetadata, inherit_supported_adapters
from nonebot.adapters import Event

from .tools import save_image
from .config import Config, menu_data
from .command import command_kawaii_logos

require("nonebot_plugin_saa")
from nonebot_plugin_saa import Image as saaImage, MessageFactory
from nonebot_plugin_saa import Text as saaText

__plugin_meta__ = PluginMetadata(
    name="kawaii_logos",
    description="logo生成器，可以生成一些logo",
    usage="/kwlogo",
    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。
    homepage="https://github.com/SuperGuGuGu/nonebot_plugin_kawaii_logos",
    # 发布必填。
    config=Config,
    # 插件配置项类，如无需配置可不填写。
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_saa",
    ),
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
    extra={'menu_data': menu_data},
)


kawaii_logos_cmd = on_command("kwlogo", priority=10, block=False)


@kawaii_logos_cmd.handle()
async def download_msg(event: Event):
    if not event.get_type().startswith("message"):
        await kawaii_logos_cmd.finish()
    msg: str = str(event.get_message().copy())
    if msg == "":
        await kawaii_logos_cmd.finish()

    command_prefix = f"{msg.split('kwlogo')[0]}kwlogo"
    args = msg.removeprefix(command_prefix).removeprefix(" ")
    args = html.unescape(args)  # 反转义文字

    msg = await command_kawaii_logos(args=args)

    await send(msg)
    await kawaii_logos_cmd.finish()


async def send(msg):
    if msg is None:
        return

    if type(msg) is not list:
        msg = [msg]

    saa_msg = []
    for m in msg:
        if type(m) is Image.Image:
            saa_msg.append(saaImage(save_image(m, to_bytes=True)))
        elif type(m) is bytes:
            saa_msg.append(saaImage(m))
        else:
            saa_msg.append(saaText(m))

    if not saa_msg:
        return

    msg_builder = MessageFactory(saa_msg)
    await msg_builder.send()
