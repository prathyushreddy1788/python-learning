#Create a SocialMediaProfile class that represents a user's social media profile.
# The class should have methods to post updates, add friends, remove friends, like posts,
# and comment on posts. Each user can have attributes like username, followers, posts,
# and friends list. Implement methods to display the user's posts, friend list, and post interactions.

class Posts:
    def __init__(self, post):
        self.post = post

    def comment(self,comment):
        self.comment = comment

    def like(self, like):
        self.like = like





class SocialMediaProfile:
    def __init__(self, user_name, followers):

        self.user_name = user_name
        self.followers = followers
        self.posts: list[Posts] = []
        self.friends: list = []

    def add_post(self, post):
        self.posts.append(post)

    def add_friends(self, friends):
        self.friends.append(friends)

    def remove_friends(self, friends):
        self.friends.append(friends)


    def friends_list(self):
        for friend in self.friends:
            print(friend)


    def user_posts(self):

        for post in self.posts:
            print(post)

    def user_interactions(self):
        for post in self.posts:
            print(f"{post.post} : {post.comment} : {post.like}")





prathyush = SocialMediaProfile("prathyush",40)
prathyush.add_friends("aakash")
prathyush.add_friends("pranathi")
prathyush.add_friends("vamshi")
prathyush.friends_list()

post1 =Posts("hi everyone")
post2 =Posts("good morning")
prathyush.add_post(post1)
prathyush.add_post(post2)
post1.comment("hiiii.....")
post2.comment("good morning")
prathyush.user_interactions()







