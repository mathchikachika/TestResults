# docker build -t mathworldimage .
# docker run -d -p 8000:8000 --name mathworldcontainer mathworldimage


# Use Ubuntu latest as the base image
FROM ubuntu:latest

# Update the package lists
RUN apt-get update
RUN apt-get upgrade -y

# Install Python 3.10 and pip
RUN apt-get install -y python3.10 python3-pip

# Install python3-venv
RUN apt-get install -y python3-venv

# Install python3-tk unattended
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Chicago
RUN apt-get install -y python3-tk

# Upgrade pip
RUN python3.10 -m pip install --upgrade pip

# Create a virtual environment
RUN python3.10 -m venv /app/venv

# Set the virtual environment as the default Python environment
ENV PATH="/app/venv/bin:$PATH"

# Copy the requirements.txt file into the container
COPY linux_requirements.txt /linux_requirements.txt

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r /linux_requirements.txt

# Create a "/src" directory in the container
RUN if [ ! -d "/app/logs" ]; then mkdir -p "/app/logs"; fi
RUN touch "/app/logs/question.log"

# Copy the host files into the "/src" directory in the container
COPY . /app

# Set the working directory to "/src"
WORKDIR /app

# Command to run your application using UVicorn
# EXPOSE 8000
# CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
