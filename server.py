from system import logger


class Server:
    def __init__(self, owner: dict, address: str, port: int):
        self._owner = owner
        self._address = address
        self._port = port
        self.server = None

    @staticmethod
    def random_emoji():
        import random

        emoji_list = ["❤️", "😷", "🫡", "🍻", "☠️", "😳", "🦀", "🦈", "🍆", "🌹", 
                      "🐔", "😎", "😈", "😇", "😍", "😘", "😼", "😱", "🤗", "😴", 
                      "🤔", "👾", "✌️", "🤪", "🙃", "😬", "🤷", "😠", "😌", "🍵", 
                      "💫", "🙈", "😉", "🤩", "🥹", "🤭", "🤫", "🤤", "🥱", "🧛"]

        return random.choice(emoji_list)

    def start():
        pass

    def stop():
        pass

    def restart():
        pass

    def info():
        pass


class Minecraft(Server):
    def __init__(self, address: str, port: int):
        self.address = address
        self.port = port
        self.server = None

    async def server_info(self):
        from mcstatus import JavaServer

        try:
            server = await JavaServer.async_lookup(f"{self.address}:{self.port}")
            server_info = await server.async_status()

            self.server = server_info

        except TimeoutError as E:
            logger.error("O servidor não está online no momento. Inicie o servidor com o comando '.start'.\n Erro: {}".format(E))

        except OSError as E:
            logger.error("O servidor não está funcionando.\n Erro: {}".format(E))

        except Exception as E:
            logger.error("Aconteceu algo de errado, contate o admin.\n Erro: {}".format(E))
            raise


    async def info(self):
        await self.server_info()

        players_online = 'Ninguém online no momento...'
        if self.server.players.sample is not None:
            players_online = [player for player in self.server.players.sample]


        return f"```" \
               f"Servidor: {self.server.description} {self.random_emoji()}\n" \
               f"Endereço: {self.address}:{self.port}\n" \
               f"Latência: {int(self.server.latency)}ms\n" \
               f"Players online: {players_online}" \
               f"```\n"
