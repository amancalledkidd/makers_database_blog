from lib.comment import Commment 

def test_for_intialise(): 
    comment = Commment(1, "Hi", "hi", 1)
    assert comment.id == 1
    assert comment.author_name == "Hi"
    assert comment.message == "hi"
    assert comment.post_id == 1
