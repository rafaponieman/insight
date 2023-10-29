from gql import gql

hourly_snapshots = gql(
    """
    query HourlySnapshots($poolId: ID!) {
      liquidityPool(id: $poolId) {
        id
        hourlySnapshots {
            id
            hourlyVolumeByTokenAmount
            hourlyVolumeUSD
            timestamp
            inputTokenBalances
        }
      }
    }
"""
)
