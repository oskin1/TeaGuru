import datetime
from haystack import indexes
from .models import Product
from decimal import Decimal

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/product_text.txt')
    name = indexes.EdgeNgramField(model_attr='name')
    price = indexes.DecimalField(model_attr='price')
    brief = indexes.CharField(model_attr='brief')
    metadata = indexes.CharField(model_attr='metadata')
    
    #related objects
    tag = indexes.MultiValueField(faceted=True)
    category = indexes.MultiValueField()
    manufacturer = indexes.CharField(model_attr='manufacturer__name', faceted=True)

    suggestions = indexes.FacetCharField()

    def get_model(self):
        return Product
        
    def prepare_price(self, obj):
        return Decimal(obj.price) * obj.netto

    def prepare_tag(self, obj):
        tags = obj.tag.all()
        if len(tags) > 0:
            return [tag.name for tag in tags]

    def prepare_category(self, obj):
        categories = obj.category.all()
        if len(categories) > 0:
            return [category.name for category in categories]
        
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date_updated__lte=datetime.datetime.now())
