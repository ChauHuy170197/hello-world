FROM python
WORKDIR /usr/src/app

COPY index.py .
COPY requaiment.txt .
RUN pip install -r requaiment.txt

CMD ["python","index.py","http://0.0.0.0:8080"]
