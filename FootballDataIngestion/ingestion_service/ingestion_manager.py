class IngestionManager:
    def __init__(self, api_client):
        self.api_client = api_client

    def ingest_data(self):
        print("Ingesting data...")
        # Get Teams
        teams = self.api_client.get_teams()

        # Get Competitions
        competitions = self.api_client.get_competitions()

        print("Teams: ", teams)
        print("Competitions: ", competitions)