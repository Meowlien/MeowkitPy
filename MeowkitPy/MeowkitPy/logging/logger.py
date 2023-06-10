# Flask 下有 app.logger.info()

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Logger():

    def LogInfomation(info: str):
        print(f'   [Debug]: {info}')

    def LogWarning(info: str):
        print(f' ! [Warning]: {info}')

    def LogError(info: str):
        print(f' @ [Error]: {info}')

# Global
log = Logger
