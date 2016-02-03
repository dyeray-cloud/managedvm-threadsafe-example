FROM gcr.io/google_appengine/python-compat
ADD . /app
RUN pip install -r requirements.txt
