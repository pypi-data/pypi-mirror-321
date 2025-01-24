# BioNet/bionet.py

import os
import requests
import logging
from .logging_config import setup_logging
from .models import *
from dotenv import load_dotenv
from .plugin_manager import PluginManager
from .plugin_interface import PluginInterface

# Setup logging
setup_logging()

# Load environment variables from .env file
load_dotenv()  # By default, this does not override existing environment variables

def getVersion():
    return "0.0.1"

def get_environment_variables():
    """
    Retrieves environment variables for BioNet Service Provider Catalog URL and Operations Library URL.
    Sets using defaults if not found in environment.
    """
    service_provider_catalog_url = os.getenv('BioNetServiceProviderCatalogURL')
    operations_library_url = os.getenv('BioNetOperationsLibraryURL')

    if service_provider_catalog_url:
        logging.info(f"BioNet Service Provider Catalog URL: {service_provider_catalog_url}")
    else:
        logging.warning("BioNetServiceProviderCatalogURL environment variable is not set. Setting to default value.")
        service_provider_catalog_url = "http://localhost:81"

    if operations_library_url:
        logging.info(f"BioNet Operations Library URL: {operations_library_url}")
    else:
        logging.warning("BioNetOperationsLibraryURL environment variable is not set. Setting to default value.")
        operations_library_url = "http://localhost:82"

    return service_provider_catalog_url, operations_library_url

service_provider_catalog_url, operations_library_url = get_environment_variables()

def send_bionet_data(command: str, bionet_payload: object, service_provider: ServiceProvider):
    """
    Sends a POST request with the BioNet data to the specified service provider's API URL.

    :param bionet_payload: PayloadData  object containing the data to be sent.
    :param service_provider: ServiceProvider object containing the API URL.
    :return: Response object from the POST request.
    """
      
    try:
        # Prepare the data payload for the POST request
        payload = PayloadData(bionet_payload)
        sender_info = BioNetSenderInfo(service_provider.name,service_provider.id)
        bionet_model = BioNetMessage(
            bionet_sender_info= sender_info,
            bionet_payload = BioNetPayload(command,payload)
        )
        data = bionet_model.to_dict()
        logging.info(f"Sending POST request to {service_provider.api_url} with payload: {data}")

        # Make the POST request
        response = requests.post(service_provider.api_url, json=data)

        # Check if the request was successful
        response.raise_for_status()
        logging.info(f"Received successful response: {response.status_code}")

        return response

    except requests.exceptions.RequestException as e:
        logging.error(f"send_bionet_data An error occurred: {e}")
        return e

def service_provider_catalog_get_providers(filter:dict = None):
    """
    Makes a GET request to the Service Provider Catalog URL specified by the BioNetServiceProviderCatalogURL environment variable.

    :return: Array of ServiceProvider from the GET request, or None if the request fails or the URL is not set.
    """
    logging.info(f"Filter: {filter}")

    if not service_provider_catalog_url:
        logging.warning("BioNetServiceProviderCatalogURL environment variable is not set.")
        return None
    
    #adjust the url based on the filter
    url = service_provider_catalog_url + "/api/provider"
    if filter:
        if hasattr(filter,'operation_name'):
            url += "/op/"+filter.operation_name

    arr = sendHTTPGet(url).json()

    objects = []
    for data in arr:
        obj = ServiceProvider.from_dict(data)
        objects.append(obj)
    return objects
    
def service_provider_catalog_get_providers_by_operation(operation_name : str):
    return service_provider_catalog_get_providers(filter={"operation_name":operation_name})


# HELPER Functions
def sendHTTPGet(url:str):
    try:
        logging.info(f"Making GET request to URL: {url}")
        # Make the GET request
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
        logging.info(f"Received successful response from url: {url} status_code: {response.status_code}")
        return response

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while fetching : {e}")
        return None