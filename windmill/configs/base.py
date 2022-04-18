import os


# Consumer configuration
# See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
KAFKA_CONSUMER_CONFIG = {
    "bootstrap.servers": os.environ["CLOUDKARAFKA_BROKERS"],
    "group.id": "%s-consumer" % os.environ["CLOUDKARAFKA_USERNAME"],
    "session.timeout.ms": 6000,
    "default.topic.config": {"auto.offset.reset": "smallest"},
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "SCRAM-SHA-256",
    "sasl.username": os.environ["CLOUDKARAFKA_USERNAME"],
    "sasl.password": os.environ["CLOUDKARAFKA_PASSWORD"],
}
