FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# --host 0.0.0.0 으로 설정하는게 중요하다. 기본값(127.0.0.1)으로 두면 컨테이너 내부에서만 접근이 가능해서 외부에서 접속이 안됨
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]