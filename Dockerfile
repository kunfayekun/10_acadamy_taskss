# Step 1: Use official lightweight Python image
FROM python:3.13-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy project files into container
COPY . /app

# Step 4: Upgrade pip and install dependencies (pytest for testing)
RUN pip install --upgrade pip \
    && pip install --no-cache-dir pytest

# Step 5: Optional - install requirements if you have a requirements.txt
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Default command when container runs
CMD ["pytest"]
