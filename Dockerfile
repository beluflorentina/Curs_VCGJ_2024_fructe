FROM python:3.10

RUN pip install --upgrade pip

RUN pip install flask

RUN pip install pytest

WORKDIR /Curs_VCGJ_2024_fructe

COPY . /Curs_VCGJ_2024_fructe

ENV FLASK_APP ./443_fructe.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
