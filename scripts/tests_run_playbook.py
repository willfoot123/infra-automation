# test_run_playbook.py
import subprocess
from scripts.run_playbook import run_playbook

def test_run_playbook_success(monkeypatch):
    def mock_run(*args, **kwargs):
        return subprocess.CompletedProcess(args, 0, stdout="Success", stderr="")
    monkeypatch.setattr(subprocess, "run", mock_run)
    result = run_playbook("playbooks/install_docker.yml", "inventory/dev_hosts.ini")
    assert result == 0
