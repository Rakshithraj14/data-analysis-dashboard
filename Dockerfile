# Use Python 3.10 (or later)
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Upgrade pip & install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port (assuming your app runs on 8501)
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py"]
