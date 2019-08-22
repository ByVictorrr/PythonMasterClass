# Learning sqlite3

## sqlite3 commands

### .headers on

* shows the columns of the db

### .backup filename
* backup the db you currently are in


### .restore filename
* allows you to restore from a backed up db

### .tables
* shows the tables in that db

### .schema
* prints out structure of your tables(shows how you created the tables)

### .dump
* it shows the sql statments that you entered in 

### .read file.sql
* excute a sql script

### .quit 
* exit the sqlite shell

## Sql commands

### CREATE table table_name (field_0 type,..., field_i type);

* creates a table with i columns

### INSERT into table_name (field_0,..., field_i) values (value_0, …, value_i)

* this is to insert values in the columns of the table
* use this if you dont want to fill in each column

### INSERT INTO table_name VALUES(value_0, …, value_i)

* this method is to fill in each column in a row

### SELECT * FROM table_name = SELECT field_0, …, field_i FROM table_name 

* to see everything in  each field


### UPDATE table_name SET field_0=replacement WHERE field_1 = value_1

* update a specific field

### DELETE FROM contacts WHERE field_0=value_0

* delete a row 

###  PRIMARY KEY
* uniquely identifies the rows in the table
* Must be unique

#### Autoincrment 

* if you dont provide a _id unique key it will auto incrment if you want to
insert 

### NOT NULL
* values must contain a value when inserting a row

### SELECT * FROM table_name ORDER BY field_0;
* could appear in alphabetic order or value
* but cases are effected

### SELECT * FROM table_name ORDER BY field_0 COLLATE NOCASE;
* orders your search in order ignoring case

### SELECT * FROM table_name ORDER BY field_0 COLLATE NOCASE DESC;
* orders your search by descending order

### SELECT * from table_name  ORDER BY field_0,.. ,field_i COLLATE NOCASE;
* if you have a list of songs it could group artist songs in order
* search first by field_0 then field_i

### JOINing tables
![join pic](https://github.com/ByVictorrr/PythonMasterClass/blob/master/section13/join.png)

### SELECT table_0.field_0, table_1.field_0 FROM table_0 INNER JOIN table_1 ON table_0.field_0 = table_1.field_0;
* allows you to show a joined db of table_0 and table_1 where table_0.field_0 =
table_1.feild_1

### SELECT table_0.field_0, table_1.field_0 FROM table_0 INNER JOIN table_1 ON table_0.field_0 = table_1.field_0 ORDER BY table_0.field_0, table_1.field_0;
* sort and join two tables

### JOINING Three tables
* SELECT artist.name, albums.artist, songs.track FROM songs INNER JOIN albums ON songs.album = album._id INNER JOIN artist ON albums.name = artist._id

### Wildcards
* SELECT artist.name, albums.artist, songs.track FROM songs INNER JOIN albums ON
songs.album = album._id INNER JOIN artist ON albums.name = artist._id WHERE
albums.name LIKE "%doctor%"

* % - wildcard in sql

#### LIKE  

* used with a wildcard instead of =

### VIEWS

* A view is like a temporary table created from select statement

* could be used to hide certain columns and show certain in a sql db

* Example: 

CREATE VIEW artist_list AS
SELECT artists.name, albums.name, songs.track, songs.title FROM songs
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artist._id
ORDER BY artists.name, albums.name, songs.track

### Deleting VIEW
* DROP VIEW view_name

### how to name field in a view 
* Example:

CREATE VIEW artist_list AS
SELECT artists.name AS artist, albums.name AS album, songs.track , songs.title FROM songs
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artist._id
ORDER BY artists.name, albums.name, songs.track


### WHERE logical operators
* <> - not equal to
* = equal to
* > 
* <


### Include functions in SELECT statements
* SELECT count(*) FROM table_name;
	* counts the number of rows (records) in table_name


