import asyncio
from aries_cloudagent.admin.client import AcaPyClient

async def setup_issuer():
    client = AcaPyClient("http://localhost:8021")  # ACA-Py agent URL

    # Define Schema
    schema = await client.schema.create_schema({
        "schema_name": "PersonhoodCredential",
        "schema_version": "1.0",
        "attributes": ["pseudonym", "verification_timestamp"]
    })

    # Create Credential Definition
    cred_def = await client.credential_definition.create_credential_definition({
        "schema_id": schema.schema_id,
        "support_revocation": False
    })

    return cred_def.credential_definition_id
