from django.conf import settings
from gql.transport.aiohttp import AIOHTTPTransport
from gql import Client

from data.queries import hourly_snapshots


def fetch_slice(from_timestamp, to_timestamp, skip):
    transport = AIOHTTPTransport(
        url='https://api.chainbase.online/v1/subgraphs/ethereum_sushiswap/1.0.0',
        headers={'x-api-key': settings.CHAINBASE_API_KEY}
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    return client.execute(
        hourly_snapshots,
        variable_values={
            'poolId': '0xc40d16476380e4037e6b1a2594caf6a6cc8da967',
            'timestampGte': from_timestamp,
            'timestampLte': to_timestamp,
            'skip': skip
        }
    )


def fetch_data(from_timestamp, to_timestamp):
    # Fetches data in batches to complete full timestamp range
    skip = 0
    data = []
    
    while True:
        data_slice = fetch_slice(from_timestamp, to_timestamp, skip)

        if (not data_slice or len(data_slice['liquidityPool']['dailySnapshots']) == 0):
            break

        data.append(data_slice['liquidityPool']['dailySnapshots'])

        skip += 100

    return data
