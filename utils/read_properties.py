def get_config(key):
    with open("config/config.properties", "r") as f:
        props = dict(line.strip().split('=') for line in f if line.strip() and not line.startswith('#'))
    return props.get(key)
