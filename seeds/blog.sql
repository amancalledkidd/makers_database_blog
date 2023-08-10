DROP TABLE IF EXISTS posts cascade;
DROP SEQUENCE IF EXISTS posts_id_seq;

DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE SEQUENCE IF NOT EXISTS comments_id_seq;


CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  author_name text,
  message text,
  post_id int,
  constraint fk_posts foreign key(post_id)
    references posts (id)
    on delete cascade
);


INSERT INTO posts (title, content) VALUES ('hello', 'hiii');
INSERT INTO posts (title, content) VALUES ('bye', 'byeeee');

INSERT INTO comments (author_name, message, post_id) VALUES ('Kumani', 'Chips', 1);
INSERT INTO comments (author_name, message, post_id) VALUES ('Hamza', 'hiii', 2);
