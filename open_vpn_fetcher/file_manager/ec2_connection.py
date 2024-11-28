# OpenVPNFetcher/ec2_connection.py
import os
import paramiko

def get_files_from_ec2():
    # Replace the values with your EC2 instance details
    ec2_host = 'ec2_host'
    ec2_username = 'ec2_username'
    pem_file_path = 'pem_file_path'

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ec2_host, username=ec2_username, key_filename=pem_file_path)
        sftp = ssh.open_sftp()

        # Replace this with the actual path on your EC2 instance
        remote_directory = '/opt/openvpn/clients/'
        files = sftp.listdir(remote_directory)
        print(files) # Add this line for debugging

        sftp.close()
        ssh.close()

        print("Files retrieved successfully:", files)  # Add this line for debugging
        return files
    except Exception as e:
        print(f"Error: {e}")
        return []
