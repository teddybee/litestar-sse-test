

def start():
    import uvicorn

    # run with api
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True, workers=2)
    # uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start()
