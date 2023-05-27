import discord
from discord.ext import commands
import random

TOKEN = 'your_token_here'
SCANLATOR_ROLE = 'Scanlator'

bot = commands.Bot(command_prefix='!')

font_lists = {
    'serif': [
        {'font': 'Times New Roman', 'link': 'https://link_to_font1'},
        {'font': 'Georgia', 'link': 'https://link_to_font2'},
        {'font': 'Baskerville', 'link': 'https://link_to_font3'},
        {'font': 'Palatino', 'link': 'https://link_to_font4'}
    ],
    'sans-serif': [
        {'font': 'Arial', 'link': 'https://link_to_font1'},
        {'font': 'Helvetica', 'link': 'https://link_to_font2'},
        {'font': 'Verdana', 'link': 'https://link_to_font3'},
        {'font': 'Calibri', 'link': 'https://link_to_font4'}
    ],
    'monospace': [
        {'font': 'Courier New', 'link': 'https://link_to_font1'},
        {'font': 'Consolas', 'link': 'https://link_to_font2'},
        {'font': 'Monaco', 'link': 'https://link_to_font3'},
        {'font': 'Inconsolata', 'link': 'https://link_to_font4'}
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
            await ctx.send(f'I suggest using "{font_name}" for {font_type} fonts. Link: {link}')
        else:
            await ctx.send(f'Sorry, I don\'t have any suggestions for "{font_type}".')
    else:
        await ctx.send(f'Can\'t access the link. Make sure you have the {SCANLATOR_ROLE} role.')

bot.run(TOKEN)
