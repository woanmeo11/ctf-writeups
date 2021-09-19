import requests, cv2, pytesseract, re

sess = requests.Session()

count = 0

port = 31454
while True:


    image = sess.get(f'http://challenge.ctf.games:{port}/static/otp.png')

    with open('img.png', 'wb') as f:
        f.write(image.content)

    image = cv2.imread('img.png')
    image = cv2.bitwise_not(image)
    captcha = pytesseract.image_to_string(image, config='digits')

    captcha = captcha[:-2]
    response = sess.post(f'http://challenge.ctf.games:{port}', data={'otp_entry': captcha})
    
    with open('a.html', 'w') as w:
        w.write(response.text)

    try:
        count = re.findall('count">(\d+)</p>', response.text)[0]
    except:
        print(response.text)
        break

    count = int(count)

    print(count, captcha)

    if count >= 150:
        response = sess.get(f'http://challenge.ctf.games:{port}')
        print(response.text)
