import discord
from myclient import gainers
from myclient import losers
from myclient import sectors
from myclient import scanner


class TheClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
# Help Command
        if message.content == 'help':
            embedVar = discord.Embed(
                title="Commands", description="", color=0x000000)
            embedVar.add_field(
                name="gainers", value="Shows todays largest movers", inline=False)
            embedVar.add_field(
                name="losers", value="Shows todays largest losers", inline=False)
            embedVar.add_field(
                name="sectors", value="Shows today's sector performances", inline=False)
            await message.channel.send(embed=embedVar)

# Gainers
        if message.content == 'gainers':
            await message.channel.send("```Gainers```")
            msg = ""
            df = gainers()[['ticker', "changesPercentage",
                            "price", "companyName"]]
            for index, row in df.iterrows():
                msg = msg + row["changesPercentage"] + " - " + \
                    row["ticker"] + " - " + row["companyName"][0: 25]+"\n"
            await message.channel.send("```"+msg+"```")
# Losers
        if message.content == 'losers':
            await message.channel.send("```Losers```")
            msg = ""
            df = losers()[['ticker', "changesPercentage",
                           "price", "companyName"]]
            for index, row in df.iterrows():
                msg = msg + row["changesPercentage"] + " - " + \
                    row["ticker"] + " - " + row["companyName"][0: 25]+"\n"
            await message.channel.send("```"+msg+"```")

# Sectors
        if message.content == 'sectors':
            await message.channel.send("```Sectors```")
            msg = ""
            df = sectors()[['sector', "changesPercentage"]]
            df = df.sort_values(by=["changesPercentage"][0: 4])
            for index, row in df.iterrows():
                msg = msg + "(" + row["changesPercentage"] + \
                    ") - " + row["sector"]+"\n"
            await message.channel.send("```"+msg+"```")

# Scanner
        if message.content == 'scanner':
            df = scanner()[['symbol', 'price', 'changesPercentage', 'yearHigh',
                            'yearLow', 'marketCap', 'volume', 'avgVolume', 'dayLow', 'dayHigh']]
            # Calculated Colmuns
            df['percentFromHigh'] = df['yearHigh']/df['price']
            df['percentFromLow'] = df['yearLow']/df['price']
            df['priceDelta'] = df['dayHigh']/df['dayLow']

            # Sending Message
            embedVar = discord.Embed(
                title="Commands", description="", color=0x000000)
            embedVar.add_field(
                name="gainers", value="Shows todays largest movers", inline=False)
            print(stock)


client = TheClient()
client.run('NjIxMTkyNDA2OTI2MjI5NTE0.XXhwgw.zlqVMwEOylAjJgYHnda2VvgQpYU')
