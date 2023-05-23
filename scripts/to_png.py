import os
import re
import sys
import glob
from cairosvg import parser, surface, svg2png



# Used in Regex replacing to capture the "M\m" command's position
def z_dot(match) -> str:
    if match.groups() is not None:
        return match.group(1) + "h.0001"




# Compile regex expressions
re_path = re.compile(r"([Mm]\s*\d*\.?\d+[,\s]*\d*\.?\d+)(z)")
re_stroke = re.compile(r"stroke=\"#[^\"]{,8}\"")
re_fill = re.compile(r"fill=\"#[^\"]{,8}\"")

# Default configuration values
width, height = 256, 256
color = '#000'
styles = ["/regular", "/solid"]

# Override config with arg values
for arg in sys.argv:
    if arg.startswith('w='):
        width = float(arg.split('=')[1])
    elif arg.startswith('h='):
        height = float(arg.split('=')[1])
    elif arg.startswith('c='):
        color = '='.join(arg.split('=')[1:])



# Begin
for style in styles:
    # Iters over all .svg files in style folder
    for svg in glob.glob("." + style + "/*.svg"):
        # Build output name and path
        name = svg[svg.rfind('/') + 1:].replace(".svg", ".png")
        out_path = "./output{style}/{name}".format(style=style, name=name)

        # Replace all #0000 color codes with "transparent" to fix in-fill issue with CairoSVG
        data = open(svg)                     \
            .read()                          \
            .replace('#0000', 'transparent')
        
        # Set stroke color, where exists
        data = re.sub(
            re_stroke, 
            'stroke="{c}"'.format(c=color), 
            data)
        
        # Set fill color, where exists
        data = re.sub(
            re_fill, 
            'fill="{c}"'.format(c=color), 
            data)

        # Add fill="<color>" if the root element doesn't have a fill attribute
        idx = data.find('>')
        if 'fill=' not in data[:idx]:
            data = '{start} fill="{c}">{end}'.format(
                start=data[:idx], 
                c=color, 
                end=data[idx + 1:]) 
        
        # Replace all M<x>,<y>z dot patterns with M<x>,<y>h.0001 to satisfy Cairo renderer
        data = re.sub(re_path, z_dot, data)

        # Ensure the output directory exists before write instruction
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        svg2png(bytestring=data.encode('utf-8'), write_to=out_path, output_width=width, output_height=height)