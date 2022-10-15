from pypresence import Presence
import psutil
import time 
import configparser


config: configparser.RawConfigParser = configparser.RawConfigParser() #Initialises our config parser.
config.read("config.properties") #Looks for config.properties in source & reads it.

CLIENT_ID: str = config.get('APPID', 'ID')
RPC = Presence(CLIENT_ID)
RPC.connect()




def main() -> None: 
      while True:
          cpu = psutil.cpu_percent()
          ram = psutil.virtual_memory().percent
          core = psutil.cpu_count()
          RPC.update(state=f"CPU Usage: {cpu}% RAM Usage: {ram}%", details=f"Cores: {core}")
          time.sleep(5)

if __name__ == "__main__":
  main()