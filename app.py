import os
import pymsteams
import boto3

from chalice import Chalice, Cron

app = Chalice(app_name='aws-service-start-stop-scheduler')
rds = boto3.client('rds')


# Run at 1:30pm (UTC) (i.e 07:00pm [IST]) every Monday through Friday.
@app.schedule(Cron(30, 13, '?', '*', 'MON-FRI', '*'))
def stop_lambda_handler(event):
    print("Stopping cluster")
    response = rds.stop_db_cluster(DBClusterIdentifier=os.environ.get("DBClusterIdentifier"))
    print('Stopped your cluster: ' + str(response))
    send_notification_to_ms_teams("Stop cluster response {}".format(response))


# Run at 02:30am(UTC) [i.e.08:00am (IST)] every Monday through Friday.
@app.schedule(Cron(30, 2, '?', '*', 'MON-FRI', '*'))
def start_lambda_handler(event):
    print("Starting cluster")
    response = rds.start_db_cluster(DBClusterIdentifier=os.environ.get("DBClusterIdentifier"))
    print('Started your cluster: ' + str(response))
    send_notification_to_ms_teams("Start cluster response {}".format(response))


def send_notification_to_ms_teams(message):
    print("Sending message {} to MS Teams".format(message))
    ms_teams_message = pymsteams.connectorcard(os.environ.get('msTeamChannelIncomingWebhook'))
    ms_teams_message.text(message)
    ms_teams_message.send()
