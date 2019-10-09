import discord



def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()



@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("tim") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="NO STOP THAT")


@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await channel.send(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):

    id = client.get_guild(444179224643895318)
    channels = ["commands"]
    valid_users = ["REDACTED#3682"]
    bad_words = ["bad", "stop", "45"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)

    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi") 
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")


client.run(token)
