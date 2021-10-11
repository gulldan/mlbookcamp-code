FROM agrigorev/zoomcamp-model:3.8.12-slim

COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy

EXPOSE 1234

ENV FILE_PATH=./

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1234", "serving:app"]