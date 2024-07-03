import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(BASE_DIR)

env_path = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(env_path)
env = environ.Env()
