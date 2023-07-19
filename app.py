import os
import pymsteams
import boto3

from chalice import Chalice, Cron

app = Chalice(app_name='start-stop-scheduler')
# rds = boto3.client('rds')
ec2 = boto3.client('ec2')


# # -----------------------START SERVICE-------------------------------#
# # Run at 03:15am(UTC) [i.e.08:45am (IST)] every Monday through Friday.
# @app.schedule(Cron(15, 3, '?', '*', 'MON-FRI', '*'))
# def start_lambda(event):
#     print("Starting cluster")
#     try:
#         response = rds.start_db_cluster(DBClusterIdentifier=os.environ.get("DBClusterIdentifier"))
#     except Exception as ex:
#         err = "Exception occurred on starting neptune due to {}".format(ex)
#         print(err)
#         send_notification_to_ms_teams(err)
#     print('Started your cluster: ' + str(response))
#     # Sending notification to Microsoft Team
#     send_notification_to_ms_teams("Start cluster response {}".format(response))
#


# -----------------------START SERVICE-------------------------------#
# Run at 03:15am(UTC) [i.e.08:45am (IST)] every Monday through Friday.
@app.schedule(Cron(15, 3, '?', '*', 'MON-FRI', '*'))
def start_ec2(event):
    print("Starting EC2")
    ec2_instances = os.environ.get("ec2").split(",")
    for ec2_instance in ec2_instances:
        try:
            response = ec2.start_instances(
                InstanceIds=[
                    ec2_instance,
                ],
              #  AdditionalInfo='string',
                DryRun=False
            )
        except Exception as ex:
            err = "Exception occurred on starting Ec2 due to {}".format(ex)
            print(err)
            send_notification_to_ms_teams(err)
        print('Started Ec2: ' + str(response))
    # Sending notification to Microsoft Team
    send_notification_to_ms_teams("Start Ec2 response {}".format(response))


# -----------------------STOP SERVICE-------------------------------#
# Run at 1:30pm (UTC) (i.e 07:00pm [IST]) every Monday through Friday.
# @app.schedule(Cron(30, 13, '?', '*', 'MON-FRI', '*'))
# def stop_lambda(event):
#     print("Stopping cluster")
#     try:
#         response = rds.stop_db_cluster(DBClusterIdentifier=os.environ.get("DBClusterIdentifier"))
#     except Exception as ex:
#         err = "Exception occurred on stopping neptune due to {}".format(ex)
#         print(err)
#         send_notification_to_ms_teams(err)
#     print('Stopped your cluster: ' + str(response))
#     # Sending notification to Microsoft Team
#     send_notification_to_ms_teams("Stop cluster response {}".format(response))

# Run at 1:30pm (UTC) (i.e 07:00pm [IST]) every Monday through Friday.
@app.schedule(Cron(30, 16, '?', '*', 'MON-FRI', '*'))
def stop_ec2(event):
    print("Stopping Ec2")
    ec2_instances = os.environ.get("ec2").split(",")
    for ec2_instance in ec2_instances:
        try:
            response = ec2.stop_instances(
                InstanceIds=[
                    ec2_instance,
                ],
                Hibernate=False,
              #  AdditionalInfo='string',
                DryRun=False
            )
        except Exception as ex:
            err = "Exception occurred on stopping Ec2 due to {}".format(ex)
            print(err)
            send_notification_to_ms_teams(err)
        print('Stoped Ec2: ' + str(response))
    # Sending notification to Microsoft Team
    send_notification_to_ms_teams("Stop Ec2 response {}".format(response))

# @app.schedule(Cron(30, 17, '?', '*', 'MON-FRI', '*'))
# def stop_neptune_at_11_pm(event):
#     stop_lambda(event)


# Sending notification to Microsoft Team
def send_notification_to_ms_teams(message):
    message += "<----->\n Posted using repo  -----> https://github.com/m-thirumal/aws-service-start-stop-scheduler"
    print("Sending message {} to MS Teams".format(message))
    ms_teams_message = pymsteams.connectorcard(os.environ.get('msTeamChannelIncomingWebhook'))
    ms_teams_message.text(message)
    ms_teams_message.send()
