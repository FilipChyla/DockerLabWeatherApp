FROM python:3.10.17-alpine AS build

RUN apk add --no-cache gcc musl-dev libffi-dev
WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade setuptools && \
    pip install --no-cache-dir -r requirements.txt


FROM python:3.10.17-alpine AS final
LABEL org.opencontainers.image.authors="Filip Chyla"

WORKDIR /app
RUN apk add --no-cache libffi expat
COPY --from=build /usr/local /usr/local
COPY . .

EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s CMD wget -q --spider http://localhost:5000/ || exit 1

CMD ["python", "app.py"]
