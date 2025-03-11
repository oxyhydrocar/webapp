FROM python:3.8-slim

ENV DB_USER=admin
ENV DB_PASS=password123
ENV APP_HOME=/usr/src/app

WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r appuser && useradd -r -g appuser appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown -R appuser:appuser $APP_HOME
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
