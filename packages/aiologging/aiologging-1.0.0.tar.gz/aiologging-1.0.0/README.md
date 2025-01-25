# aiologging #

## What is this? ##
**aiologging** - asynchronous module for logging asynchronous applications.

#### Starting from version 2.0.0, logs will be written to a file and output to "print", specifying this in "aiologging.Logger()", before version 2.0.0 they were output only in "print()". ####

## Quick Guide

---

**Connecting the module:**
> import aiologging

---

**Getting the logger:**
> logger = aiologging.Logger(name="logger name")

The 'name=' parameter is optional, the default value is 'root'.

---

**Logging:**
> await logger.log(level, message)

> await logger.log(2, message) # level = INFO (int)

> await logger.log("INFO", message) # level = INFO (str)

> await logger.log(aiologging.INFO, message) # level = INFO (int)

> from aiologging import NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
> await logger.log(INFO, message) # level = INFO (int)

Replace 'INFO' or '2' with the desired int/str level.

level is 'str' or 'int'.

| str | int |
|--|--|
| CRITICAL, FATAL | 5 |
| ERROR | 4 |
| WARNING, WARN | 3 |
| INFO | 2 |
| NOTSET | 0 |
| DEBUG | 1 |

---

### the records have the following format: ###
> 2025-01-18 16:10:16.271609 :: NAME :: LEVEL :: MESSAGE

**2025-01-18 16:10:16.271609 - date and time of the log.**
**NAME - the name of the logger, by default 'root'.**
**LEVEL - log level (NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL).**
**MESSAGE - the log message.**

---

# Other functions #

---

> async def levelToName(level: int):

Accepts level in 'int' and returns 'str' the name of the level (2 - "INFO")

---

> async def nameToLevel(level: str):

Accepts level name in 'str' and returns 'int' the number of the level ("INFO" - 2)

---

> async def log(time, name, level: str, msg):

It is used for recording or outputting logs via "Logger.log()". It is not recommended to use it outside of the class

---

# Global variables #

---

CRITICAL = 5
FATAL = CRITICAL
ERROR = 4
WARNING = 3
WARN = WARNING
INFO = 2
DEBUG = 1
NOTSET = 0

---

_levelToName = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET',
}

---

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

---