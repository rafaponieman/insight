from gql import gql

hourly_snapshots = gql(
    """
    query DailySnapshots($poolId: ID!, $timestampGte: BigInt, $timestampLte: BigInt, $skip: Int) {
        liquidityPool(id: $poolId) {
            id
            dailySnapshots(
                where: {timestamp_gte: $timestampGte, timestamp_lte: $timestampLte},
                skip: $skip
            ) {
                id
                dailyVolumeByTokenAmount
                dailyVolumeUSD
                timestamp
                inputTokenBalances
            }
        }
    }
"""
)
