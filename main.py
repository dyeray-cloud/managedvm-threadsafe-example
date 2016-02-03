from flask import Flask, request, Response
from models import NumInstances
import time
app = Flask(__name__)

counter_name = 'strike'

@app.route('/')
def hello():
    counter = NumInstances.get_by_id(counter_name)
    if counter is None:
        counter = NumInstances(id=counter_name)
    counter.count += 1
    counter.put()
    time.sleep(3)
    counter.count -= 1
    counter.put()
    return str(counter.count)


@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == '__main__':
    app.run()
