FROM python:alpine3.14
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT [ "python", "./service.py" ]

# docker build -t srv-pyhton-flask .
# docker run -itd -p 8080:5000 --rm --name api-pyhton-flask  srv-pyhton-flask
# curl server.docker:8080/produto
