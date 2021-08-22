from dudb import DUapi
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("key")

du = DUapi(token=key)

f = open('cache.txt', 'r')
Li = f.readlines()

for l in Li:
   the = l.strip()
   if "Raw IDs:" in the:
      print("[INFO] Skipping 'Raw IDs:' text...")
      not_junk = True
   try:
      if not_junk and the != "":
         du.report(the, "Server Raider [B]") # you can also add your own custom message if you feel like it
   except:
      print("[INFO] Skipping blank/other text...")
