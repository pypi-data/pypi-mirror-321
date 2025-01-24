import os
import yaml
import logging
from dotenv import load_dotenv

load_dotenv()

config_path = os.getenv("CONFIG_PATH", "/etc/cloverai-config/cloverai-config.yaml")

# Load YAML configuration from file
config = {}
if os.path.exists(config_path):
    with open(config_path, "r") as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            logging.error(f"Failed to parse config file {config_path}: {e}")

# Fetch configuration values with fallback to environment variables and defaults
log_level = config.get("logLevel", os.getenv("logLevel", "info")).upper()
llm_azure = config.get("llmAzure", os.getenv("llmAzure", "False")).lower() == "true"

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(module)s.py %(message)s", handlers=[logging.FileHandler("chat_agent_cli.log")])
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
streamHandler.setFormatter(logging.Formatter("%(message)s"))
logging.getLogger().addHandler(streamHandler)

logging.info(f"Loaded Config: {config}")
logging.info(f"Log level set to: {log_level}, llmAzure enabled: {llm_azure}")

if llm_azure:
    model = config.get("llmAzureModel", os.getenv("llmAzureModel"))
    api_key = config.get("llmAzureApiKey", os.getenv("llmAzureApiKey"))
    api_version = config.get("llmAzureApiVersion", os.getenv("llmAzureApiVersion"))
    azure_endpoint = config.get("llmAzureEndpoint", os.getenv("llmAzureEndpoint"))
    data_limit = int(config.get("llmAzureDataLimit", os.getenv("llmAzureDataLimit")))
    
    logging.info(f"Model: {model}, API Key: {api_key}, API Version: {api_version}, Azure Endpoint: {azure_endpoint}, Data Limit: {data_limit}")

llm_system_prompt = config.get("llmSystemPrompt", os.getenv("llmSystemPrompt"))
trace_url = config.get("traceUrl", os.getenv("traceUrl"))
