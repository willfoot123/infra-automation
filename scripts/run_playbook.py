import subprocess
import os

playbook = "playbooks/install_docker.yml"
inventory = "inventory/dev_hosts.ini"

playbooks = ["install_docker.yml", "configure_nginx.yml"]  
env_mapping = {"dev": "inventory/dev_hosts.ini"}  

def validate_paths(playbook_path, inventory_path):
    """Checks if playbook and inventory files exist."""
    if not os.path.exists(playbook_path) or not os.path.exists(inventory_path):
        raise FileNotFoundError("Playbook or inventory file not found.")

def run_playbook(playbook_path, inventory_path):
    """Runs an Ansible playbook and prints output."""
    command = ["ansible-playbook", "-i", inventory_path, playbook_path]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print(" Error running playbook!")
    else:
        print(" Playbook executed successfully!")
        print(result.stdout)  
    return result.returncode

if __name__ == "__main__":
    validate_paths(playbook, inventory)

    for pb in sorted(playbooks):  
        run_playbook(f"playbooks/{pb}", inventory)
