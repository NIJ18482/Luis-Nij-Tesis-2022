#Server
import socket 

host = ''

port = 18482
storedValue = "Pruema de Comunicación"

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Conexión con Socket creada")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket conectado completamente")
    return s

def SetupConnection():
    s.listen(1)
    conn, address = s.accept()
    print("Conectado a: "+address[0] + ":" + str(address[1]))
    return conn
  
def GET():
    reply = storedValue
    return reply
   
def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply
    
    
def dataTransfer(conn):
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        dataMessage = data.split(' ',1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Se nos fue")
            break
        elif commmand == 'KILL':
            print("Apagando servidor")
            s.close()
            break
        else:
            reply = 'Comando desconocido'
        conn.sendall(str.encode(reply))
        print("Datos enviados")
    conn.close()
    


s = setupServer()
 
while True:
    try: 
        conn = SetupConnection()
        dataTransfer(conn)
    except:
        break
 