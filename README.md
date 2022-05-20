# Start / Stop AWS services by scheduler
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