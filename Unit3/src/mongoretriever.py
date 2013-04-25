import pymongo
def search(*args):
	client = pymongo.Connection('localhost',27017)
	db = client.tourism_database8
	database8 = db.database8
	Type=args[0]
	Name=args[1].title()
	print Name
	State=args[2].title()
	Budget=args[3]
	Distance=args[4]
	By=args[5]
	client1=[]
	post={}
	if Type!='none':
		post.update({'Type':Type})
	if Name!='None':
		post.update({'Name':Name})
	if State!='None':
		post.update({'State':State})
	if Budget!='none':
		if re.match('less than',Budget,re.I):
			Budget=Budget.replace('less than','').strip()
			post.update({'Budget':{'$lt':int(Budget)}})
		elif re.match('greater than',Budget,re.I):
			Budget=Budget.replace('greater than','').strip()
			post.update({'Budget':{'$gt':int(Budget)}})
		else:
			Budget=Budget.strip()
			post.update({'Budget':int(Budget)})
	if Distance!='none':
		if re.match('less than',Distance,re.I):
			Distance=Distance.replace('less than','').strip()
			post.update({'Distance':{'$lt':int(Distance)}})
		elif re.match('greater than',Distance,re.I):
			Distance=Distance.replace('greater than','').strip()
			post.update({'Distance':{'$gt':int(Distance)}})
		else:
			Distance=Distance.strip()
			post.update({'Distance':int(Distance)})

	if By!='none':
		post.update({'Preferred by':By})
	#print "post=",post
	for i in database6.find(post):
		i=dict(i)
		#print "i=",i
		df=i[u'State'].replace(" ","")
		for j in database8.find({'Name':(i[u'Name'].replace(" ","").replace(",","").replace(df,"").lower())}):
			j=dict(j)
			i.update(j)
			client1.append(i)
	return client1
	if len(client1)==0:
		return None
	else:
		return client1
