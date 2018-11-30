import urllib.request
from bs4 import BeautifulSoup
import json
import requests
import tes
import subprocess

# make.pyまでのpathp
subprocess.check_call(['python','make.py'])