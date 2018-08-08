import sys
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

sys.path.append("..")

from models.main import session
from models.tag import Tag as TagModel


class Tag(SQLAlchemyObjectType):
    class Meta:
        model = TagModel
        interfaces = (relay.Node,)


class Query(graphene.AbstractType):
    node = relay.Node.Field()
    all_tags = SQLAlchemyConnectionField(Tag)
    find_tag = graphene.Field(lambda: Tag, uid=graphene.Int())

    def resolve_find_tag(self, args, context, info):
        query = Tag.get_query(context)
        uid = args.get('uid')
        return query.filter(TagModel.uid == uid).first()


class addTag(graphene.Mutation):
    class Input:
        name = graphene.String()

    tag = graphene.Field(Tag)

    @classmethod
    def mutate(cls, _, args, context, info):
        tag = TagModel(name=args.get('name'), articles=[])
        session.add(tag)
        session.commit()
        return addTag(tag=tag)


class modifyTag(graphene.Mutation):
    class Input:
        uid = graphene.Int()
        name = graphene.String()

    tag = graphene.Field(Tag)

    @classmethod
    def mutate(cls, _, args, context, info):
        query = Tag.get_query(context)
        uid = args.get('uid')
        name = args.get('name')
        tag = query.filter(TagModel.uid == uid).first()
        tag.name = name
        session.commit()
        return modifyTag(category=tag)


class removeTag(graphene.Mutation):
    class Input:
        uid = graphene.Int()

    theID = graphene.Int()

    @classmethod
    def mutate(cls, _, args, context, info):
        query = Tag.get_query(context)
        uid = args.get('uid')
        query.filter(TagModel.uid == uid).delete()
        session.commit()
        return removeTag(theID=uid)


class Mutations(graphene.AbstractType):
    add_tag = addTag.Field()
    modify_tag = modifyTag.Field()
    remove_tag = removeTag.Field()
