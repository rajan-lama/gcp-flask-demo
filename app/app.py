from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    count = cache.incr('hits')
    return f'Hello World! This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')