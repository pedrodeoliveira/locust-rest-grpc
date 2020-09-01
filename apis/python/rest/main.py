from fastapi import FastAPI
import logging
import os
import uvicorn

from apis.python.common import categorize_text, generate_random_id
from apis.python.rest.models import TextCategorizationInput, TextCategorizationOutput


log_level = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(format='%(levelname)s:%(message)s', level=getattr(logging, log_level))
log = logging.getLogger(__name__)

# instantiate FastAPI
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    log.info(f'Starting FastAPI ...')


@app.post("/predict", response_model=TextCategorizationOutput)
async def predict(body: TextCategorizationInput):
    log.debug(f'Receive the following text to categorize: {body.text}')
    category = categorize_text(body.text)
    prediction_id = generate_random_id()
    log.debug(f'Predicted category: {category}')
    response = TextCategorizationOutput(prediction_id=prediction_id, text=body.text,
                                        category=category)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
