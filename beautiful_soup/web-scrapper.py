import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# page1 = requests.post(URL)
#print(page.text)
file_object = open("html.txt","w")
file_object.write(page.text)

file_post = open("post.txt","w")
file_post.write(page1.text)
