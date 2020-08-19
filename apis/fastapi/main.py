from fastapi import FastAPI
import logging
import uvicorn

from apis.common import categorize_text, generate_random_id
from apis.fastapi.models import TextCategorizationInput, TextCategorizationOutput

# instantiate FastAPI
app = FastAPI()
log = logging.getLogger(__name__)


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
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    uvicorn.run(app, host="localhost", port=8000)
