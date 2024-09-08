# Prometheus Integration Django Project

This project, `PrometheusIntegration`, is a Django application that demonstrates how to integrate Prometheus for monitoring and exposing metrics. It includes a simple API endpoint (`/api/hello/`) that accepts various types of data (JSON, text, files, and empty requests) and responds with a "Hello World" message. The application also exposes a Prometheus metrics endpoint (`/metrics`) that can be scraped by a Prometheus server for monitoring purposes.

## Features

- **API Endpoint**: `/api/hello/` - Accepts POST requests with JSON, text, files, or empty data and returns a "Hello World" message.
- **Prometheus Metrics**: `/metrics` - Exposes Prometheus metrics for monitoring.

## Requirements

- Python 3.12.5
- Django 5.1.1
- PostgreSQL (for database backend)
- Prometheus server for scraping metrics

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PrometheusIntegration.git
cd PrometheusIntegration
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install django==5.1.1 psycopg2-binary django-prometheus prometheus-client
```

### 4. Configure the Django Project

Ensure the `ALLOWED_HOSTS` setting in `PrometheusIntegration/settings.py` allows all hosts:

```python
ALLOWED_HOSTS = ['*']
```

### 5. Apply Database Migrations

Run the following command to apply the database migrations:

```bash
python manage.py migrate
```

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`.

## Prometheus Integration

### 1. Install and Set Up Prometheus

Download and install the [Prometheus server](https://prometheus.io/download/) for your operating system. Add the following configuration to your `prometheus.yml` file:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "django-app"
    static_configs:
      - targets: ["localhost:8000"]
```

### 2. Run Prometheus Server

Run Prometheus with the configuration:

```bash
./prometheus --config.file=prometheus.yml
```

### 3. Access Metrics

Open your browser and go to:

- Prometheus UI: `http://localhost:9090`
- Django Metrics: `http://localhost:8000/metrics`

## Running Tests

### GitHub Actions Workflow

The repository includes a GitHub Actions workflow to build, test, and monitor the application automatically on every push or pull request. The workflow:

- Sets up a Python environment.
- Installs dependencies.
- Runs tests for the `/api/hello/` and `/metrics` endpoints.
- Ensures Prometheus metrics are exposed correctly.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.