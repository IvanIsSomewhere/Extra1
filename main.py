import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve


from Custom_Plots import cplot_2

# Page configuration
st.set_page_config(
    page_title="AHHHHHH",
    page_icon="🚀",
    layout="centered"
)

# Title and header
st.title("🎯 My First Streamlit Dashboard")
st.subheader("A simple interactive web app")

# Text elements
st.write("This app demonstrates basic Streamlit functionality:")
st.markdown("- **Data visualization**")
st.markdown("- **Interactive widgets**")
st.markdown("- **Layout organization**")

# Divider
st.divider()

# Create two columns
col1, col2 = st.columns(2)

# Column 1: Slider and Button
with col1:
    st.header("Controls")

    # Slider
    num_points = st.slider("Number of data points", 10, 100, 50)

    # Button
    if st.button("Generate Random Data"):
        st.session_state.generated = True
        st.success("Data generated!")

# Column 2: Data visualization
with col2:
    st.header("Visualization")
    #cplot_2()
    if 'generated' in st.session_state:
        # Generate random data
        data = pd.DataFrame({
            'x': range(num_points),
            'y': np.random.randn(num_points).cumsum()
        })



        # Plotting
        fig, ax = plt.subplots()
        ax.plot(data['x'], data['y'], 'b-')
        ax.set_title("Random Walk Plot")
        st.pyplot(fig)
    else:
        st.info("Click 'Generate Random Data' first")

    option = st.selectbox(
        "Choose your favorite programming language:",
        ("Python", "JavaScript", "Java", "C++", "Go", "Rust"),
        index=0,  # Default selection
        placeholder="Select language...",
        key="lang_select"
    )

# Expander with sample data
with st.expander("Show Raw Data"):
    if 'generated' in st.session_state:
        st.dataframe(data.head(10))
    else:
        st.warning("Generate data to view")




# Sidebar
with st.sidebar:

    st.header("Settings")
    user_name = st.text_input("Your name", "John Doe")
    color = st.color_picker("Pick a color", "#00f900")
    st.write(f"Hello, {user_name}! Your color is {color}")

# Footer
st.divider()
st.caption("© 2023 - Made with Streamlit")