# rabbit-prometheus-monitor
RabbitMQ monitored with Prometheus and Grafana in Docker Compose

The purpose of this project is to monitor a simple RabbitMQ queue and automatically take action on unusual activity.

### Useful Documentation
#### RabbitMQ
* [What is RabbitMQ](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html)
* [Official basic quque and exchange tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
* [Pika](https://pika.readthedocs.io/en/stable/intro.html)
* [Best practice](https://www.cloudamqp.com/blog/2017-12-29-part1-rabbitmq-best-practice.html)
* [Prometheus exporter](https://github.com/kbudde/rabbitmq_exporter)

#### Prometheus
* [Official documentation](https://prometheus.io/docs/introduction/overview/)
* [Prometheus integrated alerts](https://awesome-prometheus-alerts.grep.to/rules.html)
* [Alert manager](https://itnext.io/prometheus-with-alertmanager-f2a1f7efabd6)
* [Alert executor](https://github.com/imgix/prometheus-am-executor)

#### Grafana
* [Official documentation](http://docs.grafana.org/)
* [Pre-built dashboards](https://grafana.com/dashboards?search=rabbitmq)

### Intstallation
To install, clone the repository and run the following commands in the root folder:

```docker-compose build```

```docker-compose up```

This will make the following localhost ports available for monitoring:
* 15672 for RabbitMQ (username and password 'guest')
* 9090 for Prometheus
* 3000 for Grafana (username and password 'admin')

### Utilisation
#### RabbitMQ


### Activity subject to action
* number of unacknowledged messages (if high and close to no of delivered for long periods of time)
* number of ready messages (if high for long periods of time)
* memory usage (if increasing)
* number of consumers (if less than expected)
* number of connections (if less than expected)
* node load coverage (if higher than CPU cores)

### Actions
* restart consumer if failed
* start additional consumers in order to release pressure on the consumer(s)
* stop consumers if not needed (depending on usage)

### System workflow
![Monitoring System Workflow](https://drive.google.com/uc?export=view&id=1mJSsiUr52PYvBV0ia_bV0_AhmwzhgkDm)