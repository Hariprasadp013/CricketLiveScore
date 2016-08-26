#!/usr/bin/env python
import pynotify, urllib2, json,time
def score():
	while True:
		time.sleep(30)
		try:
			ur= "http://cricapi.com/api/cricket/"
			response = urllib2.urlopen(ur)
			datas=json.load(response)
			j=0
			while (datas['data']!=None):
				uid=datas['data'][j]['unique_id']
				ur2= "http://cricapi.com/api/cricketScore/?unique_id="+uid
				resp=urllib2.urlopen(ur2)
				result=json.load(resp)
				pynotify.init("Display")
				notice=pynotify.Notification("cricket Live",result['score'])
				notice.show()
				j=j+1
				if j==4:
					notice.close()
					break	
		except Exception:
			print 'No Internet'
			return	

if __name__ == '__main__':
	score()


