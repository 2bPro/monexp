## Introduction
The purpose of this project is to monitor a simple RabbitMQ queue and automatically take action on unusual activity. The combination of Prometheus, Alertmanager, Grafana and Prometheus executors can be used for monitoring other software packages, tools and technologies. The list of Prometheus integrations can be found [here](https://prometheus.io/docs/instrumenting/exporters/). In order to monitor other packages, use its appropriate Prometheus exporter.

## Useful Links
[A review of queuing and monitoring tools](https://docs.google.com/presentation/d/1E9UC7Z4gX9Nnxdm-bwKdcTaw7ntdBsG_PwtkhZVzl1M/edit#slide=id.gc6f73a04f_0_0)

### RabbitMQ
* [What is RabbitMQ](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html)
* [Official basic queue and exchange tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
* [Pika](https://pika.readthedocs.io/en/stable/intro.html)
* [Best practice](https://www.cloudamqp.com/blog/2017-12-29-part1-rabbitmq-best-practice.html)
* [Prometheus exporter](https://github.com/kbudde/rabbitmq_exporter)

### Prometheus
* [Official documentation](https://prometheus.io/docs/introduction/overview/)
* [Prometheus integrated alerts](https://awesome-prometheus-alerts.grep.to/rules.html)
* [Prometheus querying basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
* [Alert manager](https://itnext.io/prometheus-with-alertmanager-f2a1f7efabd6)
* [Alert executor](https://github.com/imgix/prometheus-am-executor)

### Grafana
* [Official documentation](http://docs.grafana.org/)
* [Pre-built dashboards](https://grafana.com/dashboards?search=rabbitmq)

## Installation and Run Instructions for Docker
**Step 1:** Make sure you have Docker installed on your machine. If you do not already have Docker installed, follow the following instructions depending on your operating system:
* [Windows](https://docs.docker.com/docker-for-windows/install/)
* [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Mac](https://docs.docker.com/docker-for-mac/install/)

**Step 2:** Clone the repository
```git clone https://github.com/2bPro/rabbit-prometheus-monitor.git```

**Step 3:** Change directory to the rabbit-prometheus-monitor folder and run the following commands

```docker-compose build```

```docker-compose up```

**Note:** To start more instances of the consumer, use docker-compose scale flag  
```docker-compose up --scale consumer=<number_of_instances>```

This will make the following localhost ports available for monitoring:
* 15672 for RabbitMQ (username and password 'guest')
* 9090 for Prometheus
* 9093 for Alertmanager
* 3000 for Grafana (username and password 'admin')

**Step 4:** Stop the services, by pressing Ctrl+C and then running the following command
```docker-compose down```

## Installation and Run Instructions for CentOS:
* [Prometheus](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Installing-and-setting-up-Prometheus-on-CentOS)
* [RabbitMQ Exporter](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Installing-and-setting-up-RabbitMQ-Exporter-on-CentOS)
* [Alertmanager]()

## Basic Utilisation
* [RabbitMQ](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Basic-Utilisation-of-RabbitMQ)
* [Prometheus and Plugins](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Basic-Utilisation-of-Prometheus-and-Plugins)
* [Grafana](https://github.com/2bPro/rabbit-prometheus-monitor/wiki/Basic-Utilisation-of-Grafana)

## System workflow
In order to make RabbitMQ communicate with Prometheus, an exporter is required to translate the metric readings from RabbitMQ format to Prometheus format. This is achieved with the help of rabbitmq_exporter. 

Prometheus expands the visualisation options of RabbitMQ metrics and also has the ability to generate alerts based on specifically defined rules such as checks on the numbers of consumers or connections. Prometheus, however, is restricted to only generating and visualising these alerts and has no ability to manipulate alerts or fire events based on them. For this, the implementation of alertmanager is required.

Alertmanager handles alerts sent by Prometheus, allowing their manipulation and integration of events such as email and slack messaging. This tool can also be used to silence, inhibit or group alerts of similar nature into a single notification in case there are thousands of same type firing at once. Alertmanager, however, is limited to handling alerts and notifications and cannot take system-related actions to rectify or prevent the issues. For this, prometheus_am_executor could present a possible solution.

Prometheus executor can execute commands or run scripts based on alert notifications. From the documentation it has been confirmed that it can be used to reboot systems on error, the question would be if it could be used to dynamically scale the number of consumers depending on RabbitMQ's performance. This could be done with the help of rules based on specific performance activity inside Prometheus which would be communicated to the executor via the alertmanager. The executor then would decide what action to take and execute it in order to rectify, prevent an issue or balance resources.

### Activity subject to action
* consumer utilisation (if less than 100%)
* number of unacknowledged messages (if high and close to number of delivered messages for long periods of time)
* number of ready messages (if high for long periods of time)
* memory usage (if increasing)
* number of consumers (if less than expected)
* number of connections (if less than expected)
* node load coverage (if higher than CPU cores)

### Actions
* restart consumer if failed
* start additional consumers in order to alleviate pressure on the current consumer(s)
* stop consumers if not needed (depending on usage)

![Monitoring System Workflow](https://drive.google.com/uc?export=view&id=1zOLxaNZxBn-yx1_Ecb9_Ug4iQeGPCU9k)
