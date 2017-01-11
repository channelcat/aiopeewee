FROM python:3.6

ADD . /code
RUN pip install -r /code/requirements.txt

WORKDIR /code
CMD python main.py