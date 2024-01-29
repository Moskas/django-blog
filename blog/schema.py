from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from blog import models
import graphene


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile


class PostType(DjangoObjectType):
    class Meta:
        model = models.Post


class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    all_tags = graphene.List(TagType)
    all_authors = graphene.List(AuthorType)
    latest_posts = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())
    posts_by_id = graphene.List(PostType, id=graphene.ID())

    def resolve_all_posts(root, info, order_by=None):
        return models.Post.objects.prefetch_related("tags").select_related("author").all()

    def resolve_all_tags(root, info):
        return models.Tag.objects.all()

    def resolve_all_authors(root, info):
        return models.Profile.objects.select_related("user").all()

    def resolve_author_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )

    def resolve_posts_by_id(root, info, id):
        return models.Post.objects.filter(id=id)

    def resolve_latest_posts(root, info):
        return models.Post.objects.prefetch_related("tags").select_related("author").order_by("-id")[:5]


schema = graphene.Schema(query=Query)
