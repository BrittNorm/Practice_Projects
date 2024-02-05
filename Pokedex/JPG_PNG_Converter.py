# a simple file converter to convert an image from JPG to PNG as part of zero to mastery projects
# Brttany Normandin 02/05/2024
import sys
import os
from PIL import Image

# grab the first and second argument
image_folder = os.path.abspath(os.path.dirname(sys.argv[0]))
# Place the Pokemon inside a pokeball
output_folder = "Pokeball"

#check is new/ exists, if not create it 
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# loop through Pokedex.
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg"):
    # convert images to png.
        clean_name = os.path.splitext(filename)[0]
    # save to new folder.
        img = Image.open(os.path.join(image_folder, filename))
    #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
        img.save(f'{output_folder}/{clean_name}.png', 'png')
        print('Pokemon Caught!!')

'''
Zero to mastery answer:

import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)
    

for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!!')

'''