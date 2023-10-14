import boto3
import os
from fabric import Connection

ec2 = boto3.resource('ec2')
instance_id = 'i-098a073c61dc1edc2'

instance = ec2.Instance(instance_id)
public_ip = instance.public_ip_address
key_name = 'boto3_G4'  

current_directory = os.getcwd()
private_key_file_name = 'boto3_G4.pem'
private_key_path = os.path.join(current_directory, private_key_file_name)
localscript_path =   os.path.join(current_directory,'backend_script.sh')
script_filename = '/backend_script.sh'
remote_script = '/home/ubuntu/backend_script.sh'
# Replace with your server's SSH details
host = public_ip
user = 'ubuntu'
key_filename = private_key_path


nginx_config = f"""
server {{
  listen 80;
  listen [::]:80;
  server_name {public_ip} api.abhijit.live;

  location / {{
    proxy_pass http://localhost:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
  }}
}}
"""

systemd_unit = """
[Unit]
Description=TravelMemory Application
After=network.target

[Service]
ExecStart=/usr/bin/node /home/ubuntu/TravelMemory/backend/index.js
WorkingDirectory=/home/ubuntu/TravelMemory/backend/
Restart=always
User=ubuntu
Group=ubuntu
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
"""

# Define a function to run remote commands
def run_remote_commands():
    with Connection(
        host=host,
        user=user,
        connect_kwargs={"key_filename": key_filename}
    ) as c:
        # c.put(localscript_path, remote_script)
        # commands = [
        #     f'chmod +x {remote_script}',
        #     f'.{script_filename}'
        # ]
        
       # List of commands to execute on the remote server
        commands = [
           # 'sudo apt-get update -y',
           # 'curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -',
           # 'sudo apt-get install -y nodejs',
           # 'sudo apt-get install -y nginx',
           # 'git clone https://github.com/abhijitganeshshinde/TravelMemory.git',
           # 'cd TravelMemory/backend/ && touch .env && echo "MONGO_URI=\'mongodb+srv://abhi:bi39msm5Vo8G6gyZ@cluster0.bta0sbt.mongodb.net/travelmemory\'" > .env',
           # 'echo "PORT=3000" >> TravelMemory/backend/.env'
            # 'cd TravelMemory/backend/ && npm install',
            # f'echo -e "{nginx_config}" | sudo tee /etc/nginx/sites-available/travelmemory',
            # 'sudo ln -s /etc/nginx/sites-available/travelmemory /etc/nginx/sites-enabled/',
            # 'sudo nginx -t',
            #'sudo systemctl reload nginx'
            #f'echo \'{systemd_unit}\' | sudo tee /etc/systemd/system/travelmemory.service',
            #'cd /etc/systemd/system/ && sudo systemctl enable travelmemory.service',
            #'cd /etc/systemd/system/ && sudo systemctl start travelmemory.service',
            #'sudo systemctl restart nginx'
        ]

       

        for command in commands:
            result = c.run(command, hide=True)
            print(f"Command Output for '{command}':")
            print(result.stdout)

if __name__ == "__main__":
    run_remote_commands()
