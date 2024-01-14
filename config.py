#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) DARK EMPIRE

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "4608228"))
    API_HASH = os.environ.get("API_HASH", "7d2ccae297d9bddc2c1a704f4db9051a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1879736366:AAEgEsv8L90BmNn5IamLJbQFa2H4AXg-WuY") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", " ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Offcil Chnl:💥 @Subscenelk 💥
Chnl Lnks: https://t.me/Subscenelk 
Grp: https://t.me/SubsceneLk_Chat 
E Mail:  Contact@subscenelk.com 📭
Ste: https://www.subscenelk.com/ 
ste: https://filmsbay.blogspot.com/ 
⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉
❤️ Join ❤️ Share ❤️ Support ❤️. ")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "-1001416144010")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "1553961614")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION" , "BQBGUOQAZgRyHvZn6xcSZK17ZwzjuwOOr8-iBVdWnLkk0pFXpo1mEXKNV0X-IjoKTAs5rCUV4QvTCJlEnj6hVDhUe34XS0OjcqAc5GBpvMUE10KGJlcshnFYjrgnpfLm4rGw0JDk4MLFAiVWuX5vrBlEtSfL7PvxMnRQru2T7MX3-fJcDnKNOnvbVYXXeV3dAhYxSu89YBXBcmM9pqUa6pbLxrWTIE3cLs1JZffbVSBIhgJkAAAIil44R7pDyUBf20kwQKR9Jy9mqfv4TvZ3gEnqgZOXzRpf8XowsAsnv-qVRdtxiPHPdiFbFJs_0vzVBGcxXU8Pt5UF9mkGzbjN_G4RcFJ9fAAAAABwCoAuAQ")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001390161207"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
