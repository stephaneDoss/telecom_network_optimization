#!/bin/bash

# Configuration Kafka
KAFKA_BROKER="kafka:9092"  # Nom du service Kafka dans Docker Compose
TOPICS=("sms-call-intenet", "mi-to-province")

# Fonction pour créer un topic Kafka
create_topic() {
    local topic=$1
    echo "Creating topic $topic..."
    kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic "$topic"
}

# Création des topics
for TOPIC in "${TOPICS[@]}"; do
    create_topic "$TOPIC"
done
