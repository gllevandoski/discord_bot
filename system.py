import subprocess


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

    async def check_connection(self):
        from threading import Thread

        Thread(target=self.check_lan_connection, daemon=True).start()
        Thread(target=self.check_wan_connection, daemon=True).start()

    def check_lan_connection(self):
        if self.os == "Linux":
            ping = f"ping -c 3 {self.lan_ip}"
        if self.os == "Windows":
            ping = f"ping -n 3 {self.lan_ip}"

        try:
            from subprocess import CalledProcessError

            pong = subprocess.run(ping, stdout=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            pong.check_returncode()
        except CalledProcessError:
            logger.warning("Conexão à LAN perdida.")

    def check_wan_connection(self):
        if self.os == "Linux":
            ping = f"ping -c 3 {self.wan_ip}"
        if self.os == "Windows":
            ping = f"ping -n 3 {self.wan_ip}"

        try:
            from subprocess import CalledProcessError

            pong = subprocess.run(ping, stdout=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            pong.check_returncode()
        except CalledProcessError:
            logger.warning("Conexão à WAN perdida.")


admins_id = [292750276048191488]
system = System("Windows", "192.168.0.190")
logger = system.setup_logging()
