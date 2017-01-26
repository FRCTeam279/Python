import logging
import sys
import time
from networktables import NetworkTables

# uncomment to see debug messages from library regarding status
logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) > 1:
	pref = sys.argv[1]
else:
	print("Error: specify a key to remove!")
	exit(0)
	
NetworkTables.initialize(server='10.2.79.2')


#connecting isn't instant, and getting the table will not error,
# just not return anything and be confusing if you skip waiting...
#print('Waiting to connect...')
while NetworkTables.isConnected() == False:
    time.sleep(0.1)

prefs = NetworkTables.getTable("Preferences")

if prefs.containsKey(sys.argv[1]):
	if prefs.isPersistent(sys.argv[1]):
		prefs.clearPersistent(sys.argv[1])
		print('Persistance Removed from Key: ' + sys.argv[1])
	prefs.delete(sys.argv[1])
	#NetworkTables.
	NetworkTables.flush()
	print('Key removed: ' + sys.argv[1])
else:
	print("Key not found: " + sys.argv[1])

NetworkTables.shutdown()




