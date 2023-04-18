from .models import User
from haystack import indexes


class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')

    def get_model(self):
        return User

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
