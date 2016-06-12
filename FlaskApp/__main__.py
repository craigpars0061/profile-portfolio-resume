#!/usr/bin/env python3

from Flask import Flask

app = Flask(__name__)
from app import views
