import streamlit as st
import speedtest
import time

# Title and description
st.title("Internet Speed Test")
st.write("This app checks your upload and download speeds using Speedtest.")

# Add start and stop buttons
start_test = st.button("Start Test")
stop_test = st.button("Stop Test")

# Function to run the speed test
def run_speed_test():
    with st.spinner("Running speed test..."):
        test = speedtest.Speedtest()
        time.sleep(2)  # Simulate a loading time
        
        download_speed = test.download()
        upload_speed = test.upload()
        
        # Convert speeds from bps to Mbps (Megabits per second)
        download_mbps = download_speed / 1_000_000
        upload_mbps = upload_speed / 1_000_000
        
        # Convert Mbps to MB/s (Megabytes per second)
        download_mbs = download_mbps / 8
        upload_mbs = upload_mbps / 8
        
        st.success("Speed Test Completed!")
        
        # Simulate a progress bar animation
        progress = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)  # Simulate progress bar loading
            progress.progress(percent_complete + 1)
        
        # Display the download and upload speeds
        st.write(f"**Download speed**: {download_mbs:.2f} MBps")
        st.write(f"**Upload speed**: {upload_mbs:.2f} MBps")
        
        # Add a gauge-like effect using columns and colors
        st.subheader("Speed Summary")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="Download Speed", value=f"{download_mbs:.2f} MBps")
        
        with col2:
            st.metric(label="Upload Speed", value=f"{upload_mbs:.2f} MBps")

# Logic for button control
if start_test:
    run_speed_test()

if stop_test:
    st.write("Test Stopped.")  # You can't stop the speed test once started, but this simulates the idea.
