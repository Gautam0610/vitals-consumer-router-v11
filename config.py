# config.py
import os

INPUT_TOPIC = os.environ.get("INPUT_TOPIC", "input_topic")
OUTPUT_TOPIC = os.environ.get("OUTPUT_TOPIC", "output_topic")
ERROR_TOPIC = os.environ.get("ERROR_TOPIC", "error_topic")
KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "localhost:9092")
SASL_USERNAME = os.environ.get("SASL_USERNAME", "")
SASL_PASSWORD = os.environ.get("SASL_PASSWORD", "")