import discord
from discord.ext import commands
from system import logger
from server import Minecraft
from dotenv import load_dotenv
from os import getenv


load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents, help_command=None)
minecraft_server = Minecraft(getenv('SERVER_IP'), getenv('SERVER_PORT'))


@bot.event
async def on_ready():
    logger.info("Logado como " + bot.user.name)

@bot.command()
async def status(context):
    await context.send(await minecraft_server.info())

@bot.command()
async def help(context):
    await context.send("**Olá! 🤗. Lista de comandos disponíveis:**\n"
                        "\n"
                        "`server add <game> <options>`\n"
                        "--game: 'minecraft'. (soon also: 'cs2', 'unturned', etc)\n"
                        "--password: opcional\n"
                        "--public: opcional. Habilite se quiser que seu servidor seja listado com o comando 'server list public'.\n"
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


bot.run(getenv('BOT_TOKEN'))
