Next Pathway Hackathon
====================

Hello All ! </br>
This repository is for my submissions of the Problem statements for [Next-Pathway-Hackathon](https://wuelev8.tech/drills/next-pathway-hack-backpackers). </br>

Problem Statement 2
====================
DataStage expression and function to ADF expression and dynamic contents </br>

Link for DataStage functions and expressions: DataStage functions and expressions
Understand the functions on which you need to work(mentioned below in Datastage Functions to
work upon) from the Datastage link mentioned above and create equivalent Python or Javascript
code using equivalent ADF functions and expressions (example below),</br>


An example to understand what solution you need to provide: </br>
Below is the sample of writing an equivalent code for Datastage function CurrentDate which returns
the current date.
Scenario</br>
ADF does not have a direct function which can return the date value. Hence, In the code, utc_now()
is a ADF function which gives datetime in the format 2018-04-15T13:00:00.0000000Z and then we
will take the substring till T to return the date.</br>
There can be other better ways to do this which you can put in your code.</br>
Solution in Javascript code</br>
```
function get_curr_date() {
var day = utc_now(“dd”)
var month = utc_now(“MM”)
var year = utc_now(“yyyy”)
curr_dt = day + “/” + month + “/” + year
return curr_dt
}
```
Solution in Python code
```
def get_curr_date:
day = utc_now(“dd”)
month = utc_now(“MM”)
year = utc_now(“yyyy”)
curr_dt = day + “/” + month + “/” + year
```