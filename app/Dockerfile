FROM python:3.8.18

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Python by default writes to stdout using a buffer, which k8s can't handle
ENV PYTHONUNBUFFERED=1

CMD ["python", "./app.py"]
