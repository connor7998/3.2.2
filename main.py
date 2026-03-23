
#Activity 3.2.2 Step 7
from Post import Post

all_posts_archive = []


# your code here

post1 = Post("Marie", "This is my first post!")
print (post1)
post2 = Post("bob", "This is my second post")
post3 = Post("joe", "This is my third post")
print (post2)
print (post3)

username = input("enter username")
print(username)
print ("welcome to your account")
options = ["new", "remove", "change user", "print", "quit"]
user_input = None
while user_input != "quit":
	user_input = input("what would you like to do? (new, remove, change user, print, quit)")
	if user_input == "new":
		message = input("Add a post to the archive")
		new_post = Post(username, message)
		all_posts_archive.append(new_post)
	elif user_input == "remove":
		post_id = int(input("Remove a post from the archive"))
		for post in all_posts_archive:
			if post.get_post_id() == post_id:
				all_posts_archive.remove(post)
				print("post removed")
				break
	elif user_input == "change user":
		username = input("enter new username")
		print("username changed to " + username)
	elif user_input == "print":
		for post in all_posts_archive:
			print(post)
print("goodbye")
