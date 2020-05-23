import requests
import discord

from utils import *
from discord.ext import commands

class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    def api_call(self, city="Dumaguete"):
        api_key = utility.get_api_key("openweathermap")
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        unit = "metric"
        search_url = base_url + "q=" + city + "&units" + unit + "&appid=" + api_key
        response = requests.get(search_url)
        x = response.json()
        if x["cod"] == "404":
            return 404
        if x["cod"] == 401:
            return 401
        return x

    def google_maps(self, lon, lat):
        api_key = utility.get_api_key("google_staticmap")
        base_url = "https://maps.googleapis.com/maps/api/staticmap?"
        center = "{},{}".format(lon, lat)
        size = "400x300"
        zoom = "7"
        request_url = base_url + "center=" + center + "&markers=" + center + "&zoom=" + zoom + "&size=" + size + "&key=" + api_key
        return request_url

    def WeatherMap(self, ctx, arg1):
        x = self.api_call(arg1)
        city = x["name"]
        country = x["sys"]["country"]
        z = x["weather"]
        description = z[0]["description"]
        icon_url = "http://openweathermap.org/img/w/{}.png".format(z[0]["icon"])
        temperature = "%.2f " % round(x["main"]["temp"] - 273.15, 2)  # convert kelvin to Celsius and format float
        humidity = x["main"]["humidity"]
        pressure = x["main"]["pressure"]
        wind_speed = x["wind"]["speed"]
        wind_deg = x["wind"]["deg"]
        cloud = x["clouds"]["all"]
        time = utility.unix_to_utc(x["dt"], x["timezone"])
        lon = x["coord"]["lon"]
        lat = x["coord"]["lat"]
        try:
            rain = x["rain"]["1h"]

        except KeyError:
            rain = None

        try:
            snow = x["snow"]["1h"]
        except KeyError:
            snow = None

        if x["timezone"] >= 0:
            tz = "UTC +" + str(int(x["timezone"]) / 3600)
        else:
            tz = "UTC " + str(int(x["timezone"]) / 3600)
        embed = discord.Embed(title="{}, {}".format(city, country), description=description)
        embed.set_thumbnail(url=icon_url)
        embed.add_field(name="Temperature", value="{}°C".format(temperature), inline=True)
        embed.add_field(name="Pressure", value="{} hPA".format(pressure), inline=True)
        embed.add_field(name="Humidity", value="{}%".format(humidity), inline=True)
        embed.add_field(name="Wind", value="{}m/s, {}°".format(wind_speed, wind_deg), inline=True)
        embed.add_field(name="Cloud Cover", value="{}%".format(cloud), inline=True)
        if rain is not None:
            embed.add_field(name="Rain Volume (in the last hr)", value="{}".format(rain), inline=True)
        if snow is not None:
            embed.add_field(name="Snow Volume (in the last hr)", value="{}".format(snow), inline=True)
        embed.add_field(name="Local Time", value="{} | {}".format(time, tz), inline=False)
        embed.add_field(name="Coordinates", value="[{}, {}]".format(lon, lat), inline=False)
        embed.set_image(url=self.google_maps(lat, lon))
        embed.set_footer(text="Data gathered from https://openweathermap.org/")
        return embed

    @commands.command()
    async def weather(self, ctx, *, city):
        if self.api_call(city) == 404:
            await ctx.send("City not found")
            return
        if self.api_call(city) == 401:
            await ctx.send("API Key not Working")
            return
        await ctx.send(embed=self.WeatherMap(ctx, city))


def setup(client):
    client.add_cog(Weather(client))
    print("weather module loaded")
