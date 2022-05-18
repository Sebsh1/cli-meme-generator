# cli-meme-generator
A command-line tool for creating memes of common formats.  

## Features
* Supports the classic meme format with toptext/bottomtext.
* Adding your own image macros is as simple as adding them to the `data/images` folder.
* "Deep-Frying" of memes inspired by [r/deepfriedmemes](https://www.reddit.com/r/DeepFriedMemes/).

## How to use
Arguments:

* `--meme` or `-m`: The name or partial name of the template you want.
* `--toptext` or `-t`: Text at the top of the meme. Leave out if you only want bottom text.
* `--bottomtext` or `-b`: Text at the bottom of the meme. Leave out if you only want top text.
* `--deepfry` or `-df`: For when you want your meme way past well done.

Example of meme creation:
```
python create_meme.py -m one-does-not -t 'One does not simply' -b 'Give an example'
```
creates the following meme:  
![Example Meme](example.jpg)

## TODO
* Include support for the newer meme formats with text in non-standard locations, like the Distracted Boyfriend format.
* Add more meme templates and in higher resolution.
