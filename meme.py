import ast
import os
import argparse
import textwrap
from PIL import Image, ImageDraw, ImageFont
import meme_addons

def parse_args():
    parser = argparse.ArgumentParser(description='A CLI meme generator')
    parser.add_argument('meme', help="Name of meme template as base. Seperate words must be connected with hyphens. Partial names might be recognized", type=str, nargs=1)
    parser.add_argument("text", default=['toptext', 'bottomtext'], help="Text to be diplayed on the meme, ordered from how it is displayed on the meme left to right", nargs='+')
    parser.add_argument("--save", '-s', default=None, help="filename to save the meme as, not including file extension", type=str)
    parser.add_argument("--deepfry", '-df', action='store_true')
    args = parser.parse_args()
    return args

def match_template_name(name):
    template = []
    all_templates = os.listdir('data/images/topbottom') + os.listdir('data/images/custom')
    for template_name in all_templates:
        if name.lower() in template_name.lower():
            template.append(template_name)
    assert len(template) < 2, f'It appears multiple templates fit your name, please be more specific: \n {template}'
    assert len(template) > 0, 'It appears no template matched your name'

    return template[0]

def create_top_bottom_meme(template_name, args):
    font = ImageFont.truetype("data/fonts/impact.ttf", 30)
    meme = Image.open('data/images/topbottom/' + template_name)
    w, h = meme.size    
    chars_per_line = int(w/font.size*2)
    toptext_wrapped = "\n".join(textwrap.wrap(args.text[0], width=chars_per_line))
    bottomtext_wrapped = "\n".join(textwrap.wrap(args.text[1], width=chars_per_line))

    meme_drawer = ImageDraw.Draw(meme)
    meme_drawer.text((w/2, 0), toptext_wrapped, font=font, anchor='ma', stroke_width=2, stroke_fill='black', align = "center")
    meme_drawer.text((w/2, h-1), bottomtext_wrapped, font=font, anchor='md', stroke_width=2, stroke_fill='black', align = "center")

    return meme

def create_custom_meme(template_name, args):
    font = ImageFont.truetype("data/fonts/impact.ttf", 30)
    meme = Image.open('data/images/custom/' + template_name)
    w, h = meme.size   
    chars_per_line = int(w/font.size*2)
    with open("data/meta_data.txt", 'r') as meta_file:
        meta_content = meta_file.read()
        all_meta_data = ast.literal_eval(meta_content)
    meta_data = all_meta_data[template_name]
    meme_drawer = ImageDraw.Draw(meme) 

    for i, pos in enumerate(meta_data['textpositions']):
        text_wrapped = "\n".join(textwrap.wrap(args.text[i], width=chars_per_line))
        if meta_data['textcolor'] == 'white':
            meme_drawer.text(pos, text_wrapped, font=font, anchor='ma', stroke_width=2, stroke_fill='black', align = "center")
        else: 
            meme_drawer.text(pos, text_wrapped, font=font, anchor='ma', fill=meta_data['textcolor'], align = "center")

    return meme

def create_meme(args):
    template_name = match_template_name(args.meme[0])
    
    if template_name in os.listdir('data/images/custom'):
        meme = create_custom_meme(template_name, args)
    else:
        meme = create_top_bottom_meme(template_name, args)

    if args.deepfry:
        meme = meme_addons.deepfry(meme)

    if args.save is not None:
        filename = args.save + '.jpg'
        meme.save(filename)
        print('Meme was saved as', filename)
    else:
        meme.show()

if __name__ == '__main__':
    args = parse_args()
    create_meme(args)
