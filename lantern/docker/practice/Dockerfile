FROM python:3.8
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
CMD ["python", "wsgi.py"]