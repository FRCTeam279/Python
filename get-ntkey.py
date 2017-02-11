import logging
import sys
import time
import argparse
from networktables import NetworkTables


#https://docs.python.org/3.3/library/argparse.html
parser = argparse.ArgumentParser(description='Get the value of a variable on a NetworkTable')


parser.add_argument('key', nargs='?', default='')
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

#connecting isn't instant, and getting the table will not error,
# just not return anything and be confusing if you skip waiting...
#print('Waiting to connect...')
NetworkTables.initialize(server=str(args.server))
while NetworkTables.isConnected() == False:
    time.sleep(0.1)

nt = NetworkTables.getTable(str(args.table))

if args.key == '':
	print("All keys on table " + str(args.table))
	keys = nt.getKeys()
	keys.sort()
	for key in keys:
		val = nt.getValue(key, '')
		print('{:<40}{:<40}'.format(key, str(val)))
else:
	if nt.containsKey(str(args.key)):
		val = nt.getValue(str(args.key), '')
		print(str(args.key) + ": " + str(val))
	else:
		print("Key not found: " + str(args.key))

NetworkTables.shutdown()


