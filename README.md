# get-artist-lyrics

## About
**I do not own the lyrics and images, this work is for educational purposes.**

The script helps to get all lyrics from an album by Artist. The current example uses Taylor Swift albums.

<img width="679" alt="Screen Shot 2022-07-23 at 4 27 03 PM" src="https://user-images.githubusercontent.com/109247582/180623363-d671d86a-07a9-40da-88e2-fafc59bf13c4.png">

## Setup
1. Go to [API Client Genius](https://genius.com/api-clients).
2. Generate an Access Token.
3. Copy the Access Token [here](https://github.com/abiicodes/get-artist-lyrics/blob/0f7416d57fa0df877da6823196a06bd498a7cefb/src/main.py#L35).
4. Change Artist name [here](https://github.com/abiicodes/get-artist-lyrics/blob/0f7416d57fa0df877da6823196a06bd498a7cefb/src/main.py#L36).
5. Add albums name [here](https://github.com/abiicodes/get-artist-lyrics/blob/0f7416d57fa0df877da6823196a06bd498a7cefb/src/main.py#L4).
6. Go to Images and add album images, add it with the following format:
   - If your album name is: *"Red Taylor's version"*
   - Then, you should save your image as folllows: *"redtaylor'sversion.jpg"*
7. Add colors [here](https://github.com/abiicodes/get-artist-lyrics/blob/0f7416d57fa0df877da6823196a06bd498a7cefb/src/main.py#L16), albums names should mach in both [here](https://github.com/abiicodes/get-artist-lyrics/blob/0f7416d57fa0df877da6823196a06bd498a7cefb/src/main.py#L4) and with colors keys.
8. You can check this link to see [more colors in RGB format](https://www.webucator.com/article/python-color-constants-module/).
9. Run `py main.py`, `python main.py`, or `python3 main.py`.

## Future Updates
* Delete duplicated songs.
* Format song names.

* Add validations.
