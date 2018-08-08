import graphene
from .articles import Query as ArticleQuery, Mutations as ArticleMutations, Article
from .categories import Query as CategoryQuery, Mutations as CategoryMutations, Category
from .comments import Query as CommentQuery, Mutations as CommentMutations, Comment
from .tags import Query as TagQuery, Mutations as TagMutations, Tag
from .users import Query as UserQuery, Mutations as UserMutations, User


class Query(ArticleQuery, CategoryQuery, CommentQuery, TagQuery, UserQuery, graphene.ObjectType):
    pass


class Mutations(ArticleMutations, CategoryMutations, CommentMutations, TagMutations, UserMutations,
                graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations, types=[Article, Category, Comment, Tag, User])

__version__ = "1.0"

__all__ = [
    "__version__",
    "schema"
]
