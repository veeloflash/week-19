ALLOWED_COMMANDS = ["run", "predict", "evaluate"]


def is_safe_input(command):
    if not isinstance(command, str):
        return False
    command = command.strip().lower()
    if command in ALLOWED_COMMANDS:
        return True
    if any(bad in command for bad in ["rm", "del", "shutdown", "format", "drop", "import os", "subprocess"]):
        return False
    return False
