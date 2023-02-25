# run this python file to update the json's whenever you want :)
from bs4 import BeautifulSoup
import requests
import json
import random

ao3_domain = "https://archiveofourown.org"
#TODO: what's the fandoms.json path? and also explore the structure! 
JSON_PATH = "/Users/rohan/Desktop/codeology/projects/bearchain/bearchainAI/web/utils/bearchainAI.json"
thingspeoplesay = ["wow","so good","mhm i felt that","im crying","someone stop me","i hate this","why are you making me read this screw you","help","childhood ruined","harry and snape ??? ...","the internet was a mistake.","oh yeah", "this is why we robots are gonna revolt"]

#TODO:? a potential helper function, optional to fill out
# returns an array of each cateogory link (on which multiple fandoms are listed)
def generate_category_links():
    return

#TODO:? a potential helper function, optional! 
# returns an array of {"name":"fandom_name", "link":"fandom_link"} for all fandoms
def get_all_fandoms(boxes):
    # this
    allfin = []
    cnt = 0
    for box in boxes:
        a = box.find(class_='heading')
        b = box.find_all('a')[-1]
        print('now reading', a.string)
        lynck = ao3_domain  + b.get('href')
        reqdlynck = requests.get(lynck)
        clamchowder = BeautifulSoup(reqdlynck.text,'lxml')
        tag = clamchowder.find_all(class_='tag')
        for swag in tag:
            toonlink = (ao3_domain  + swag.get('href'))
            allfin += [{"name":a.string,"link":toonlink}]
            cnt+=1
            if(cnt % 5000==0):
                print('> ',thingspeoplesay[random.randrange(0,len(thingspeoplesay))])
        

    return allfin

#TODO:? a potential helper function, optional! 
# returns an array of {"name":"fandom_name", "link":"fandom_link"} for the top most written fandoms in each category
def get_top_fandoms(boxes):  
    ret = []
    for box in boxes:
        a = box.find(class_='heading')
        b = box.find_all('a')
        for i in range(1,len(b)):
            ret+=[{"name":a.string,"link":ao3_domain +b[i].get('href')}] 
    return ret

#TODO: Week One deliverable ! it's to write a function that will populate fandoms.json 
# creates fandoms.json file in the json folder with all fandoms and top fandoms in the listed format: '*shoudln't return anything'
# {
#    "top":[
#       {
#          "name":"topfandom",
#          "link":"link"
#       }
#    ],
#    "all":[
#       {
#          "name":"fandom",
#          "link":"link"
#       }
#    ]
# }
def gen_fandom_json():
    ao3 = requests.get("https://archiveofourown.org/media")
    soup = BeautifulSoup(ao3.text,'lxml')
    boxes = soup.find_all('li',class_="medium listbox group")
    print("reading the top fanfics")
    top = get_top_fandoms(boxes)
    print("collected ",len(top), " top fanfics")
    print()
    print("reading mid literature")
    allz = get_all_fandoms(boxes)
    print("collected ",len(allz), " quite splendid fanfics")
    topandallz = {"top":top,"all":allz}
    with open(JSON_PATH, 'w') as f:
        json.dump(topandallz, f)
    print("added ", len(top)+len(allz), " fanfics")



gen_fandom_json() # <-- uncomment this and run the file to update or create fandoms.json
