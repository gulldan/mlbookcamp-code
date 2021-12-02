FROM agrigorev/zoomcamp-cats-dogs-lambda:v2

RUN pip install --upgrade --no-cache-dir --extra-index-url https://google-coral.github.io/py-repo/ pip tflite_runtime

COPY lambda_function.py lambda_function.py

CMD [ "lambda_function.lambda_handler" ]