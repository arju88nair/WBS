# WDS Demo

## Problem statement: 

In construction industry, all projects use a master plan. A master plan is basically a file having list of activities to be executed in that project with their start date and end dates. As an example, if construction of a “house” is the project, the masterplan will have something like below:



|Sl No          |Activity       | Start Date   |End Date   |
| ------------- |:-------------:| -----:|-----:|
|1|House|2018-08-01|2019-02-28|
|1.1|Foundation|2018-08-01|2019-09-04|
|1.1.1|Digging |2018-08-01|2019-08-10|
|1.1.2|Piling|2018-08-11|2019-09-04|
|1.2|Floor|2018-09-06|2019-11-04|
|1.2.1|Tiling|2018-09-06|2019-11-04|
|1.3|Walls|2018-11-06|2019-01-14|
|1.4|Roof|2019-01-15|2019-02-28|
|1.5|Boundary wall|2018-08-01|2018-09-02|



In the masterplan above, there are parent activities like ‘House’ , ‘Foundation’ etc under which there are one or more child activities. Any activity without a child is called leaf activity. In the above example, ‘Tiling’, ‘Piling’ etc are leaf activities. Any masterplan will follow the same order for planning a construction project which is usually based on the WBS number (Eg: 1.1, 1.1.1, 1.2.1). Typically in a large construction project, there will be at least 3000 to 5000 activities spread across 2 to 3 years of duration.





Construction project managers require the masterplan to be downloaded as csv file frequently, that’s shared with others to let them know the status of project. Your task is to create a RESTful web application that satisfies the below user stories.

- As a project manager, I should be able to download all the activities in the masterplan in a csv file.

- As a project manager, I should be able to view all the details like start and end dates of the activities in the csv file.
- As a project manager, I should be able to download a list of activities sorted by WBS number as a CSV file.
- As a project manager, I should be able to download a sorted csv file based on the start date of activities followed by WBS number in the masterplan.

## Prerequisites:
- Python 2
- Flask
-SQLAlchemy


## Installation

Install the required libraries using 

>> pip install -r requirements.txt 



