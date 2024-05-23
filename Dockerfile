FROM python:3.10

RUN pip install --upgrade pip

RUN pip install flask

RUN pip install pytest

WORKDIR /app

COPY . /app


ENV FLASK_APP ./fructe.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
