
from PIL import Image, ImageDraw,ImageFont
import random


version_list = ["1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9", "1.10",
                "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19", "1.19",
                "1.20"]


def update_overlay(versions_str: str):
    overlay_str = f"Versions:{versions_str}"
    img = Image.new('RGB', (255, 255), color='green')
    overlay = ImageDraw.Draw(img)
    overlay.text((10,10), overlay_str, font=ImageFont.truetype('arial.ttf', size=20))
    img.save('overlay.png')


def roll_versions() -> list[str]:
    possible_versions = version_list.copy()
    rolled_versions = [str]
    for i in range(5):
        version = possible_versions[random.randint(1, len(possible_versions) - 1)]
        rolled_versions.append(version)
        possible_versions.remove(version)
    return rolled_versions

