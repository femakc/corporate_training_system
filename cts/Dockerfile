FROM python:3.11-slim
LABEL maintainer="Alexander Borisov"

COPY app/ /app

WORKDIR /app

RUN pip3 install -r requirements.txt --no-cache-dir \
    && groupadd --gid 2000 nonrootuser \
    && useradd --uid 2000 --gid nonrootuser --shell /bin/bash --create-home nonrootuser \
    && chown -R nonrootuser:nonrootuser /app

USER 2000

CMD ["gunicorn", "cts.wsgi:application", "--bind", "0:8000" ]