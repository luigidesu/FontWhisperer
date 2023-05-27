# This bot will send a random font suggestion, along with a link.
# The command is /suggest + a list name.
import discord
from discord.ext import commands
import random

TOKEN = 'Yo token here'
SCANLATOR_ROLE = 'Scanlator'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# This the font list, the font is the name and the link is... the link.
# Make sure the font lists names are in lowercase, it'll make sense later.
font_lists = {
    'List 1': [
        {'font': 'Font 1', 'link': 'https://link_to_font1'},
        {'font': 'Font 2', 'link': 'https://link_to_font2'},
        {'font': 'Font 3', 'link': 'https://link_to_font3'},
        {'font': 'Font 4', 'link': 'https://link_to_font4'}
    ],
    'List 2': [
        {'font': 'Font 1', 'link': 'https://link_to_font1'},
        {'font': 'Font 2', 'link': 'https://link_to_font2'},
        {'font': 'Font 3', 'link': 'https://link_to_font3'},
        {'font': 'Font 4', 'link': 'https://link_to_font4'}
    ],
    'List 3': [
        {'font': 'Font 1', 'link': 'https://link_to_font1'},
        {'font': 'Font 2', 'link': 'https://link_to_font2'},
        {'font': 'Font 3', 'link': 'https://link_to_font3'},
        {'font': 'Font 4', 'link': 'https://link_to_font4'}
    ]
}

# Console nerd stuff
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

# It makes sure the user has the scanlator role.
@bot.command()
async def suggest(ctx, font_type: str):
    member = ctx.author
    scanlator_role = discord.utils.get(member.guild.roles, name=SCANLATOR_ROLE)
    
    font_type = font_type.lower() # Converts the input text into lowercase, useful to avoid creating 20 lists variations.
    
    if font_type in font_lists:
        suggestions = font_lists[font_type]
        suggestion = random.choice(suggestions) # This is the random suggestion
        font_name = suggestion['font']
        link = suggestion['link']
        
        message = f'I suggest using "{font_name}" for {font_type}.\n{link}\n' # This sends a normal message, in case the user has the scanlator role.
        
        if scanlator_role is not None and scanlator_role not in member.roles:
            message += f'Can\'t access the link? Make sure you have the {SCANLATOR_ROLE} role.\nYou can ask for it on https://discord.com/channels/846402995252232232/951959937746083870' # This will send a extra text in case the user does not have the scanlator role.
        
        await ctx.send(message)
    else:
        await ctx.send(f'Sorry, I don\'t have any suggestions for "{font_type}".')  # In case there's no fonts on a list, it'll send this.

bot.run(TOKEN)
