# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy only the dependency specification files first, to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . .

# Command to run the bot
CMD ["poetry", "run", "python", "bot.py"]
