from gql import Client
from gql.transport.requests import RequestsHTTPTransport

class APIClient:
    def __init__(self, api_key):
        url = "https://se-staging.ee.ethz.ch/graphql" # "https://endoc.ethz.ch/graphql"
        self.client = Client(
            transport = RequestsHTTPTransport(
                url=url,
                headers={'x-api-key': api_key}
            ),
            fetch_schema_from_transport=True,
        )

    def execute_query(self, query, variable_values=None):
        return self.client.execute(query, variable_values or {})