import discord
from discord.ext import commands
import random

TOKEN = 
SCANLATOR_ROLE = 'Scanlator'

bot = commands.Bot(command_prefix='!')

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

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

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
            await ctx.send(f'I suggest using "{font_name}" for {font_type}. Link: {link}')
        else:
            await ctx.send(f'Sorry, I don\'t have any suggestions for "{font_type}".')
    else:
        await ctx.send(f'Cant access the link? Make sure you have the {SCANLATOR_ROLE} role.')

bot.run(TOKEN)
