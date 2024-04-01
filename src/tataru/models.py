from __future__ import annotations

import uuid

from sqlalchemy import Uuid, ForeignKey, String, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

# TODO: investigate swapping ids to uuid7

class DiscordUser(Base):
    __tablename__ = 'discorduser'

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    characters: Mapped[list[Character]] = relationship(back_populates='owner')


character_static = Table(
    'character_static',
    Base.metadata,
    Column('character_id', ForeignKey('character.id'), primary_key=True),
    Column('static_id', ForeignKey('static.id'), primary_key=True),
)


class Character(Base):
    __tablename__ = 'character'

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('discorduser.id'))
    owner: Mapped[DiscordUser] = relationship(back_populates='characters')
    statics: Mapped[list[Static]] = relationship(
        secondary=character_static, back_populates='characters'
    )


class Static(Base):
    __tablename__ = 'static'

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    characters: Mapped[list[Character]] = relationship(
        secondary=character_static, back_populates='statics'
    )
