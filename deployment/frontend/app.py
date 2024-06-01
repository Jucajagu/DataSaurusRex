import dash
import dash_uploader as du
from dash.dependencies import Input, Output, State
import numpy as np
import os
from PIL import Image
import base64
import io
import requests
from dash import dcc, html
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import cv2


# Set up the request URL and authorization token
REQUEST_URL = "http://jucajagu.ddns.net:3000/predict/"
AUTH_TOKEN = "d391a9b3ef4e483880986aae70e164f2"

# Configure Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Configure dash-uploader
UPLOAD_FOLDER_ROOT = "C:/uploads"
du.configure_upload(app, UPLOAD_FOLDER_ROOT)

colors = ('b', 'g', 'r')

# Function to display the image
def parse_contents(contents):
    return html.Img(src=contents, style={"width": "50%", "margin": "auto", "display": "block"})

#### Mostrar histogramas
def crear_histograma(img_array):
    histograma = []
    for i, _ in enumerate(colors):
        hist = cv2.calcHist([img_array], [i], None, [256], [0,256])
        histograma.append(hist)
    return histograma

def mostrar_histograma(hist_array):
    plt.figure()
    for i, col in enumerate(colors):
        plt.plot(hist_array[i], color=col)
    plt.legend(colors)
    plt.xlabel('Nivel de intensidad')
    plt.ylabel('Cantidad de pixeles')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

@app.callback(
    Output("output-uploaded-image", "children"),
    Output("stored-image", "data"),
    [Input("upload-image", "isCompleted")],
    [State("upload-image", "fileNames"), State("upload-image", "upload_id")]
)
# Callback to display the uploaded image immediately after it is uploaded
def display_uploaded_image(is_completed, fileNames, upload_id):
    if is_completed and fileNames is not None:
        root_folder = UPLOAD_FOLDER_ROOT
        file_path = os.path.join(root_folder, upload_id, fileNames[0])
        
        # Lee la imagen y convierte a base64
        image = Image.open(file_path)
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        encoded_image = base64.b64encode(buffered.getvalue()).decode()
        content = f"data:image/png;base64,{encoded_image}"
        
        return html.Img(src=content), encoded_image
    return "No hay imagen seleccionada.", None

@app.callback(
    Output("output-uploaded-graph", "figure"),
    [Input("stored-image", "data")]
)
def update_graph(encoded_image):
    if encoded_image is not None:
        decoded_image = base64.b64decode(encoded_image)
        img_array = np.array(Image.open(io.BytesIO(decoded_image)))
        
        # Crear el histograma
        histograma = crear_histograma(img_array)
        
        # Mostrar el histograma
        buf = mostrar_histograma(histograma)
        encoded_hist = base64.b64encode(buf.getvalue()).decode()
        
        return {
            'data': [{
                'x': list(range(256)),
                'y': histograma[0].flatten(),
                'type': 'line',
                'name': 'Blue'
            }, {
                'x': list(range(256)),
                'y': histograma[1].flatten(),
                'type': 'line',
                'name': 'Green'
            }, {
                'x': list(range(256)),
                'y': histograma[2].flatten(),
                'type': 'line',
                'name': 'Red'
            }],
            'layout': {
                'title': 'Histograma de la Imagen'
            }
        }
    return {
        'data': [],
        'layout': {'title': 'Sin datos'}
    }
# Function to handle the API request upon clicking the Analyze button
@app.callback(
    Output("output-image", "children"),
    [Input("analyze-button", "n_clicks")],
    [State("upload-image", "fileNames"), State("upload-image", "upload_id")],
)
def analyze_image(n_clicks, fileNames, upload_id):
    if n_clicks and fileNames is not None:
        root_folder = UPLOAD_FOLDER_ROOT
        file_path = os.path.join(root_folder, upload_id, fileNames[0])

        # Read the image
        with open(file_path, "rb") as image_file:
            files = {"image": image_file}
            headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
            response = requests.post(REQUEST_URL, files=files, headers=headers)

            # Parse the response and display the predictions
            if response.status_code == 200:
                predictions = response.json()
                prediction_label = predictions["prediction"]["label"]
                prediction_probability = predictions["prediction"]["probability"]
                nearest_neighbors = predictions["nearest_neighbors"]

                # Construct HTML content for predictions
                prediction_html = html.Div(
                    [
                        html.H2("Prediction:", className="text-primary"),
                        html.P(f"Label: {prediction_label}"),
                        html.P(f"Probability: {prediction_probability}"),
                    ],
                    className="my-3"
                )

                # Construct HTML content for nearest neighbors
                neighbors_html = html.Div(
                    [
                        html.H2("Nearest Neighbors:", className="text-primary"),
                        html.Ul(
                            [
                                html.Li(
                                    [
                                        html.Img(
                                            src=f"data:image/png;base64,{neighbor['base64']}",
                                            style={"width": "50%", "margin": "auto", "display": "block"},
                                        ),
                                        html.P(f"Label: {neighbor['label']}"),
                                        html.P(f"Position: {neighbor['position']}"),
                                    ]
                                )
                                for neighbor in nearest_neighbors
                            ]
                        ),
                    ],
                    className="my-3"
                )

                # Combine prediction and nearest neighbors HTML content
                return html.Div([prediction_html, neighbors_html], className="mt-4")
            else:
                return html.Div(f"Error: {response.status_code}", className="text-danger")

    return "No hay imagen seleccionada."

# Define the layout of the application
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1("Escoja la imagen que desea analizar", className="text-center my-4"))),
        dbc.Row(dbc.Col(du.Upload(
            id="upload-image",
            text="Haga click para subir la imagen",
            max_file_size=3000,  # Max file size in megabytes
            filetypes=["jpg", "png", "jpeg"],
            upload_id="my-upload-image",
        ), width=6, className="offset-md-3")),
        dbc.Row(dbc.Col(html.Div(id="output-uploaded-image", className="text-center my-4"), width=6, className="offset-md-3")),
        dbc.Row(dbc.Col(html.Div(dcc.Graph(id="output-uploaded-graph"), className="text-center my-4"), width=6, className="offset-md-3")),
        dcc.Store(id='stored-image', data=None),

        dbc.Row(dbc.Col(dbc.Button("Analyze", id="analyze-button", n_clicks=0, color="primary"), width=6, className="text-center offset-md-3")),
        dbc.Row(dbc.Col(html.Div(id="output-image", className="mt-4"), width=6, className="offset-md-3")),
    ],
    fluid=True
)

# Run the application
if __name__ == "__main__":
    app.run_server(host="127.0.0.1", port=8053, debug=True)