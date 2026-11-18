FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python","-m","robot_trial.cli","data/example.json"]
