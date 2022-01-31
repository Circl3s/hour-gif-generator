# Hour GIF Generator
Generate meme GIFs in which an image you choose can be viewed by the user only after they wait a whole hour.
## Installing
Clone this repository and make sure you have Pillow installed.
```
# git clone https://github.com/Circl3s/hour-gif-generator.git
# pip install Pillow
```
## Usage
Run the Python script and specify the target "reward" image.
```
// Windows
# py hour_gif.py path/to/image.jpg
// Other
# python hour_gif.py path/to/image.jpg
```
The script will prompt you to enter a caption for your image. That's what the "reward" will be referred to by the countdown. For example if you choose a picture of a cute dog you want the caption to be "Cute dog", then the countdown will read "Cute dog in 0:59:59".
## RAM
Running this script will take up 4-5GB of RAM to generate 3600 frames at a decent enough resolution. I am currently looking into lowering the RAM usage.
