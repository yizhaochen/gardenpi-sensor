# import subprocess
# import time
# import board
# import adafruit_dht
import Adafruit_DHT as dht

def read_dht(pinno):

    sensor = dht.DHT11

    h, tc = dht.read_retry(sensor, pinno)
    return (tc, tc * (9/5) + 32, h)

print(read_dht(16))
# def kill_pulsein_process():
#     process = subprocess.run(['pgrep', 'libgpiod_pulsei'], capture_output=True, text=True)
#     if process.stdout != '':
#         plist = process.stdout.split('\n')
#         for process in plist:
#             if process != '':
#                 print('killing', process)
#                 _ = subprocess.run(['kill', process])
#                 time.sleep(2.0)
#     # print(process.stdout.split('\n'))


# def read_DHT(pinno):
#     """ Reads the humidity/moisture sensor given the pin number as a string
#         Returns tuple(temp, humidity)
#     """
#     dht_sensor = adafruit_dht.DHT11(board.__dict__[pinno])
#     try:
#         temp_c = dht_sensor.temperature
#         temp_f = temp_c * (9/5) +32
#         humidity = dht_sensor.humidity
#         print(f'Temp: {temp_f}F   Humidity: {humidity}')
#         return (temp_f, humidity)
#     except RuntimeError as err:
#         print(err.args[0])
#         if err.args[0] == 'Timed out waiting for PulseIn message':
#             kill_pulsein_process()
#             time.sleep(1)
#         if err.args[0] in ['A full buffer was not returned. Try again.', 'A full buffer was not returned. Try Again']:
#             time.sleep(2)
#         return read_DHT(pinno)
#         
# print(read_DHT('D16'))
# kill_pulsein_process()
