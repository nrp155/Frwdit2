#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) DARK EMPIRE

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "4608228"))
    API_HASH = os.environ.get("API_HASH", "7d2ccae297d9bddc2c1a704f4db9051a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6946445545:AAFi7Pi8QZhWU8sDRIVn3DPGEZpRPRan7cU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "-1001416144010")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "1553961614")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION" , "")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001390161207"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
