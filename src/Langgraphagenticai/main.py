
import streamlit as st
import json
from src.Langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
#from src.Langgraphagenticai.LLMS.groqllm import GroqLLM
#from src.Langgraphagenticai.graph.graph_builder import GraphBuilder
#from src.Langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

# MAIN Function START
def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
   
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")

   