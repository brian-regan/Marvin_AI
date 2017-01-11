import json

def get_creds():
	try:
		json_data=open("creds.json").read()
	except:
		print("Could not find creds.json file")

	data = json.loads(json_data)

	return data