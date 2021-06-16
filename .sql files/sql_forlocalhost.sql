create database if not exists Bookstore;
use Bookstore;
create table if not exists books (
BookID int Not Null primary key,
BookName tinytext Not Null,
BookGenre tinytext Not Null,
Author tinytext Not Null,
PubYear int,
Stocks int not Null,
Price int Not null
);

 create table if not exists customer(
 CustID int Not null,
 CustName tinytext not null,
 CustPhnum bigint,
 CustAddress mediumint);
 
 create table credentials(
 email varchar(100) unique not null,
 username varchar(100) not null primary key,
 password varchar(100) not null);