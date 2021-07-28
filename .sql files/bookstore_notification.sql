CREATE TABLE notification (
  message longtext,
  seenvar int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES notification WRITE;
/*!40000 ALTER TABLE notification DISABLE KEYS */;
INSERT INTO notification VALUES ('Sara Joseph (ID 1) should be credited with 121212 rupees as a part of their salary [2021-07-01]',NULL),('Micheal (ID 2) should be credited with 5000 rupees as a part of their salary [2021-07-01]',NULL);