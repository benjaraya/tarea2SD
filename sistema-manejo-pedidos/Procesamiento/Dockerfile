FROM python:3.9-slim

WORKDIR /app

COPY ProcesamientoService.py /app
COPY requirements.txt /app

RUN pip3 install -r requirements.txt

CMD ["python", "ProcesamientoService.py"]
