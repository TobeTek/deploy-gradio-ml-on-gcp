# deploy-gradio-ml-on-gcp
A demo ML application that provides first aid information to people diagnosed with internal bleeding.A simple ML application built with HuggingFace and Gradio Deployed on GCP

## Live Demo
> https://ml-gradio-demo.ew.r.appspot.com/

## KaggleX Mentee - My Experience
> [EDA | RSNA Abdominal Injury Competition 2023](https://www.kaggle.com/code/tobetek/eda-rsna-abdominal-injury-competition-2023)

> [LinkedIn Post - My experience as a KaggleX Mentee](https://www.linkedin.com/posts/emmanuel-katchy_kaggle-kagglex-bipoc-activity-7126311581159727105-QzS_?utm_source=share&utm_medium=member_desktop)

## KaggleX Program Website
> https://www.kaggle.com/kagglex
## Helpful Tutorials
 - https://medium.com/@mehmetcanfarsak/ci-cd-using-github-actions-to-deploy-on-gcp-app-engine-in-3-simple-steps-399fa9764cf2

### Notes/Todos:
  - You need to disable Gradio flagging in GCloud because the environment is read-only
  - Allow users to upload scan images, and perform live inference
  - To be able to use this template/project, create a blank `env.yaml` locally. Environment variables can then be defined as needed.
    An example:
  ```yaml
  HUGGING_FACE_TOKEN=<YOUR_API_KEY>
  ```
