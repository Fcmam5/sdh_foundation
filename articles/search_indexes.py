import datetime
from haystack import indexes
from articles.models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    description = indexes.CharField(model_attr='description')
    pub_date = indexes.DateTimeField(model_attr='posted')

    def get_model(self):
        return Article

    # TODO: Get only non-drafted articles
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(published=True)
