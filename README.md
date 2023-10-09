# deploy-gradio-ml-on-gcp
A demo ML application that provides first aid information to people diagnosed with internal bleeding.A simple ML application built with HuggingFace and Gradio Deployed on GCP

## Live Demo: https://ml-gradio-demo.ew.r.appspot.com/

## Helpful Tutorials
 - https://medium.com/@mehmetcanfarsak/ci-cd-using-github-actions-to-deploy-on-gcp-app-engine-in-3-simple-steps-399fa9764cf2

### Notes/Todos:
  - You need to disable Gradio flagging in GCloud because the environment is read-only
  - Allow users to upload scan images, and perform live inference