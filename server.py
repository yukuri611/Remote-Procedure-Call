'''
-server: python, client: JavaScript(Node.js)
-ソケットを利用
-リクエストとレスポンスの形式はJSON形式
-クライアントにIDを振り分け区別することで複数人に対応。ソケットとのHashMap
-エラー時はエラーの内容をクライアントに返す。
-関数はfloor, nroot, reverse, validANagram, sortの5つ。HashMapを作って呼び出す。
-先にパラメータの型を確認する
'''

import socket
import math
import json
import os
floor = lambda x: math.floor(x)
nroot = lambda n,x: math.pow(x,1/n)
reverse = lambda s: s[::-1]
validAnagram = lambda str1,str2: sorted(str1) == sorted(str2)
sort = lambda str_arr: sorted(str_arr)

function_hashmap = {"floor": floor, "nroot": nroot, "reverse": reverse, "validAnagram": validAnagram, "sort": sort}

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "./socket_file"

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)
print("starting up socket")

sock.listen(1)

print("Waiting for connection")

while True:
    connection, address = sock.accept()
    data = connection.recv(2048).decode("utf-8")
    print("data from client: " + data)
    json_data = json.loads(data)
    method = json_data["method"]
    params = json_data["params"]
    param_types = json_data["param_types"]
    id = json_data["id"]

    results = function_hashmap[method](params)
    print(results)
    reply = {"results": results, "result_type":"int", "id": id}
    json_reply = json.dumps(reply)
    connection.sendall(json_reply.encode())
    
    print("Closing connection")
    connection.close()








