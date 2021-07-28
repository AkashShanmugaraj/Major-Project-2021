CREATE TABLE books (
  BookID varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT null unique,
  BookName tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  ISBN bigint NOT null,
  Author tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PubYear int DEFAULT NULL,
  Stocks int NOT NULL,
  Price int NOT NULL,
  Status varchar(100) NOT NULL,
  PRIMARY KEY (ISBN)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
