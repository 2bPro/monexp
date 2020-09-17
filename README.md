## Introduction  
The purpose of this project is mainly to show how to set up and use a monitoring system with the use of Prometheus, Alertmanager, Grafana and Prometheus executor. In addition, it also covers the installation, basic utilisation and monitoring of RabbitMQ.  

A list of endpoints other than RabbitMQ that can be monitored by Prometheus can be found [here](https://prometheus.io/docs/instrumenting/exporters/).

## Contents
* [Installation and Run Instructions for CentOS](#installation-and-run-instructions-for-centos)
* [Installation and Run Instructions for Docker](#installation-and-run-instructions-for-docker)
* [Basic Utilisation](basic-utilisation)
* [Useful Links](useful-links)

## Installation and Run Instructions for CentOS  
*  [Prometheus](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Installing-and-setting-up-Prometheus-on-CentOS)
*  [RabbitMQ Exporter](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Installing-and-setting-up-RabbitMQ-Exporter-on-CentOS)
*  [Alertmanager](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Installing-and-setting-up-Alertmanager-on-CentOS)
*  [Script Executor](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Installing-and-setting-up-Prometheus-Executor-on-CentOS)
*  [Grafana](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Installing-and-setting-up-Grafana-on-CentOS)

**Note:** The configuration files described in these installation instructions can be found in the `rabbit-prometheus-monitor/centos-setup` folder. Once everything is set up, this can be tested with the consumer and producer provided in the `general` folder.

## Installation and Run Instructions for Docker  
**Step 1:** Make sure you have Docker installed on your machine. If you do not already have Docker installed, follow the following instructions depending on your operating system:  
*  [Windows](https://docs.docker.com/docker-for-windows/install/)
*  [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
*  [Mac](https://docs.docker.com/docker-for-mac/install/)

**Step 2:** Clone the rabbit-prometheus-monitor repository  
```git clone https://github.com/2bPro/rabbit-prometheus-monitor.git```

**Step 3:** Copy the consumer and producer folders from the rabbit-prometheus-monitor/general folder to the rabbit-prometheus-monitor/docker-setup folder.  
```cp -a general/. docker-setup/```

 **Step 4:** Change directory to rabbit-prometheus-monitor/docker-setup and run the following commands:  
```docker-compose build```

```docker-compose up```

**Note:** To start more instances of the consumer, use docker-compose scale flag  
```docker-compose up --scale consumer=<number_of_instances>```

This will make the following localhost ports available for monitoring:  
* 15672 for RabbitMQ (username and password 'guest')
* 9090 for Prometheus
* 9093 for Alertmanager
* 3000 for Grafana (username and password 'admin')

**Step 5:** Stop the services by pressing Ctrl+C and then running the following command:  
```docker-compose down```

## Basic Utilisation  
*  [RabbitMQ](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Basic-Utilisation-of-RabbitMQ)
*  [Prometheus and Plugins](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Basic-Utilisation-of-Prometheus-and-Plugins)
*  [Grafana](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Basic-Utilisation-of-Grafana)

## Useful Links  
[A review of queuing and monitoring tools](https://docs.google.com/presentation/d/1E9UC7Z4gX9Nnxdm-bwKdcTaw7ntdBsG_PwtkhZVzl1M/edit#slide=id.gc6f73a04f_0_0)

### RabbitMQ  
*  [What is RabbitMQ](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html)
*  [Official basic queue and exchange tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
*  [Pika](https://pika.readthedocs.io/en/stable/intro.html)
*  [Best practice](https://www.cloudamqp.com/blog/2017-12-29-part1-rabbitmq-best-practice.html)
*  [Prometheus exporter](https://github.com/kbudde/rabbitmq_exporter)

### Prometheus  
*  [Official documentation](https://prometheus.io/docs/introduction/overview/)
*  [Prometheus integrated alerts](https://awesome-prometheus-alerts.grep.to/rules.html)
*  [Prometheus querying basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
*  [Alertmanager](https://itnext.io/prometheus-with-alertmanager-f2a1f7efabd6)
*  [Script Executor](https://github.com/imgix/prometheus-am-executor)

### Grafana  
*  [Official documentation](http://docs.grafana.org/)
*  [Pre-built dashboards](https://grafana.com/dashboards?search=rabbitmq)
