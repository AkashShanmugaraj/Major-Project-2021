CREATE TABLE transactions (
  Date datetime NOT NULL,
  TransactionID varchar(20) NOT NULL,
  BookID varchar(10) DEFAULT NULL,
  ISBN bigint NOT NULL,
  BookQuantity int NOT NULL,
  CustPhNum bigint DEFAULT NULL,
  Cost int NOT NULL,
  PRIMARY KEY (TransactionID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
