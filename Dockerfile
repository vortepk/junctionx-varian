FROM python:3.11-alpine
RUN apk update && apk add curl wget
RUN addgroup -S dev
RUN adduser --ingroup dev --disabled-password dev
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY --chown=dev . .
USER dev
ENV GUI_PORT="8083"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENTRYPOINT [ "sh", "-c", "gunicorn radiancex.asgi:application -k uvicorn.workers.UvicornWorker --access-logfile '-' --error-logfile '-' --capture-output --bind 0.0.0.0:${GUI_PORT}"]
