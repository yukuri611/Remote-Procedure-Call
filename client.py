import socket
import json

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "./socket_file"
sock.connect(server_address)

method = input("Method: ")
params = input("Params: ").split(",")   
param_types = input("Params type: ").split(",")  
id = int(input("ID: "))

if method in ["floor","nroot"]:
    params = list(map(float, params))
    #エラー処理が必要


request = {"method": method, "params": params, "param_types": param_types, "id": id}
json_request = json.dumps(request)

sock.sendall(json_request.encode())
print("Successfully sent data to the server.")

data = sock.recv(2048).decode("utf-8")
print("\nReceived data from server: " + data)

dict_data = json.loads(data)
print("Results: {}".format(dict_data["results"]))