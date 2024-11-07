import streamlit as st
from  load_lstm import LSTM_functions
from load_bert import BertClassifier,BertClassifierMultiLabel
from utils import process_image
#from logger import customlogging as log
from gemini import Suggestions_model,log
import time



log.info("Libraries Loaded")
#from load_NB import NaiveBayesClassifier

st.header("Cyber Crime Classification 🐱‍💻")

name=st.text_input("Enter Your Name ")
complaint=st.text_area("Enter You Complaint  **manadatory**")

radio_btn=st.radio("Which Model to Use",options=("LSTM","Bert","Bert_Multilabel"))#"Naive Bayes"
image_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if "confirm_submission" not in st.session_state:
    st.session_state.confirm_submission = False

submit=st.button("Submit & Predict")

log.info("UI Loaded")

log.info("AI suggestions loaded")
if submit:
    st.session_state.confirm_submission = True
    log.info("Submit Button clicked")
    log.info("Loading Confirmation Box")
    st.text("Loading AI suggestions")


if st.session_state.confirm_submission:
    mdl=Suggestions_model()                                  
    answer=mdl.get_suggestions(complaint)
    st.write(answer)
    st.warning("Do you want to continue submitting the compalint or Reenter the complaint !")   
    col1, col2 = st.columns(2)
    with col1:
        confirm = st.button("Confirm")
    with col2:
        reenter = st.button("Re-enter")
    if confirm:
        st.session_state.confirm_submission = False  # Reset confirmation
        st.success("You have confirmed! Processing your complaint...")
        log.info("Processing Details")
        process_image(image_file, name, complaint)
        st.success("Data stored successfully! Initiating Prediction this could take some time")
        log.info("Data stored successfully! Initiating Prediction this could take some time")
        if radio_btn=="LSTM":
            lstm=LSTM_functions()
            preds=lstm.load_and_predict(complaint)
            st.success(preds)
        if radio_btn=="Bert_Multilabel":
            bert=BertClassifierMultiLabel()
            preds=bert.predict(complaint)
            print(preds)
            st.success(preds)
        if radio_btn=="Bert":
            bert=BertClassifier()
            preds=bert.predict(complaint)
            st.success(preds)
        #if radio_btn=="Naive Bayes":
            #nb=NaiveBayesClassifier()
            #preds=nb.predict(compalint)
            #st.success(preds)
    if reenter:
        st.session_state.confirm_submission = False
        st.rerun()
