```python
import sqlite3 as sq
import pandas as pd
```


```python
conn = sq.connect('london_crime.db')
```


```python
df=pd.read_csv('D:/tableau/Uk crime/london_crime.csv')
```


```python
curs = conn.cursor()
```


```python
df.to_sql('London_crime', conn, if_exists='replace', index=False)
```




    142756




```python
pd.read_sql("""SELECT *
                        FROM london_crime
                        limit 10;""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Month-Year</th>
      <th>Type</th>
      <th>Crime Section</th>
      <th>Crime Group</th>
      <th>BCU Name</th>
      <th>OCU Name</th>
      <th>Financial Year</th>
      <th>DateUpTo</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-04-01</td>
      <td>Offences</td>
      <td>Miscellaneous Crimes Against Society</td>
      <td>Other Forgery</td>
      <td>Central North BCU</td>
      <td>Islington</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-04-01</td>
      <td>Sanction Detections</td>
      <td>Miscellaneous Crimes Against Society</td>
      <td>Perverting Course of Justice</td>
      <td>Central West BCU</td>
      <td>Hammersmith &amp; Fulham</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-04-01</td>
      <td>Sanction Detections</td>
      <td>Arson and Criminal Damage</td>
      <td>Arson</td>
      <td>West BCU</td>
      <td>Hillingdon</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-04-01</td>
      <td>Offences</td>
      <td>Theft</td>
      <td>Shoplifting</td>
      <td>West BCU</td>
      <td>Ealing</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>128</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-04-01</td>
      <td>Offences</td>
      <td>Robbery</td>
      <td>Robbery of Personal Property</td>
      <td>South East BCU</td>
      <td>Lewisham</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>47</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-04-01</td>
      <td>Offences</td>
      <td>Possession of Weapons</td>
      <td>Possession of Other Weapon</td>
      <td>North BCU</td>
      <td>Enfield</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>7</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2017-04-01</td>
      <td>Sanction Detections</td>
      <td>Theft</td>
      <td>Bicycle Theft</td>
      <td>Central North BCU</td>
      <td>Camden</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-04-01</td>
      <td>Offences</td>
      <td>Miscellaneous Crimes Against Society</td>
      <td>Threat or Possession With Intent to Commit Cri...</td>
      <td>Central South BCU</td>
      <td>Southwark</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017-04-01</td>
      <td>Offences</td>
      <td>Miscellaneous Crimes Against Society</td>
      <td>Making Supplying or Possessing Articles for use i</td>
      <td>South BCU</td>
      <td>Croydon</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2017-04-01</td>
      <td>Sanction Detections</td>
      <td>Public Order Offences</td>
      <td>Racially or Religiously Aggravated Public Fear Al</td>
      <td>West BCU</td>
      <td>Ealing</td>
      <td>fy17-18</td>
      <td>2023-03-01</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_sql("""SELECT type
                        FROM london_crime
                        limit 10;""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Offences</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sanction Detections</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sanction Detections</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Offences</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Offences</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Offences</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Sanction Detections</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Offences</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Offences</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Sanction Detections</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
