import os
import numpy as np

# Colors for each point in HTML.
pastel = [
    "#ffcccc", "#ffe0cc", "#ffeacc", "#fff4cc", "#fffecc",
    "#effac8", "#c7f5c4", "#c4f0f4", "#c4daf4", "#c9c4f4",
    "#e1c4f4", "#f6c6e6"]

# shuffle colors so classes have distinct colors when fewer
np.random.seed(320)
np.random.shuffle(pastel)

rainbow = [
    "#fbb735", "#e98931", "#eb403b", "#b32E37", "#6c2a6a",
    "#5c4399", "#274389", "#1f5ea8", "#227FB0", "#2ab0c5",
    "#39c0b3"
]
COLOR_LIST = pastel + rainbow + [ '#bccacc', '#bd968a', '#bfb6aa', '#bfcdc9', '#c1cfdd', '#c4d9d6', '#c5d4d7', '#c5e5e2', '#c6cdd3', '#c79797', '#c7d8d6', '#c99262', '#cbe2f4', '#cc9d7a', '#cddbf5', '#cef5fc', '#d0a8b9', '#d0f8ef', '#d3c2bd', '#d5d1cf', '#d6b98d', '#d6cbca', '#d6f6e1', '#d7e5d4', '#d7e5ec', '#d9ebe0', '#db8876', '#dbaf81', '#dbdde4', '#dbe5eb', '#dcd6c9', '#dce8f7', '#decab2', '#dee0e7', '#dee1e4', '#dfd6a4', '#e0b2a3', '#e2cdbe', '#e2e2b8', '#e2e8c9', '#e4e3e4', '#e4e6fb', '#e5cab3', '#e5d8d9', '#e5e3b0', '#e9f3a2', '#eabc96', '#eac3a2', '#ead79d', '#eafaeb', '#ebf9e3', '#edd7ac', '#edd9c7', '#efad9e', '#efcab2', '#eff1f4', '#f1e1d9', '#f1e5b9', '#f2d580', '#f2ebda', '#f3e1cd', '#f4a77a', '#f4f8d0', '#f6cf97', '#f6e183', '#f6f4f8', '#f7ddbb', '#f7ec86', '#f8bbb1', '#f8c785', '#f98056', '#f9d3b8', '#f9d89a', '#f9f7ca', '#fbdf73', '#fce1a8', '#fceea1', '#fde6b1', '#fdecd0', '#fdf4ba', '#fdf998', '#fee6c5', '#fefcd3', '#ffa642', '#ffe3c8', '#fff9aa'] + ['#34a4ca', '#416081', '#4c86ab', '#4e72c7', '#506e90', '#515b80', '#525f83', '#536a97', '#59d7dd', '#5b625a', '#5e7fb1', '#657489', '#6bafd2', '#6d9ed7', '#6f749e', '#727288', '#74bddb', '#758391', '#7695aa', '#7696cd', '#7b9ea7', '#7e74b2', '#8087ad', '#848896', '#857d8d', '#868080', '#889db6', '#8c5962', '#8d7b6c', '#8dd6c3', '#8e889b', '#8e9fa4', '#8fb2e4', '#8fb8ee', '#947461', '#95a5bc', '#95b3bf', '#9a8daf', '#9baf93', '#a2e0f9', '#a38b8a', '#a4c8d5', '#a4c8dc', '#a5b8ce', '#a78a92', '#a7bdb8', '#a7d3cb', '#a8d1eb', '#a8f2f0', '#adacb2', '#b0cff0', '#b3a2c2', '#b3cae5', '#b4ced8', '#b4d9e1', '#b7b29b', '#bb9d78', '#bca391', '#bcc1c4'] 

# Symbols to be used for points in HTML.
symbol_list = ["&#%d;"%i for i in range(913, 1014)] # Greek and Coptic

SYMBOL_LIST= ["&#%d;"%i for i in range(9642, 9727)] + symbol_list # geometrical shapes

POINT_TEMPLATE = "<div id=item{item_index} class=\"genre\" scan=true style=\"color: {color_hex}; top: {button_x}px; left: {button_y}px;\" onmouseover=\"playx(&quot;{file_name}&quot;, &quot;{item_index}&quot;,[], this);\" title=\"{class_label}\"><b>{item_symbol}</b></div>"

LABEL_TEMPLATE = '<div class="embossed" style="position: absolute; color: {class_color}; top: {class_label_x}px; left: {class_label_y}px; font-size: 150%"><b>{label_symbol}-{class_label}</b></div>'
