logAnalysis

overview
This is the third Back-end developer Udacity nanodegree project
In this project, you will try complex queries like in a real-world web application,
with a real database and tables, the program uses psycopg2 python module to conect the Database and complex SQL queries to
ask the questions below.

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?


Setup Project:
Install Vagrant and VirtualBox - > https://www.virtualbox.org/wiki/Download_Old_Builds_5_1, https://www.vagrantup.com/downloads.html
If you is a back-end developer nanodegree student, you can Download in this link https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
If not Download or Clone https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile.
Download the data from here -> https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip.
Unzip this file after downloading it. The file inside is called newsdata.sql.
Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from Here
Launching the Virtual Machine:
Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  $ vagrant up
Then Log into this using command:
  $ vagrant ssh
Change directory to /vagrant and look around with ls.
Setting up the database and Creating Views:
Load the data in local database using the command:
  psql -d news -f newsdata.sql
The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles data.
The log table includes one entry for each Http requests with informations like
Status, path, time, etc.


Running the queries:
From the vagrant directory inside the virtual machine,run logAnalysis.py using:
  $ python3 logAnalysis.py