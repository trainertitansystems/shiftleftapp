FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

<<<<<<< HEAD
CMD ["uvicorn", "autoscale_demo.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

>>>>>>> 0d2a30d (Clean app packaging, fix Docker imports, add Kubernetes manifests)
