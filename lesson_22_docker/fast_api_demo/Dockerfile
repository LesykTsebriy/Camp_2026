FROM python:3.10

RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    libjpeg62-turbo-dev \
    bzip2 \
    g++ \
    graphviz \
    libgl1 \
    libhdf5-dev \
    openmpi-bin \
    screen \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
COPY . /app

EXPOSE 5000
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]