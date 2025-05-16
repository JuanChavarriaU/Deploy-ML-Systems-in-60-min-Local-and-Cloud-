FROM python:3.13.3-alpine3.21


# Set the working directory inside the container
WORKDIR /code

RUN apk add --no-cache \
    build-base \
    gcc \
    g++ \
    python3-dev

# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

RUN python3 --version
RUN pip3 --version

# Install the Python dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the app folder into the container
COPY ./app /code/app

# Copy the model directory (with the saved model file) into the container
COPY ./model /code/model

# Expose port 80 for FastAPI
EXPOSE 80

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]