LOAD DATA INFILE '/Users/apple/Desktop/mp6input.csv'
INTO TABLE sys.mp6
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;
use sys;
select * from mp6;
