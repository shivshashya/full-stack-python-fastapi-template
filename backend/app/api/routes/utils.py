
# --- POC Test Endpoint for CodeRabbit Review ---
import time

@router.get("/poc/report")
async def generate_user_report(user_id: int, api_secret: str = "SUPER_SECRET_POC_KEY_12345"):
    """
    POC endpoint to test CodeRabbit reviews
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
