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

# JOIN tables
[join pic](https://github.com/ByVictorrr/PythonMasterClass/blob/master/section13/join.png)



