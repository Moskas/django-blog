from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from blog.models import Post


class RssTutorialsFeeds(Feed):
    title = "Tutorials"
    link = "/latesttutorials/"
    description = "Recent free tutorials on LearnDjango.com."

    def items(self):
        return Post.objects.order_by("-publish_date")[:100]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)

    def item_lastupdated(self, item):
        return item.publish_date