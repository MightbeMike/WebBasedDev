import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def test_ip_connectivity(ip, port):
    try:
        # I use curl command
        subprocess.run(['curl', '-I', f'--connect-timeout', '5', f'{ip}:{port}'], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def read_ips_from_files(directory):
    ips = []
    try:
        # files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                file_path = os.path.join(directory, filename)
                # aaaannnnndddd we read IP addresses from the file
                with open(file_path, 'r') as file:
                    ip_addresses = file.readlines()
                    
                    ips.extend([ip.strip() for ip in ip_addresses])
        return ips
    except FileNotFoundError:
        logging.error(f"Directory '{directory}' not found.")
        return []

def write_ips_to_file(working_ips, output_file):
    try:
        with open(output_file, 'w') as file:
            for ip in working_ips:
                file.write(ip + '\n')
        logging.info(f"Successfully wrote working IPs to '{output_file}'.")
    except IOError:
        logging.error(f"Failed to write working IPs to '{output_file}'.")

# place your full absolute path to the directory containing the text files with IP`s`
directory = '/home/user/Downloads/ips'

# Provide the path for the output file. YOU WILL HAVE TO CREATE THE TXT FILE HERE
output_file = '/home/user/Downloads/working_ips.txt'

# Call the function 
ips = read_ips_from_files(directory)

# Test the connectivity and hope we dont crash and burn
working_ips = []
for ip_port in ips:
    ip, port = ip_port.split(':')
    if test_ip_connectivity(ip, port):
        logging.info(f"IP {ip} on port {port} is reachable.")
        working_ips.append(ip_port)

# haza! it works. now to document the file
write_ips_to_file(working_ips, output_file)
