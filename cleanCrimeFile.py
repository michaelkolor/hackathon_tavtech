import pandas as pd
import numpy as np
import random

def cleanFile():

	file = pd.read_csv('crime.csv', encoding = 'latin-1')
	#print(list(file))

	file = file.drop(['INCIDENT_NUMBER', "HOUR", "STREET", "Location", "OFFENSE_CODE",
		"UCR_PART", "REPORTING_AREA", "DISTRICT", "OFFENSE_CODE_GROUP", "DAY_OF_WEEK", 
		"SHOOTING"], axis = 1)

	file = file[0:200]

	return (file)


def main():
	cleanedFile = cleanFile()
	Israel = pd.read_csv("lat_long.csv")
	Israel['Type'] = "Missle"
	Islat = list(Israel['Latitude'])
	Islon = list(Israel['Longitude'])

	Islat = [x for x in Islat if str(x) != 'nan' and x < 32 and x > 30]
	Islon = [x for x in Islon if str(x) != 'nan' and x > 34 and x < 35]

	Bolat = cleanedFile['Lat']
	Bolon = cleanedFile['Long']

	Bolat = [x for x in Bolat if str(x) != 'nan']
	Bolon = [x for x in Bolon if str(x) != 'nan']

	BolatNew = []
	BolonNew = []

	minIslat = np.min(Islat)
	maxIslat = np.max(Islat)

	minIslon = np.min(Islon)
	maxIslon = np.max(Islon)


	for i in range(len(cleanedFile['Lat'])):
		newLat = random.choice(Islat)
		newLon = random.choice(Islon)
		BolatNew.append(newLat)
		BolonNew.append(newLon)

	cleanedFile['Latitude'] = BolatNew
	cleanedFile['Longitude'] = BolonNew
	cleanedFile['Type'] = "Crime"

	newDf = pd.DataFrame()
	cleanedFile =cleanedFile[['Latitude', 'Longitude', 'Type']]
	Israel = Israel[['Latitude', "Longitude", "Type"]]

	frames = [cleanedFile, Israel]
	result = pd.concat(frames)

	print(result)

	result.to_csv('combined_long_lat.csv')


		
main()