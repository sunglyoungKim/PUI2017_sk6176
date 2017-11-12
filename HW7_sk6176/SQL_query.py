
# coding: utf-8

# # SQL CARTO QUERY FUNCTION
# # written for PUI2016_Python2

# ##### This notebook is set up to link as a default to the fb55 account.  To turn in the homework use the same account you used in the lab (hvt201)  and query the database that you were querying in class (citibike_feb_2015)

# In[1]:


SQL_SOURCE = 'https://sk6176.carto.com/api/v2/sql?q='

import urllib2
import urllib
import StringIO
import ast
import pandas as pd

def queryCartoDB(query, format='CSV', source=SQL_SOURCE):
    '''queries carto datasets from a given carto account
    Arguments: 
    query - string: a valid sql query string
    format - outlut format  OPTIONAL (default CSV)
    source - a valid sql api endpoint OPTIONAL (default carto fb55 account)
    Returns:
    the return of the sql query AS A STRING
    NOTES:
    designed for the carto API, tested only with CSV return format'''
    
    data = urllib.urlencode({'format': format, 'q': query})
    try:
        response = urllib2.urlopen(source, data)
    except urllib2.HTTPError, e:
        raise ValueError('\n'.join(ast.literal_eval(e.readline())['error']))
    except Exception:
        raise
    return response.read()


# #### Finding start stations less than 3 hours trip duration of head and tail of 10

# In[2]:


task1_1 = '''
SELECT * FROM citibike
WHERE tripduration<10800
ORDER BY start_station_id
LIMIT 10
'''


# #### Showing for top 10 by stat_station_id

# In[3]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task1_1)), sep=',')


# #### Showing for the tail

# In[4]:


task1_1 = '''
SELECT * FROM citibike
WHERE tripduration < 10800
ORDER BY start_station_id DESC
LIMIT 10
'''


# In[5]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task1_1)), sep=',')


# #### Let's sort by tripduration top 10 and last 10

# #### Top 10

# In[6]:


task1_1 = '''
SELECT * FROM citibike
WHERE tripduration < 10800
ORDER BY tripduration
LIMIT 10
'''


# In[7]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task1_1)), sep=',')


# #### Last 10

# In[8]:


task1_1 = '''
SELECT * FROM citibike
WHERE tripduration < 10800
ORDER BY tripduration DESC
LIMIT 10
'''


# In[9]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task1_1)), sep=',')


# #### Showing all unique start_station_ID

# In[10]:


task1_2 = '''
SELECT DISTINCT start_station_id FROM citibike
ORDER BY start_station_id
'''


# In[11]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task1_2)), sep=',')


# In[12]:


task1_3 = '''
SELECT Count(tripduration) as numtrips,
       Avg(tripduration) as avgtrips,
       Min(tripduration) as mintrips,
       Max(tripduration) as maxtrips
FROM citibike
'''


# In[13]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task1_3)), sep=',')


# #### Task 2 Selecting only Feb, 2nd, 2015 data 

# In[14]:


task2_1 = '''
SELECT * FROM citibike
WHERE starttime >= '2015-02-02 00:00'
AND   starttime  < '2015-02-03 00:00'

'''


# In[15]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task2_1)), sep=',')


# #### Selecting only started at weekend

# In[16]:


task2_2 = '''
SELECT * FROM citibike
WHERE extract(DOW FROM starttime) in (0,6)
'''


# In[17]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task2_2)), sep=',')


# #### Finding the Average trips

# In[18]:


task2_2 = '''
SELECT AVG(tripduration) as avgtrips FROM citibike
WHERE extract(DOW FROM starttime) in (0,6)
'''


# In[19]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task2_2)), sep=',')


# #### What about weekdays?

# In[20]:


task2_3 = '''
SELECT * FROM citibike
WHERE extract(DOW FROM starttime) in (1,2,3,4,5)
'''


# In[21]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task2_3)), sep=',')


# In[22]:


task2_3 = '''
SELECT AVG(tripduration) as avgtrips FROM citibike
WHERE extract(DOW FROM starttime) in (1,2,3,4,5)
'''


# In[23]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task2_3)), sep=',')


# # extra credit: make the function python 2 and 3 compatible so that it works on the  PUI2016_Python3 kernel

# In[24]:


task3 = '''
SELECT CDB_TransformTowebmercator(CDB_latLng(start_station_latitude, start_station_longitude)) as the_geom_webmercator,
        Min(cartodb_id) as cartodb_id, 
        count(tripduration) as numtrips, 
        Min(start_station_name) as start_station_name from citibike

where ST_DWithin(CDB_LatLng(start_station_latitude, start_station_longitude)::geography,
                CDB_LatLng(40.7577, -73.9857)::geography,
               500)
group by start_station_latitude, start_station_longitude
'''


# In[25]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task3)), sep=',')


# #### task 4

# In[26]:


task4 = '''
SELECT ST_MakeLine(CDB_TransformTowebmercator(CDB_latLng(start_station_latitude, start_station_longitude)),
                   CDB_TransformTowebmercator(CDB_latLng(end_station_latitude, end_station_longitude))) as the_geom_webmercator,Min(cartodb_id) as cartodb_id, 
        count(tripduration) as numtrips FROM citibike

where ST_DWithin(CDB_LatLng(start_station_latitude, start_station_longitude)::geography,
                CDB_LatLng(40.7577, -73.9857)::geography,
               500)
      and tripduration < 7200

group by start_station_latitude, start_station_longitude, end_station_latitude, end_station_longitude

'''


# In[27]:


pd.read_csv(StringIO.StringIO(queryCartoDB(task4)), sep=',')

