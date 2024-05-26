FROM python:3.10

RUN pip install

WORKDIR /app

COPY source dest

ENTRYPOINT [ "executable" ]

