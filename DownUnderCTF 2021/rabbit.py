import os

while True:
    filename = os.listdir()[0]
    if filename == 'rabbit.py':
        filename = os.listdir()[1]
    print(filename)
    os.system(f'mv {filename} wm11')
    status = os.popen('7z x wm11').read()
    print(status)
    if 'Compressed: 0' in status:
       break 
    os.system('rm wm11')
