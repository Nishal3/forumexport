from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Text, String, TIMESTAMP, ForeignKey, Column
from sqlalchemy.orm import relationship

Base = declarative_base()


class Post(Base):
    # create table posts (
    # id SERIAL PRIMARY KEY,
    # body TEXT NOT NULL,
    # author_name VARCHAR(50) NOT NULL,
    # created_on TIMESTAMP NOT NULL DEFAULT NOW()
    # );
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    author_name = Column(String(50), nullable=False)
    created_on = Column(TIMESTAMP)

    comments = relationship(
        "Comment", order_by="Comment.comment", back_populates="posts"
    )


class Comment(Base):
    # create table comments (
    # id SERIAL PRIMARY KEY,
    # post_id INTEGER REFERENCES posts(id),
    # comment TEXT NOT NULL,
    # sentiment VARCHAR(10) NOT NULL,
    # commenter_name VARCHAR(50) NOT NULL,
    # created_on TIMESTAMP NOT NULL DEFAULT NOW()
    # );
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    comment = Column(Text, nullable=False)
    sentiment = Column(String(10), nullable=False)
    commenter_name = Column(String(50), nullable=False)
    created_on = Column(TIMESTAMP)

    posts = relationship("Post", back_populates="comments")
