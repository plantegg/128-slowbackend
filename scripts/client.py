#!/usr/bin/env python3

import time
import requests
import signal
import sys

# Define the signal handler
def signal_handler(sig, frame):
    print(f'Signal({sig}) received, exiting...')
    sys.exit(0)

# Register the signal handler for SIGINT and SIGTERM
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

while True:
    try:
        start = time.time()
        r = requests.get('http://nginx/ping', timeout=(3, 10))
        spend = int((time.time() - start) * 1000)
        r.raise_for_status()
        print(f'{time.strftime("%Y-%m-%dT%H:%M:%S")} OK {spend}ms {r.content.decode("utf-8")}')
    except requests.HTTPError as err:
        print(f'{time.strftime("%Y-%m-%dT%H:%M:%S")} HTTP error: {err}')
    except Exception as err:
        print(f'{time.strftime("%Y-%m-%dT%H:%M:%S")} Error: {err}')
    time.sleep(0.1)
