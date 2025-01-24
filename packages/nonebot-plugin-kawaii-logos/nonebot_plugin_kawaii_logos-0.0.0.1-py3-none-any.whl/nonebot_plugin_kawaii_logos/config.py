# coding=utf-8
from nonebot import get_plugin_config, logger
from pydantic import BaseModel
from pathlib import Path
from nonebot import require

try:
    require("nonebot_plugin_localstore")
    import nonebot_plugin_localstore as store

    plugin_cache_dir: Path = store.get_plugin_cache_dir()
    # plugin_config_dir: Path = store.get_plugin_config_dir()
    plugin_data_dir: Path = store.get_plugin_data_dir()
except Exception as e:
    plugin_cache_dir: Path = Path("./nonebot_plugin_kawaii_logos/cache")
    plugin_data_dir: Path = Path("./nonebot_plugin_kawaii_logos/data")


class Config(BaseModel):
    ...


try:
    plugin_config = get_plugin_config(Config)
    # qb_url = plugin_config.qbm_url
except Exception as e:
    pass


menu_data = [
    {
        "trigger_method": "qb帮助",
        "func": "列出命令列表",
        "trigger_condition": " ",
        "brief_des": "qb帮助",
    }
]
