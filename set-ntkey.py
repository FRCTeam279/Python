import logging
import sys
import time
import argparse
from networktables import NetworkTables


#https://docs.python.org/3.3/library/argparse.html
parser = argparse.ArgumentParser(description='Set the value of a variable on the Preferences NetworkTable')

# store flag value

parser.add_argument('key')
parser.add_argument('value')
parser.add_argument('-d', '--debug', action='store_true')
parser.add_argument('-s', '--server', default='10.2.79.2')
parser.add_argument('-nt', '--table', default='Preferences')

#see putvalue http://robotpy.readthedocs.io/projects/pynetworktables/en/stable/api.html#networktables-api
#PutValue Types
#bool	EntryTypes.BOOLEAN	 
#int	EntryTypes.DOUBLE	 
#float	EntryTypes.DOUBLE	 
#str	EntryTypes.STRING	 
#bytes	EntryTypes.RAW	Doesn’t work in Python 2.7
#list	Error	Use putXXXArray methods instead
#tuple	Error	Use putXXXArray methods instead
#parser.add_argument('-t', '--type', required=True, choices=['bool', 'int', 'float', 'str', 'bytes'])
args = parser.parse_args(sys.argv[1:len(sys.argv)])

if args.debug:
	print('Setting value')
	print('Server: ' + str(args.server))
	print('Table: ' + str(args.table))
	print('Key: ' + str(args.key))
	print('Value: ' + str(args.value))
	#print('Type: ' + str(args.type))
	print('Debug: ' + str(args.debug))
	
	logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize(server=str(args.server))
while NetworkTables.isConnected() == False:
    time.sleep(0.1)

	
nt = NetworkTables.getTable(str(args.table))
res = nt.putValue(str(args.key), args.value)
NetworkTables.flush()
val = nt.getValue(str(args.key))
if val:
	print("Value set: " + str(args.table) + "/" + str(args.key) + " = " + str(val))
else: 
	print("Error - did not set key correctly!")

NetworkTables.shutdown()



