import discord
from discord.ext import commands, tasks
from mcstatus import JavaServer
from os import system, popen


async def minecraft_server_info():
    try:
        server = await JavaServer.async_lookup("cs16redirect.servegame.com:25566")
        server_status = await server.async_status()
        players_list = []

        if server_status.players.sample:
            for player in server_status.players.sample:
                players_list.append(player.name)
        else:
            players_list = "Ninguém online no momento..."

        output = f"```Servidor: {server_status.description} 👻\n" \
                f"Endereço: {server.address[0]}:{server.address[1]}\n" \
                f"Latência: {int(server_status.latency)}ms\n" \
                f"Players online: {players_list}```\n"

    except TimeoutError:
        output = "O servidor não está online no momento. Inicie o servidor com o comando '.start'"

    except WindowsError as E:
        output = "O servidor não está funcionando.\n Erro: {}".format(E)

    except Exception as E:
        output = "Aconteceu algo de errado, contate o admin.\n Erro: {}".format(E)

    return output


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=".", intents=intents, help_command=None)

    @bot.event
    async def on_ready():
        print("Logado como ", bot.user)
        await check_con.start()

    @tasks.loop(seconds=900)
    async def check_con():
        a = system("ping -n 10 www.google.com.br")
        if a != 0:
            popen("shutdown /r /t 1")

    @bot.command()
    async def status(ctx):
        await ctx.send(await minecraft_server_info())

    @bot.command()
    async def help(ctx):
        await ctx.send("```Olá️! Os comandos disponíveis atualmente são:\n"
                       ".status -> exibe o status atual do servidor;\n"
                       ".start -> inicia o servidor, se não estiver ligado.```")

    @bot.command()
    async def dev_help(ctx):
        if ctx.author.id == 292750276048191488:
            await ctx.send("```Olá, dev! Os comandos disponíveis atualmente são:\n"
                           ".status -> exibe o status atual do servidor;\n"
                           ".start -> inicia o servidor, se não estiver ligado;\n"
                           ".stop -> desliga o servidor, se estiver ligado;\n"
                           ".anydesk -> inicia o anydesk;\n"
                           ".restart_pc -> reinicia o computador.```")

    @bot.command()
    async def anydesk(ctx):
        if ctx.author.id == 292750276048191488:
            await ctx.send("Iniciando anydesk")
            system('cd C:/Program Files (x86)/AnyDesk && "./AnyDesk.exe"')

    @bot.command()
    async def restart_pc(ctx):
        if ctx.author.id == 292750276048191488:
            await ctx.send("Reiniciando sistema")
            system("shutdown /r /t 1")

    @bot.command()
    async def start(ctx):
        c = popen('tasklist /fi "WINDOWTITLE eq Minecraft Server"').read()
        d = popen('tasklist /fi "IMAGENAME eq DUC40.exe"').read()
        if "javaw.exe" in c:
            await ctx.send("Ops! O servidor já está online!")
        elif "nenhuma" in c:
            await ctx.send("Iniciando servidor")
            popen('cd "C:/Users/pc/AppData/Roaming/.minecraft 1.8.9 server/" && javaw -jar server.jar -XX:+UseG1GC '
                  '-Xmx4G -Xms4G -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+UnlockExperimentalVMOptions '
                  '-XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 '
                  '-XX:G1HeapRegionSize=32M')
        if "nenhuma" in d:
            popen('cd "C:/Program Files (x86)/No-IP" && "DUC40.exe"')


    @bot.command()
    async def stop(ctx):
        if ctx.author.id == 292750276048191488:
            c = popen('tasklist /fi "WINDOWTITLE eq Minecraft Server"').read()
            d = popen('tasklist /fi "IMAGENAME eq DUC40.exe"').read()
            if "javaw.exe" in c:
                await ctx.send("Desligando o servidor")
                system("taskkill /F /im javaw.exe")
            else:
                await ctx.send("Ops! O servidor não está online!")

            if "DUC40.exe" in d:
                system("taskkill /F /im DUC40.exe")

    bot.run("MTA3MzYwNDM5Mzg4ODM4NzExMg.Gzxs8Q.Y6HiFcDb4Wg2_lfel4X-uJk3DCpjuf_Ky8v7Es")

# printar log do servidor
# desligar o servidor automaticamente se ninguém estiver conectado a mais de 30 minutos
