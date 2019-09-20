import socket
import pickle
from threading import Thread
import socket
import pickle
from utils import ServerSocket


serverSocket = ServerSocket('localhost', 3000, 'tcp')
serverSocket.listener()

