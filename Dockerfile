FROM python:3.10

RUN pip install flask pytest pylint

WORKDIR /app
COPY . .

EXPOSE 5000

CMD ["flask", "--app=app/443D_fructe", "run", "--host=0.0.0.0", "--port=5000"]
