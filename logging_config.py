import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    handlers =[
                        logging.StreamHandler(),
                        logging.FileHandler("app.log")
                    ])