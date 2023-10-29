from django.conf import settings
from gql.transport.aiohttp import AIOHTTPTransport
from gql import Client

from data.queries import hourly_snapshots


def fetch_slice(from_timestamp, to_timestamp):
    transport = AIOHTTPTransport(
        url='https://api.chainbase.online/v1/subgraphs/ethereum_sushiswap/1.0.0',
        headers={'x-api-key': settings.CHAINBASE_API_KEY}
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    result = client.execute(hourly_snapshots, variable_values={ 'poolId': '0xc40d16476380e4037e6b1a2594caf6a6cc8da967' })

    print(result)


def fetch_data(from_timestamp, to_timestamp):
    # Fetches data in batches to complete full timestamp range
    pass
