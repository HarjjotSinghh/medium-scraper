# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Install the dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application.
COPY . .

# Expose the port on which the FastAPI app will run.
EXPOSE 8080

# Default command: run the FastAPI app.
CMD ["python", "app.py"] 