from fastapi import FastAPI, responses
import gradio as gr
from src.model_interface import iface
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return responses.FileResponse("pages/index.html")


app = gr.mount_gradio_app(app, iface, path="/gradio")
