import socket

HOST = ''
PORT = 2002

#Response Message Eka
response = """\
HTTP/1.1 200 OK

<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
"""

print("Enter Url : 127.0.0.1:2002 in your browser \n\n")
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:

            browser_request = conn.recv(2**10).decode('utf-8')  #Meken Wenne Browser Eken Ewana Message eka(HTTP Request Eka) Variable ekakata Aragena Decode Karagannawa
            print(browser_request)                              #Variable eka print karanawa
            print('Connected by', addr)                         #HTTP Request eka ewapu IP_address ekai Port ekai print karanwa
            
            conn.send(response.encode('utf-8'))                 #Response kiyana variable eke value eka aragena ENCODE karala Browser ekata yawanawa




# Mekedi Encode decode karanne network ekaka comunicate karaddi binary walin comunication eka sidda wena nisa :)
# UTF-8 Kiyanne unicode walata adala encoding system ekak --> https://en.wikipedia.org/wiki/UTF-8


#   Request eka gana      -> https://www.tutorialspoint.com/http/http_requests.htm
#   Response MSG Eka gana -> https://www.tutorialspoint.com/http/http_responses.htm
#   HTTP Message Examples -> https://www.tutorialspoint.com/http/http_message_examples.htm

