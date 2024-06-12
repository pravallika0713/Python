import boto3

ec2 = boto3.client('ec2')
# describe instances 
instance_response = ec2.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}])
# store instance ids
instance_ids=[]

for Reservations in instance_response['Reservations']:
    for instance in Reservations['Instances']:
        instance_ids.append(instance['InstanceId'])

# describe snapshots
response = ec2.describe_snapshots(OwnerIds=['self'])
# check if volume id is attached to snapshot and that volume is attached to instance
# if volume is not attached to instance delete snapshot
for snapshot in response['Snapshots']:
    snapshot_id = snapshot['SnapshotId']
    volume_id = snapshot.get('VolumeId')
    if not volume_id:
        ec2.deletesnapshot(SnapshotID=snapshot_id)
        print(f"Deleted snapshot:{snapshot_id} as it was not attached to any volume")

    else:
        try:
            volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
            if not volume_response['Volumes'][0]['Attachments']:
                 ec2.delete_snapshot(SnapshotId=snapshot_id)
                 print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
        except ec2.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
        
    



