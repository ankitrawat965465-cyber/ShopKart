
# 1. Python base image
FROM python:3.12-slim

# 2. Container ke andar working directory
WORKDIR /app

# 3. Dependency file copy karo
COPY requirements.txt .

# 4. Required Python packages install karo
RUN pip install --no-cache-dir -r requirements.txt

# 5. Application code, templates aur static files copy karo
COPY . .

# 6. Flask application port
EXPOSE 8080

# 7. Container start hone par app run karo
CMD ["python", "app.py"]
