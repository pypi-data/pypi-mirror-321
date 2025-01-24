import logging


class GetContainerIpError(Exception):
  def __init__(self, message, traceback=None):
    super().__init__(message)
    self.traceback = traceback


def __validate_input(container_name: str, network_name: str, verbose: bool, raise_exc: bool):
  if not container_name or container_name.strip() == '':
    raise ValueError("Container name must be defined")
  if not isinstance(container_name, str):
    raise ValueError("Container name must be a string")
  if network_name and not isinstance(network_name, str):
    raise ValueError("Network name must be a string")
  if verbose is None or not isinstance(verbose, bool):
    raise ValueError("Verbose must be a boolean")
  if raise_exc is None or not isinstance(raise_exc, bool):
    raise ValueError("Raise exception must be a boolean")


def __docker_inspect(container_name:str, verbose: bool)->dict:
  import subprocess
  import json
  try:
    # Execute the command
  
    result = subprocess.run(
        ["docker", "inspect", container_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
        text=True
      )
      
      # Parse the JSON output
    container_info = json.loads(result.stdout)
    return container_info
  except subprocess.CalledProcessError as e:
    if verbose:
      logging.error(f"Error executing command: {e.stderr}")
    raise
  except (IndexError, KeyError, GetContainerIpError) as e:
    if verbose:
      logging.error(f"Error parsing container information: {e}")
    raise
  except (Exception) as e:
    if verbose:
      logging.error(f"Unknown error occurred: {e}")
    raise


def __extract_ip_address(container_info: dict, container_name: str, network_name: str, verbose: bool) -> str:
    try:
      # Extract the IP address
      if network_name:
        ip_address = container_info[0]['NetworkSettings']['Networks'][network_name]['IPAddress']
      else:
        ip_address = container_info[0]['NetworkSettings']['IPAddress']
      return ip_address
    except (IndexError, KeyError) as e:
      if verbose:
        logging.error(f"Error extracting IP address from container information: {e}")
      if network_name:
        raise GetContainerIpError(f"Error retrieving IP address for container {container_name} and network '{network_name}'", traceback=e)
      raise GetContainerIpError(f"Error retrieving IP address for container {container_name}", traceback=e)
  

def get_container_ip(container_name: str, network_name: str = None, raise_exc: bool = False, verbose: bool = False) -> str|None:
  try:
    __validate_input(container_name=container_name, network_name=network_name, verbose=verbose, raise_exc=raise_exc)

    container_info  = __docker_inspect(container_name=container_name, verbose=verbose)
    ip_address      = __extract_ip_address(container_info=container_info, container_name=container_name, network_name=network_name, verbose=verbose)
    
    return ip_address
  except Exception:
    if raise_exc:
      raise
    else:
      return None

