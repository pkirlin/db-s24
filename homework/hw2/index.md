---
title: Homework 2
nav_exclude: true
---

# Database Homework #2
*To receive full credit for this assignment, all your writing should be legible and all pages you submit should be stapled together. You may, of course, type your responses if you'd like.*

## Connecting to the database
For this homework, you will use a database of flight information.  To access the database, use pgAdmin to connect to database.rhodescs.org, as we've been doing in class to access the Harry Potter database.  **However**, you must connect with a different username and password.  Your username is your standard Rhodes username (like your email, minus the `@rhodes.edu` part), and your password is the same as your username.  We changed this in class, but you may have missed it if you were absent or didn't have your laptop that day.

Once connected, look for the **flights** database.  The tables are as follows:
* **customers(customerID, first, last, city, state, birthday)**
        The customers table represents people traveling by airplane. We have unique ID for every customer, their first name, last name, the city and state in which they live, and their birthday. `customerID` is a key.

* **airports (name, airportCode, city, state, airportLat, airportLong, cityLat, cityLong, population)**
        The airports table represents airports that travelers will arrive at and depart from. For each airport, the table stores the name of the airport, a three-letter code that is unique for each airport, the main city and state the airport serves, the latitude and longitude of the airport itself, the latitude and longitude of the city served by the airport, and the population of the city.

* **airlines (name,  airlineCode)**  
        The airlines table stores information about the airlines that fly the planes between the airports. For each airline, the table stores the name of the airline and a two-character unique code that identifies the airline.

* **schedule (airlineCode, flightNumber, source, destination, departTime, arriveTime)**  
        The schedule table stores information about the individual flights that will happen on a particular day (the day itself is not important, but you can imagine this is a list of all flights that occur on one single day). For each flight, the table stores the airline's two-character code, the flight number, the three-letter codes for the airport where the flight departs (source) and arrives (destination), and the departure and arrival times in a 24-hour clock format. Note that flight numbers may be duplicated across airlines, but not across flights. In other words, two airlines may both have a flight with number 42, but there is only one Delta flight #42 on a particular day. That means the combination of the attributes (airlineCode, flightNumber) is a key.
        
* **bookings (customerID, airlineCode, flightNumber, boardingGroup, seatRow, seatLetter)**  
        The bookings table stores information about the customers who have made reservations to fly. For each reservation, the table stores the customerID, the two-character airline code, the flight number, the boarding group for the customer (an integer between 1 and 3, inclusive), and the seat assignment (a row between 1 and 30, and a letter from A to F).
    
##  Directions
For each question below (most anyway), you will write an SQL query.  **Additionally, for each question with a star (*), provide the SQL query output (the table that is printed).** The output can be cut-and-pasted from pgAdmin. (You can either paste a screenshot, or there is a button on the toolbar that will copy the table cells.)

Unless otherwise specified, each of these questions should be answered with a  _single_  SQL SELECT query that would hypothetically work for any logical database instance. In other words, you shouldn't "hard-code" anything in a query that will make the query return incorrect information if any of the information in the database changes.

Question: Can I use SQL VIEWs?  
Answer: Yes, if you wish.  Use the syntax:  `CREATE VIEW [name] AS SELECT ...  ` Make sure to give the `CREATE VIEW` statement(s) in addition to your `SELECT` query.

## Queries
 (Remember, queries with stars must also include the query output.)
    
1.  *Select the customer IDs, first, and last names of all customers who live in Memphis. [Sanity check: 6 rows]
        
2.  *Select the airline code, flight numbers, and departure/arrival times of all flights scheduled to fly from MEM to ATL (MEM and ATL are the airport codes for Memphis and Atlanta). [Sanity check: 7 rows]
        
3.  *Find the names, codes, and cities of all the airports in Tennessee that serve cities of at least 100,000 people. [Sanity check: 6 rows]
        
4.  Find the passenger manifest (passenger first name & last name, seat row, and seat number, sorted by last name) for everyone on Delta (DL) flight 1147. [Sanity check: 29 rows]
        
5.  *Find the first & last names of all passengers who reside in Tennessee who are departing the Memphis airport on flights between 9 and 10 am, along with the airline code, flight number, departure time, and destination airport. [Sanity check: 8 rows] Hint: You can compare times in PostgreSQL using the regular less-than and greater-than operators; e.g., `...WHERE arrivalTime > '4:00 PM'`
        
6.  Find the total number of airports in each state in the country. Return two columns: state, and number of airports.
        
7.  *Find the total number of people on Delta flight 45. Hint: Delta's two-character code is DL.
        
8.  *Find the total number of rows occupied on Delta flight 45. A row is occupied if at least one person is sitting in the row.
    
9. Find a listing of all flights (here "flight" means the airline code and flight number combination) and the number of people on each flight. Return a table with columns for airline code, flight number, and number of passengers. [Sanity check: 23983 rows]  

10. Using your query from the last question, augment the table with the source and destination airport codes.  (So this should be the same 23983 rows as before, but now you should have 5 columns total.) **Hint: Save this as a view! You will want to use it again!**
        
11. *Find the largest number of passengers on any single flight. Return this number of passengers (one row/one column). [Sanity check: the number is between 100 and 200.]
        
12.  *Find the airline code, flight number, source, and destination airport codes for the flight(s) with the largest number of passengers. Do not use any literal numbers in the query; your query should calculate the size of the largest flight and retrieve the relevant information in one query.
        
        **Note that  _in general_, there is no guarantee that there will be only one flight that has this number of passengers on it! Your query should be able to return them all if there is more than one.**
        
        [Sanity check: For this particular database instance, there is only one flight with the largest number of passengers on it and it involves a New York City airport.]

13. Find a listing of the most popular routes flown, sorted in order of descending popularity.  Here, a "route" means a single source airport and destination airport combination, and popularity is measured by the total number of passengers on _all_ the flights between those two airports on a single day.  **Hint: use your previously-created view, and use grouping and aggregation to add up all the passengers on all the flights that share a common source/destination airport combination.  Use `ORDER BY` to sort them.** [Sanity check: 4482 rows.] 

14. *Find the most popular route, along with its source and destination airport.  Your query should return one row with the total passengers, the source airport, and the destination airport.  [Sanity check: it's a southerly route from a midwest airport to a Texas airport.]

15. *Find the most popular route, along with the source and destination airports, for each individual airline.  (Note that in this question,
the concept of a flight necessarily differentiates between different airlines that fly between the same pair of cities, whereas
the previous two questions did not make this distinction.) 

    Return the airline code, the source and destination airport codes, and the total number of passengers that are flying that route.
        
    Hint: this is hard. You may want to use more views. 

    Hint 2: You may find it useful as well to read the book section on correlated subqueries.  [This may be helpful as well.](http://www.xaprb.com/blog/2006/12/07/how-to-select-the-firstleastmax-row-per-group-in-sql/) This question can be solved with correlated subqueries or joining a table to itself.
        
    Hint 3: You should end up with a 12-row table. [Sanity check: You should end up with the most popular Delta (DL) route being from Minneapolis/St. Paul (MSP) to Salt Lake City (SLC), carrying 572 passengers in total.
        

## Other hints, guidelines, and clarifications

-   Do not use the LIMIT keyword. In particular, you should not use LIMIT 1 combined with ORDER BY to find the largest or smallest anything, in SQL. The reason is that sorting results with ORDER BY is an O(n log n) operation, and then using LIMIT 1 to find the largest or smallest item wastes much of that computation; you can do this with aggregation in O(n) time.
    
    The second reason why LIMIT 1 is often deceptive is that while it can help you find the maximum or minimum something in SQL (albeit inefficiently), it can create problems when you try to expand your query to find other attributes related to the maximum or minimum something, if the maximum or minimum appears multiple times. For instance, pretend you have a database table that stores items sold in a store and their prices. You want to find the price of the most expensive item. You can do this with an ORDER BY/LIMIT 1 query (again, it's horribly inefficient and you shouldn't do it!) but it works. What doesn't work, however, is where you try to then get the name of the item that has the most expensive price --- what if there are multiple items with this price? Using LIMIT 1 will only retrieve one of them, and you don't know which one. This kind of query should be done with a subquery (see the link in the last question above for an example of this exact situation).
