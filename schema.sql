DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS contents;
DROP TABLE IF EXISTS metas;
DROP TABLE IF EXISTS options;
CREATE TABLE comments (
  cid     INTEGER PRIMARY KEY AUTOINCREMENT,
  author  TEXT NOT NULL,
  email   TEXT NOT NULL,
  content TEXT NOT NULL,
  date    TEXT NOT NULL
);
CREATE TABLE contents (
  cid        INTEGER PRIMARY KEY AUTOINCREMENT,
  title      TEXT NOT NULL,
  text       TEXT NOT NULL,
  date       TEXT NOT NULL,
  category   INTEGER,
  tag        INTEGER,
  status     TEXT NOT NULL,
  type       TEXT NOT NULL,
  commentnum INTEGER
);
CREATE TABLE metas (
  cid      INTEGER PRIMARY KEY AUTOINCREMENT,
  name     TEXT NOT NULL,
  type     TEXT NOT NULL,
  nickname TEXT NOT NULL,
  count    INTEGER
);
CREATE TABLE options (
  sitename        TEXT NOT NULL,
  description     TEXT NOT NULL,
  defaultpage     INTEGER,
  numberofarticle INTEGER
);
INSERT INTO options VALUES ('No name', 'No description', 0, 0);
