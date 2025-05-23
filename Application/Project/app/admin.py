from django.contrib import admin
from .models import Sale, BadOrder
from .models import Inventory
from .models import Expense


admin.site.register(Sale)
admin.site.register(BadOrder)
admin.site.register(Inventory)
admin.site.register(Expense)

