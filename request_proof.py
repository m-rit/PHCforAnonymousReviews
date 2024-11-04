async def request_proof(client: AcaPyClient, user_did, cred_def_id):
    # Request proof of possession of the PHC without revealing full details
    proof_request = {
        "name": "Personhood Proof",
        "version": "1.0",
        "requested_attributes": {
            "attr1_referent": {
                "name": "pseudonym",
                "restrictions": [{"cred_def_id": cred_def_id}]
            }
        },
        "requested_predicates": {}
    }

    # Send proof request to the user
    proof = await client.present_proof.send_request(
        {
            "connection_id": user_did,
            "proof_request": proof_request
        }
    )
    return proof
