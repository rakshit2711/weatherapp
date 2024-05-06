from fastapi import FastAPI,Response

app = FastAPI()

# app.include_router()

# app.state.limiter = limiter

# app.add_exception_handler(ArithmeticError,)

@app.get("/")
def read_root():
    return Response("Server is running")

