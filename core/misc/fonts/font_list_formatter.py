from fonts import *

new_vals = ()

def format_font_name(font_name):
    return font_name.replace(' ', '_').lower()

for font_name in fonts_list:
    new_vals = new_vals + ((font_name, format_font_name(font_name)),)

print(new_vals)
