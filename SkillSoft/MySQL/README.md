# MySQL

## Unit 1 - MySQL Set Up
* The teacher is a fan of Windows and MySQL workshop. This
  heresy is unforgivable. Linux is the one true OS and anyone
  who wants to be a DBA should get used to doing things on
  the command line.
* The traditional way to implement many-to-many relationships
  is to have a separate intersection table, the two items then
  have one-to-many relationships with objects in the intersection
  table.
* Good design is to have all functional dependencies as flowing
  from the primary key. (Just like Motro taught.)
* A good candidate for an index is one that is rarely set, but
  frequently looked up. Can we have multiple indices? Yes.

## Unit 2 - The Select Statement
* Good documentation 
* We can have spaces in field names if we quote them. For example,
  SELECT name AS 'full name' FROM people;
* Functions can be used to get values from anywhere, unlike SELECT.
* What does group by do if you don't have any aggregate functions
  in the query?
