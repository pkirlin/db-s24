---
title: Milestone 3
parent: Project
---

# Project Milestone 3

Your task for this milestone is twofold: (a) get data that you can use to populate your database, and (b) determine the general functionality of your project website.

## Part A

Your database will probably need some initial "seed" data to get started, as usually an application running with an empty database is not particularly useful, because lots of features can't be demonstrated on an empty database. For instance, if you are building an online store, having no products and/or no registered customers does not make for a useful application.

For this part, you should think about how you will find or generate data that you can use to populate your database. This data does not necessarily have to be "real world" data, but it's nice if it is. On the other hand, there are many ways to generate fake data that appears to be real. As an example, for the flights database used in HW2, I used a real-world listing of airlines, sources, and destinations, but I wrote a Python program to generate fake flight numbers and picked source-destination pairs randomly. Then I generated a bunch of fake name/address data by using [Mockaroo](https://www.mockaroo.com/). If you google for "fake data generator" you'll find other websites that can generate plenty of data.

The point of this part is that you should have enough data to demonstrate all the functionality of your website.  This means you probably need data for most, if not all of your tables.  If it makes sense for *your* application to leave one or more of the tables empty, that's ok.

After brainstorming where to get data for each table, you should collect or generate data using one or more of these methods:
- Create/generate a CSV file of your data.  We used this idea for two tables in the Python/PostgreSQL lab.
- Create/generate a `.sql` file with SQL `INSERT` commands.  We used this idea for the `entries` table in the Flask lab.
- Create a Python program that generates data using other data.  For instance, for the flights database that we used in the SQL homework, I created that database with CSV files for the passengers and flights tables, but to generate data for actual bookings (which passengers were on which flights) I used a simple Python program that picked a random passenger and put them on a random flight.  This is why sometimes the same passenger ended up on two flights that conflicted with each other.  :) 
	- You can write such a program by using ideas from our Python/PostgreSQL lab.  In that lab, we added students to classes by using the keyboard to ask for input, but we could have easily done that by generating a random student and a random class instead.

### To turn in for Part A
- Write a `schema.sql` file (similar to the Python/PostgreSQL lab and the Flask lab) that creates all your tables.
- Write one or more scripts that populate the tables with data.  These can be Python scripts or SQL scripts. 
- Suggested, but not required: Create a Flask application with command-line options (like we did in the Flask lab) that will let you initialize the database with empty tables (`flask initdb`) and populate the database with your initial data (`flask populate`).

## Part B

While you can design your website any way that is appropriate for your topic, I suggest keeping things very simple. Your project website will not be graded on look and feel, but rather content and functionality. To that end, for part B, I would like your group to create a list of every operation your website can perform. Each operation is a start-to-finish concept of something the user can do on the website. For instance, for the blog we created during the Flask lab, we created four operations:

-   Add an entry
-   Edit an entry
-   Browse/list entries
-   Delete an entry

You should create a list such as this for your project. The intent behind this part is that if nothing else, you can use this list to guide development of your website. I do not mind if your project website literally is nothing more than a list of links to these operations (just like the blog). You can order these hierarchically if some of the operations are nested or depend on each other. For instance, for an online store, you might have:

-   Create account
-   Modify account
    -   Change email
    -   Change address
    -   Change credit card
-   Log into account
-   Browse for products
    -   Add product to shopping cart
-   Search for products
    -   Add product to shopping cart
-   View shopping cart
    -   Remove product from cart
    -   Remove all products from cart

Your list should include at least one operation that will include an SQL SELECT statement, at least one operation that includes an INSERT, at least one that includes an UPDATE, and at least one that includes a DELETE. Deviating from this is OK, but must be justified. (For instance, I can imagine a situation where it would be inappropriate to ever DELETE anything.)

## What to turn in

For Part A, you may either email me your `schema.sql` file and your other scripts and data files that you have created.  Or, (this is preferable if you are working in replit), you can add me to your replit and share the link with me and I can see your code that way.

For Part B, you can either email or print out your list of everything you want your website to do.  

