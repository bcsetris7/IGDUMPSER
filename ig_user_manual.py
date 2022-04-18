from PersonalLib.Shadow import *
from PersonalLib.Fast import *
from PersonalLib.More import *

try:
	from bs4 import BeautifulSoup
	from fake_useragent import UserAgent
	import requests
	import json
	import sys
except ImportError:
	print("""One or more modules are not installed.
Run the following command to install missing modules:
pip install bs4 fake_useragent requests json""")

######################
session = requests.Session()
######################
headers1_1 = {
	'user-agent' : UserAgent().random
}
######################

def AskUser(session):
    try :
        command = input (LB+"root@#kali "+R+"/ "+LB+"USERNAME "+R+"> "+W)
        if command.lower() == "help" : 
            print (f'{dict["Help"]}')	
            AskUser()
        elif command.lower() == "exit" :
            print (f'{BG_P} {dict["GoodBye"]} {W}')
            sys.exit()
        else :
            try :
            	DumpUser(command, session)
            except :
            	print (f'{BG_P} {command} {BG_R} MASUKAN NAMA YANG BENAR {W}')
            	sys.exit()
    except KeyboardInterrupt :
        print (f'{BG_P} {dict["GoodBye"]} {W}')
        sys.exit()
        
def DumpUser(User, session):
	BaseUrl = "https://www.instagram.com/"+User+"/channel"
	data = session.get(BaseUrl, headers=dict["Headers"])
	csrftoken = data.cookies["csrftoken"]
	referer = "https://www.instagram.com/"+User+"/"
	soup = BeautifulSoup(data.text, 'html.parser')
	for i in range(0, 50) :
		script = soup.find_all('script')[i]
		if isData in str(script) :
			script = soup.find_all('script')[i]
			break
	ToJson(script, csrftoken, referer, session)
	
def ToJson(Script, csrftoken, referer, session) :
	JsonFile = str(Script).split(Ghost1)[1]
	JsonFile = JsonFile.split(Ghost2)[0]
	JsonFile = json.loads(str(JsonFile))
	UserId = JsonFile["entry_data"]["ProfilePage"][0]["graphql"]["user"]["id"]
	AllData = JsonFile["entry_data"]["ProfilePage"][0]
	HasStoryIsLive(UserId, AllData, csrftoken, referer, session)
	
	
def HasStoryIsLive(UserId, Data, csrftoken, referer, session):
	try :
		QueryJson.update({"user_id": UserId})
		TargetUrl = QueryUrl+QueryHash+HashContent+QueryVariables+str(QueryJson)+FixParameter
		TargetUrl = TargetUrl.replace("'",'"')
		TargetUrl = TargetUrl.replace(" ","")
		TargetUrl = TargetUrl.replace("False","false")
		TargetUrl = TargetUrl.replace("True","true")
		try :
			data = session.get(TargetUrl, headers=dict["Headers"])
			StoryAnswer = data.json()["data"]["user"]["has_public_story"]
			LiveAnswer = data.json()["data"]["user"]["is_live"]
		except :
			StoryAnswer = "I Dont Know"
			LiveAnswer = "I Dont Know"
#		AllPosts(Data, UserId, csrftoken, referer, session)
		MirrorInfo(StoryAnswer, LiveAnswer, Data)
		
	except :
		print ("[ Error : HasPublicStoryLive ]")
		AllPosts(Data, UserId, csrftoken, referer, session)
		MirrorInfo(Failed, Failed, Data)

def main(session):
	os.system("clear || cls")
	Screen()
	AskUser(session)
	
##############################
def MirrorInfo(StoryAnswer, LiveAnswer, Data):
	UserName = Data["graphql"]["user"]["username"]
	#### SURE FACE DATA ####
	print (f"{Y}INFO :{W}\n			{G}True{W} >>>>> Yes.\n			{G}False{W} >>>>> No.\n")
	print ("= "*25)
	time.sleep(2)
	Username(Data["graphql"]["user"], UserName)
	FullName(Data["graphql"]["user"], UserName)
	id(Data["graphql"]["user"], UserName)
	Fbid(Data["graphql"]["user"], UserName)

print("""BUAT DATA DENGAN NAMA user.txt/setera kalian -> CARA [nano user.txt]""")
# RUN
main(session)
