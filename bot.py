if __name__ == "__main__":
    import discord
    from discord.ext import commands, tasks
    from system import system
    from server import Minecraft

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=".", intents=intents, help_command=None)

    @bot.event
    async def on_ready():
        print("Logado como ", bot.user)
        await check_con.start()

    @tasks.loop(seconds=60)
    async def check_con():
        system.check_connection()

    @bot.command()
    async def status(context):
        mine = Minecraft("grupocycle.ddns.net", 25566)
        await context.send(await mine.info())

    @bot.command()
    async def help(context):
        context.send("help")

    bot.run("MTA3MzYwNDM5Mzg4ODM4NzExMg.Gzxs8Q.Y6HiFcDb4Wg2_lfel4X-uJk3DCpjuf_Ky8v7Es")
