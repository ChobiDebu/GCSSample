from flask import Flask, request
import re
import os
import logging
from gcsutil import GCSUtil
logging.getLogger().setLevel(logging.INFO)


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def main():
    try:
        logging.info('start')
        query = request.args.get('target', '')
        env = os.environ.get('PATTERN')
        pattern = re.compile(r'%s' % env)
        logging.info(pattern)
        match = re.match(pattern, query)
        if match:
            logging.info('match!')
        else:
            logging.info('not matcn!')
        gcsUtil = GCSUtil()
        logging.info(
            gcsUtil.Read(
                '',
                '',
                ''
                )
            )
        gcsUtil.Write(
            '',
            '',
            '',
            ''
            )
        gcsUtil.Copy(
            '',
            '',
            '',
            '',
            ''
            )
        logging.info('stop')
        return 'Hello World!'
    except Exception as e:
        logging.error(e)
        return 'error!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
