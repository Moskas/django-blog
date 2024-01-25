from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from blog.models import Post


class RssTutorialsFeeds(Feed):
    title = "Moskas' Blog"
    link = "http://localhost:8000/feed/"
    description = "Random ramblings"

    def items(self):
        return Post.objects.order_by("-publish_date")[:100]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_pubdate(self, item):
        return item.publish_date
