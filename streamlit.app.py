import streamlit as st
import speedtest
import time

# Title and description
st.title("Internet Speed Test")
st.write("This app checks your upload and download speeds using Speedtest.")

# Animation: progress bar
with st.spinner("Running speed test..."):
    test = speedtest.Speedtest()
    
    # Simulating a loading time
    time.sleep(2)
    
    download_speed = test.download()
    upload_speed = test.upload()

# Convert speeds from bps to Mbps (Megabits per second)
download_mbps = download_speed / 1_000_000
upload_mbps = upload_speed / 1_000_000

# Convert Mbps to MB/s (Megabytes per second)
download_mbs = download_mbps / 8
upload_mbs = upload_mbps / 8
# Display the results with basic animation
st.success("Speed Test Completed!")

progress = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)  # simulate animation
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
