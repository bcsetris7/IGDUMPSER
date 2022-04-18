################################
						# Important #
import time, sys, os, requests
W = "\033[0m"
Y = '\033[33;1m'
LB = '\033[1;36;40m'
################################
def BeforeFlush(Word):
    print (f'{Y}	、__ [~] {LB}{Word} : {W}', end='')
    
def Flush(Which, Color1, Color2, SleepTime1, SleepTime2):
    for char in Which :
        sys.stdout.write(Color1+char+Color2)
        sys.stdout.flush()
        time.sleep(SleepTime1)
    time.sleep(SleepTime2)
    
def ShortLink(Link) :
	ApiUrl = "http://tinyurl.com/api-create.php?url="+Link
	Shorted = requests.get(ApiUrl)
	Flush(Shorted.text, W, W, 0.05, 1)
	
def SaveAsTextFile(SaveThis, FileName) :
	paths = [os.path.join(r,file) for r,d,f in os.walk("Users/") for file in f ]
	if "Users/"+FileName in paths :
		pass
	elif "Users/"+FileName+"/"+FileName+".txt" in paths :
		pass
	else :
		os.system("mkdir Users/"+FileName)
	with open("Users/"+FileName+"/"+FileName+".txt","a+") as File :
		File.write(SaveThis+"\n")
		
		
################################
							# Dump #
################################

def LogginPageId(Data, FileName):
	try :
		BeforeFlush("Loggin Page Id")
		Flush(str(Data["logging_page_id"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Loggin Page Id : "+str(Data["logging_page_id"]), FileName)
	except :
		BeforeFlush("Loggin Page Id")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Loggin Page Id : "+"None", FileName)
	print ("")
		
def ShowSuggestedProfiles(Data, FileName):
	try :
		BeforeFlush("Show Suggested Profiles")
		Flush(str(Data["show_suggested_profiles"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Show Suggested Profiles : "+str(Data["show_suggested_profiles"]), FileName)
	except :
		BeforeFlush("Show Suggested Profiles")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Show Suggested Profiles : "+"None", FileName)
	print ("")
		
def ShowFollowDialog(Data, FileName):
	try :
		BeforeFlush("Show Follow Dialog")
		Flush(str(Data["show_follow_dialog"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Show Follow Dialog : "+str(Data["show_follow_dialog"]), FileName)
	except :
		BeforeFlush("Show Follow Dialog")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Show Follow Dialog : "+"None", FileName)
	print ("")

def ShowViewShop(Data, FileName):
	try :
		BeforeFlush("Show View Shop")
		Flush(str(Data["show_view_shop"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Show View Shop : "+str(Data["show_view_shop"]), FileName)
	except :
		BeforeFlush("Show View Shop")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Show View Shop : "+"None", FileName)
	print ("")
	

def CountryBlock(Data, FileName):
	try :
		BeforeFlush("Country Block")
		Flush(str(Data["country_block"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Country Block : "+str(Data["country_block"]), FileName)
	except :
		BeforeFlush("Country Block")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Country Block : "+"None", FileName)
	print ("")
	

def HasArEffects(Data, FileName):
	try :
		BeforeFlush("Has Ar Effects")
		Flush(str(Data["has_ar_effects"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Ar Effects : "+str(Data["has_ar_effects"]), FileName)
	except :
		BeforeFlush("Has Ar Effects")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Ar Effects : "+"None", FileName)
	print ("")
	
def HasClips(Data, FileName):
	try :
		BeforeFlush("Has Clips")
		Flush(str(Data["has_clips"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Clips : "+str(Data["has_clips"]), FileName)
	except :
		BeforeFlush("Has Clips")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Clips : "+"None", FileName)
	print ("")
	
def HasGuides(Data, FileName):
	try :
		BeforeFlush("Has Guides")
		Flush(str(Data["has_guides"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Guides : "+str(Data["has_guides"]), FileName)
	except :
		BeforeFlush("Has Guides")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Guides : "+"None", FileName)
	print ("")
	
def HasChannel(Data, FileName):
	try :
		BeforeFlush("Has Channel")
		Flush(str(Data["has_channel"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Channel : "+str(Data["has_channel"]), FileName)
	except :
		BeforeFlush("Has Channel")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Channel : "+"None", FileName)
	print ("")
	
def HighlightReelCount(Data, FileName):
	try :
		BeforeFlush("Highlight Reel Count")
		Flush(str(Data["highlight_reel_count"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Highlight Reel Count : "+str(Data["highlight_reel_count"]), FileName)
	except :
		BeforeFlush("Highlight Reel Count")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Highlight Reel Count : "+"None", FileName)
	print ("")
	
def id(Data, FileName):
	try :
		BeforeFlush("id")
		Flush(str(Data["id"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] id : "+str(Data["id"]), FileName)
	except :
		BeforeFlush("id")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] id : "+"None", FileName)
	print ("")
	

	
def Username(Data, FileName):
	try :
		BeforeFlush("Username")
		Flush(str(Data["username"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Username : "+str(Data["username"]), FileName)
	except :
		BeforeFlush("Username")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Username : "+"None", FileName)
	print ("")
	
