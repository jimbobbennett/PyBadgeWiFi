import board
import busio
import adafruit_requests as requests
from connection import Connection

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

conn = Connection()
conn.connect_pybadge(spi, True)

TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"

print("Fetching text from", TEXT_URL)
r = requests.get(TEXT_URL)
print('-'*40)
print(r.text)
print('-'*40)
r.close()

print("Done!")