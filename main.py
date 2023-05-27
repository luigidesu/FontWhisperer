import discord
from discord.ext import commands
import random

TOKEN = 
SCANLATOR_ROLE = 'Scanlator'

bot = commands.Bot(command_prefix='!')

#This the font list, the font is the name and the link is... the link.
font_lists = {
    'Dialogue': [
        {'font': 'Font 1', 'link': 'https://link_to_font1'},
        {'font': 'Font 2', 'link': 'https://link_to_font2'},
        {'font': 'Font 3', 'link': 'https://link_to_font3'},
        {'font': 'Font 4', 'link': 'https://link_to_font4'}
    ],
    'Narration': [
        {'font': 'Font 1', 'link': 'https://link_to_font1'},
        {'font': 'Font 2', 'link': 'https://link_to_font2'},
        {'font': 'Font 3', 'link': 'https://link_to_font3'},
        {'font': 'Font 4', 'link': 'https://link_to_font4'}
    ],
    'SFX': [
        {'font': 'Font 1', 'link': 'https://link_to_font1'},
        {'font': 'Font 2', 'link': 'https://link_to_font2'},
        {'font': 'Font 3', 'link': 'https://link_to_font3'},
        {'font': 'Font 4', 'link': 'https://link_to_font4'}
    ]
}

#Console nerd stuff
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

#It makes sure the user has the scanlator role.
@bot.command()
async def suggest(ctx, font_type: str):
    member = ctx.author
    scanlator_role = discord.utils.get(member.guild.roles, name=SCANLATOR_ROLE)
    
    if scanlator_role in member.roles:
        if font_type in font_lists:
            suggestions = font_lists[font_type]
            suggestion = random.choice(suggestions)
            font_name = suggestion['font']
            link = suggestion['link']
            await ctx.send(f'I suggest using "{font_name}" for {font_type}. Link: {link}') #Positive suggestion
        else:
            await ctx.send(f'Sorry, I don\'t have any suggestions for "{font_type}".') #Negative suggestion 
    else:
        await ctx.send(f'Cant access the link? Make sure you have the {SCANLATOR_ROLE} role.') #If the user doesn't have the scanlator role it sends this

bot.run(TOKEN)
