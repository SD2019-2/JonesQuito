import socket
import pickle
from threading import Thread
import socket
import pickle
from utils import ServerSocket


serverSocket = ServerSocket('129.213.164.45', 3000, 'tcp')
serverSocket.listener()

