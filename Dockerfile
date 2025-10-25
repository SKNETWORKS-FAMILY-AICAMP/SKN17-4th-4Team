FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY parent_bot_project_main/ .

RUN python manage.py collectstatic --noinput

CMD ["uvicorn", "babyguide.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
