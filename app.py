from flask import Flask
from flask import render_template
from flask import request
from threading import Thread

app = Flask(__name__)
log_num = 0


# Loading Data
def grabData():
    with open('SaveData.txt', 'r') as f:
        global log_num
        log_num = int(f.readline(1))


def storeData():
    with open('SaveData.txt', 'w') as f:
        f.write(str(log_num) + '\n')


def writeNew(data):
    with open('IPs.txt', 'a') as f:
        f.write(data + '\n')


grabData()


# Server-Side
@app.route("/", methods=["GET"])
def home():
    global log_num
    log_num += 1
    storeData()
    x_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    writeNew(f'IP {log_num}: {x_ip}')
    return render_template('page.html')


def run():
    app.run(host='0.0.0.0', port=8080)


def Start():
    t = Thread(target=run)
    t.start()


if __name__ == '__main__':
    Start()
