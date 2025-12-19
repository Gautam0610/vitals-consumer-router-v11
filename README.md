# vitals-consumer-router-v11

A Kafka consumer for routing vitals data based on validation.

## Usage

1.  Set the following environment variables:
    *   `INPUT_TOPIC`: The Kafka topic to consume from.
    *   `OUTPUT_TOPIC`: The Kafka topic to produce valid data to.
    *   `ERROR_TOPIC`: The Kafka topic to produce invalid data to.
    *   `KAFKA_BROKER`: The Kafka broker address.
    *   `SASL_USERNAME`: The SASL username for Kafka authentication.
    *   `SASL_PASSWORD`: The SASL password for Kafka authentication.

2.  Build the Docker image:
    `docker build -t vitals-consumer-router-v11 .`

3.  Run the Docker container:
    `docker run -e INPUT_TOPIC=<input_topic> -e OUTPUT_TOPIC=<output_topic> -e ERROR_TOPIC=<error_topic> -e KAFKA_BROKER=<kafka_broker> -e SASL_USERNAME=<sasl_username> -e SASL_PASSWORD=<sasl_password> vitals-consumer-router-v11`