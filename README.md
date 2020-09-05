# Faust-Bot

![236P](http://www.dustloop.com/wiki/images/1/16/GGXRD_Faust_WhatCouldThisBe.png)

###### AKA 236P Simulator - What Could This Be?

I wanted to make a bot out of a game we play in Discord by sending fighting game moves under spoiler tags and guessing if it's high or low. Some work better than others and obviously do not translate from actual fighting game to this game, but hey it killed a few hours for me.

## Prerequisites

Built using [discord.py 1.5](https://discordpy.readthedocs.io/en/latest/index.html) API and a little brain juice. Read the docs there and understand [Messages](https://discordpy.readthedocs.io/en/latest/api.html?highlight=reactions#message) and [Reactions](https://discordpy.readthedocs.io/en/latest/api.html?highlight=reactions#reaction).

Yes this is in Python 3. I specifically used 3.8.4 and am unsure if older versions are supported. Check the `discord.py` docs, they would probably know.

I stored all my images in the `/img` directory in this repo, and manually added them in [`Move.list`](https://github.com/tedzchu/faust-bot/blob/master/Move.py#L10). You can probably spend some time setting up a store with the data required and making calls to populate that list instead. This is a TODO for me if I remember to look at this again sometime.

## Getting Started

These are steps for a Windows machine, so some of the Python commands will differ on other OSes.

1. `git clone` or download project and add a `token.txt` where the first line is just your bot token.

2. Navigate to the `faust-bot` directory in your command line.

3. Run `python -m venv bot-env`

4. Run `bot-env/Scripts/activate.bat`

5. Run `pip install -U discord.py`

6. Start up the bot by running `py -3 Faust.py`

7. (Optional) Adjust `loop` and `sleep` times. Currently defaulting to 24 hour wait times in between images with 1 hour to guess on each one.

## TODOs

- Move images to database and populate move data that way
- Properly implement command grabs (⬆️) and left-rights (➡️)
- Clean up main file so it doesn't make me sad, but that would require thinking a lot about Python on a weekend

## Screenshots

![Sure hope Twitter embeds stay forever](https://pbs.twimg.com/media/EhIpdpJVgAAWo4Z?format=png&name=small)

![Millia 6K online Sadge](https://pbs.twimg.com/media/EhIr1uFUMAIPGvz?format=png&name=small)
