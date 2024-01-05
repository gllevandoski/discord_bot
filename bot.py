if __name__ == "__main__":
    import discord
    from discord.ext import commands, tasks
    from system import system, logger
    from server import Minecraft

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="/", intents=intents, help_command=None)
    minecraft_server = Minecraft("grupocycle.ddns.net", 25566)

    @bot.event
    async def on_ready():
        logger.info("Logado como " + bot.user.name)
        await check_con.start()

    @tasks.loop(seconds=60)
    async def check_con():
        await system.check_connection()

    @bot.command()
    async def status(context):
        await context.send(await minecraft_server.info())

    @bot.command()
    async def help(context):
        await context.send("**Olá! 🤗. Lista de comandos disponíveis:**\n"
                           "\n"
                           "`server add <game> <options>`\n"
                           "--game: 'minecraft', 'cs2, 'unturned'\n"
                           "--password: opcional\n"
                           "--public: opcional. Habilite se quiser que seu servidor seja listado com server list public.\n"
                           "\n"
                           "`server list <filters>`\n"
                           "--game\n"
                           "--name")
        
    @bot.command()
    async def server(context, *args):
        try:
            match args[0]:
                case "start":
                    received_arguments = args[1:]
                    validated_arguments = dict()
                    valid_arguments = ["--game", "--config", "--password", "--public"]

                    for argument in received_arguments:
                        if argument in valid_arguments:
                            validated_arguments[argument] = received_arguments[received_arguments.index(argument) + 1]
                    
                    await context.send(validated_arguments)

                case "restart":
                    pass

                case "stop":
                    pass
                
                case "list":
                    pass
        except Exception:
            await context.send("Utilização incorreta do comando. Para ler sobre o comando, digite 'mc!help'")

    bot.run("MTA3MzYwNDM5Mzg4ODM4NzExMg.Gzxs8Q.Y6HiFcDb4Wg2_lfel4X-uJk3DCpjuf_Ky8v7Es")
