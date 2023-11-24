 
from keys import api_key
import requests
import csv 
import re


#test and works
#movie_id='tt6751668'

#res=requests.get(f"https://www.omdbapi.com/?apikey={api_key}&i={movie_id}")
#print(res.json())



def movie():
    with open ('oscar_winners.csv','r') as file:
        rows= csv.reader(file) #in a dictionary form
        headers=['Movie Title', 'Runtime', 'Genre','Award Wins','Award Nominations','Box Office']
        
        
        with open('movies.csv', 'w', newline='', encoding='utf-8') as newfile:
            writer = csv.writer(newfile)
            writer.writerow(headers)
            
            for row in rows:
                movie_id= row['IMDB']
                res=requests.get(f"https://www.omdbapi.com/?apikey={api_key}&i={movie_id}")
                data=res.json()
                title=str(data['Title'])
                time=int(data['Runtime']).split(''[0])
                genre=str(data['Genre'])
                awards= re.findall(r'\d+', data['Awards'])
                wins=int(awards[0]) if awards else 0
                noms=int(awards[1]) if len(awards) >1 else 0
                boxoffice= int(data['BoxOffice'].strip('$').replace(","," "))
                
                
                info = [title, time, genre,wins, noms,boxoffice]
                
                with open('movies.csv','w', newline='', encoding='utf-8') as f:
                    writer.writerow(info)
                
            
            

movie()