# rabbit-prometheus-monitor
RabbitMQ monitored with Prometheus and Grafana in Docker Compose

The purpose of this project is to monitor a simple RabbitMQ queue and automatically take action on unusual activity.

### Unusual activity subject to action
* difference between published and delivered messages
* number of ready messages (if high)
* memory usage (if increasing)
* number of consumers (if less than expected)
* node load coverage (if higher than CPU cores)

### Possible actions
* restart consumer if failed
* prevent consumer from failing by starting another consumer
* stop consumers if not needed (depending on usage)