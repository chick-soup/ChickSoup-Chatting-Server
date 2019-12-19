from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    ListField,
    IntField
)


class chatDataModel(EmbeddedDocument):
    userId = StringField()

    name = StringField()

    chat = StringField()

    time = IntField()


class chattingRoomModel(Document):
    roomId = StringField(primary_key=True)

    roomName = StringField()

    peoples = ListField()

    chatData = ListField(
        list = EmbeddedDocumentField(chatDataModel),
    )