import os

import boto3
from chalice import Chalice, Cron

app = Chalice(app_name='aws-service-start-stop-scheduler')
rds = boto3.client('rds')


# Run at 07:00pm (UTC) every Monday through Friday.
@app.schedule(Cron(0, 19, '?', '*', 'MON-FRI', '*'))
def stop_lambda_handler(event):
    print("Stopping cluster")
    response = rds.stop_db_cluster(DBClusterIdentifier=os.environ.get("DBClusterIdentifier"))
    print('Stopped your cluster: ' + str(response))


# Run at 08:00am (UTC) every Monday through Friday.
@app.schedule(Cron(0, 8, '?', '*', 'MON-FRI', '*'))
def start_lambda_handler(event):
    print("Starting cluster")
    response = rds.start_db_cluster(DBClusterIdentifier=os.environ.get("DBClusterIdentifier"))
    print('Started your cluster: ' + str(response))

