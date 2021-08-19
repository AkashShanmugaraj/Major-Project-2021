CREATE TABLE books (
  BookID varchar(10) NOT null unique,
  BookName tinytext NOT NULL,
  ISBN bigint NOT null,
  Author tinytext NOT NULL,
  PubYear int DEFAULT NULL,
  Stocks int NOT NULL,
  Price int NOT NULL,
  Status varchar(100) NOT NULL,
  PRIMARY KEY (ISBN)
);
