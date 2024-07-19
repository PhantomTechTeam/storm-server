# Use an official Python runtime as a base image
FROM alpine:

RUN apt-get update &&  \
    apt-get install -y libpq-dev gcc

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]

EXPOSE 5000
