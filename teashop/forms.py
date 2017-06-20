from django import forms
from collections import defaultdict

from haystack.forms import FacetedSearchForm, SearchForm

class ProductSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()
        
    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        if not self.cleaned_data.get('q'):
            return self.no_query_found()

        sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

        if self.load_all:
            sqs = sqs.load_all()
            
        found = True
            
        if not sqs:
            sqs = self.searchqueryset.all()
            found = False

        return (sqs, found)

class FacetedNotEmptySearchForm(FacetedSearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()

    @property
    def selected_multi_facets(self):
        selected_multi_facets = defaultdict(list)
        for facet_kv in self.selected_facets:
            if ":" not in facet_kv:
                continue
            field_name, value = facet_kv.split(':', 1)
            selected_multi_facets[field_name].append(value)
        return selected_multi_facets

    def search(self):
        sqs = super(FacetedSearchForm, self).search()
        for field, values in self.selected_multi_facets.items():
            if not values:
                continue
            clean_values = ['"%s"' % sqs.query.clean(val) for val in values]
            sqs = sqs.narrow(u'%s:(%s)' % (field, " OR ".join(clean_values)))
        return sqs

class UploadFileForm(forms.Form):
    file = forms.FileField()
    
class ExportProductsForm(forms.Form):
    slug = forms.CharField()

