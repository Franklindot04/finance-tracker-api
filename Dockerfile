FROM python:3.11

ENV PASSLIB_BUILTIN_BCRYPT=enabled

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn[standard] \
    sqlalchemy \
    pydantic \
    psycopg2-binary \
    pydantic[email] \
    passlib[bcrypt] \
    bcrypt==3.2.2 \
    python-jose

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

