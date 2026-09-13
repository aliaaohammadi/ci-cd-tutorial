# A minimal image that installs our package and runs it.
FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .

# What the container does when it starts:
CMD ["python", "-c", "from calc import add; print('2 + 3 =', add(2, 3))"]
