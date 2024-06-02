from fastapi import FastAPI, File, UploadFile, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import numpy as np
import io

from utils import transform_image, file_to_base64, load_label_encoder
from model_manage import start_model

from db_utils import find_nearest_neighbors

app = FastAPI()

security = HTTPBearer()

TOKEN = "d391a9b3ef4e483880986aae70e164f2"

model = start_model("model.h5")
neighbor_model = start_model("neighbor_model.h5")
label_encoder = load_label_encoder("label_encoder.pickle")

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.post("/predict/")
async def predict(
    credentials: HTTPAuthorizationCredentials = Depends(verify_token),
    image: UploadFile = File(...),
):
    image_data = await image.read()
    image_file = io.BytesIO(image_data)
    img_array = transform_image(image_file)

    # Make a prediction
    prediction = model.predict(img_array)

    # Process the prediction result as needed
    predicted_encoded_label = np.argmax(prediction, axis=1)
    predicted_proba = np.round(np.max(prediction), 2)
    predicted_label = label_encoder.inverse_transform(predicted_encoded_label)[0]
    rounded_proba = round(float(predicted_proba), 2)

    # Get embedding from neighbor model
    neighbor_embedding = neighbor_model.predict(img_array)

    # Find nearest neighbors in the database
    nearest_neighbors = find_nearest_neighbors(neighbor_embedding, predicted_label)

    base64_files = []
    for position, neighbor in enumerate(nearest_neighbors, 1):
        base64_files.append({
            "base64": file_to_base64(neighbor['location']),
            "label": neighbor["label"],
            "position": position
        })

    return JSONResponse(
        content={
            "prediction": {"label": str(predicted_label), "probability": rounded_proba},
            "nearest_neighbors": base64_files,
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
