CREATE TABLE `zipcodes`(
`zip` CHAR(5) NOT NULL,
`city` CHAR(64),
`state` CHAR(2),
`lat` REAL,
`long` REAL,
`timezone` INT(2),
`dst` INT(2),
PRIMARY KEY ( zip));

/*Load CSV data*/
sqlite3 zipcodes.db
.mode csv
.import zipcode.csv zipcodes