from api_client.client import FootballApiClient
from ingestion_service.ingestion_manager import IngestionManager

def main():
    api_client = FootballApiClient()
    print("Client: ", api_client)
    ingestion_manager = IngestionManager(api_client)
    print("Manager: ", ingestion_manager)
    ingestion_manager.ingest_data()

if __name__ == '__main__':
    main()