from forumexport.config import Session
from forumexport.models import Comment, Post

from sqlalchemy.sql import func

import csv

csv_file = open("forum_data.csv", "w")
fields = [
    "id",
    "body",
    "author_name",
    "created_on",
    "comments",
    "positive_comments",
    "negative_comments",
]
csv_writer = csv.DictWriter(csv_file, fields)

session = Session()

comments = (
    session.query(Comment.post_id, func.count("*").label("comments"))
    .group_by(Comment.post_id)
    .subquery()
)

negative_comments = (
    session.query(Comment.post_id, func.count("*").label("negative_comments"))
    .filter(Comment.sentiment == "negative")
    .group_by(Comment.post_id)
    .subquery()
)

positive_comments = (
    session.query(Comment.post_id, func.count("*").label("positive_comments"))
    .filter(Comment.sentiment == "positive")
    .group_by(Comment.post_id)
    .subquery()
)

data_fields = (
    session.query(
        Post,
        comments.c.comments,
        negative_comments.c.negative_comments,
        positive_comments.c.positive_comments,
    )
    .outerjoin(comments, Post.id == comments.c.post_id)
    .outerjoin(negative_comments, Post.id == negative_comments.c.post_id)
    .outerjoin(positive_comments, Post.id == positive_comments.c.post_id)
)


for post, comments, neg_comments, pos_comments in data_fields:
    csv_writer.writerow(
        {
            "id": post.id,
            "body": post.body,
            "author_name": post.author_name,
            "created_on": post.created_on.date(),
            "comments": comments or 0,
            "positive_comments": pos_comments or 0,
            "negative_comments": neg_comments or 0,
        }
    )

csv_file.close()
