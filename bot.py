import discord
from discord.ext import commands
from system import logger
from server import Minecraft
from dotenv import load_dotenv
from os import getenv
from requests import get, post


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
                response = post(getenv('START_URL'), headers={"x-api-key": getenv('API_KEY')})
                if response.status_code == 200:
                    await context.send("Iniciando o servidor")
                else:
                    await context.send("Não foi possível iniciar o servidor. Tente novamente mais tarde. Erro:" + str(response.status_code))

            case "stop":
                response = post(getenv('STOP_URL'), headers={"x-api-key": getenv('API_KEY')})
                
                if response.status_code == 200:
                    await context.send("Iniciando o servidor")
                else:
                    await context.send("Não foi possível iniciar o servidor. Tente novamente mais tarde. Erro:" + str(response.status_code))

            case "restart":
                pass

            case "list":
                pass
    except Exception:
        await context.send("Utilização incorreta do comando. Para ler sobre o comando, digite 'mc!help'")


bot.run(getenv('BOT_TOKEN'))
