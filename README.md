# logAnalysis

## Overview

This is the third Back-end developer Udacity nanodegree project
In this project, you will try complex queries like in a real-world web application,
with a real database and tables, the program uses psycopg2 python module to conect the Database and complex SQL queries to
ask the questions below.

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?

## Setup Project

Install VirtualBox and Vagrant:

1. Download Virtualbox [**Here**](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
2. Download Vagrant [**Here**](https://www.vagrantup.com/downloads.html)

3. If you **is** a back-end developer nanodegree student, you can Download the Vagrant File with the configurations in [**This Link**](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)\
If **not** Download or Clone [**this repository**](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)

4. Download the content of this current repository, by either downloading or cloning it from [**Here**](https://github.com/GiuseppeVarriale/udacity-logsAnalysis.git)

5. Unzip the newsdata.zip.

## Launching the Virtual Machine

1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
     >`$ vagrant up`

2. Then Log into this using command:
      > `$ vagrant ssh`
3. Change directory to /vagrant and look around with ls.

## Setting up the database

1. Load the data in local database using the command:
    > `$ psql -d news -f newsdata.sql`

### The database includes three tables

- The authors table includes information about the authors of articles.
- The articles table includes the articles data.
- The log table includes one entry for each Http requests with informations like
Status, path, time, etc.

## Running the the program

- From the vagrant directory inside the virtual machine,run the file logAnalysis.py using:
     > `$ python3 logAnalysis.py`