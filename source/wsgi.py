"""
App endpoint handlers
"""
import importlib

from flask import render_template, request, make_response, abort, Flask

app = Flask(__name__)  # pylint: disable=invalid-name

CODECS = {
  'ym': "Yandex Money",
  'youtube': "YouTube",
  'fb': "FaceBook",
  'ok': 'Odnoklassniki.ru',
  'twitter': "Twitter",
  'reddit': "Reddit",
  'lj': 'LiveJournal',
  # not implemented handlers, just store message to db
  'store': None,
  'vk': None,
  'vif': None,
  'hh': None,
}


def run(codec, body):
    """
    run codec for transform body
    """
    if isinstance(body, unicode):
        body = body.encode('utf8')

    lines = body.splitlines()
    subj = lines[0]
    text = '\n'.join(lines[1:])

    try:
        if CODECS[codec] is None:
            from modules import store
            ret = store(codec, subj, text)
        else:
            pmod = importlib.import_module("modules.{}".format(codec))
            ret = pmod.start(subj, text)

    except Exception:
        from models import SavedSource
        SavedSource(label=codec, subject=subj, body=text).put()
        raise

    response = make_response(ret)
    response.mimetype = "text/plain"
    return response


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    """
    root page
    """
    if request.method == 'POST':
        return run(request.form.get('codec'), request.form.get('source'))

    context = {
      'codecs': CODECS,
    }
    return render_template('main.html', **context)


@app.route('/transform/<codec>/', methods=['POST'])
def transform(codec):
    """
    transform post
    """
    if codec not in CODECS:
        return abort(404)

    return run(codec, request.get_data())


@app.route('/_ah/warmup')
def warmup():
    """
    handle warmup request to suppress  warning into logs
    """
    return 'OK'


@app.route('/_ah/start')
def backend_start():
    """
    handle backend start request to suppress  warning into logs
    """
    return 'OK'
