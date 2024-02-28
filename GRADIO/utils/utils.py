import yaml


def read_yaml_config(file_path):
    """
    Read a YAML file and return its content as a dictionary.

    Args:
    file_path (str): Path to the YAML file.

    Returns:
    dict: Dictionary containing the YAML file content.
    """
    try:
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            return config
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error reading YAML file: {e}")
        return None
