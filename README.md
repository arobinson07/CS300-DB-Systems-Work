# CS300-DB-Systems-Work

Reuqirements:
      -Python 3.7 or later
      -Microsoft SQL Server
      -Microsoft SQL Server Management Studio
      -PYODBC Database connector for python

Included:
      -DML and DDL Scripts for creatingthe Database in SQL Server and inserting basic data for testing purposes.
      -SQL scripts for creating stored procedures used and called in the python application
      -Excel document of data for testing purposes
      -Python Application for interacting with the database
      -2 Visio files; these are database diagrams from the planning stages of this project; there is a version 1 and a version 2 due to revisions during that time.

My final project from a SQL Database Management course (CS300) I took in Fall of 2018 at Bellarmine University in Louisville, Kentucky.

The python file included is a GUI for interacting with a SQL Server 2019 database hosted locally.
The structure and implementations are very basic because I taught myself basics of TKinter specifically for this project. The SQL Database 
itself was written by hand by myself, a novice, so the database is also very basic.

The database code and application included here represent a manually controlled asset tracking system. Given more time and experience I may
revisit this project in the future.

As it stands, look up functionality works, but editing the database via the python application can not be done successfully, and I am 
unsure in which part of the project the failure occurs; the application, the connector, or duringn execution of the stored procedure 
in SQL Server.
