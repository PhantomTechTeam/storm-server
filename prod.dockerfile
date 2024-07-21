# Use an official Python runtime as a base image
FROM python:3.11-slim as builder

ENV PYTHONUNBUFFERED 1

RUN apt-get update &&  \
    apt-get install -y libpq-dev gcc

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src/requirements.txt /app

# Create virtual env
RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run multistage as best practice
FROM python:3.11-slim as runner
WORKDIR /app/
COPY --from=builder /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./src /app/

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
