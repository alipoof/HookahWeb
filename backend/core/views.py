from django.views.generic import ListView
from .models import Table, Reserve, Review


class TableListView(ListView):
    model = Table
    pass


class ReserveView():
    pass


class ReviewView():
    pass
