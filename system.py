class System:
    def __init__(self, lan_ip = "192.168.1.254", wan_ip = "www.google.com.br") -> None:
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
        Thread(target=self.test_connection, args=(self.wan_ip,), daemon=True).start()
        Thread(target=self.test_connection, args=(self.lan_ip,), daemon=True).start()

    def test_connection(self, address, count: int = 3):
        try:
            import subprocess
            pong = subprocess.run(f"ping -c {count} {address}", stdout=subprocess.DEVNULL, stdin=subprocess.DEVNULL, shell=True)
            pong.check_returncode()
        except subprocess.CalledProcessError:
            logger.warning("Conexão perdida.")


admins_id = [292750276048191488]
system = System("192.168.1.254")
logger = system.setup_logging()
