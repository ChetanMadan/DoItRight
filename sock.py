import socket
import time
from threading import Thread
import re
from base64 import b64encode
from hashlib import sha1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 1234
address = (ip,port)
s.bind(address)
s.listen(2)

websocket_answer = (
	'HTTP/1.1 101 Switching Protocols',
	'Upgrade: websocket',
	'Connection: Upgrade',
	'Sec-WebSocket-Accept: {key}\r\n\r\n',
)

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

print("Waiting for connection ...")

client,addr = s.accept()

print( "Client connected from "+str(addr[0])+":"+str(addr[1]))

start_time = time.time()
elapsed_time = 0

AUTH_response=''
key=''

def listen():
	global s
	global client,addr
	global AUTH_response, key
	while True:
	  data = client.recv(1024)
	  #client_resp = unmask_data(data)
	  #client_resp = str(data.decode("utf-8"))

	  print (data)

	  #str(addr[0])+" > "+str(data)

	  key = (re.search('Sec-WebSocket-Key:\s+(.*?)[\n\r]+', data))
	  if key:
	    key = key.groups()[0].strip()

	    response_key = b64encode(sha1(key + GUID).digest())
	    AUTH_response = '\r\n'.join(websocket_answer).format(key=response_key)

	    print (key)

def send():
	global s
	global client,addr
	global start_time, elapsed_time
	global AUTH_response, key
	while True:
	  if key:
	    print (AUTH_response)
	    client.send(AUTH_response)
	    key=''
	  
	  elapsed_time = time.time() - start_time
	  if False:#elapsed_time > 10:
	    start_time = time.time()
	    elapsed_time = 0
	    msg = "hola"#raw_input(">")
	    client.send(msg)

def unmask_data(rcv_msg):
	# as a simple server, we expect to receive:
	#    - all data at one go and one frame
	#    - one frame at a time
	#    - text protocol
	#    - no ping pong messages
	data = bytearray(rcv_msg)
	if len(data) < 6:
	  raise Exception("Error reading data")
	# FIN bit must be set to indicate end of frame
	assert(0x1 == (0xFF & data[0]) >> 7)
	# data must be a text frame
	# 0x8 (close connection) is handled with assertion failure
	assert(0x1 == (0xF & data[0]))

	# assert that data is masked
	assert(0x1 == (0xFF & data[1]) >> 7)
	datalen = (0x7F & data[1])

	str_data = ''
	if datalen > 0:
	  mask_key = data[2:6]
	  masked_data = data[6:(6 + datalen)]
	  unmasked_data = [masked_data[i] ^ mask_key[i % 4] for i in range(len(masked_data))]
	  str_data = str(bytearray(unmasked_data).decode("utf-8"))
	
	return str_data

if __name__=="__main__":
	Thread(target=listen).start()
	Thread(target=send).start()