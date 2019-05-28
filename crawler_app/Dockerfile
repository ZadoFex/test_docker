FROM python:3

WORKDIR /app

COPY server.py .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pymongo

COPY . .

CMD [ "python", "./server.py" ]