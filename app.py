import os
import pymsteams
import boto3

from chalice import Chalice, Cron

app = Chalice(app_name='aws-service-start-stop-scheduler')
rds = boto3.client('rds')


# -----------------------START SERVICE-------------------------------#
# Run at 03:00am(UTC) [i.e.08:30am (IST)] every Monday through Friday.
@app.schedule(Cron(00, 3, '?', '*', 'MON-FRI', '*'))
def start_lambda_handler(event):
    print("Starting cluster")
    response = rds.start_db_cluster(DBClusterIdentifier=os.environ.get("DBClusterIdentifier"))
    print('Started your cluster: ' + str(response))
    # Sending notification to Microsoft Team
    send_notification_to_ms_teams("Start cluster response {}".format(response))


# -----------------------STOP SERVICE-------------------------------#
# Run at 1:15pm (UTC) (i.e 06:45pm [IST]) every Monday through Friday.
@app.schedule(Cron(15, 13, '?', '*', 'MON-FRI', '*'))
def stop_lambda_handler(event):
    print("Stopping cluster")
    response = rds.stop_db_cluster(DBClusterIdentifier=os.environ.get("DBClusterIdentifier"))
    print('Stopped your cluster: ' + str(response))
    # Sending notification to Microsoft Team
    send_notification_to_ms_teams("Stop cluster response {}".format(response))


# Sending notification to Microsoft Team
def send_notification_to_ms_teams(message):
    print("Sending message {} to MS Teams".format(message))
    ms_teams_message = pymsteams.connectorcard(os.environ.get('msTeamChannelIncomingWebhook'))
    ms_teams_message.text(message)
    ms_teams_message.send()
