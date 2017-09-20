from disqusapi import DisqusAPI
import config

class User():
    def __init__(self, username, num_followers, display_name, joined_at, user_since,
                 about, connections, num_posts, reputation, num_likes_received,
                 owns_their_own_forum, disqus_unique_id, num_following):
        self.username = username
        self.num_followers = num_followers
        self.display_name = display_name
        self.joined_at = joined_at
        self.user_since = user_since
        self.about = about
        self.connections = connections
        self.num_posts = num_posts
        self.reputation = reputation
        self.num_likes_received = num_likes_received
        self.owns_their_own_forum = owns_their_own_forum
        self.disqus_unique_id = disqus_unique_id
        self.num_following = num_following

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
    def __init__(self, users_list, website_list):
        self.users_list = users_list
        self.website_list = website_list

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








