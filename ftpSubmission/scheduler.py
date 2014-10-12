#!/usr/bin/python


# there are few important points...
# you should do chdir at your main script..


from crontab import CronTab
 
tab = CronTab(user=True) # here we are setting true to user, and job will run with current user
cmd = '/home/gaurav/Desktop/SubmissionGaurav/ftpSalesforce.py' # you need to enter your absolute script path here 
# don't run without making changes in ftpSalesforce.py main method where you need to uncomment os.chdir and put abosulte path of 
#directory
cron_job = tab.new(cmd) # this is for running job
cron_job.minute.on(0)
cron_job.hour.on(22)# running daily at 10 P.M.
tab.write()
print tab.render()


