import Adafruit_DHT

DHT_69 = Adafruit_DHT.DHT11
DHT_JOL = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_69, DHT_JOL)

    if humidity is not None and temperature is not None: 
        print("Suhu Ruangan={0:0.1f}*C  Kelembapan={1:0.1f}%".format(humidity, temperature))
    else:
        print("Lost Data")
