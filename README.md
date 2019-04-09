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


#### Prometheus


#### Grafana
The first step when monitoring with Grafana is creating a Data Source for Prometheus in order to link Grafana to the Prometheus metric readings of RabbitMQ. In order to do this, open the configuration options in the side menu and select the 'Data Source' option.

![Creating a data source](https://drive.google.com/uc?export=view&id=1s9AbCskDcmLO6DPoIMNXMmISeqNYMw0L)

This will open a set of data source options recgnised by Grafana. Selecting Prometheus will take you to the following page. Here, select the host and port where Prometheus management console is currently running and specify that this is being accessed via a browser. Clicking save and test should show a confirmation message for the creation of the data source and a confirmation message for a successful connection.

![Connecting to Prometheus](https://drive.google.com/uc?export=view&id=1WrCPTvS6MKFdIh2PjxEIAF70KmXZsULm)

Now you can choose whether to create a new dashboard or use pre-built community dashboards. I imported a community dashboard with ID '2121'. To import this, open the create options in the side menu and select import. Type in the dashboard ID and load dashboard or copy and paste the JSON found under the 'prometheus' folder. This has an additional graph showing the number of active alerts.

After loading the dashboard, select a name, folder and select the previously created data source. Finally, click import to load the dashboard.

![Importing dashboard](https://drive.google.com/uc?export=view&id=1G-3wK9CXblRSya_EmL2_AH7NqGq1WUMD)

On the dashboard you should be able to see that the RabbitMQ server is up and running and for how long, the number of exchanges between the producer and the consumer, the number of channels, consumers, connections, queues, the status of the messages and how many of them are ready, published, delivered or unacknowledged, the total number of messages in the queue, how much of RabbitMQ's memory is used in the transfer, number of used file descriptors and number of open sockets.

![Looking at the dashboard](https://drive.google.com/uc?export=view&id=1z9pz1JhevHJ_G2bxeY4UG2_x3dGmN0w-)

### Activity subject to action
* number of unacknowledged messages (if high and close to no of delivered for long periods of time)
* number of ready messages (if high for long periods of time)
* memory usage (if increasing)
* number of consumers (if less than expected)
* number of connections (if less than expected)
* node load coverage (if higher than CPU cores)

### Actions
* restart consumer if failed
* start additional consumers in order to alleviate pressure on the consumer(s)
* stop consumers if not needed (depending on usage)

### System workflow
![Monitoring System Workflow](https://drive.google.com/uc?export=view&id=1mJSsiUr52PYvBV0ia_bV0_AhmwzhgkDm)