from flask import Flask
import sys
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'index'


@app.route('/upload/file')
def upload_file():
    return 'upload file'


@app.route('/download/file')
def download_file():
    return 'download_file'


def get_url_patterns():
    url_prefix = '/api/v1/wechat'
    urlpatterns = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint == 'static':
            continue
        urlpatterns.append((
            url_prefix + str(rule),
            getattr(sys.modules[__name__], rule.endpoint),
            {'methods': list(rule.methods)}
        ))
    return urlpatterns


print(get_url_patterns())
if __name__ == '__main__':
    app.debug = True
    app.run()
