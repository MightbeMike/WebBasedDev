I found myself in need of a way to check if a larg number of proxies had valid connections and which where dead. 

I decided this would be a great opportunbiity to create a script to check said connections. sense doign it manauly sounded like a nightmare. 

here is what this script does 
---------------------------------------------------------------------------------------------------------------------------------------------


   imports necessary modules: os for file operations, subprocess for running shell commands, and logging for logging messages.

   defines a function test_ip_connectivity(ip, port) that uses the curl command to test the connectivity of a given IP address and port. If the connection succeeds, it returns True; otherwise, it returns False.

defines a function read_ips_from_files(directory) that reads IP addresses and ports from text files in a specified directory. It then returns a list of IP address-port pairs.

    defines a function write_ips_to_file(working_ips, output_file) that writes the IP addresses that are reachable to a specified output file.

  sets up the directory containing the text files with IP addresses and the output file where the reachable IP addresses will be written.

 calls the read_ips_from_files function to retrieve the list of IP addresses and ports from the text files.

 iterates over each IP address-port pair, tests its connectivity using the test_ip_connectivity function, and logs whether it is reachable or not.

   an IP address-port pair is reachable, it adds it to a list of working IPs.

    Finally, it calls the write_ips_to_file function to write the list of working IPs to the specified output file.

-----------------------------------------------------------------------------------------------------------------------------------------------

please be sure you have the requirments for the imports 

