import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage
from src.Langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
  def __init__(self):
    self.config = config()
    self.user_controls ={}