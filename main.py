import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()
GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


prompt = ChatPromptTemplate.from_template(
    "you are a brilliant {course} courseal , explain me about {topic} in {words} words with {radio_button} for {course} {radio_button2}"
) # radio_button = real world example / code, radio_button2 = assingnment/interview/exam


llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=GOOGLE_API_KEY)


output_parser=StrOutputParser()


chain=prompt|llm|output_parser






# Title of the web app
st.title("Teaching Assistant")

# course Section
st.subheader("course")
course = st.text_area("Enter your course",)

# Topic Section
st.subheader("Topic")
topic = st.text_area("Enter your topic")

# Words Section
st.subheader("Words")
word_count = st.text_area("Enter word count")

# Real world Example / Code Section
example_type = st.radio("Select the type of example",('Real world Example', 'Code'))

# Assignments / Interview / Exam Section
task_type = st.radio("Select the type of task", ('Assignments', 'Interview', 'Exam'))

# Display the user inputs


if st.button("Submit"):
    final_result = chain.invoke({"course": {course}, "topic": {topic}, "words": {word_count}, "radio_button": {example_type}, "radio_button2":{task_type}})
    st.markdown(final_result)

