from django.contrib.sitemaps import Sitemap
from .models import Category, Product, ForeignPage
from blog.models import Post
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return ['Index',]

    def location(self, item):
        return reverse(item)

class ForeignPageSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.5
	protocol = 'https'
	
	def items(self):
		return ForeignPage.objects.all()

class BlogSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.5
	protocol = 'https'
	
	def items(self):
		return Post.objects.all()
		
class ProductSitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.8
	protocol = 'https'
	
	def items(self):
		return Product.objects.all()
		
class CategorySitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.6
	protocol = 'https'
	
	def items(self):
		return Category.objects.all()