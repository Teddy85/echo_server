import socket                                                                   
import os                                                                       
                                                                     
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('0.0.0.0', 2222))                                                       
s.listen(10)                                                                    
for i in range(10) :                                                             
   pid=os.fork()                                                                
                                                       
   try                                                                        
        while True:                                                             
              conn, addr = s.accept()                                           
                                                                     
                 data = conn.recv(1024)                                         
                 if not data:                                              
                 conn.send(data)                                                
                 if data=='close':                                        
                 conn.close()    
