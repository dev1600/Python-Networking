import socket
import cv2

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
server.bind((ip,10020))
server.listen()
client_socket,client_address=server.accept()

file=open('server.jpg','wb')
# stream based protocol hence image received in chunks
image_chunk=client_socket.recv(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk=client_socket.recv(2048)

file.close()
server.close()
img=cv2.imread('server.jpg',cv2.IMREAD_COLOR)
cv2.imshow("Meme",img)
cv2.waitKey(0)
