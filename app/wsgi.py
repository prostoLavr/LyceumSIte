from . import wsgi_app

if __name__ == '__main__':
    wsgi_app.run(host='0.0.0.0', port=80)
