from lib.post import Post 

def test_for_intialise(): 
    post = Post(1, "Hi", "hi")
    assert post.id == 1
    assert post.title == "Hi"
    assert post.content == "hi"