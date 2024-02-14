FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "sso.external.fast_api:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
