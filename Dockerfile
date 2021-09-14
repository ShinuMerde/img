FROM python:3
COPY templates /app/templates
COPY main.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mkdir "img"
CMD [ "python", "main.py"]

