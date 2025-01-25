import requests

def get_server_url(IN_DEV_MODE=False, USE_BETA_URL=False):
    """
    Determine the appropriate server URL based on the mode.
    :param IN_DEV_MODE: Whether to use the development server
    :param USE_BETA_URL: Whether to use the beta environment
    :return: The appropriate server URL
    """
    try:
        if IN_DEV_MODE:
            config_url = "http://localhost:8080/api/login/getConfigModeAndVersionREST"
            print(f"Using dev mode, fetching config from {config_url}")
        else:
            if USE_BETA_URL:
                config_url = "https://beta-mlops.infoapps.apple.com/api/login/getConfigModeAndVersionREST"
                print(f"Using beta mode, fetching config from {config_url}")
            else:
                config_url = "https://mlops.infoapps.apple.com/api/login/getConfigModeAndVersionREST"
                print(f"Using prod mode, fetching config from {config_url}")

        response = requests.get(config_url)
        response.raise_for_status()  # Raises an error for bad status codes
        config_data = response.json()

        if config_data["configMode"] == "production":
            server_url = config_data["prodUrl"]
            if config_data["environment_mode"] != "kube":
                server_url = "http://localhost:8080"
        else:
            server_url = config_data["devUrl"]
            if config_data["environment_mode"] != "kube":
                server_url = "http://localhost:8080"

        print(f"Server URL determined: {server_url}")
        return server_url

    except requests.RequestException as e:
        print(f"Error retrieving server URL from config: {e}")
        return "https://mlops.infoapps.apple.com"  # Default fallback URL