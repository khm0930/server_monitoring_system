# **🚀 Server Monitoring System**

### **Monitor, Visualize, and Analyze Your Server's Performance in Real-Time**

![Server Monitoring](https://github.com/khm0930/server_monitoring_system/blob/main/assets/server_monitoring_system_screenshot.png)

---

## **🔍 Overview**

The **Server Monitoring System** is an all-encompassing tool designed to keep track of your server's key performance indicators (KPIs). It offers real-time visualization, alert notifications, and comprehensive data analysis to help administrators make informed decisions.

---

## **🎯 Features**

- **🖥️ Server Status Monitoring**: Real-time tracking of CPU usage, memory consumption, disk usage, and more.
- **📈 Live Data Visualization**: Interactive dashboards showing real-time server performance data.
- **⚠️ Alert System**: Automatically triggers alerts when KPIs exceed defined thresholds.
- **📊 Log Storage & Analysis**: Stores server logs for historical analysis and trend discovery.
- **💾 Time Series Database Integration**: Efficiently stores time-series data for long-term monitoring.

---

## **🏗️ Project Architecture**

The architecture of the Server Monitoring System is designed for scalability, modularity, and ease of deployment. Below is a high-level overview of the system components:

![Project Architecture](https://github.com/khm0930/server_monitoring_system/blob/main/assets/project_architecture.png)

- **Frontend**: 
  - Built with React, the frontend communicates with the Django backend to fetch server status data and displays it in an interactive dashboard.
- **Backend**:
  - Django-based API server that processes requests from the frontend and interacts with the databases.
  - Uses Prometheus for collecting metrics data and InfluxDB for storing time-series data.
- **Database Layer**:
  - **MySQL**: Stores general-purpose data, such as user information and configuration settings.
  - **InfluxDB**: Optimized for handling high-volume time-series data, used for storing server metrics.
- **Monitoring**:
  - **Prometheus**: Collects and stores metrics, provides an API for the backend to query the data.
  - **Grafana**: Integrated with Prometheus to create rich, customizable dashboards for data visualization.
- **Infrastructure**:
  - **Docker**: Containerizes the entire application stack for consistent and reliable deployment.
  - **AWS**: Deployed on AWS infrastructure, taking advantage of EC2 for compute and S3 for storage.

---

## **🛠️ Technology Stack**

- **🧑‍💻 Programming Language**: Python
- **💾 Database**:
  - **InfluxDB**: For time-series data storage.
  - **MySQL**: For general-purpose data storage.
- **🌐 Frontend**: 
  - **React**: For building an intuitive and responsive user interface.
- **🛠️ Backend**:
  - **Django**: Powers the API server.
- **📡 Monitoring Tools**:
  - **Prometheus**: Handles data collection and storage.
- **📊 Visualization Tools**:
  - **Grafana**: For advanced data visualization.
- **🌍 Deployment & Infrastructure**:
  - **Docker**: Containerization for consistent development and deployment environments.
  - **AWS**: Cloud-based infrastructure (including EC2, S3, etc.) for scalability and reliability.

---

## **📷 Screenshots**

### **📊 Server Status Dashboard**

![Server Status Dashboard](https://github.com/khm0930/server_monitoring_system/blob/main/assets/server_status_dashboard.png)

---

## **📦 Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/khm0930/server_monitoring_system.git
2. **Navigate to the Project Directory**:
   ```bash
   cd server_monitoring_system
3. **Set Up the Backend Environment**:
   ```bash
    cd backend
    pip install -r requirements.txt
    python manage.py migrate
4. **Set Up the Frontend Environment**:
   ```bash
   cd ../frontend
   npm install
5. **Build and Start the Docker Containers**:
   ```bash
    cd ..
    docker-compose up --build
