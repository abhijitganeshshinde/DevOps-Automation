import boto3

ec2 = boto3.resource('ec2')

instance_params = {
    'ImageId': 'ami-0f5ee92e2d63afc18',  
    'InstanceType': 't2.micro',
    'KeyName': 'boto3_G4', 
    'MinCount': 1,
    'MaxCount': 1,
   'TagSpecifications': [
       {
           'ResourceType': 'instance',
           'Tags': [
               {
                   'Key': 'Name',
                   'Value': 'backendusingboto3_G4'
               },
              
           ]
       },
   ],
}


# Create a new EC2 instance
instances = ec2.create_instances(**instance_params)
instance = instances[0]
instance.wait_until_running()
print(f"Instance ID: {instance.id}")
print(f"Instance Name: {instance.tags[0]['Value']}")
print(f"Public IP Address: {instance.public_ip_address}")