---
title: Project
has_children: true
nav_order: 5
---



# Group Project Information

For this course, each group will design, build, document, and demonstrate a database-backed web application. Not only does this project provide an opportunity to experiment with and apply the ideas discussed in class, it also provides experience in teamwork and project management. Groups are encouraged to design their application around an idea that excites them, with the caveat that the idea necessitates the use of a database behind the scenes to let users interact with the web app.

The web applications will be programmed using the  [Flask](http://flask.pocoo.org/)  microframework in Python. We will use PostgreSQL or SQLite for the database backend. Basic instruction in these technologies will be provided, though groups will likely need to read parts of the documentation on their own and seek out additional resources.

## Group Project Guidelines

Here are some guidelines that should help you make project decisions. Of the following, the first four guidelines are the most important.

**Team**: Choose your project team (minimum four people, one group will have three) very, very carefully. When choosing partners, you should look at the obvious factors: preferred database system, programming environment, applications, etc. However, please also take the time to make sure that your goals, style of working, target grade, etc., also match those of your partners. Do not be shy in interviewing potential group members! I give you full freedom to choose the classmates with whom you'd like to work. On the flip side, I will absolutely not serve as an arbiter of any group disputes that arise, short of those involving academic dishonesty. I suspect I will be asked if it is OK to work in a smaller group. The answer is no. While I know that many students may be more productive working in groups of two or even alone, a major objective of the course is to make sure students know how to work in a group.

**Effective use**: Try to make effective use of as much of the course material as possible. As we progress through this course, try to incorporate what we learn into your projects. For example, use joins, aggregates, cursors, different transaction isolation levels, indexes, etc. While it is certainly not necessary that your project use each and every topic covered in class, in most nontrivial applications one can find use for most of these topics. If you have trouble figuring out how some topic is applicable to your project, stop by during office hours.

**Completeness**: The project must be complete and stable enough for a good demonstration at the end of the course. This requirement is very important. If you are unable to give a reasonable demonstration, your project grade will suffer greatly. I cannot stress this point enough. A demonstration in which only five simple tasks work is far better than one in which nothing works but there are many complex and fascinating tasks that "almost work." When planning your work, make sure you get the simple stuff working before tackling more ambitious tasks.

**Database size**: All project databases must be of nontrivial size. You may interpret nontrivial based on your application. However, (1) there should be at least 8 nontrivial relations; and (2) the total number of attributes times the total number of tuples should be at least 5000. (These are guidelines only; if you feel your application warrants exceptions, come see me during office hours.)

**Practicality**: The application you build should be of practical use to a sizeable community (at least in the forseeable future).

**Innovation**: The more innovative ideas you include in your project, the more credit you will receive. It is perfectly OK to build "yet another Amazon or eBay" but if you include some innovative ideas, you'll get more credit.

**Miscellany**: In addition to the above, your project grade will take into account factors such as teamwork, overall effort, timeliness, answers to questions about the project, justification of design decisions, and intermediate and final project reports.

## Ideas for projects

Here are some rough notes that may be useful for deciding on a topic for the class project. You should treat the following as starting points for further discussion and development, not as canned project suggestions. In particular, the following are not intended to serve as replacements for discussing project ideas and plans (among project team members and with the instructor).

Note that some of these are too simple for a project and others may be too complex. Treat the following merely as a collection of ideas from which you can pick some you like, combining them to get a project that both interests you and is sufficiently challenging from a technical viewpoint. You are encouraged to stop by during office hours to discuss any of the following that may interest you.

As mentioned above, innovative projects are encouraged. While the number of truly innovative ideas in your project is not a primary factor in deciding the project grade, picking an innovative and unusual project has the significant advantage that you will be less likely to get bored with the project and will have more fun working on it.

-   Online store of some kind (similar to Amazon)
	- books, movies, electronic music, ...  
	- catalog, browsing, shopping cart functions, payment, fulfillment, ...
    
-   Auction site (similar to eBay)
-   Re-design BannerWeb
-   Airline/train/bus/taxi/ZipCar reservations
	- Manage routes, search and book flights, frequent flier miles, ...
    
-   Library/bibliography database
	- search collections, check status, checkout and checkin, ...
    
-   Reviews website (similar to Yelp or Consumer Reports)
-   Banking
	- debit, credit, billing, interest, ...
    
-   Personal finance or stocks
-   Job postings
	- openings, contacts, references, reviews, requirements, bidding, ...
    
-   Social networking site (similar to Facebook, Instagram, Snapchat, etc)
-   Recipes
-   Movies (like IMDB or Netflix)
-   Real estate or apartments (like AirBnb)
-   Room scheduling
-   Address book or personal information manager
	- contacts, addresses, phones, appointments, diary, to-do list, ...
    
-   Meeting scheduler
-   Buying tickets (similar to Ticketmaster)
-   Parking garage or lot manager
	- Which spots are open, find a spot, reserve a spot, manage payments, ...
    
-   Weather database
	- retrieve historical weather info and use to make forecasts, discover trends, records, trivia, ...
    
-   Sports database
-   Traffic database
-   Courseware (like Canvas)
-   Build a search engine
-   Photo-sharing website

_These project guidelines were inspired by an assignment designed by  [Sudarshan S. Chawathe](http://aturing.umcs.maine.edu/~sudarshan.chawathe/)._
