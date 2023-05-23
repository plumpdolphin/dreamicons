<div align="center">
<img src="dream.svg" width=200 height=150/>
<h2><strong>Dream Icons: hyper-optimized SVG icons for all!</strong></h2>

[![License](https://img.shields.io/badge/License-CC0%201.0-informational?style=flat-square)](https://github.com/plumpdolphin/dreamicons/blob/main/LICENSE)
[![SVG](https://img.shields.io/badge/SVG-v2-orange?style=flat-square&logo=svg&logoColor=orange)](http://www.w3.org/Graphics/SVG/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-orange.svg?style=flat-square&logo=python&logoColor=yellow)](https://img.shields.io/badge/rust-1.61%2B-orange.svg)
![Last Commit](https://img.shields.io/github/last-commit/plumpdolphin/dreamicons?style=flat-square&label=Last%20Commit)
</div>
<hr>

The **Dream Icons** project is a open repository of lightweight, hand-crafted svg icons for use in applications where clean, modern style and load performance is of paramount importance. 
All icons come in one of two types: **regular** and **solid**. 

All Dream Icons are CC0 licensing, which means not only are they copyright-free, but they are attribution free as well. 
Dream Icons are the perfect fit for anything from web and desktop applications to games and even embedded web servers!

<hr>

## **Usage instructions**

There are many ways you can use Dream Icons, and all SVG files can be used as-is in any `<img>`, `<object>`, or `<svg>` tags as inline out of the box. 
However, depending on your use case, you may require PNG variants for use in game engines, 3D modelling software, etc. 

If this is the case, you can do so with the [to_png](https://github.com/plumpdolphin/dreamicons/blob/main/scripts/to_png.py) script. 
To use it you must first install the [CairoSVG](https://pypi.org/project/CairoSVG/) Python package. To do this, you can run the command below:
```
pip install CairoSVG
```

With CairoSVG installed, navigate to the root of the dreamicons folder and run this command:
```
python3 ./scripts/to_png.py
```
This will generate a folder called `/output` with a sub-folder for each icon style.
For some, this may be all you need. However, if you would like a different size icon than the default 256x256, or a different color, here are some command-line args you can use:

- `w=<WIDTH>`
- `h=<HEIGHT>`, 
- `c=<COLOR>`, can be a hex value or css color name (i.e.  #FFF, #010F2C, lightblue, etc)

So, if you require 64x64 PNG icons in yellow, you can use the command:
```
python3 ./scripts/to_png.py w=64 h=64 c=yellow
```
And now you have a fresh batch of icons ready to drop-and-go!
<hr>

I wish you the best of luck in your projects. If you have any questions, feel free to reach out!

<div align=center font-size="4rem">
    <h3>:cloud: <strong><i>Happy coding!</i></strong> :cloud:</h3>
</div>