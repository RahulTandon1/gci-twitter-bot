**About**
A Twitter bot for tweeting the titles and links of new articles from  https://fedoramagazine.org/. 

**Install**
run ```pip3 install -r requirements.txt```

**Test it**
run ```python3 index.py```

**See the output**
https://youtu.be/wc7JKTlv3KM

**Initial Algorithm / Pseudocode**
---------
0. Scrape the titles and links of all posts from https://fedoramagazine.org/

1. Check if there are any NEW posts and if so, save them in the mongodb database

2. If there are new posts
    2.1 Login (if not already)

    2.2 compose new tweet
    2.3 Post tweet
    2.4 Exit

3. If No new posts
    3.1 Inform use about the same
    3.2 Exit

**Tech Used**
Used 
- Selenium for webscraping
- BeautifulSoup for parsing the https://fedoramagazine.org/ page and getting new posts
- Pymongo (MongoDB driver for Python) for storing new posts

**Contents**
- index.py
Heart of the program.
It's ```execute``` function runs the whole program
Besides that, the ```login``` and ```tweet``` functions from it are used to well....login and tweet. 
I could've made a new file for it, but I'm too lazy and stuff works rn, and I want to get over with the task

Uses ```db.py```'s ```getNewPosts``` for getting all the new posts (posts whose ```isNew``` property is set to True).

- getFedora.py
Scrapes the fedora magazine website for articles. 
Uses ```db.py```'s ```saveNewPost``` function to save only new posts to db with their 
```isNew``` property set to True. 

- db.py
Responsible for all MongoDB related operations.
Each "post" object/dictionary/documents has the following properties, (besides the _id):
1. title -> title of the post {string}
2. link -> link to the post   {string}
3. isNew -> determines whether the given post is newly stored in the db and has not been posted before. {string}


Note to self: Although you won't do this, experiment with the typing in tweeting box problem you faced. It's most probably to do with the 'contenteditable' thingie, but still do experiment. 
(TBH Knowing me I won't)