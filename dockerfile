FROM nginx/unit:1.26.0-python3.9

WORKDIR /api

COPY ./app/requirements.txt ./api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./api/requirements.txt

COPY ./app /api/