# Start / Stop AWS services by scheduler

This lambda helps to start / stop AWS services such as AWS Neptune... by `CRON` scheduler 


Building the project
=================

Create Virtual environment::
   
    $ python3 -m venv venv37

Activate the vitual environment::
    
	$ . venv37/bin/activate
	
Go to project directory::

	$ cd {PATH}/aws-service-start-stop-scheduler/
	
Install Chalice::

	$ python3 -m pip install chalice

Install requirements::

    $ pip install -r requirements.txt

To Run local::

    $ chalice local
 
To Run test::
	
	$ py.test tests/
	
	$ pytest --log-cli-level=DEBUG
	 
 
## Deploy

    chalice deploy --stage prod


# Microsoft Teams 

### Create Webhook Incoming channel

Add an incoming webhook to a Teams channel:

1. Navigate to the channel where you want to add the webhook and select (•••) More Options from the top navigation bar.
2. Choose Connectors from the drop-down menu and search for Incoming Webhook.
3. Select the Configure button, provide a name, and optionally, upload an image avatar for your webhook.
4. The dialog window will present a unique URL that will map to the channel. Make sure that you copy and save the URL — you will need to provide it to the outside service.
5. Select the Done button. The webhook will be available in the team channel.
