FROM python:3.8-alpine
LABEL maintainer="MythicalKitten#0001 <root@mythicalkitten.com>"

RUN apk update && apk upgrade

RUN apk add --no-cache gcc musl-dev linux-headers git make build-base

WORKDIR /exporter

COPY index.py ./index.py
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8750
CMD ["python", "index.py"]