#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("22336547"))
API_HASH = getenv("1e6fcd73ada729e6917bfe05456d1ceb")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("6061921084:AAFVT2IG5C5DzodcXjuEu9w8JUg1G6R5J_E")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "5879188380").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("-1001650917260"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to my Personal Assistant Bot",
)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Musicbot58:93529352@cluster0.n6wscri.mongodb.net/?retryWrites=true&w=majority")
