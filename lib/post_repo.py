from lib.post import Post
from lib.comment import Commment

class PostRepo:
    def __init__(self, connection):
        self._connection = connection

    def find_with_comments(self, post_id):
        rows = self._connection.execute("SELECT posts.id AS post_id, posts.title, posts.content, comments.id AS comment_id, comments.author_name, comments.message " \
                                        "FROM posts JOIN comments ON posts.id = comments.post_id " \
                                            "WHERE posts.id = %s", [post_id])
        comments = []
        for row in rows:
            comment = Commment(row["comment_id"], row["author_name"], row["message"], row["post_id"])
            comments.append(comment)
        
        return Post(rows[0]["post_id"], rows[0]["title"], rows[0]["content"], comments)
