from PIL import Image, ImageDraw, ImageFont
from datetime import timedelta
import sys

if len(sys.argv) == 1:
    raise Exception("You must specify an image.")


caption = input("What will this gif show after an hour passes?\n")


def frame(size, time_remaining):
    print("Generating {} at {} x {}".format(str(time_remaining), size[0], size[1]))
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)
    text = "{0}\nin\n{1}".format(caption, str(time_remaining))
    font = ImageFont.truetype("arial.ttf", 48)
    draw.multiline_text((size[0] / 2, size[1] / 2), text, fill = "black", font = font, align = "center", anchor = "mm")
    return image


def gif(image_path):
    reward = Image.open(image_path)
    reward.thumbnail((600, 600))
    frames = []
    duration = timedelta(minutes = 59, seconds = 59)
    while duration.total_seconds() > 0:
        frames.append(frame(reward.size, duration))
        duration = duration - timedelta(seconds = 1)
    frames.append(reward)
    frame_one = frames[0]
    print("\nGenerating the final gif, this WILL take a while...")
    frame_one.save("hour.gif", format = "GIF", append_images = frames, save_all = True, duration = 1000, loop = 1)


if __name__ == "__main__":
    gif(sys.argv[1])
