CREATE TABLE employees (
  EmpID varchar(100) NOT NULL,
  EmpName varchar(100) NOT NULL,
  EmpPhone varchar(100) DEFAULT NULL,
  salary int NOT NULL,
  PRIMARY KEY (EmpID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES employees WRITE;
/*!40000 ALTER TABLE employees DISABLE KEYS */;
INSERT INTO employees VALUES ('1','Sara Joseph','8760342177',121212),('2','Micheal','1222315634',5000);
/*!40000 ALTER TABLE employees ENABLE KEYS */;
UNLOCK TABLES;
