from dotenv import load_dotenv
from os import getenv


class System:
    @staticmethod
    def return_current_time():
        from datetime import datetime
        return datetime.now().strftime("%y%m%d%H%M%S")

    def setup_logging(self):
        import logging
        logging.basicConfig(handlers=[logging.FileHandler(f"logs/{self.return_current_time()}"),
                                      logging.StreamHandler()], level=logging.DEBUG)
        return logging.getLogger("discord")


load_dotenv()
admins_id = getenv('ADMINS_ID')
system = System()
logger = system.setup_logging()
