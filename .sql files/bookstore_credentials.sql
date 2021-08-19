CREATE TABLE credentials (
  email varchar(100) NOT NULL,
  username varchar(100) NOT NULL,
  password varchar(100),
  medium varchar(100) NOT NULL,
  PRIMARY KEY (username),
  UNIQUE KEY email (email)
);