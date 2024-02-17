import aminofix as amino

client = amino.Client()
client.parse_headers = lambda data=None, type=None: {**amino.headers.ApisHeaders(deviceId=amino.helpers.gen_deviceId() if client.autoDevice else client.device_id, data=data, type=type).headers, 'Host': 'service.aminoapps.com'}

n=input("Profile link: ")
fok=client.get_from_code(n)
id=client.get_from_code(n).objectId
cid=fok.path[1:fok.path.index("/")]
print("this mf ndc://g/user-profile/"+id)
#print("yoyo" +cid) #for comid #remove hashtag and add hashtag to other print to change to it
