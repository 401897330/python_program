
import socket
import subprocess
import struct
import json


phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8080))
phone.listen(5)
while True:
    print('starting....')
    conn,addr=phone.accept()
    print('cliet addr',addr)
    while True:
        try:
            cmd=conn.recv(1024)
            if not cmd:break
            res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            err=res.stderr.read()
            if err:
                cmd_res=err
            else:
                cmd_res=res.stdout.read()
            head_dic={'filename':None,'hash':None,'total_size':len(cmd_res)}
            head_json=json.dumps(head_dic)
            head_bytes=head_json.encode('utf-8')
            conn.send(struct.pack('i',len(head_bytes)))
            conn.send(head_bytes)
            conn.send(cmd_res)
        except Exception:
            break
    conn.close()
phone.close()













