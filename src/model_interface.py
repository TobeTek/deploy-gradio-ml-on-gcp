"""
Gradio related stuff
"""
from enum import Enum
from typing import Optional

import gradio as gr
from src import utils


class InjuryType(str, Enum):
    NO_INJURY = "NO_INJURY"
    LIVER = "LIVER"
    KIDNEY = "KIDNEY"
    SPLEEN = "SPLEEN"
    EXTRAVASATION = "EXTRAVASATION"
    BOWEL = "BOWEL"


INJURY_PROMPTS = {
    InjuryType.LIVER: "[INST] What are some first aid for liver internal injury [/INST]",
    InjuryType.KIDNEY: "[INST] What are some first aid for kidney internal injury [/INST]",
    InjuryType.SPLEEN: "[INST] What are some first aid for spleen internal injury [/INST]",
    InjuryType.EXTRAVASATION: "[INST] What are some first aid for extravasation internal injury [/INST]",
    InjuryType.BOWEL: "[INST] What are some first aid for bowel internal injury [/INST]",
    InjuryType.NO_INJURY: "[INST] What are some general medical fitness tips [/INST]",
}


# Define function to be executed when "Run" button is clicked
def interface_handler(choice: Optional[InjuryType]) -> str:
    if choice is None:
        return ""
    input_prompt = INJURY_PROMPTS[choice]
    return utils.query(inputs=input_prompt)


interface_description = """
<center>
<img src="/static/images/image-robot.jpg" alt="image of a robot" width="350px"/>
</center>

<strong>This application is based on the [RSNA 2023 Kaggle Competition](),
and attempts to provide first aid information to patients with abdominal injuries.</strong>

It does this by prompting the <em>[mistralai/Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)</em>
text generation model via the [HuggingFace Inference API](https://huggingface.co/inference-api).
This model is not medically accurate, and this entire application has been created for illustrative purposes.
Do enjoy!

"""


# Gradio interface configuration
iface = gr.Interface(
    fn=interface_handler,
    allow_flagging="never",
    title="Ask eMLily",
    description=interface_description,
    inputs=[
        gr.Radio(
            label="Get some first aid advice!",
            info="What is the patient's diagnosis?",
            choices=[
                ("Liver", InjuryType.LIVER),
                ("Bowel", InjuryType.BOWEL),
                ("Extravasation", InjuryType.EXTRAVASATION),
                ("Kidney", InjuryType.KIDNEY),
                ("Spleen", InjuryType.SPLEEN),
                (
                    "No Internal Injury. I'd just like general medical advice",
                    InjuryType.NO_INJURY,
                ),
            ],
        ),
    ],
    outputs=gr.Textbox("Model output ..."),
    live=True,
    theme="light",
)
