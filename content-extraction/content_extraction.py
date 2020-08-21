import pandas as pd
import numpy as np
import nltk   
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from wordpress_xmlrpc import WordPressPost


#You dont need these commented out lines if you use wordpress_xmlrpc
# blogs_list=pd.read_csv("blog_links.csv", header=None)
# blogs_list.rename(columns={0: 'Links'}, inplace=True)


from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, GetPost
from wordpress_xmlrpc.methods.users import GetUserInfo

client = Client("https://trustmeyourealive.wordpress.com/xmlrpc.php", 'username', 'password')
all_posts = client.call(GetPosts({'number':80,'post_status': 'publish'}, results_class=WordPressPost))

print(all_posts[0])


titles=[] #all_posts[0] etc
content=[] #one_post.content etc
post_id=0
for i,post in enumerate(all_posts):
	post_id = all_posts[i].id
	one_post=client.call(GetPost(post_id))
	one_post.content=re.sub(r'<[^<]+?>', '', one_post.content)
	one_post.content=re.sub(r"\[.*?\]", '', one_post.content)

	titles.append(all_posts[i])
	one_post.content = one_post.content.encode('ascii', 'ignore').decode('ascii')
	content.append(one_post.content)

print(titles,len(content))

df=pd.DataFrame()
df["Titles"]=titles
df["content"]=content

df.to_csv("blog_content and titles.csv",index=None)
