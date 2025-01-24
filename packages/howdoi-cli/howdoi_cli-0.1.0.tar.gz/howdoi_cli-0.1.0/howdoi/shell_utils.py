import os

def detect_shell():
    shell_path = os.environ.get('SHELL', '')
    shell_name = os.path.basename(shell_path)
    return shell_name or 'bash'  # default to bash if detection fails
