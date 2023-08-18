from app.main import app


if __name__ == "__main__":
    # uvicorn.run(app="pasaj:app", host='127.0.0.1', port=8000, reload=False, workers=4)
    uvicorn.run(app="main_local:app", host='127.0.0.1', port=8000, reload=True)


