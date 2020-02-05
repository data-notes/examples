import os

# import sys
import importlib
from fastapi import FastAPI, APIRouter
from pydantic import Field, BaseModel
from glob import glob


class Params(BaseModel):
    args: dict = Field({})


app = FastAPI()
router = APIRouter()

data = {}
for file in glob("/main/notebooks/rest/*py"):
    name = os.path.basename(file.replace(".py", ""))
    pkg = importlib.import_module(f"notebooks.rest.{name}")

    for x in dir(pkg):
        if x.startswith("_"):
            continue
        element = getattr(pkg, x)
        if not callable(element):
            continue
    data[name] = element

# FUNC_TEMPLATE = """def wrapper_{0}(params: Params): return func(**params.args)"""
# thismodule = sys.modules[__name__]

for name, func in data.items():

    print(name, func)
    # exec(FUNC_TEMPLATE.format(name))

    def wrapper(params: Params):
        try:
            return func(**params.args)
        except Exception as e:
            return {"failure": str(e)}

    wrapper.__name__ = name
    router.post(f"/{name}")(wrapper)
    # router.post(f"/{name}")(getattr(thismodule, f"wrapper_{name}"))

app.include_router(router, prefix="/functions")


@app.get("/")
async def root():
    return {"message": "Hello World"}
