FROM python:3

WORKDIR  /usr/src/app

COPY server.py .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install pymongo
#RUN pip install scrapy

COPY . .

CMD [ "python", "./server.py" ]