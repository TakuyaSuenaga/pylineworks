#!/usr/bin/env python3

import os
from os.path import join, dirname
from dotenv import load_dotenv


load_dotenv(verbose=True)
load_dotenv(join(dirname(__file__), ".env"))

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
SERVICE_ACCOUNT = os.environ.get("SERVICE_ACCOUNT")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
DOMAIN_ID = os.environ.get("DOMAIN_ID")
ADMINISTRATOR = os.environ.get("ADMINISTRATOR")
CALENDAR_MEMBER_ID = os.environ.get("CALENDAR_MEMBER_ID")
