import sys
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

sys.path.append("..")

from models.main import session
from models.article import Article as ArticleModel
from models.category import Category as CategoryModel


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (relay.Node,)


class Query(graphene.AbstractType):
    node = relay.Node.Field()
    all_categories = SQLAlchemyConnectionField(Category)
    find_category = graphene.Field(lambda: Category, uid=graphene.Int())

    def resolve_find_category(self, args, context, info):
        query = Category.get_query(context)
        uid = args.get('uid')
        return query.filter(CategoryModel.uid == uid).first()


class addCategory(graphene.Mutation):
    class Input:
        name = graphene.String()

    category = graphene.Field(Category)

    @classmethod
    def mutate(cls, _, args, context, info):
        category = CategoryModel(name=args.get('name'), articles=[])
        session.add(category)
        session.commit()
        return addCategory(category=category)


class modifyCategory(graphene.Mutation):
    class Input:
        uid = graphene.Int()
        name = graphene.String()

    category = graphene.Field(Category)

    @classmethod
    def mutate(cls, _, args, context, info):
        query = Category.get_query(context)
        uid = args.get('uid')
        name = args.get('name')
        category = query.filter(CategoryModel.uid == uid).first()
        category.name = name
        session.commit()
        return modifyCategory(category=category)


class removeCategory(graphene.Mutation):
    class Input:
        uid = graphene.Int()

    theID = graphene.Int()

    @classmethod
    def mutate(cls, _, args, context, info):
        query = Category.get_query(context)
        uid = args.get('uid')
        query.filter(CategoryModel.uid == uid).delete()
        session.commit()
        return removeCategory(theID=uid)


class Mutations(graphene.AbstractType):
    add_category = addCategory.Field()
    modify_category = modifyCategory.Field()
    remove_category = removeCategory.Field()
