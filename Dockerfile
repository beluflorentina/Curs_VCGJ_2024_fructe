FROM python:3.8-alpine

ENV FLASK_APP 443D_pomelo
RUN adduser -D andra1402

USER andra1402

WORKDIR /home/Desktop/curs_vcgj_443D_fructe
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER andra1402
WORKDIR /home/Desktop/curs_vcgj_443D_fructe/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
