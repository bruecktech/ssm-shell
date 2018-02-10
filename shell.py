#!/usr/bin/env python3
import sys
import time
import boto3

ssm = boto3.client('ssm')

if len(sys.argv) < 2:
    print('Usage: ./shell.py i-01234567890')
    sys.exit('You need to provide an instance ID')

instance_id = sys.argv[1]

def ssm_command(command, instance_id):
    params = {'commands': [command]}
    response = ssm.send_command(InstanceIds=[instance_id], DocumentName='AWS-RunShellScript', Parameters=params)
    command_id = response['Command']['CommandId']

    invocation_status = 'InProgress'
    while invocation_status == 'InProgress':
        try:
            time.sleep(1)
            invocation = ssm.get_command_invocation(CommandId=command_id, InstanceId=instance_id)
            invocation_status = invocation['Status']
        except ssm.exceptions.InvocationDoesNotExist as e:
            pass

    return invocation

#ssm_command('yum -y install tmux', instance_id)
#ssm_command('tmux new-session -d -s rbt123', instance_id)

while True:
    command = input('> ')

    #invocation = ssm_command('tmux send-keys -t rbt123 "' + command + '" C-m; tmux show-buffer', instance_id)
    invocation = ssm_command(command, instance_id)

    if invocation.get('StandardOutputContent', '') != '':
        print(invocation.get('StandardOutputContent'))
    if invocation.get('StandardErrorContent', '') != '':
        print(invocation.get('StandardErrorContent'))

