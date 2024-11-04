async def verify_proof(client: AcaPyClient, presentation_exchange_id):
    result = await client.present_proof.verify_presentation(
        {
            "presentation_exchange_id": presentation_exchange_id
        }
    )
    if result.verified:
        print("Proof verified. User is eligible to submit an anonymous review.")
    else:
        print("Verification failed.")
