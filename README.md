
# macOS System Health Monitor 🖥️🍎

A modular, real-time system health monitoring solution for macOS, built with Python, Flask, Prometheus, and Grafana. The system captures, analyzes, and visualizes key system metrics such as CPU usage, memory, disk, battery, and network activity, enabling proactive alerts and efficient diagnostics.

---

## 📦 Features

- 🧠 **Modular Design**: Easy to extend and maintain
- 📊 **Real-Time Monitoring**: Tracks CPU, RAM, disk, network, and battery status
- 🚨 **Custom Alerts**: Triggered via rules defined in Prometheus
- 📈 **Interactive Dashboards**: Beautiful Grafana UI for system insights
- 🐍 **Python & Flask Backend**: Lightweight API server for metrics collection
- 📡 **Prometheus Integration**: Collect and scrape metrics periodically

---

## 🔧 Tech Stack

- **Python** – for core monitoring scripts
- **Flask** – to expose system metrics as HTTP endpoints
- **Prometheus** – for metrics scraping and alerting
- **Grafana** – for dashboards and visualizations
- **Shell (setup.sh)** – to automate configuration

---

## 🗂️ Project Structure

```

.
├── alerts/            # Alert rules for Prometheus
├── config/            # Configuration files
├── data/              # Logs or collected metrics (if any)
├── grafana/           # Grafana dashboards and config
├── monitor/           # Python monitoring scripts
├── .gitignore
├── .DS\_Store
├── Dockerfile         # Docker setup for deployment
├── requirements.txt   # Python dependencies
├── setup.sh           # Setup script

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/snehalgjrakas2027/macos-system-health-monitor.git
cd macos-system-health-monitor
````

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask App

```bash
python monitor/app.py
```

It will expose system metrics at:
`http://localhost:5000/metrics`

### 4. Set Up Prometheus

Update the Prometheus config in `config/prometheus.yml` to scrape from `localhost:5000`.

```yaml
scrape_configs:
  - job_name: 'macos-monitor'
    static_configs:
      - targets: ['localhost:5000']
```

Then run Prometheus:

```bash
prometheus --config.file=config/prometheus.yml
```

### 5. Visualize in Grafana

* Import the dashboard JSON from `grafana/`
* Add Prometheus as a data source
* Explore your system metrics!

---

## 🐳 Docker Support (Optional)

```bash
docker build -t macos-monitor .
docker run -p 5000:5000 macos-monitor
```

---

## 🔔 Alerts

Define alert rules in `alerts/` and configure Prometheus to use them.
Integrate with email, Slack, etc., as needed.

---


## 🙋‍♀️ Author

**Snehal G J Rakas (snehalgjrakas2027)**
Feel free to connect or report issues via GitHub!


