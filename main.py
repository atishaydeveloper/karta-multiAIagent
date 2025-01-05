#!/usr/bin/env python
import sys
import warnings
import streamlit as st
import os

from crew import Karta

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

import os

# Set the Generative Language API Key
os.environ["GENERATIVE_LANGUAGE_API_KEY"] = "key-by-google"

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(inputs):
    """
    Run the crew.
    """
    return Karta().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Karta().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Karta().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Karta().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def main():
    st.title("Topic Input Interface")
    st.write("Please enter a topic for the project:")

    topic = st.text_input("Topic")

    if st.button("Submit"):
        if topic:
            st.success(f"You have entered: {topic}")
            # Process the topic and generate output
            inputs = {'topic': topic}
            result = run(inputs)
            st.write("Generated Output:")
            st.write(result)
        else:
            st.error("Please enter a topic before submitting.")
            
if __name__ == "__main__":
    main()