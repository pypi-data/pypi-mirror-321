import uvicorn

from sandbox_func.web import sandbox_app


if __name__ == '__main__':
    uvicorn.run(sandbox_app.app, host="0.0.0.0", port=9000, log_level="info")
