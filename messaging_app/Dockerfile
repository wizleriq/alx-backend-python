# Use official Python 3.10 image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Expose Django default port
EXPOSE 8000

# Avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
