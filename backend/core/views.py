from django.views.generic import ListView
from .models import Table, Reserve, Review


class TableListView(ListView):
    model = Table


class ReserveView():
    pass


class ReviewView():
    pass
