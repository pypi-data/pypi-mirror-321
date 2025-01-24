# FILE: get_container_ip/get_container_ip/__init__.py
# This file is intentionally left blank.

def app():
  import argparse
  from get_container_ip.get_ip import get_container_ip
  
  parser = argparse.ArgumentParser(description="Get the IP address of a Docker container.")
  parser.add_argument("container_name", type=str, help="Name of the Docker container")
  parser.add_argument("--network", type=str, default=None, help="Name of the Docker network", required=False)
  parser.add_argument("--raise-exc", action="store_true", help="Raise exception on error", default=False)
  parser.add_argument("--verbose", action="store_true", help="Enable verbose output", default=False)
  
  args = parser.parse_args()

  try:
    ip_address = get_container_ip(
      container_name=args.container_name,
      network_name=args.network,
      raise_exc=args.raise_exc,
      verbose=args.verbose
    )
    if ip_address:
      print(f"IP address of container '{args.container_name}': {ip_address}")
    else:
      print(f"Could not retrieve IP address for container '{args.container_name}'")
  except Exception as e:
    print(f"Error: {e}")