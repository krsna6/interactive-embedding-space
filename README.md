# Embed interactive audio in a 2D space

This script takes a CSV file with 2D embedding space details with corresponding audio files and creates a interactive webpage for visualization.  
Created with help from [Alan Cowen](https://www.alancowen.com/bio) with original example [here](https://www.alancowen.com/music). 

If used please cite "Somandepalli, K. & Cowen, A. S. (2020). A simple python wrapper to generate embedding space with interactive audio using HTML and JS. https://doi.org/10.5281/zenodo.4047184". 


Examples created using this script: [Speech commands](https://sail.usc.edu/~somandep/maps/command_id_2.html) and [Speaker embeddings](https://sail.usc.edu/~somandep/maps/speaker_id.html)  

## Step 0: Preparation   
1. Make sure that you are using python 3+ and packages in the requirements (pandas and numpy) are installed.
2. Copy the `map_files` directory in this repository to your target webpage

## Step 1: Create CSV file  
Add all the details of the files' physical location as well as the 2D coordinates to a CSV file as shown below. Important to keep the same header names.  

| x      | y      | file                                                                                | label | class |
|--------|--------|-------------------------------------------------------------------------------------|-------|-------|
| -32.25 | 6.11   | https://sail.usc.edu/~somandep/maps/speech_commands_data/bed_652b3da7_nohash_2.wav  | bed   | 0     |
| -57.77 | -27.33 | https://sail.usc.edu/~somandep/maps/speech_commands_data/bird_e0344f60_nohash_1.wav | bird  | 1     |

## Step 2: Run `plot_interactive_audio_tsne.py` as below:
```
usage: plot_interactive_audio_tsne.py [-h]
                                      tsne_file title description output_file

Plot interactive audio in 2D space.

positional arguments:
  tsne_file    Location of the CSV file with plot details.
  title        Title of the plot.
  description  Description of the plot.
  output_file  Output HTML file.

optional arguments:
  -h, --help   show this help message and exit
```

> Example usage: `python plot_interactive_audio_tsne.py speech_commands_plot.csv 'MY TITLE' 'MY DESCRIPTION' output.html`

Finally, copy `map_files` and `output.html` to target webpage directory and visualize [examples like this](https://sail.usc.edu/~somandep/maps/command_id_2.html#modal).
