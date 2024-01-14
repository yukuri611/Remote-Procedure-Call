import socket
import json

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "./socket_file"
sock.connect(server_address)

method = "floor"
params = 6.11   #ホントはリスト
param_types = "double"  #ホントはリスト
id = 1

request = {"method": method, "params": params, "param_types": param_types, "id": id}
json_request = json.dumps(request)

sock.sendall(json_request.encode())

data = sock.recv(2048).decode("utf-8")
print("Received data from server: " + data)

dict_data = json.loads(data)
print("Results: {}".format(dict_data["results"]))