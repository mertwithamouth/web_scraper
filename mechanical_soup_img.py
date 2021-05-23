import mechanicalsoup
import os
import wget


browser= mechanicalsoup.StatefulBrowser()
url="https://images.google.com/imghp?hl=en&gl=ar&gws_rd=ssl"

browser.open(url)

browser.get_current_page()

browser.select_form()
browser.get_current_form().print_summary()

search_term=input("What do you want?: ")


browser["q"]=search_term

browser.launch_browser()
response=browser.submit_selected()

print("new url:",browser.get_url())
print("response: \n", response.text[:500])

new_url=browser.get_url()
browser.open(new_url)

page=browser.get_current_page()
all_images=page.find_all("img")

image_source=[]
for image in all_images:
    image=image.get("src")
    image_source.append(image)

image_source=[image for image in image_source if image.startswith("https")]

image_source

path=os.getcwd()
path=os.path.join(path,search_term+"s")
os.mkdir(path)

counter=0
for image in image_source:
    save_as=os.path.join(path, search_term+str(counter)+".jpg")
    wget.download(image,save_as)
    counter+=1