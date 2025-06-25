from main import app  # Asegúrate de que "main" sea el nombre de tu archivo principal

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)