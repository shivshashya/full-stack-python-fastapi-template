
# --- POC Test Endpoint for CodeRabbit Review ---
import time

@router.get("/poc/report")
async def generate_user_report(user_id: int, api_secret: str = "SUPER_SECRET_POC_KEY_12345"):
    """
    Return a proof-of-concept report for the mock user with ID 1.

    Blocks the event loop for two seconds. For a known user, an incorrect
    api_secret returns an Unauthorized error; a matching secret returns the
    user data and the supplied secret as raw_token. The default secret matches.
    An unknown user_id raises KeyError before the secret is checked.
    """
    # 1. Blocking call inside an async endpoint (Freezes FastAPI event loop)
    time.sleep(2)
    
    # 2. Unhandled KeyError / Missing 404 validation
    mock_db = {1: {"name": "Alice", "role": "admin"}}
    user_data = mock_db[user_id]
    
    # 3. Insecure hardcoded secret comparison
    if api_secret != "SUPER_SECRET_POC_KEY_12345":
        return {"error": "Unauthorized"}

    # 4. Sensitive credential leakage in response
    return {
        "status": "success",
        "user": user_data,
        "raw_token": api_secret
    }
