import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import summary_page
from app_pages.page_data_visualizer import page_data_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_hypothesis import hypothesis_page
from app_pages.page_ml_performance import performance_metrics_page

app = MultiPage(app_name="Mildew Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Brief Project Summary", summary_page)
app.add_page("Leaves Visualiser", page_data_visualizer_body)
app.add_page("Mildew Detection", page_mildew_detector_body)
app.add_page("Project Hypothesis", hypothesis_page)
app.add_page("ML Performance Metrics", performance_metrics_page)

app.run()  # Run the ap
