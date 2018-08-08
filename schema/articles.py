import sys
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

sys.path.append("..")
from models.main import session
from models.article import Article as ArticleModel
from models.user import User as UserModel
from models.category import Category as CategoryModel
from models.tag import Tag as TagModel


class Article(SQLAlchemyObjectType):
    class Meta:
        model = ArticleModel
        interfaces = (relay.Node,)


class Query(graphene.AbstractType):
    node = relay.Node.Field()
    all_articles = SQLAlchemyConnectionField(Article)
    find_article = graphene.Field(lambda: Article, uid=graphene.Int())

    def resolve_find_article(self, args, context, info):
        query = Article.get_query(context)
        uid = args.get('uid')
        article = query.filter(ArticleModel.uid == uid).first()
        return article


class addArticle(graphene.Mutation):
    class Input:
        title = graphene.String()
        content = graphene.String()
        user_id = graphene.Int()
        cate_id = graphene.Int()
        tags_id = graphene.List(graphene.Int)

    article = graphene.Field(Article)

    @classmethod
    def mutate(cls, _, args, context, info):
        user = session.query(UserModel).filter_by(uid=args.get('user_id')).first()
        category = session.query(CategoryModel).filter_by(uid=args.get('cate_id')).first()
        article = ArticleModel(title=args.get('title'), content=args.get('content'), author=user, category=category, comments=[], tags=[])
        for id in args.get('tags_id'):
            tag = session.query(TagModel).filter_by(uid=id).first()
            article.tags.append(tag)
        session.add(article)
        session.commit()
        return addArticle(article=article)


class modifyArticle(graphene.Mutation):
    class Input:
        uid = graphene.Int(required=True)
        title = graphene.String()
        content = graphene.String()
        cate_id = graphene.Int()
        tags_id = graphene.List(graphene.Int)

    article = graphene.Field(Article)

    @classmethod
    def mutate(cls, _, args, context, info):
        query = Article.get_query(context)
        article = query.filter(ArticleModel.uid == args.get('uid')).first()
        if args.get('title') is not None:
            article.title = args.get('title')
        if args.get('content') is not None:
            article.content = args.get('content')
        if args.get('user_id') is not None:
            user = session.query(UserModel).filter_by(uid=args.get('user_id')).first()
            article.author = user
        if args.get('cate_id') is not None:
            category = session.query(CategoryModel).filter_by(uid=args.get('cate_id')).first()
            article.category = category
        if args.get('tags_id') is not None:
            article.tags = []
            for id in args.get('tags_id'):
                tag = session.query(TagModel).filter_by(uid=id).first()
                article.tags.append(tag)
        session.commit()
        return modifyArticle(article=article)


class removeArticle(graphene.Mutation):
    class Input:
        uid = graphene.Int(required=True)

    uid = graphene.Int()

    @classmethod
    def mutate(cls, _, args, context, info):
        query = Article.get_query(context)
        uid = args.get('uid')
        query.filter(ArticleModel.uid == uid).delete()
        session.commit()
        return removeArticle(uid=uid)


class Mutations(graphene.AbstractType):
    add_article = addArticle.Field()
    modify_article = modifyArticle.Field()
    remove_article = removeArticle.Field()
