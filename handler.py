from dotenv import load_dotenv
from pathlib import Path

load_dotenv(verbose=True)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


# def get_env_variable(var_name):
#     """ Get the environment variable or return exception """
#     try:
#         return os.environ[var_name]
#     except KeyError:
#         raise Exception('Set the {} environment variable'.format(var_name))

# dotenv.read_dotenv('.env')