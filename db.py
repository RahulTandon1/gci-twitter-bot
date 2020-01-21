import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['twitterBotDB']
fedoraPosts = db['posts']


# saves a post only if it's new
def saveNewPost(title, link):
    is_a_new_post = True

    # checking if it's a new post or not
    # based on the presence of same link
    for post in fedoraPosts.find():
        if link == post['link']:
            is_a_new_post = False
            break

    # if it's a new post, saving it to db
    if is_a_new_post:
        post = {
            'title': str(title),
            'link': str(link),
            'isNew': bool(True)
        }
        result = fedoraPosts.insert_one(post)


# returns new posts from the db
# and changes their 'isNew' to False during the process
# returns a string in case there is no new post
# else returns a list of new posts
def getNewPosts():
    newPosts = list()
    for post in fedoraPosts.find({'isNew': True}):

        result = fedoraPosts.update_one(
            {'_id': post['_id']},
            {'$set': {'isNew': False}}
        )

        newPosts.append({
            'title': post['title'],
            'link': post['link']
        })
    if len(newPosts) == 0:
        return 'No new postss'
    else:
        return newPosts
