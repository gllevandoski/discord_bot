import os


class System:
    def __init__(self, os, lan_ip = "192.168.1.254", wan_ip = "www.google.com.br") -> None:
        self.os = os
        self.lan_ip = lan_ip
        self.wan_ip = wan_ip

    @staticmethod
    def return_current_time():
        from datetime import datetime
        return datetime.now().strftime("%y%m%d%H%M%S")

    def setup_logging(self):
        import logging
        logging.basicConfig(handlers=[logging.FileHandler(f"logs/{self.return_current_time()}"),
                                      logging.StreamHandler()], level=logging.DEBUG)
        return logging.getLogger("discord")

    def check_connection(self):
        logger.debug("Testando conexão")

        lan_ping = self.check_lan_connection()
        wan_ping = self.check_wan_connection()

        if lan_ping or wan_ping:
            raise ConnectionError

    def check_lan_connection(self):
        if self.os == "Linux":
            ping = f"ping -c 3 {self.lan_ip}"
        if self.os == "Windows":
            ping = f"ping -n 3 {self.lan_ip}"

        pong = os.system(ping)
        logger.debug(pong)
        return pong

    def check_wan_connection(self):
        if self.os == "Linux":
            ping = f"ping -c {self.wan_ip}"
        if self.os == "Windows":
            ping = f"ping -n 3 {self.wan_ip}"

        pong = os.system(ping)
        logger.debug(pong)
        return pong


admins_id = [292750276048191488]
system = System("Windows")
logger = system.setup_logging()
