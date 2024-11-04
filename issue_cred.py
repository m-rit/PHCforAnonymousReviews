async def issue_credential(client: AcaPyClient, user_did, cred_def_id):
    credential_data = {
        "pseudonym": "user12345",  # A unique pseudonym to protect identity
        "verification_timestamp": str(int(time.time()))  # Issue timestamp
    }

    # Send Credential Offer
    offer = await client.issue_credential.send_offer(
        {
            "connection_id": user_did,
            "cred_def_id": cred_def_id,
            "credential_proposal": {
                "attributes": [
                    {"name": "pseudonym", "value": credential_data["pseudonym"]},
                    {"name": "verification_timestamp", "value": credential_data["verification_timestamp"]}
                ]
            }
        }
    )
    return offer
