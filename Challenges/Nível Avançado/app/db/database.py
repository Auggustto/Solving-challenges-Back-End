from sqlalchemy import Integer, String, create_engine, Column, Date, ForeignKey, Time, Boolean, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime



engine = create_engine('sqlite:///blog.db')
Base = declarative_base()


post_tags_association = Table('post_tags', Base.metadata,
    Column('post_id', Integer, ForeignKey('posting.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    birthdata = Column(Date, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    posts = relationship("Posting", back_populates="author")

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "birthdata": self.birthdata.strftime("%d/%m/%Y"),
            "email": self.email,
            "posts": [post.as_dict() for post in self.posts]
        }


class Posting(Base):
    __tablename__ = "posting"

    id = Column(Integer, primary_key=True)
    category = Column(String(30), nullable=False)
    title = Column(String(30), nullable=False)
    post = Column(String(1500), nullable=False)
    date = Column(Date, default=datetime.now)
    image_url = Column(String)

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="posting")
    likes = relationship("LikeDislike", back_populates="posting")
    tags = relationship("Tag", secondary=post_tags_association, back_populates="posts")

    def as_dict(self):
        return { 
            "id": self.id,
            "category": self.category,
            "title": self.title,
            "post": self.post,
            "comments": [comment.as_dict() for comment in self.comments],
            "date": self.date.strftime("%d/%m/%Y"),
            "time": self.date.strftime("%H:%M:%S"),
            "image_url": self.image_url,
            "total_likes": self.total_likes,
            "total_dislikes": self.total_dislikes,
            "tags": [tag.name for tag in self.tags]
        }
    
    # Method for calculating the total number of likes
    @property
    def total_likes(self):
        return sum(like.like for like in self.likes if like.like)

    # Method for calculating the total number of dislikes
    @property
    def total_dislikes(self):
        return sum(1 for like in self.likes if not like.like)
    

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    text = Column(String(500), nullable=False)
    posting_id = Column(Integer, ForeignKey("posting.id"))
    posting = relationship("Posting", back_populates="comments")

    def as_dict(self):
        return {
            "id": self.id,
            "text": self.text
        }


class LikeDislike(Base):
    __tablename__ = "like_dislike"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    posting_id = Column(Integer, ForeignKey("posting.id"), nullable=False)
    like = Column(Boolean, default=True)
    timestamp = Column(Date, default=datetime.now)

    posting = relationship("Posting", back_populates="likes")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    posts = relationship("Posting", secondary=post_tags_association, back_populates="tags")




Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()