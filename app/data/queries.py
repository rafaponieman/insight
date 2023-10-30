from gql import gql

hourly_snapshots = gql(
    """
    query HourlySnapshots($poolId: ID!, $timestampGte: BigInt, $timestampLte: BigInt, $skip: Int) {
        liquidityPool(id: $poolId) {
            id
            hourlySnapshots(
                where: {timestamp_gte: $timestampGte, timestamp_lte: $timestampLte},
                skip: $skip
            ) {
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
