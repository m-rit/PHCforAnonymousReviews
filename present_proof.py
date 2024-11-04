async def present_proof(client: AcaPyClient, proof_request_id):
    # Respond to proof request
    proof_response = await client.present_proof.send_presentation(
        {
            "presentation_exchange_id": proof_request_id,
            "requested_attributes": {
                "attr1_referent": {
                    "cred_id": "<USER_CRED_ID>",
                    "revealed": True
                }
            },
            "requested_predicates": {}
        }
    )
    return proof_response
