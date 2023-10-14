import boto3

# Create a Boto3 EC2 resource
ec2 = boto3.resource('ec2')

# Replace 'your-instance-id' with the ID of the instance you want to stop/start
#instance_id = 'i-0e42e0da8733f0c06'
instance_id ='i-0f8e266d3dd480f0f'

# Get the current state of the EC2 instance
instance = ec2.Instance(instance_id)

# Print the instance state before stopping
print(f"Instance ID: {instance_id}")

# Print the instance state after stopping
instance.load()  # Reload the instance information
print(f"Instance State after stopping: {instance.state['Name']}")

# Start the EC2 instance
ec2.instances.filter(InstanceIds=[instance_id]).start()

# Print the instance state after starting
instance.load()  # Reload the instance information
print(f"Instance State after starting: {instance.state['Name']}")