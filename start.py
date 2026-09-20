import os
import uvicorn
import traceback

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    try:
        uvicorn.run("app.main:app", host="0.0.0.0", port=port)
    except Exception as e:
        print("CRITICAL STARTUP ERROR:")
        traceback.print_exc()
        raise e