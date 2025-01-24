# coding=utf-8
import os
import random
import cv2
import numpy as np
from PIL import Image
from nonebot import logger

from .config import plugin_cache_dir
from .tools import circle_corner, text_to_b64, load_image, draw_text, save_image


text_full = (
    "あアいイうウえエおオかカきキくクけケこコさサしシすスせセそソたタちチつツてテとトなナにニぬヌねネのノはハひヒふフへヘほホまマみミむムめメもモや"
    "ヤゆユよヨらラりリるルれレろロわワをヲんンがガぎギぐグげゲごゴざザじジずズぜゼぞゾだダぢヂづヅでデどドばバびビぶブべベぼボぱパぴピぷプぺペぽポ"
)
text_half = "ゃャゅュょョ"


async def template_1(logo_data: dict[str, str]) -> Image.Image:
    """
    模板1
    :param logo_data:
    :return:
    """
    image_size = (1000, 500)
    image = Image.new("RGBA", image_size, "#FFFFFF00")

    size_list = [random.randint(110, 190) for _ in range(len(logo_data["标题"]))]
    rotate_list = [random.randint(-20, 20) for _ in range(len(logo_data["标题"]))]
    y_list = [random.randint(-20, 20) for _ in range(len(logo_data["标题"]))]

    image_size_list = [2, 1, 0, -1]
    image_color_list = ["#7c71ec", "#fff", "#7c71ec", "#fff"]
    for i, image_size in enumerate(image_size_list):
        color = image_color_list[i]
        x, y = 0, 100
        for i_t, text in enumerate(logo_data["标题"]):
            rotate = rotate_list[i_t]
            size = size_list[i_t]

            paste_alpha = await kawaii_text_to_image(text, image_size)
            paste_alpha = paste_alpha.resize((size, size))
            paste_alpha = paste_alpha.rotate(rotate)
            image_color = Image.new("RGBA", paste_alpha.size, color)
            image.paste(image_color, (x, y + y_list[i_t]), mask=paste_alpha)

            x += int(size * 0.7)

    return image


async def kawaii_text_to_image(text: str, size=0) -> Image.Image:
    """
    获取字符图片
    高光仅适用于日文
    :param text:要获取的文字
    :param size: -1:高光, 0:本体, 1:描边一, 2:描边二
    :return:PLI.Image.Image
    """
    text_image_path = plugin_cache_dir / "text"
    text_image_path.mkdir(exist_ok=True)
    text_image_path = text_image_path / f"{text_to_b64(text, replace=True)}_{size}.png"
    if os.path.exists(text_image_path):
        image = await load_image(text_image_path)
        return image

    logger.debug(f"未绘制‘{text}’，进行绘制")
    if size == -1:
        if text not in text_full + text_half:
            return Image.new("RGBA", (200, 200), (0, 0, 0, 0))
        for i, t in enumerate(text_full + text_half):
            if t == text:
                text = i + 1
        url = f"https://cdn.kanon.ink/api/image?imageid=knapi-kawaii_logos-{text}_{size}.png"
        try:
            image = await load_image(url, cache_image=False)
            save_image(image, text_image_path.parent, text_image_path.name, mode="png")
        except Exception as e:
            logger.error("请求高光图片失败")
            logger.error(e)
            image = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
        return image

    image_0_path = text_image_path.parent / f"{text_to_b64(text, replace=True)}_0.png"
    if os.path.exists(image_0_path):
        image_0 = await load_image(image_0_path)
    else:
        paste_image = await draw_text(
            text,
            size=170,
            textlen=50,
            fontfile="胖胖猪肉体_猫啃网.otf",
            text_color="#fff",
            calculate=False
        )
        image_0 = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
        image_0.alpha_composite(paste_image, (
            int((image_0.size[0] - paste_image.size[0]) / 2),
            int((image_0.size[1] - paste_image.size[1]) / 2)
        ))
        save_image(image_0, image_0_path.parent, f"{text_to_b64(text, replace=True)}_0.png", mode="png")
    if size == 0:
        return image_0

    if size == 1:
        image_1 = draw_out_line(image_0, 7, (255, 255, 255, 255))
        image_1 = image_1.convert("RGBA")
        save_image(image_1, text_image_path.parent, text_image_path.name, mode="png")
        return image_1

    if size == 2:
        image_2 = draw_out_line(image_0, 11, (255, 255, 255, 255))
        image_2 = image_2.convert("RGBA")
        save_image(image_2, text_image_path.parent, text_image_path.name, mode="png")
        return image_2


def draw_out_line(image, size=5, color=None):
    if color is None:
        logger.warning("color is None")
        color = [100, 100, 100, 255]
    image_np = np.array(image)
    image_gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # 使用形态学操作生成描边
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(image_gray, kernel, iterations=size)

    edges = dilated - image_gray

    # 将描边区域叠加到原图上
    image_np[edges > 0] = color  # 描边颜色

    # 将结果转换回 PIL 图像
    result_image = Image.fromarray(image_np)

    image = Image.new("RGBA", result_image.size, (0, 0, 0, 0))
    image.alpha_composite(result_image)

    pixels = image.load()
    for i in range(image.width):
        for j in range(image.height):
            if pixels[i, j] == (0, 0, 0, 255):
                pass
                # pixels[i, j] = (0, 0, 0, 0)
            elif pixels[i, j] == (0, 0, 0, 0):
                pass
            else:
                pixels[i, j] = (color[0], color[1], color[2], 255)

    return image



