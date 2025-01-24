# test_bionet.py

import os
import unittest
import BioNet as bionet
from unittest.mock import patch, Mock


class TestBioNet(unittest.TestCase):

    def setUp(self):
        self.service_provider_standalone_url = "https://localhost:8081/api"
        self.service_provider_catalog_url = os.getenv('BioNetServiceProviderCatalogURL', "http://localhost:81")
        print(f"Service Provider Catalog URL: {self.service_provider_catalog_url}")
        print(f"Service Provider Standalone URL: {self.service_provider_standalone_url}")

        service_provider_data = {
            "id": "532508cc-ddb4-40ef-82d6-c3c81879c862",
            "name": "Brent Zboncak",
            "email": "FAkeZboncak@gmail.com",
            "organization": "Magnesium and Sons Laboratories",
            "api_url": "https://localhost/api",
            "operations": [
                {"operation": "MakeDNA", "version": "1.0.0"},
                {"operation": "DefineConcept", "version": "1.0.0"}
            ]
        }
        self.service_provider = bionet.models.ServiceProvider.from_dict(service_provider_data)

        # Create a OperationsLibrary object  with the required data
        self.operation_data = {
                "id": "unique",
                "name": "MakeDNAScore",
                "version": "1.0",
                "creationUTC": "2023-10-03T14:48:00Z",
                "inputs": {
                    "sequence": "AGTC",
                    "sequenceName": "sequence Name",
                    "quantity": "30mg",
                    "vector": {
                        "name": "name of vector",
                        "catalogId": "Vendor Catalog id"
                    },
                    "glycerolStock": "true",
                    "payment": "payment object",
                    "shipping": "shipping object",
                    "deliveryFormat": "tube"
                },
                "outputs": {
                    "shippingManifest": "document",
                    "deliveredProduct": "dna"
                }
            }
        self.command = "MakeDNAScore"

    def test_send_bionet_data_success(self):
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}

        with patch('BioNet.bionet.requests.post') as mock_post:
            mock_post.return_value = mock_response
            
            # Act
            response = bionet.send_bionet_data(self.command,self.operation_data, self.service_provider)

            print("response",response.content)
            # Assert
            #mock_post.assert_called_once_with(self.service_provider_standalone_url, json={'data': {"key": "value"}})
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"success": True})


if __name__ == '__main__':
    unittest.main()