# BioNet/models.py
import json

class ServiceProvider:
    """ Represents a service provider with its details.
    Example usage:
    data = {
        "id": "532508cc-ddb4-40ef-82d6-c3c81879c862",
        "name": "Brent Zboncak",
        "email": "FAkeZboncak@gmail.com",
        "organization": "Magnesium and Sons Laboratories",
        "api_url": "API_URL",
        "operations": [
            {"operation": "MakeDNA", "version": "1.0.0"},
            {"operation": "DefineConcept", "version": "1.0.0"}
        ]
    }
    # Example usage:
    provider = ServiceProvider.from_dict(data)
    print(provider.name)  # Output: Brent Zboncak

    """
    def __init__(self, id: str, name: str, email: str, organization: str, api_url: str, operations: list):
        self.id = id
        self.name = name
        self.email = email
        self.organization = organization
        self.api_url = api_url
        self.operations = operations

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            organization=data["organization"],
            api_url=data["api_url"],
            operations=data["operations"]
        )

    def __str__(self):
        operations_str = ', '.join([f"{op['operation']} (v{op['version']})" for op in self.operations])
        return (f"ServiceProvider [ID: {self.id}, Name: {self.name}, Email: {self.email}, "
                f"Organization: {self.organization}, API URL: {self.api_url}, "
                f"Operations: {operations_str}]")
    
# class TokenInfo:
#     def __init__(self, token_api_username: str, token_api_key: str):
#         self.token_api_username = token_api_username
#         self.token_api_key = token_api_key

class BioNetSenderInfo:
    def __init__(self, name: str, id: str):  # , token_info: dict):
        self.name = name
        self.id = id
        # self.token_info = TokenInfo(**token_info)
    def __str__(self):
        return f"BioNetSenderInfo(Name: {self.name}, ID: {self.id})"
    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id
        }

class PayloadData:
    def __init__(self, obj: object):
        
        # Convert the object to a JSON string
        #jsonStr = json.dumps(obj)
        # Save the JSON string in the json field
        #self.json = jsonStr
        self.data = obj
    
    def __str__(self):
        return f"PayloadData({json.dumps(self.data)})"

    def to_dict(self):
        return self.data
        #return json.dumps(self.json)

class BioNetPayload:
    def __init__(self, command: str, payload_data: PayloadData):
        self.command = command
        self.payload_data = payload_data
    def __str__(self):
        return f"BioNetPayload(Command: {self.command}, PayloadData: {self.payload_data})"
    def to_dict(self):
        return {
            "command": self.command,
            "payloadData": self.payload_data.to_dict()
        }

class BioNetMessage:
    """
    Example:
    BioNetMessage
    {
    "schema": "http://json-schema.org/draft-07/schema#",
    "version" : "1.0.0",
    "bionetSenderInfo": {
        "name": "BioNetSenderInfo name",
        "id": "BioNetSenderInfo id",
        "tokenInfo": {
            "tokenAPIUsername": "tokenAPIUsername",
            "tokenAPIKey": "tokenAPIKey"
        }
    },
    "bionetPayload": {
        "command": "MakeDNAVector",
        "payloadData": "{}"
    }
    }
    """
    def __init__(self, bionet_sender_info: BioNetSenderInfo, bionet_payload: BioNetPayload):
        self.bionet_sender_info = bionet_sender_info
        self.bionet_payload = bionet_payload
    
    def __str__(self):
        return (f"BioNetMessage(\n"
                f"  SenderInfo: {self.bionet_sender_info},\n"
                f"  Payload: {self.bionet_payload}\n"
                f")")
    def to_dict(self):
        return {
            "bionetSenderInfo": self.bionet_sender_info.to_dict(),
            "bionetPayload": self.bionet_payload.to_dict()
        }