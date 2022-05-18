import os
import argparse
import textwrap
from PIL import Image, ImageDraw, ImageFont
import meme_addons

def parse_args():
    parser = argparse.ArgumentParser(description='A CLI meme generator')
    parser.add_argument("--meme", '-m', help="Name of meme template as base, partial names might be recognized", type=str)
    parser.add_argument("--toptext", '-t', default='toptext', help="Top text of meme", type=str)
    parser.add_argument("--bottomtext", '-b', default='bottomtext', help="Bottom text of meme", type=str)
    parser.add_argument("--deepfry", '-df', action='store_true')
    args = parser.parse_args()

    return args

def get_template_name(name):
    template = []
    all_templates = os.listdir('data/images')
    for template_name in all_templates:
        if name.lower() in template_name.lower():
            template.append(template_name)
    assert len(template) < 2, f'It appears multiple templates fit your name, please be more specific: \n {template}'
    assert len(template) > 0, 'It appears no template matched your name'

    return template[0]

def create_meme(args):
    template_name = get_template_name(args.meme)
    meme = Image.open('data/images/' + template_name)
    w, h = meme.size

    font = ImageFont.truetype("data/fonts/impact.ttf", 30)
    chars_per_line = int(w/font.size*2)
    toptext_wrapped = "\n".join(textwrap.wrap(args.toptext, width=chars_per_line))
    bottomtext_wrapped = "\n".join(textwrap.wrap(args.bottomtext, width=chars_per_line))

    meme_drawer = ImageDraw.Draw(meme)
    meme_drawer.text((w/2, 0), toptext_wrapped, font=font, anchor='ma', stroke_width=2, stroke_fill='black', align = "center")
    meme_drawer.text((w/2, h-1), bottomtext_wrapped, font=font, anchor='md', stroke_width=2, stroke_fill='black', align = "center")

    if args.deepfry:
        meme = meme_addons.deepfry(meme)

    meme.show()

if __name__ == '__main__':
    args = parse_args()
    create_meme(args)
