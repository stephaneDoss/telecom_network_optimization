from kafka import KafkaProducer
import os

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Assurez-vous que le port est correct
    value_serializer=lambda v: v,  # Pas de sérialisation, envoi des bytes directement
    api_version=(2, 7, 0)  # Spécifiez la version du broker Kafka
)

# Fonction pour lire un fichier CSV et envoyer son contenu à Kafka


def ingest_csv_to_kafka(file_path, topic):
    with open(file_path, mode='rb') as file:
        file_content = file.read()
        producer.send(topic, value=file_content)
        print(f"Envoyé: {file_path} à {topic}")


# Liste des fichiers CSV et des topics correspondants
csv_files = {
    'data\\sms-call-internet\\sms-call-internet-mi-2013-11-01.csv': 'sms-call-intenet',
    'data\\mi-to-province\\mi-to-provinces-2013-11-01.csv': 'mi-to-province'
}

# Ingestion des fichiers CSV
for file_path, topic in csv_files.items():
    if os.path.exists(file_path):
        ingest_csv_to_kafka(file_path, topic)
        print('ingestion')
    else:
        print(f"Fichier non trouvé: {file_path}")

# Fermer le producteur
producer.flush()
producer.close()
