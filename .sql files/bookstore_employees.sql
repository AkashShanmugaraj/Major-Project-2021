CREATE TABLE employees (
  EmpID varchar(100) NOT NULL,
  EmpName varchar(100) NOT NULL,
  EmpPhone varchar(100) DEFAULT NULL,
  salary int NOT NULL,
  PRIMARY KEY (EmpID)
);

INSERT INTO employees VALUES ('1','Sara Joseph','8760342177',121212),('2','Micheal','1222315634',5000);
