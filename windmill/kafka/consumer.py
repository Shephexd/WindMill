import os
import sys

from confluent_kafka import Consumer, KafkaException, KafkaError

from windmill.configs import KAFKA_CONSUMER_CONFIG

if __name__ == "__main__":
    topics = os.environ["CLOUDKARAFKA_TOPIC"].split(",")

    c = Consumer(**KAFKA_CONSUMER_CONFIG)
    c.subscribe(topics)
    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                # Error or event
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write(
                        "%% %s [%d] reached end at offset %d\n"
                        % (msg.topic(), msg.partition(), msg.offset())
                    )
                elif msg.error():
                    # Error
                    raise KafkaException(msg.error())
            else:
                # Proper message
                sys.stderr.write(
                    "%% %s [%d] at offset %d with key %s:\n"
                    % (msg.topic(), msg.partition(), msg.offset(), str(msg.key()))
                )
                print(msg.value())

    except KeyboardInterrupt:
        sys.stderr.write("%% Aborted by user\n")

    # Close down consumer to commit final offsets.
    c.close()
