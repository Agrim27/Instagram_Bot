from instapy import InstaPy

session = InstaPy(username="_urja_12", password="foodforgood")
session.login()


#like section
session.like_by_tags(['javascript', 'python'], amount=4)

#following section
session.set_do_follow(True, percentage=10)


#comment section
session.set_do_comment(True, percentage=50)
session.set_comments('Great')


session.end()
