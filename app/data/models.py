from django.db import models
from insight.models import AbstractBaseModel


class Token(AbstractBaseModel):
    symbol = models.CharField('symbol', max_length=100)

    def __str__(self):
        return self.symbol

    class Meta:
        verbose_name = 'token'
        verbose_name_plural = 'tokens'


class Pair(AbstractBaseModel):
    pool_id = models.CharField('pool id (address)', max_length=255)
    token_1 = models.ForeignKey(Token, on_delete=models.PROTECT, related_name='pairs_token_1')
    token_2 = models.ForeignKey(Token, on_delete=models.PROTECT, related_name='pairs_token_2')

    def __str__(self):
        return f'{self.token_1.symbol} - {self.token_2.symbol}'

    class Meta:
        verbose_name  = 'pair'
        verbose_name_plural  = 'pairs'


class DailySnapshot(AbstractBaseModel):
    pair = models.ForeignKey(Pair, on_delete=models.PROTECT)
    snapshot_id = models.CharField('pool id (address)', max_length=255, db_index=True, unique=True)
    timestamp = models.PositiveBigIntegerField('timestamp', db_index=True)
    volume = models.PositiveBigIntegerField('volume', help_text='volume in token units') # Decimals are currently irrelevant for calculations
    volume_usd = models.PositiveBigIntegerField('volume (USD)')
    token_1_balance = models.PositiveBigIntegerField('token 1 balance')
    token_2_balance = models.PositiveBigIntegerField('token 2 balance')
    token_1_price = models.FloatField('token 1 price (in token 2 units)') # DecimalField would be more adequate, using FloatField for development speed
    token_1_price_usd = models.FloatField('price')

    class Meta:
        verbose_name = 'daily snapshot'
        verbose_name_plural = 'daily snapshots'
        ordering = ('timestamp', )


class HourlySnapshot(AbstractBaseModel):
    pair = models.ForeignKey(Pair, on_delete=models.PROTECT)
    snapshot_id = models.CharField('pool id (address)', max_length=255, db_index=True, unique=True)
    timestamp = models.PositiveBigIntegerField('timestamp', db_index=True)
    volume = models.PositiveBigIntegerField('volume', help_text='volume in token units') # Decimals are currently irrelevant for calculations
    volume_usd = models.PositiveBigIntegerField('volume (USD)')
    token_1_balance = models.PositiveBigIntegerField('token 1 balance')
    token_2_balance = models.PositiveBigIntegerField('token 2 balance')
    token_1_price = models.FloatField('token 1 price (in token 2 units)') # DecimalField would be more adequate, using FloatField for development speed
    token_1_price_usd = models.FloatField('price')

    class Meta:
        verbose_name = 'hourly snapshot'
        verbose_name_plural = 'hourly snapshots'
        ordering = ('timestamp', )
