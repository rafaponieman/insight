from django.contrib import admin

from data.models import Pair, Token


class TokenAdmin(admin.ModelAdmin):
    pass


class PairAdmin(admin.ModelAdmin):
    pass


admin.site.register(Token, TokenAdmin)
admin.site.register(Pair, PairAdmin)
