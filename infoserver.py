import platform
import psutil
import socket

def get_server_info(server):
  # Get the server's hostname and IP address
  hostname, ip_address = socket.gethostbyname(server), socket.gethostbyname(server)

  # Get the server's port number
  port = 80

  # Get the operating system name and version
  os_name = platform.system()
  os_version = platform.version()

  # Get the CPU and memory usage
  cpu_usage = psutil.cpu_percent()
  memory_usage = psutil.virtual_memory().percent

  # Get the disk usage
  disk_usage = psutil.disk_usage('/').percent

  # Get the network usage
  network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

  return (f"Hostname: {hostname}\nIP address: {ip_address}\nPort: {port}\n"
          f"Operating system: {os_name} {os_version}\nCPU usage: {cpu_usage}%\n"
          f"Memory usage: {memory_usage}%\nDisk usage: {disk_usage}%\n"
          f"Network usage: {network_usage} bytes")

def main():
  # Get the server information
  server = "example.com"
  server_info = get_server_info(server)

  # Print the server information
  print(server_info)

if __name__ == '__main__':
  main()
