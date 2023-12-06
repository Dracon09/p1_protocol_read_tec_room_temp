import logging


def configure_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.StreamHandler(),
                            logging.FileHandler('logfile.txt')
                        ])

    # Optionally, you can add more configuration or customizations here
