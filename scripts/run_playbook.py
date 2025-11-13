import subprocess

def run_playbook(playbook_path, inventory_path):
    command = ["ansible-playbook", "-i", inventory_path, playbook_path]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    return result.returncode

if __name__ == "__main__":
    playbook = "playbooks/install_docker.yml"
    inventory = "inventory/dev_hosts.ini"
    run_playbook(playbook, inventory)


