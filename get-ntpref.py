import logging
import sys
import time
from networktables import NetworkTables

# uncomment to see debug messages from library regarding status
#logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) > 1:
    pref = sys.argv[1]
else:
    pref = ''

NetworkTables.initialize(server='10.2.79.2')

#connecting isn't instant, and getting the table will not error,
# just not return anything and be confusing if you skip waiting...
#print('Waiting to connect...')
while NetworkTables.isConnected() == False:
    time.sleep(0.1)

prefs = NetworkTables.getTable("Preferences")

if len(sys.argv) < 2:
    keys = prefs.getKeys()
    for key in keys:
        val = prefs.getValue(key, '')
        print(key + ": " + str(val))
else:
    if prefs.containsKey(sys.argv[1]):
        val = prefs.getValue(sys.argv[1], '')
        print(sys.argv[1] + ": " + str(val))
    else:
        print("Key not found: " + sys.argv[1])

NetworkTables.shutdown()


