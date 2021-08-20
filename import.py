import requests
import os
import sys
from dotenv import load_dotenv
import time

load_dotenv()

print("Import a valid logs.beemo.gg url")
url = input()

print("\n Checking you have a valid .env file with a key...")

if os.getenv("key") is None:
      print("\n\033[91m##################################################################")
      print("You do not have a DDUB token. Please add one to the .env file!")
      print("##################################################################\033[0m")
      sys.exit()

print("\n Key OK")

print("\n Removing old logs...")

try:
   os.remove("cache.txt")
except:
   print("\n cache.txt file wasn't found, this is probably your first time using this script...")

print("\n Getting ready to fetch requested url")

h = {
    'User-Agent': 'ddub mass import (+https://discord.riverside.rocks)'
}

response = requests.get(url, headers=h)

cache = open("cache.txt", "a")
cache.write(response.text)
cache.close()

print("\033[92m Running the report script, reporting to Discord Dangerous User Database. This may take a few minutes depending on the size of the log file.\033[0m")

time.sleep(3.5)

os.system("python3 report.py")

print("\n Done, thanks for cleaning up Discord!")
