import sys
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from .articles import ArticleModel

sys.path.append("..")

from models.main import session
from models.comment import Comment as CommentModel


class Comment(SQLAlchemyObjectType):
    class Meta:
        model = CommentModel
        interfaces = (relay.Node,)


class Query(graphene.AbstractType):
    node = relay.Node.Field()
    all_comments = SQLAlchemyConnectionField(Comment)


class addComment(graphene.Mutation):
    class Input:
        article_id = graphene.Int(required=True)
        author = graphene.String(required=True)
        email = graphene.String(required=True)
        content = graphene.String()

    comment = graphene.Field(Comment)

    @classmethod
    def mutate(cls, _, args, context, info):
        comment = CommentModel(author=args.get('author'), email=args.get('email'), content=args.get('content'))
        article = session.query(ArticleModel).filter_by(uid=args.get('article_id')).first()
        article.comments.append(comment)
        session.commit()
        return addComment(comment=comment)


class removeComment(graphene.Mutation):
    class Input:
        uid = graphene.Int(required=True)

    uid = graphene.Int()

    @classmethod
    def mutate(cls, _, args, context, info):
        query = Comment.get_query(context)
        uid = args.get('uid')
        query.filter(CommentModel.uid == uid).delete()
        session.commit()
        return removeComment(uid=uid)


class Mutations(graphene.AbstractType):
    add_comment = addComment.Field()
    remove_comment = removeComment.Field()
