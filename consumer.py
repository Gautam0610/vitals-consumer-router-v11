
import json
import os
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from validator import validate_vitals

# Read environment variables
INPUT_TOPIC = os.environ.get("INPUT_TOPIC")
OUTPUT_TOPIC = os.environ.get("OUTPUT_TOPIC")
ERROR_TOPIC = os.environ.get("ERROR_TOPIC")
KAFKA_BROKER = os.environ.get("KAFKA_BROKER")
SASL_USERNAME = os.environ.get("SASL_USERNAME")
SASL_PASSWORD = os.environ.get("SASL_PASSWORD")

# Configure Kafka consumer
consumer = KafkaConsumer(
    INPUT_TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    sasl_mechanism="PLAIN",
    security_protocol="SASL_SSL",
    sasl_plain_username=SASL_USERNAME,
    sasl_plain_password=SASL_PASSWORD,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
)

# Configure Kafka producer
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    sasl_mechanism="PLAIN",
    security_protocol="SASL_SSL",
    sasl_plain_username=SASL_USERNAME,
    sasl_plain_password=SASL_PASSWORD,
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)


def main():
    try:
        for message in consumer:
            vitals_data = message.value
            is_valid, errors = validate_vitals(vitals_data)

            if is_valid:
                producer.send(OUTPUT_TOPIC, value=vitals_data)
                producer.flush()
                print(f"Valid data routed to {OUTPUT_TOPIC}: {vitals_data}")
            else:
                producer.send(ERROR_TOPIC, value={"data": vitals_data, "errors": errors})
                producer.flush()
                print(f"Invalid data routed to {ERROR_TOPIC}: {vitals_data}, Errors: {errors}")

    except KafkaError as e:
        print(f"Kafka error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        consumer.close()
        producer.close()

if __name__ == "__main__":
    main()
