#!/usr/bin/python

import zipfile
import requests
import base64
import json

import os

from datetime import datetime

from ftplib import FTP
from simple_salesforce import Salesforce
from crontab import CronTab

loggerFile = None

class ftpSalesforce:
	
	# constructor of this class
	def __init__(self):
		information = {} # dictionary which will contain information from configuration file
		# below we are opening file "configuration.txt" and reading line by line
		# we are than striping "\n"and white spaces and spliting on "="
		# finally we are storing info in dictionary information
		
		with open('configuration.txt') as fileConfig:
			for line in fileConfig:
				line.rstrip('\n')
				detail = line.split("=")
				information [detail[0].strip()]=detail[1].rstrip().strip()
		# calling ftpdownload to download zip file from ftp.. We are passing information dictionary
		result=self.ftpDownload(information)
		if(result==1):
			#if above step was successful we are calling zipfile function, which will unzip the file..
			result = self.zipFile(information)
	
		if (result ==1):
			print "Success"
		else:
			print "Not Success"
		# this ends our constructor




	# this is our ftpDownload method, which will download file from ftp server
	def ftpDownload(self,information):
		# making connection with FTP
		ftp = FTP(information['ftpServer'])
		# providing login credentials to validate
		ftp.login(information['ftpUsername'],information['ftpUserPassword'])
		# getting list of all files and directory
		allFilesList = ftp.nlst()
		flag = 0
		#traversing all files to see check whether the file which we want to download exists or not
		for files in allFilesList:
			if (files == information['filename']+".zip"):
				print "file download started"
				flag=1
				break
		if(flag==0):
			loggerFile.write("Module ftpDownload:File not found")
			loggerFile.write("\n")
			print "File not found"
			return flag
		# getting filehandle and opening file into which we will write locally.. this is temperary file.
		fileFtpDownloaded = open(information['filename']+".zip","wb")
		# writing mode is binary... Here we are writing into file..
	    	ftp.retrbinary("RETR " + information['filename']+".zip",fileFtpDownloaded.write)
		# closing file handle
		fileFtpDownloaded.close()
		#closing ftp connection
		ftp.close()
		return flag


# this is our salesforceUpload method, which will upload file in salesforce
	def salesforceUpload(self,information):
		# we are making safe connection with salesforce by passing account information
		sf = Salesforce(username=information['salesforceUserName'], password=information['salesforcepassword'], security_token=information['salesforcesecurityToken'])
		# we are getting session id here
		sessionId = sf.session_id
	
		flag = 0
		# we are querying all folders in your salesforce account
		documentQuery = sf.query("SELECT ID,Name FROM folder")
		# we are traversing all folders and fetching the folderid for our target folder which is SpringCM
		for f in documentQuery['records']:
			if (information['targetFoldername'] == f['Name']):
				folderid = f['Id']
				flag = 1
				print "folder found"
				break

		if flag ==0:
			loggerFile.write("Module salesforceUpload:folder not found")
			loggerFile.write("\n")
			print "folder not found"
			print "Leaving this program"
			return 0
		body = ""
		# here we are opening our xml file and encoding into base4..this is required to send files to salesforce
		with open(information['filename'], "r") as f:
			body = base64.b64encode(f.read())

		# Rest API post method call.. using requests post method
		# here we are sending parameters:
		#first one is url
		#second one is header, with content type as json
		#third one is our actual data
		response = requests.post('https://%s.salesforce.com/services/data/v24.0/sobjects/Document/' % information['salesforceinstance'],
		    headers = { 'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % sessionId },
		    data = json.dumps({
				'FolderId':folderid,
			'Name': information['filename'],
			'body': body
		    })
		)
		#printing the response output
		print response.text
		json_data = json.loads(response.text)
		if(json_data['success']== True):
			return 1
		else:
			loggerFile.write("Module salesforceUpload:Upload Failed")
			loggerFile.write("\n")
			return 0






    	# zip method to unzip file
	def zipFile(self,information):
		try:
			# extracting all files inside this zip 
			with zipfile.ZipFile(information['filename']+".zip", "r") as z:
	    			z.extractall()
		except:
			print "Error in Zip File"
			loggerFile.write("Module Zipfile:Error in Zip File")
			loggerFile.write("\n")
			return 0
		st = os.stat(information['filename'])
		if( st.st_size == 0):
			print "Error:Zero File Size"
			loggerFile.write("Module Zipfile:Error:Zero File Size")
			loggerFile.write("\n")
			return 0
		# calling salesforceUpload method to upload file into salesforce folder inside document tab
		result = self.salesforceUpload(information)

		# cleaning extracted file
		os.remove(information['filename'])
		# cleaning zipfile downloaded from ftp
		os.remove(information['filename']+".zip")
		if(result == 1):
			print "file is uploaded in your salesforce folder"
		else:
			print "salesforce upload failed"
			loggerFile.write("Module Zipfile:salesforce upload failed")
			loggerFile.write("\n")
			return 0
		return 1
	


	
	


def runner(): #main method
	#creating an object of ftpSalesforce class
	# you need to uncomment below line and put your path address if you are using crontab.
	#os.chdir("/home/gaurav/Desktop/finale") 
	loggerFile = open("logger.txt","a")
	loggerFile.write(str(datetime.now()))
	loggerFile.write("\n")
	utilityObject = ftpSalesforce() # creating object 
	loggerFile.close()
	




