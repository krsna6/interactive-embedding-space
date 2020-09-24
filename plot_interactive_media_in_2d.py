import pandas as pd
import numpy as np
import sys
from collections import OrderedDict
import argparse
import os
from config import *

parser = argparse.ArgumentParser(description='Plot interactive audio in 2D space.')
parser.add_argument('tsne_file', type = str, help = 'Location of the CSV file with plot details.')
parser.add_argument('title', type = str, help = 'Title of the plot.')
parser.add_argument('description', type = str, help = 'Description of the plot.')
parser.add_argument('output_file', type = str, help = 'Output HTML file.')

args = parser.parse_args()

# start with a pandas DataFrame
# must have these columns: 
    # (1) x--dimension 1, e.g., tsne-x 
    # (2) y-- dimension 2, e.g., tsne-y
    # (3) label--a string name for a class
    # (4) class--number for the label (start at 0) 
    # (5) file--location of the mp4/wav file to play audio from 
df = pd.read_csv(args.tsne_file)
for k_ in ['x', 'y', 'label', 'class', 'file']:
    if k_ not in df.keys(): sys.exit('COLUMN HEADERS INVALID')
print('1. column headers valid')

print('2. mapping labels to symbols')
labels = sorted(set(df['label']))
classes = sorted(set(df['class']))
label_dict = OrderedDict(zip(classes, labels))
label_to_symbol_dict = OrderedDict(zip(labels, SYMBOL_LIST[:len(labels)]))
df['symbol'] = [label_to_symbol_dict[l] for l in list(df['label'])]
n_classes = len(classes)

## PREP DATA!
print('3. estimate button locations')
data_map = np.array(df[['x', 'y']]) # Nx2 array
data_map[:,1] = -1*data_map[:,1]
data_map = data_map - np.min(data_map,0) # center data
button_positions = data_map/np.max(data_map,0)*700 + 10
button_positions[:,0] = button_positions[:,0]*1.25 + 50
df['button_0'] = list(button_positions[:,0])
df['button_1'] = list(button_positions[:,1])
# if angles and word locations are prelisted they need to be updated!

## PREPARE TEMPLATE
print('4. prepare templates')
html_part1 = open('plot_sounds_firstpart.html').read()
html_part1 = html_part1.replace('TITLE GOES HERE', args.title)
# (TODO) configure angle words
html_part1.replace('</style>', '\n.ylabel  { -ms-transform: rotate(-90deg); -webkit-transform: rotate(-90deg); transform: rotate(-90deg); transform-origin: top left;}\n</style>');


# RENDER 2D POINTS
print('5. render point items')
all_html_tag_list = []
for index,row in df.iterrows():
    formatted_point = POINT_TEMPLATE.format(item_index = index, 
                                            color_hex = COLOR_LIST[row['class']], 
                                            button_x = row['button_1'],
                                            button_y = row['button_0'], 
                                            file_name = row['file'], 
                                            class_label = row['label'], 
                                            item_symbol = row['symbol'])
    all_html_tag_list.append(formatted_point)

html_tag_str = '\n'.join(all_html_tag_list)

## PLOT LABELS	
print('6. render label items')
label_positions = []
button_pos_mean = np.mean(button_positions,0) #.reshape((1,2))
for label_ix, label in enumerate(labels):
    df_ix = df[df['label']==label]
    button_pos_ix = np.array(df_ix[['button_0', 'button_1']])
    label_positions.append(np.mean(button_pos_ix,0) + (np.mean(button_pos_ix,0) - button_pos_mean)*.4)

all_label_html_tag = []
for label_ix, label in enumerate(labels):
    formatted_label = LABEL_TEMPLATE.format(class_color = COLOR_LIST[label_ix],
                                            class_label_x = label_positions[label_ix][1],
                                            class_label_y = label_positions[label_ix][0],
                                            label_symbol = label_to_symbol_dict[label],
                                            class_label = label)
    all_label_html_tag.append(formatted_label)

label_html_str = '\n'.join(all_label_html_tag)

print('7. append and save as ', args.output_file)
html_final_part = open('plot_sounds_lastpart.html').read()
html_final_part = html_final_part.replace('TITLE GOES HERE', args.title)
html_final_part = html_final_part.replace('DESCRIPTION GOES HERE', args.description)

output_html = '\n'.join([html_part1, html_tag_str, label_html_str, html_final_part])
with open(args.output_file, 'w') as f:
    f.write(output_html)
f.close()
