import discord
import requests
import json

from discord.ext import tasks, commands
from utils import *

class FixerioRequest(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.get_symbols()
        self.update_forex.start()

    def get_forex(self):
        forex_url = "http://data.fixer.io/api/latest?access_key={}".format(utility.get_api_key("fixerio"))
        forex = requests.get(forex_url).json()
        with open('libraries/fixerio_rates.json', 'w') as f:
            json.dump(forex, f, indent=4)
        return forex['timestamp']

    def get_symbols(self):
        symbols_url = "http://data.fixer.io/api/symbols?access_key={}".format(utility.get_api_key("fixerio"))
        symbols = requests.get(symbols_url).json()
        with open('libraries/fixerio_symbols.json', 'w') as f:
            json.dump(symbols, f, indent=4)

    @tasks.loop(hours=1)
    async def update_forex(self):
        with open('libraries/fixerio_logs.txt', 'a+') as f:
            f.write('\n{}'.format(utility.unix_to_utc(self.get_forex())))

    @update_forex.before_loop
    async def wait_for_ready(self):
        await self.client.wait_until_ready()


class Forex(commands.Cog):

    def __init__(self, client):
        self.client = client

    def read_cache(self, arg1, arg2='rates'):
        with open('libraries/fixerio_rates.json', 'r') as f:
            data = json.load(f)
        return data[arg2][arg1]

    def get_symbol_name(self, symbol):
        with open('libraries/fixerio_symbols.json', 'r') as f:
            data = json.load(f)
        return data['symbols'][symbol]

    def convert_currency(self, value: float, base_currency: str, target_currency: str):
        base = self.read_cache(base_currency.upper())
        target = self.read_cache(target_currency.upper())
        return (value * target) / base

    @commands.command(aliases=['exchange'])
    async def forex(self, ctx, value: float, base, to, target):
        converted_value = self.convert_currency(value, base, target)
        base_name = self.get_symbol_name(base.upper())
        target_name = self.get_symbol_name(target.upper())
        exchange_rate = self.convert_currency(1.0, base, target)
        desc = 'Converting {} {:.2f} to {}'.format(base.upper(), value, target.upper())
        with open('libraries/fixerio_rates.json', 'r') as f:
            data = json.load(f)
        time = utility.unix_to_utc(data['timestamp'])
        embed = discord.Embed(title='Foreign Exchange', description=desc)
        embed.set_author(name='Stan', url=constants.bot_url, icon_url=str(self.client.user.avatar_url))
        embed.add_field(name='Converted value', value='{} {:.2f}'.format(target.upper(), converted_value), inline=False)
        embed.add_field(name="Exchange Rate", value='{}'.format(exchange_rate), inline=False)
        embed.add_field(name='Exchange Path', value='{} to {}'.format(base_name, target_name), inline=False)
        embed.add_field(name="As of", value='{} (UTC)'.format(time), inline=False)
        embed.set_footer(text="Forex data provided by fixer.io")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Forex(client))
    #client.add_cog(FixerioRequest(client))
    print("forex module loaded")
