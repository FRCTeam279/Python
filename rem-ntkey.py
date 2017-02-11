import logging
import sys
import time
import argparse
from networktables import NetworkTables


#https://docs.python.org/3.3/library/argparse.html
parser = argparse.ArgumentParser(description='Remove a key from a NetworkTable')

parser.add_argument('key')
parser.add_argument('-d', '--debug', action='store_true')
parser.add_argument('-s', '--server', default='10.2.79.2')
parser.add_argument('-nt', '--table', default='Preferences')

args = parser.parse_args(sys.argv[1:len(sys.argv)])



if args.debug:
	print('Setting value')
	print('Server: ' + str(args.server))
	print('Table: ' + str(args.table))
	print('Key: ' + str(args.key))
	print('Debug: ' + str(args.debug))
	
	logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize(server=str(args.server))
while NetworkTables.isConnected() == False:
    time.sleep(0.1)

nt = NetworkTables.getTable(str(args.table))

if nt.containsKey(str(args.key)):
	if nt.isPersistent(str(args.key)):
		nt.clearPersistent(str(args.key))
		print('Persistance Removed from Key: ' + str(args.key))
	nt.delete(str(args.key))
	NetworkTables.flush()
	print('Key removed: ' + str(args.table) + "/" + str(args.key))
else:
	print("Key not found: " + str(args.table) + "/" + str(args.key))

NetworkTables.shutdown()




