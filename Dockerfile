# 第一阶段：构建阶段
FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5080
CMD ["python", "app.py"]

