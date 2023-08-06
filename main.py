import enum
import random
from re import A
import typing
import discord 
from discord.ext import commands
from discord import app_commands

TOKEN = '' #add your bot token here

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents) 

#I think this part is not necessary anymore, but it might be I dunno
async def has_scanlator_role(member):
    role = discord.utils.get(member.roles, name=SCANLATOR_ROLE)
    return role is not None

# Console nerd stuff
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------------------------------')

def has_scanlator_role(ctx):
    return discord.utils.get(ctx.author.roles, name=SCANLATOR_ROLE) is not None

# This the font lists, Use this format "{'font': 'NAME', 'link': 'LINK', 'image': 'IMAGE_LINK'},"
font_lists = {
    'list 1': [{'font': 'Font 1', 'link': 'Link 1', 'image': 'Image Link 1'},
        {'font': 'Font 2', 'link': 'Link 2', 'image': 'Image Link 2'}
    ],
    'list 2': [{'font': 'Font 3', 'link': 'Link 3', 'image': 'Image Link 3'},      
        {'font': 'Font 4', 'link': 'Link 4', 'image': 'Image Link 4'} #Add as many as you want, all the lists names will get updated automatically
]
}

#This part gets the name of the lists automatically, to prevent having a list to change manually
def current_lists() -> typing.List[app_commands.Choice[str]]:
    lists = [app_commands.Choice(name=key, value=key.lower()) for key in font_lists.keys()]
    return lists

async def font_autocompletion(
    interaction: discord.Interaction,
    current: str
) -> typing.List[app_commands.Choice[str]]:
    data = []
    for choice in current_lists():
        if current.lower() in choice.value:
            data.append(choice)
    return data  #this part os the autompletion thing, its in lowercase, I guess you can change it.

#Use bot tree command to send the commands to discord.
@bot.tree.command()
@app_commands.autocomplete(item=font_autocompletion)
async def suggest(interaction: discord.Interaction, item: str):
    scanlator_role_id = 846671524425629756 #This part makes sure the user has the role or not
    member = interaction.guild.get_member(interaction.user.id)
    scanlator_role = discord.utils.get(member.roles, id=scanlator_role_id)
    if not scanlator_role:
        await interaction.response.send_message("Oops! you need the 'SPECIFIC_ROLE' role to use this command. ephemeral=True) #It'll send this in case the user doesn't have an specific role, is using a role ID instead of a role name
        return
    if item.lower() not in font_lists:
        await interaction.response.send_message("Invalid font list. Please choose one from the available font lists.", ephemeral=True) #Just the negative message
        return

    font_list = font_lists[item.lower()]
    random_font = random.choice(font_list)

    font_name = random_font['font']
    font_link = random_font['link']
    font_image = random_font.get('image')

    message_content = f"I suggest using: {font_name} for {item}\nLink: {font_link}" #The actual suggestion message, it's ephemeral to avoid channels spam
    await interaction.response.send_message(message_content, ephemeral=True)
    
    if font_image:
        await interaction.followup.send(content=font_image, ephemeral=True)


bot.run(TOKEN)
