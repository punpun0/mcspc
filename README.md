# Minecraft Skin Pack Converter

Converts Minecraft Bedrock Edition skin packs to a format the Minecraft Java launcher uses.

# Credits
Big thank you to https://github.com/bs-community/skinview3d
for the project, without it the skins wouldn't have thumbnails!

# Rendering skins
If you want the skin thumbnails to be rendered:
1. Grab the latest geckodriver and place it in the root folder:
    https://github.com/mozilla/geckodriver/releases
2. Install Selenium by typing: 'pip install selenium' in the command line!

# Usage
1. Place your skin pack without its folder (important!) in ./input
2. Run convert.py
3. Program creates a 'launcher_skins.json' file, replace it with the one in %appdata%/.minecraft/

Warning! All of your previous skins will be replaced with the ones in the skin pack.

# UPDATE:

Thumbnails for the skins are now working!
  
 
 ![Showcase](https://i.ibb.co/41yPqsc/Minecraft-Launcher-2-Oo-Jwouiw-G.png)
