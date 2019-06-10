# rabbit-prometheus-monitor
RabbitMQ monitored with Prometheus and Grafana in Docker Compose

The purpose of this project is to monitor a simple RabbitMQ queue and automatically take action on unusual activity.

### Useful Links
[A review of queuing and monitoring tools](https://docs.google.com/presentation/d/1E9UC7Z4gX9Nnxdm-bwKdcTaw7ntdBsG_PwtkhZVzl1M/edit#slide=id.gc6f73a04f_0_0)

#### RabbitMQ
* [What is RabbitMQ](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html)
* [Official basic queue and exchange tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
* [Pika](https://pika.readthedocs.io/en/stable/intro.html)
* [Best practice](https://www.cloudamqp.com/blog/2017-12-29-part1-rabbitmq-best-practice.html)
* [Prometheus exporter](https://github.com/kbudde/rabbitmq_exporter)

#### Prometheus
* [Official documentation](https://prometheus.io/docs/introduction/overview/)
* [Prometheus integrated alerts](https://awesome-prometheus-alerts.grep.to/rules.html)
* [Prometheus querying basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
* [Alert manager](https://itnext.io/prometheus-with-alertmanager-f2a1f7efabd6)
* [Alert executor](https://github.com/imgix/prometheus-am-executor)

#### Grafana
* [Official documentation](http://docs.grafana.org/)
* [Pre-built dashboards](https://grafana.com/dashboards?search=rabbitmq)

### Intstallation and Run
To install, clone the repository and run the following commands in the root folder:

```docker-compose build```

```docker-compose up```

To start more instances of the consumer, use docker-compose's scale flag:
```docker-compose up --scale consumer=<number_of_instances>```

This will make the following localhost ports available for monitoring:
* 15672 for RabbitMQ (username and password 'guest')
* 9090 for Prometheus
* 9093 for Alertmanager
* 3000 for Grafana (username and password 'admin')

To stop services, press Ctrl+C and the run the following command:
```docker-compose down```

### Basic Utilisation
#### RabbitMQ
RabbitMQ's management console overview section shows two main graphs, one for queued messages and one for the message rates and their statuses.

##### Message status types
* ready = messages that are waiting in the queue to be delivered
* published = messages that have been sent
* delivered = messages that have reached the consumer(s)
* unacked = messages that have been sent but have not been acknowledged by the consumer(s)

![Creating a data source](https://drive.google.com/uc?export=view&id=1fqjLDC3wOVSXaZycATAsYtDyHsD0PwwU)

Below, under 'Global counts', there can be found a count of the connections, channels, exchanges, queues and consumers. This is followed by a description of any existent nodes inside the RabbitMQ cluster together with how long they have been up and running and how much of the resources they have been consuming since.

The connections tab shows the current connections with the RabbitMQ server, including the connection onto which it opperates, the state, protocol (AMQP), the number of active channels using the connection and whether the connection is secured with SSL.

![RMQ Connections](https://drive.google.com/uc?export=view&id=1y-JEyyaxJ5SG3yhg0SUlv3ioBTZGIZ3k)

Clicking on the connection will show the connection's details such as activity, channels running in it and their details, runtime metrics and the option to force the connection closed.

![RMQ Connection Details](https://drive.google.com/uc?export=view&id=1737nUYskACCWeC82Q-Za6tLuDj2sIXhz)

The channel tab shows all RabbitMQ's channels and in a similar way to the connections these can be expanded for further specific details.

An exchange is the procedure used by the producer to send the messages. It can either be sending them to all consumers, directly to a specific consumer or to consumers interested in a specific topic. The exchange tab shows all defined exchanges and their types. Clicking on an exchange can allow the visualisation of what queues are added to the exchange and allows the addition of more bindings or deletion of exchanges.

![RMQ Exchanges](https://drive.google.com/uc?export=view&id=16lJsuWXVNCM8cWzXqmNqVTsPC7k0SCOE)

In the queues tab, runtime metrics can be visualised as well as all available queues. These can also be manipulated starting with checking the consumers connected to it, the bindings, publishing, getting and moving of messages, deletion or purge of queues.

![RMQ Queues](https://drive.google.com/uc?export=view&id=1jF9QeoCDyWFPDEjNtKptYIevoo1s1Stq)

And finally, the Admin view offers the possibility of adding and deleting users, changing user permissions and setting up virtual hosts.

#### Prometheus
Prometheus's management console has basic structure and options that can offer valuable insight into the system's state and performance. The main page holds a query field and a graphical representation of the query results. Right next to the 'Execute' button there is a list of main queries available for general use. These can, however, be expanded on and can be later used as rules for alarm configurations and more detailed visual representations of the data. Documentation on the basics of Prometheus' querying language can be found above.

![Prometheus Graphs Page](https://drive.google.com/uc?export=view&id=1XLKVZjlMENxpj3YzQDIE5VoXRsB2Dzx8)

A sample query indicates the percentage of the availability of the current consumer. It can be observed that the consumer struggles to ingest all the messages considering a delay of three seconds on every ingest. This is particularly useful for testing queries for alert rules and how a slow consumer can affect the workflow.

![Looking for bottlenecks](https://drive.google.com/uc?export=view&id=1CxrmnPfHkj04G_eukswhEdG0MbBSocZ9)

Prometheus also offers a simple view of the defined alarms, together with their details and status. Options for the manipulation of alerts does not take place here but in alertmanager's console. 

![Alerts](https://drive.google.com/uc?export=view&id=1WzZUXHsBbE4iooXKoGImpmUzmxw8u2Ur)

Under the status option there can be found the rules for these alerts together with the targets, runtime and build information.

![Rules](https://drive.google.com/uc?export=view&id=1HP_pjJheTQcWFKUT7yv-HWI-iE51Iirc)

#### Alertmanager  
Alertmanager will require a Slack webhook URL defined in the configuration file for notifications. This requires the setup of an app in your Slack workspace, the activation of incoming webhooks and the addition of a new webhook to the workspace with a defined channel for the alert notifications to target. More detailed instructions on how to do this can be found [here](https://api.slack.com/incoming-webhooks).

Please note that the alertmanager console will only show alerts once they are fired by Prometheus.

![Alertmanager console](https://drive.google.com/uc?export=view&id=12IRbZN02Pl1BPJCHeuHKW4MRI3Vc8s1C)

Alertmanager will then send a notification with the details of the alert on the specified Slack channel.

![Slack notification](https://drive.google.com/uc?export=view&id=1-x01fIg79KN6cznxpPfH-p837WxcjO8T)

When this issue is resolved, another notification will be sent to Slack.

![Slack resolved](https://drive.google.com/uc?export=view&id=1scBh1hJ-38j2Qnw6jTgEobKcppfwfqdL)

#### Prometheus-Executor
This golang based tool is used to listen to the alert manager and trigger actions to fix the system issues causing the notifications. These actions can be restarting a service, launching another one to balance workload and more to the limits of bash scripting.

To build the executor, clone prometheus-am-executor in the executor file, change line 7 of the Makefile to ```export  GOPATH := ${CURDIR}/prometheus-am-executor-go```, save and run ```make all```. This will create a 'prometheus-am-executor-go' file which contains an executable 'prometheus-am-executor' script inside a bin folder.

To run the executor, run the following command in a terminal window from the bin file containing the 'prometheus-am-executor' script:
```./prometheus-am-executor [options] ../../action_scripts/test_script.sh```

Where the options are:
```
-l string
    for HTTP port to listen on (default is 8080)
-v 
    to enable verbose/debug logging
``` 

#### Grafana
The first step when monitoring with Grafana is creating a Data Source for Prometheus in order to link Grafana to the Prometheus metric readings of RabbitMQ. In order to do this, open the configuration options in the side menu and select the 'Data Source' option.

![Creating a data source](https://drive.google.com/uc?export=view&id=1s9AbCskDcmLO6DPoIMNXMmISeqNYMw0L)

This will open a set of data source options recognised by Grafana. Selecting Prometheus will open the following page. Here, select the host and port where Prometheus management console is currently running and specify that this is being accessed via a browser. Clicking save and test will show a confirmation message for the creation of the data source and a confirmation message for a successful connection.

![Connecting to Prometheus](https://drive.google.com/uc?export=view&id=1WrCPTvS6MKFdIh2PjxEIAF70KmXZsULm)

Now there is the choice between the creation of a new dashboard or usage of pre-built community dashboards. This repository is based on an imported community dashboard with ID '2121'. The repository also contains the JSON file of an expanded version of this dashboard containing two additional graphs showing the number of active alerts and the availability of the consumers. To import a dashboard, open the create options in the side menu and select import. Type in the dashboard ID for the base community version or copy and paste the JSON found under the 'prometheus' folder for the expanded version.

After setting up the dashboard, select a name, folder and select the previously created data source. Finally, click import to load the dashboard.

![Importing dashboard](https://drive.google.com/uc?export=view&id=1G-3wK9CXblRSya_EmL2_AH7NqGq1WUMD)

On the dashboard you should be able to see that RabbitMQ server is up and running and for how long, the number of exchanges between the producer and the consumer, the number of channels, consumers, connections, queues, the status of the messages and how many of them are, the total number of messages in the queue, how much of RabbitMQ's memory is used in the transfer, number of used file descriptors and number of open sockets.

![Looking at the dashboard](https://drive.google.com/uc?export=view&id=1lH_GR5Mu6Ae1fexs50H2bA6yD11TGrd3)

One major disadvantage of using Grafana as a Docker container is the volatility of the dashboards. The expectations of monitoring systems in general are for them to be constantly running services which, it could be argued, do not require the use of tools created for services to be easily and quickly restarted such as Docker. The use of Grafana outside Docker allows preservation of monitoring dashboards and settings with every run.

### System workflow
In order to make RabbitMQ communicate with Prometheus, an exporter is required to translate the metric readings from RabbitMQ format to Prometheus format. This is achieved with the help of rabbitmq_exporter. 

Prometheus can expand the visualisation options of the RabbitMQ metrics and also has the ability to generate alerts based on specifically defined rules such as checks on the numbers of consumers or connections. Prometheus, however, is restricted to only generating and visualising these alerts and has no ability to manipulate alerts or fire events based on them. For this, the implementation of alertmanager is required.

Alertmanager handles alerts sent by Prometheus, allowing their manipulation and integration of events such as email and slack messaging. This tool can also be used to silence, inhibit or group alerts of similar nature into a single notification in case there are thousands of same type firing at once. Alertmanager, however, is limited to handling alerts and notifications and cannot take system-related actions to rectify or prevent the issues. For this, prometheus_am_executor could present a possible solution.

Prometheus executor can execute commands or run scripts based on alert notifications. From the documentation it has been confirmed that it can be used to reboot systems on error, the question would be if it could be used to dynamically scale the number of consumers depending on RabbitMQ's performance. This could be done with the help of rules based on specific performance activity inside Prometheus which would be communicated to the executor via the alertmanager. The executor then would decide what action to take and execute it in order to rectify, prevent an issue or balance resources.

#### Activity subject to action
* consumer utilisation (if less than 100%)
* number of unacknowledged messages (if high and close to number of delivered messages for long periods of time)
* number of ready messages (if high for long periods of time)
* memory usage (if increasing)
* number of consumers (if less than expected)
* number of connections (if less than expected)
* node load coverage (if higher than CPU cores)

#### Actions
* restart consumer if failed
* start additional consumers in order to alleviate pressure on the current consumer(s)
* stop consumers if not needed (depending on usage)

![Monitoring System Workflow](https://drive.google.com/uc?export=view&id=1zOLxaNZxBn-yx1_Ecb9_Ug4iQeGPCU9k)