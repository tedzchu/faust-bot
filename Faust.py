import discord
import Move
from random import randint
from discord.ext import tasks
from time import sleep


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


def read_channel():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[1].strip()


token = read_token()

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


def format_message(guessed_right, got_hit, move_name, move_block):
    return "{right} blocked {move} {block}, {conjunction} {wrong} {plural} playing on delay-based netcode!".format(
        move=move_name,
        block=move_block,
        conjunction=("and" if guessed_right == got_hit or got_hit == 0 else "but"),
        right=("No one" if guessed_right == 0 else guessed_right),
        wrong=("no one" if got_hit == 0 else got_hit),
        plural=("are" if got_hit > 1 else "is"),
    )


async def results(channel, message_id, move_name, move_block):
    message = await channel.fetch_message(message_id)
    back = 0
    down_back = 0
    for reaction in message.reactions:
        if reaction.emoji == "⬅":
            back = reaction.count - 1
        if reaction.emoji == "↙":
            down_back = reaction.count - 1
    guessed_right = back if move_block == "high" else down_back
    got_hit = down_back if move_block == "high" else back
    message = "Everyone tried to hold forward and got IK'd. Sadge"
    if guessed_right > 0 or got_hit > 0:
        message = format_message(guessed_right, got_hit, move_name, move_block)
    if move_block == "unblockable":
        message = "{move} is unblockable online, try again with better netcode".format(
            move=move_name
        )
    await channel.send(message)


@tasks.loop(hours=24.0)
async def what_could_this_be():
    await client.wait_until_ready()
    channel_id = int(read_channel())
    channel = client.get_channel(channel_id)
    move = Move.list[randint(0, len(Move.list) - 1)]
    bot_message = await channel.send(file=discord.File(move.path))
    await channel.send(
        "What could this be? Guess the mixup by reacting to the image above!"
    )
    await bot_message.add_reaction("⬅")
    await bot_message.add_reaction("↙")
    sleep(3600.0)
    await results(channel, bot_message.id, move.name, move.block)


what_could_this_be.start()
client.run(token)