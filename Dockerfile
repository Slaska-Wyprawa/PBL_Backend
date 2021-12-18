FROM python:latest
COPY . /home/pbl
WORKDIR /home/pbl
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install -U pytest
ARG DATABASE_CONNECTION_URL
ARG OPEN_ROUTE_API_KEY 
EXPOSE 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]


