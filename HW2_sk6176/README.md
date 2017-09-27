
This is for HW2 that pratice of munging data by using Panda in python.

	 show_bus_locations.py

This script will be grab information of a MTA bus line.

It will return the <bus name>, <the number of vehicles on operation>, and <their current positon>

Input -> python show_bus_location.py <MTA_KEY> <BUS_LINE> (e.g: python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxx B52

	get_bus_info

output

Selcted bus line is  M11
Total number of running M11 :  7
Bus 0 is latitude at 40.759087 and longitude at -73.992153
Bus 1 is latitude at 40.763716 and longitude at -73.992491
Bus 2 is latitude at 40.785888 and longitude at -73.972609
Bus 3 is latitude at 40.746762 and longitude at -74.004842
Bus 4 is latitude at 40.814564 and longitude at -73.955403
Bus 5 is latitude at 40.770704 and longitude at -73.987404
Bus 6 is latitude at 40.82641 and longitude at -73.955253


This script will be grab information of a MTA bus line, too.

It will return <BUS_LINE>.csv file

The file includes 

 <Latitude,Longitude,Stop Name,Stop Satus>

Output will look like

Latitude, Longitude, Stop Name, Stop Status
40.698045 , -73.925655 , MYRTLE AV/DE KALB AV , at stop
40.699839 , -73.911902 , GATES AV/WYCKOFF AV , approaching
40.694003 , -73.987191 , JAY ST/MYRTLE PLZ , approaching
40.694727 , -73.954843 , MYRTLE AV/WALWORTH ST , approaching
40.693515 , -73.987235 , JAY ST/MYRTLE PLZ , approaching
40.695333 , -73.94959 , MYRTLE AV/NOSTRAND AV , < 1 stop away

HW2_3_sk6176.ipynb

This script grab Daily Report of Homeless Shelter in NYC.

The data set will be remain only two numerical columns and it will scatter plot


Extra_HW_2.ipynb

This script also using the same data set but

left Date of Census and Total Individuals in Families with Children in Shelter columns
The Date of Census will be replace to panda format of date and 
Plot Total Individuals in Families with Children in shelter VS Date in Scatter
