import pytest
import logging


# Logging setup
def pytest_configure(config):
    logging.basicConfig(filename='logs/test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

