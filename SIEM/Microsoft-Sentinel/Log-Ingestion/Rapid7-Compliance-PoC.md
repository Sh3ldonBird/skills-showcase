# Thought behind it
- The idea is to create a segregated Azure workspace in which compliance scans for PCI DSS are ingested into Microsoft Sentinel to then be viewed and sifted through.  
- An Azure function app is created to with the proper requirements to house the python scripting to pull the logs into the Microsoft Sentinel Data Connector.  
- Secure coding practices are in place because of the use of Azure Key Vault. No secrets are visible in the repository.  

To secure this further, adding in managed identities, VNet Integrations, making the function app a Private Endpoints, only accept Rapid7's IP addresses, signed HTTP requests, including a WAF in the same vNET in front of the Function App.
# Terraform Code
Main.tf
```HCL
terraform {
  required_version = ">=1.0.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~>3.1"
    }
  }
}

provider "azurerm" {
  features {}
  # Assumes you've set your subscription via `az account set --subscription "subscription needed"`
  # or environment variables for ARM_SUBSCRIPTION_ID.
}

variable "location" {
  type    = string
  default = "West US"
}

variable "resource_group_name" {
  type    = string
  default = "PCI-Compliance"
}

variable "workspace_name" {
  type    = string
  default = "Sentinel-PCI"
}

# Name of the pre-existing Key Vault that holds all secrets needed to pass the     # correct variables to each function.
variable "key_vault_name" {
  type    = string
  default = "pci-compliance-kv"
}

# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

# Log Analytics Workspace
resource "azurerm_log_analytics_workspace" "law" {
  name                = var.workspace_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

# Application Insights linked to Workspace
resource "azurerm_application_insights" "app_insights" {
  name                = "${var.workspace_name}-ai"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  application_type    = "web"
  workspace_id        = azurerm_log_analytics_workspace.law.id
  ingestion_mode      = "ApplicationInsights"
}

# Storage Account for Function App
resource "random_string" "suffix" {
  length  = 5
  special = false
  upper   = false
}

resource "azurerm_storage_account" "sa" {
  name                     = "pcicompliancesa${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"  # Best option?
  account_replication_type = "LRS"       # More redundancy needed?
}

# Consumption Plan for Function App
resource "azurerm_service_plan" "service_plan" {
  name                = "rapid7-pci-func-plan"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "Y1"  # Consumption tier, pay for execution time only
  reserved            = true
}

# Reference existing Key Vault
data "azurerm_key_vault" "existing_kv" {
  name                = var.key_vault_name
  resource_group_name = var.resource_group_name
}

# Retrieve Secrets from Key Vault
data "azurerm_key_vault_secret" "r7_api_key" {
  name         = "R7-ApiKey"
  key_vault_id = data.azurerm_key_vault.existing_kv.id
}

data "azurerm_key_vault_secret" "r7_base_url" {
  name         = "R7-BaseUrl"
  key_vault_id = data.azurerm_key_vault.existing_kv.id
}

data "azurerm_key_vault_secret" "workspace_id" {
  name         = "Log-Analytics-Workspace-Id"
  key_vault_id = data.azurerm_key_vault.existing_kv.id
}

data "azurerm_key_vault_secret" "workspace_key" {
  name         = "Log-Analytics-Primary-Key"
  key_vault_id = data.azurerm_key_vault.existing_kv.id
}

# Function App
resource "azurerm_linux_function_app" "function_app" {
  name                       = "rapid7-pci-compliance-func-app"
  resource_group_name         = azurerm_resource_group.rg.name
  location                   = azurerm_resource_group.rg.location
  service_plan_id            = azurerm_service_plan.service_plan.id
  storage_account_name       = azurerm_storage_account.sa.name
  storage_account_access_key = azurerm_storage_account.sa.primary_access_key
  functions_extension_version = "~4"

  site_config {
    application_stack {
      python_version = "3.9"
    }
  }

  # Provide Key Vault-based secrets as environment variables
  app_settings = {
    "APPLICATIONINSIGHTS_CONNECTION_STRING" = azurerm_application_insights.app_insights.connection_string
    "KEY_VAULT_NAME"                         = var.key_vault_name
  }

  identity {
    type = "SystemAssigned"
  }
}

# Grant Function App access to Key Vault secrets
data "azurerm_client_config" "current" {}

resource "azurerm_key_vault_access_policy" "function_kv_access" {
  key_vault_id = data.azurerm_key_vault.existing_kv.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = azurerm_linux_function_app.function_app.identity.principal_id

  secret_permissions = [
    "get", "list"
  ]
}
```

# Python Code
Data structure
```
function_app/
  timer_trigger/
    __init__.py
    function.json
  requirements.txt
```

Function.json (Timer Trigger every 30 days for monthly scans)
```
{
  "bindings": [
    {
      "name": "mytimer",
      "type": "timerTrigger",
      "direction": "in",
      "schedule": "0 0 0 */30 * *"
    }
  ]
}
```
requirements.txt
```txt
requests
azure-identity
azure-keyvault-secrets
```

init.py
```Python
import os
import json
import datetime
import hmac
import hashlib
import base64
import logging
import requests
import azure.functions as func

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def main(mytimer: func.TimerRequest) -> None:
    # Fetch secrets from Key Vault
    r7_api_key, r7_base_url, workspace_id, shared_key = get_secrets_from_key_vault()

    # Fetch PCI DSS compliance data from Rapid7 InsightVM
    compliance_data = fetch_pci_dss_data(r7_base_url, r7_api_key)

    if compliance_data:
        # Send data to Microsoft Sentinel (Log Analytics)
        send_to_sentinel(workspace_id, shared_key, compliance_data)
    else:
        logging.warning("No PCI DSS data retrieved.")

def get_secrets_from_key_vault():
    key_vault_name = os.environ["KEY_VAULT_NAME"]
    vault_uri = f"https://{key_vault_name}.vault.azure.net"

    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=vault_uri, credential=credential)

    r7_api_key_secret = secret_client.get_secret("R7-ApiKey")
    r7_base_url_secret = secret_client.get_secret("R7-BaseUrl")
    workspace_id_secret = secret_client.get_secret("Log-Analytics-Workspace-Id")
    primary_key_secret = secret_client.get_secret("Log-Analytics-Primary-Key")

    return (
        r7_api_key_secret.value,
        r7_base_url_secret.value,
        workspace_id_secret.value,
        primary_key_secret.value
    )

def fetch_pci_dss_data(base_url, api_key):
    # Example endpoint: adjust based on Rapid7 API docs
    endpoint = f"{base_url}/api/3/compliances?standard=pci-dss"
    headers = {
        "Authorization": f"APIKey {api_key}",
        "Accept": "application/json"
    }

    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Failed to fetch PCI DSS data: {response.status_code} {response.text}")
        return None

def send_to_sentinel(workspace_id, shared_key, data):
    body = json.dumps(data)
    rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    string_to_hash = f"POST\n{len(body)}\napplication/json\nx-ms-date:{rfc1123date}\n/api/logs"
    signature = build_signature(shared_key, string_to_hash)

    uri = f"https://{workspace_id}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"SharedKey {workspace_id}:{signature}",
        "Log-Type": "Rapid7PCIDSSCompliance_CL",
        "x-ms-date": rfc1123date
    }

    response = requests.post(uri, data=body, headers=headers)
    if response.status_code in (200, 202):
        logging.info("Data successfully sent to Sentinel.")
    else:
        logging.error(f"Failed to send data to Sentinel: {response.status_code} {response.text}")

def build_signature(shared_key, message):
    decoded_key = base64.b64decode(shared_key)
    encoded_message = message.encode('utf-8')
    digester = hmac.new(decoded_key, encoded_message, hashlib.sha256).digest()
    return base64.b64encode(digester).decode('utf-8')
```

# To Run
## Initialize and Apply Terraform:
   
    ```bash
    terraform init
    terraform plan
    terraform apply
    ```
    
Confirm with "yes" when prompted.
    
## Deploy Function Code: Zip the function code:
    
```bash
cd function_app
zip -r ../function_package.zip .
cd ..
```
    
Deploy the code to the function app:
    
```bash
az functionapp deployment source config-zip \
   -g PCI-Compliance \
   -n rapid7-pci-compliance-func-app \
   --src function_package.zip
```
    
## Validate:
- Check the Function App logs in Azure Portal.
- Query data in Sentinel (Log Analytics workspace):
       
```kusto
Rapid7PCIDSSCompliance_CL
| sort by TimeGenerated desc
```
        
