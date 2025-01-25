"""
import aiologging

logger = aiologging.Logger()

logger.log(level, msg)

await logger.log(5, "my CRITICAL message")
await logger.log(4, "my ERROR message")
await logger.log(3, "my WARNING message")
await logger.log(2, "my INFO message")
await logger.log(1, "my DEBUG message")
await logger.log(0, "my NOTSET message")

await logger.log("CRITICAL", "my CRITICAL message")
await logger.log("FATAL", "my CRITICAL message")
await logger.log("ERROR", "my ERROR message")
await logger.log("WARNING", "my WARNING message")
await logger.log("WARN", "my WARNING message")
await logger.log("INFO", "my INFO message")
await logger.log("DEBUG", "my DEBUG message")
await logger.log("NOTSET", "my NOTSET message")

await logger.log(aiologging.CRITICAL, "my CRITICAL message")
await logger.log(aiologging.FATAL, "my CRITICAL message")
await logger.log(aiologging.ERROR, "my ERROR message")
await logger.log(aiologging.WARNING, "my WARNING message")
await logger.log(aiologging.WARN, "my WARNING message")
await logger.log(aiologging.INFO, "my INFO message")
await logger.log(aiologging.DEBUG, "my DEBUG message")
await logger.log(aiologging.NOTSET, "my NOTSET message")

from aiologging import CRITICAL, FATAL, ERROR, WARNING, WARN, INFO, DEBUG, NOTSET

await logger.log(CRITICAL, "my CRITICAL message")
await logger.log(FATAL, "my CRITICAL message")
await logger.log(ERROR, "my ERROR message")
await logger.log(WARNING, "my WARNING message")
await logger.log(WARN, "my WARNING message")
await logger.log(INFO, "my INFO message")
await logger.log(DEBUG, "my DEBUG message")
await logger.log(NOTSET, "my NOTSET message")
"""

import datetime

CRITICAL = 5
FATAL = CRITICAL
ERROR = 4
WARNING = 3
WARN = WARNING
INFO = 2
DEBUG = 1
NOTSET = 0

_levelToName = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET',
}

_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
}

async def levelToName(level: int):
    return _levelToName.get(level)

async def nameToLevel(name: str):
    return _nameToLevel.get(name)

async def log(time, name, level: str, msg):
    print(f"{time} :: {name} :: {level} :: {msg}\n")

async def error_handler(time, name, level: str, msg):
    print(f"{time} :: aiologging.error_handler | logger \'{name}\' :: {level} :: {msg}\n")

class Logger:
    def __init__(self, name="root"):
        self.name = name

    async def log(self, level, msg):
        time = datetime.datetime.now()
        if type(level) == int:
            result = await levelToName(level)
            if result is not None:
                await log(time, self.name, await levelToName(level), msg)
            else:
                await error_handler(time, self.name, await levelToName(ERROR), f"Level \'{level}\' was not found in \'_levelToName\'")
        elif type(level) == str:
            if level in _nameToLevel:
                await log(time, self.name, level, msg)
            else:
                await error_handler(time, self.name, await levelToName(ERROR), f"Level \'{level}\' was not found in \'_nameToLevel\'")
        else:
            await error_handler(time, self.name, await levelToName(ERROR), f"parametr level \'{level}\' is not \'int\' or \'str\'")