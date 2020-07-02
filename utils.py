import json
from datetime import datetime

class utility:

    def get_api_key(arg1: str):
        with open('api_keys.json', 'r') as f:
            data = json.load(f)
        return data[arg1]

    def is_owner(ctx):
        if ctx.author.id == utility.get_id("special_users", "owner"):
            return True

    def get_id(key1: str, key2: str):
        with open('server_id.json', 'r') as f:
            data = json.load(f)
        return data[key1][key2]

    def unix_to_utc(unix: int, timezone: int):
        time = datetime.utcfromtimestamp(unix + timezone)
        return time

class constants:

    bot_url = 'https://github.com/TristanDBioC/discord-stan'
    version = "1.2.3"
    inv = "https://discord.gg/gcaHu8G"  # invite link
