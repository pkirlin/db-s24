---
title: Homework 3
nav_exclude: true
---

# Databases Homework #3

**To receive full credit for this assignment, all your writing should be legible and all pages you submit should be stapled together. You may, of course, type your responses if you’d like.**

In this assignment, you will practice constructing E/R diagrams and turning them into database schemas. Though we have seen how to describe a database schema informally by listing the names of the relations and underlining their keys, we have not seen the SQL syntax for actually creating tables and assigning keys. Luckily, the syntax for doing this is very straightforward; read section 2.3 (pgs 29-36) for details on the CREATE TABLE statement and the various SQL datatypes. You can also read here:
- [CREATE TABLE](https://www.w3schools.com/sql/sql_create_table.asp)
- [PostgreSQL datatypes](https://www.postgresql.org/docs/14/datatype.html)
	- If the complete list of datatypes above is too overwhelming, just use the "compatibility" list at the end of that webpage.
- [Primary keys with CREATE TABLE](https://www.w3schools.com/sql/sql_primarykey.ASP)

You will construct E/R diagrams for three different situations, plus corresponding database schemas for two of the three situations.

**Guidelines for E/R diagrams**: Make sure to indicate primary keys, multiplicity constraints (arrow types and/or labels on relationships), and weak entity sets (if any) with their supporting relationships. If you can't directly express a constraint in the diagram, include it in a note below the diagram. Also list any  _reasonable_  assumptions you make in constructing the diagram that are not specified in the problem.

**Guidelines for database schemas**: Make sure that each schema captures primary key constraints via underlining appropriate attributes. Identify any additional constraints or restrictions that you are not able to capture in the SQL itself but would have to be enforced in some other way. Explicitly note any situations where you combined relations involved in a many-one relationship.

**Guidelines for CREATE TABLE statements**: Make sure your CREATE TABLE statement includes appropriate syntax for table names, attribute names, data types, and primary keys.

1.  (E/R diagram only)
    
    Suppose we want to create a database representing sports teams, players, and their fans. We want to represent the following pieces of information:
    
    -   For each team, we want to represent its name, its players, its team captain (who is one of the players), and the color(s) of its uniform.
    -   For each player, we want to represent their name.
    -   For each fan, we want to represent their name, their favorite team, favorite player, and favorite color. Assume that each fan can at have at most one favorite team, at most one favorite player, and at most one favorite color.
    
    Draw an E/R diagram for this database. Follow the E/R guidelines above.
    
2.  (E/R diagram and schema)
    
    We want to design a database for a local garage that fixes cars. For each customer, we want to record their name (assume names are unique), their address, and their phone number. For each vehicle, we want to record the unique vehicle identification number (VIN), and the vehicle's make, model and year.
    
    The garage keeps track of each repair job, which involves exactly one car, a description of what was done to the car, the date, and the total cost. A repair job includes zero or more parts being replaced on the car (e.g., "windshield wipers", "battery", etc.). For each part we want to record its (unique) part number, the part name and its cost. In addition, note that:
    
    -   Each vehicle may have 1 or more repair jobs.
    -   Each customer may own 1 more more cars.
    -   Every car has only one primary owner (we ignore co-owners).
    -   No vehicle can have more than one repair job in any given day.
    
    **Part A:**  Draw an E/R diagram for this database. Follow the E/R guidelines above.
    
    **Part B:**  Translate your E/R diagram into a relational database schema (i.e. give the relations and underline primary keys). Follow the schema guidelines above.
    
3.  (E/R diagram, schema, and CREATE TABLE statements)
    
    You are building a database to help students decide where to eat off campus. You decide to model students' preferences for the nearby restaurants and the dishes served at each restaurant. For example, the student Alice Smith may give the "pulled pork sandwich" at "Central BBQ" a 5 out of 5 stars, but also give the "pulled pork sandwich" at "Barbecue Shop" only 3 out of 5 stars.
    
    Include the following:
    
    -   Each student has an R-number, name, and major.
    -   Each restaurant has a name and mailing address.
    -   The name of a restaurant may not be unique, but the mailing address is unique.
    -   Each dish (item on the menu at a restaurant) has a name and price.
    -   The price of a dish might differ at different restaurants. For example, the pulled pork sandwich at Central BBQ 
might be $8.99, but at the Barbecue Shop the same sandwich might be $7.99.
    -   The name of a dish is unique within a restaurant, but multiple restaurants may have dishes with the same name (e.g., "pulled pork sandwich").
    -   Each dish is offered by at least one restaurant, and each restaurant offers at least one dish.
    -   Students assign ratings (1 to 5 stars) to a specific dish at a specific restaurant. Each student may rate each (dish, restaurant) pair only once, but may rate multiple dishes at a single restaurant, or the same dish at different restaurants.
    
    **Part A:**  Draw an E/R diagram for this database. Follow the E/R guidelines above.
    
    **Part B:**  Translate your E/R diagram into a relational database schema (i.e. give the relations and underline primary keys). Follow the schema guidelines above.
    
    **Part C:**  Give a set of CREATE TABLE statements that creates the relations and primary keys specified in part B.
