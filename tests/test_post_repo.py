from lib.post_repo import PostRepo
from lib.post import Post
from lib.comment import Commment

def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog.sql")

    repo = PostRepo(db_connection)

    post = repo.find_with_comments(1)

    assert post == Post(1, "hello", "hiii", [
        Commment(1, "Kumani", "Chips", 1)
    ])


def test_find_with_co(db_connection):
    db_connection.seed("seeds/blog.sql")

    repo = PostRepo(db_connection)

    post = repo.find_with_comments(1)

    assert post == Post(1, "hello", "hiii", [
        Commment(1, "Kumani", "Chips", 1)
    ])