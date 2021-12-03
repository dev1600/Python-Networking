import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
client.connect((ip,10020))

file=open('meme.jpg','rb')
image_data=file.read(2048)

while image_data:
        client.send(image_data)
        image_data=file.read(2048)
file.close()
client.close()