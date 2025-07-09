FROM python:3.11-slim

# Install uv
RUN curl -Ls https://astral.sh/uv/install.sh | sh

WORKDIR /app
COPY . /app

# Install dependencies using uv
RUN uv sync

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
