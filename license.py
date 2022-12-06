
import psycopg2
import requests
import json 
conn = psycopg2.connect(
   database="postgres", user='postgres', password='root', host='localhost', port= '5432'
)
def insert_license(license):
    cursor = conn.cursor()
    cursor.execute("insert into license(key,name,spdx_id,url,node_id)values(%s,%s,%s,%s,%s)",(license['key'],license['name'],license['spdx_id'],license['url'],license['node_id']))
    cursor.execute("select * from license")
    result = cursor.fetchall()
    for row in result:
        print(row[0],row[1],row[2],row[3],row[4],row[5])
url = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=1&page=2" 
responce = requests.get(url) 
data = responce.json() 
repos = data['items'] 
for repo in repos: 
    l = repo['license'] 
    insert_license(l) 
    #print(license['key']
    conn.commit()
 








