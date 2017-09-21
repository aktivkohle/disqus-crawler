# https://github.com/disqus/disqus-python/issues/34
# pip install --upgrade https://github.com/disqus/disqus-python/archive/master.zip
from disqusapi import DisqusAPI
from config import *

disqus = DisqusAPI(SECRET_KEY, PUBLIC_KEY)

def softget(dictionary, key):
    if key in dictionary:
        return dictionary[key]

class User():
    def __init__(self, ID, username=None, about=None, name=None, disable3rdPartyTrackers=None,
                 isPowerContributor=None, joinedAt=None, rep=None, profileUrl=None, url=None,
                 reputation=None, location=None, isPrivate=None, signedUrl=None, isPrimary=None,
                 isAnonymous=None, reputationLabel=None, avatar=None, numFollowers=None,
                 numFollowing=None, numForumsFollowing=None, numLikesReceived=None,
                 numPosts=None):
        self.username = username
        self.about = about
        self.name = name
        self.disable3rdPartyTrackers = disable3rdPartyTrackers
        self.isPowerContributor = isPowerContributor
        self.joinedAt = joinedAt
        self.rep = rep
        self.profileUrl = profileUrl
        self.url = url
        self.reputation = reputation
        self.location = location
        self.isPrivate = isPrivate
        self.signedUrl = signedUrl
        self.isPrimary = isPrimary
        self.isAnonymous = isAnonymous
        self.id = ID   # capitals as Python protected
        self.reputationLabel = reputationLabel
        self.avatar = avatar
        self.numFollowers = numFollowers  # this and following rows need to come from a different API call
        self.numFollowing = numFollowing
        self.numForumsFollowing = numForumsFollowing
        self.numLikesReceived = numLikesReceived
        self.numPost = numPosts

    def add_to_sql(self):
        """
        Add this users data to the database
        """
        pass

    def list_recent_posts(self):
        pass

    def list_forums_visited(self):
        pass

class WebsiteForum():
    def __init__(self, url, language, disqus_website_id, disqus_admin_website_name):
        self.url = url
        self.language = language
        self.disqus_website_id = disqus_website_id
        self.disqus_admin_website_name = disqus_admin_website_name

    def add_to_sql(self):
        """
        Add this websites data to the database
        """
        pass

    def yield_csv_row(self):
        """
        returns just 1 row for use in writing in other functions
        """
        pass


class ObjectPopulator():
    def __init__(self, users_list, website_list, forum_name):
        self.users_list = users_list
        self.website_list = website_list
        self.forum_name = forum_name

    @property
    def get_users_list(forum_name):
        userslist = disqus.get('forums.listUsers', method='GET', forum=forum_name, limit=100).response
        assert isinstance(userslist, list)
        return userslist

    # https://stackoverflow.com/questions/30420621/python-creating-object-instances-in-a-loop-with-independent-handling

    def add_user(self):
        """
        Add an item of class User to ObjectPopulator.users_list
        """
        pass

    def add_website(self):
        """
        Add an item of class WebsiteForum to ObjectPopulator.website_list
        """
        pass

    def load_from_file(self):
        """
        populate the contents of this class from a previous session from a pickle file or similar
        """
        pass

    def load_from_sql(self):
        """
        populate the contents of this class from a previous session from a sql or sqllite3 table
        """
        pass

    def filter_users_list(self, criteria):
        pass

    def filter_website_list(self, criteria):
        pass

class Crawler(ObjectPopulator):
    def __init__(self):
        super().__init__()
        self.qualified_user_list = []
        self.qualified_website_list = []

    def crawl_from_user(self):
        pass

    def crawl_from_website(self):
        pass

    def remove_website(self):
        pass

    def remove_user(self):
        pass

# create one test instance :

user_one = User(
    username = softget(u,'username'),
    about = softget(u,'about'),
    name = softget(u,'name'),
    disable3rdPartyTrackers = softget(u,'disable3rdPartyTrackers'),
    isPowerContributor = softget(u,'isPowerContributor'),
    joinedAt = softget(u,'joinedAt'),
    rep = softget(u,'rep'),
    profileUrl = softget(u,'profileUrl'),
    url = softget(u,'url'),
    reputation = softget(u,'reputation'),
    location = softget(u,'location'),
    isPrivate = softget(u,'isPrivate'),
    signedUrl = softget(u,'signedUrl'),
    isPrimary = softget(u,'isPrimary'),
    isAnonymous = softget(u,'isAnonymous'),
    ID = softget(u,'id'),
    reputationLabel = softget(u,'reputationLabel'),
    avatar = softget(u,'avatar'),
    numFollowers = softget(v,'numFollowers'),
    numFollowing = softget(v,'numFollowing'),
    numForumsFollowing = softget(v,'numForumsFollowing'),
    numLikesReceived = softget(v,'numLikesReceived'),
    numPosts = softget(v,'numPosts'),
)


