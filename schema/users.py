import sys
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

sys.path.append("..")

from models.main import session
from models.user import User as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


class Query(graphene.AbstractType):
    node = relay.Node.Field()
    find_user = graphene.Field(lambda: User, uid=graphene.Int())

    def resolve_find_user(self, args, context, info):
        query = User.get_query(context)
        uid = args.get('uid')
        return query.filter(UserModel.uid == uid).first()


class addUser(graphene.Mutation):
    class Input:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        nickname = graphene.String()
        email = graphene.String(required=True)

    user = graphene.Field(User)

    @classmethod
    def mutate(cls, _, args, context, info):
        user = UserModel(username=args.get('username'), password=args.get('password'), nickname=args.get('nickname'),
                         email=args.get('email'), articles=[])
        session.add(user)
        session.commit()
        return addUser(user=user)


class modifyUser(graphene.Mutation):
    class Input:
        uid = graphene.Int(required=True)
        username = graphene.String()
        password = graphene.String()
        nickname = graphene.String()
        email = graphene.String()

    user = graphene.Field(User)

    @classmethod
    def mutate(cls, _, args, context, info):
        query = User.get_query(context)
        uid = args.get('uid')
        user = query.filter(UserModel.uid == uid).first()
        if args.get('username') is not None:
            user.username = args.get('username')
        if args.get('password') is not None:
            user.username = args.get('password')
        if args.get('nickname') is not None:
            user.username = args.get('nickname')
        if args.get('email') is not None:
            user.username = args.get('email')
        session.commit()
        return modifyUser(user=user)


class removeUser(graphene.Mutation):
    class Input:
        uid = graphene.Int()

    theID = graphene.Int()

    @classmethod
    def mutate(cls, _, args, context, info):
        query = User.get_query(context)
        uid = args.get('uid')
        query.filter(UserModel.uid == uid).delete()
        session.commit()
        return removeUser(theID=uid)


class Mutations(graphene.AbstractType):
    add_user = addUser.Field()
    modify_user = modifyUser.Field()
    remove_user = removeUser.Field()
