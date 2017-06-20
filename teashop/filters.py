from .models import Product, Tag, Property
        
class Facets(object):
    def __init__(self, category_slug):
        facets = {}
        props = Property.objects.filter(categories__slug=category_slug)
        
        for p in props:
            tag_set = Tag.objects.filter(prop__id=p.id, 
                                         products__in=Product.objects.filter(category__slug=category_slug)).distinct()
            facets[str(p.id)] = { 'name' : p.name,
                                  'tags' : tag_set }
                                  
        self.facets = facets.values()
        
class Fields(object):
    def __init__(self, product_slug):
        fields = {}
        props = Property.objects.filter(tags__products=Product.objects.get(slug=product_slug)).distinct()
        
        for p in props:
            tag_set = Tag.objects.filter(prop__id=p.id, 
                                         products__slug=product_slug)
            fields[str(p.id)] = { 'name' : p.name,
                                  'tags' : tag_set }
                                  
        self.fields = fields.values()