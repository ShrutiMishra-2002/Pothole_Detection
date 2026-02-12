import streamlit as st
from detector import detect_video

st.title("🚧 Pothole Detection System")

uploaded_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:

    input_path = "uploaded_video.mp4"

    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    st.video(input_path)
    st.write("Processing... Please wait ⏳")

    output_path = detect_video(input_path)

    st.success("Detection Complete ✅")

    st.video(output_path)

    with open(output_path, "rb") as f:
        st.download_button(
            "Download Processed Video",
            f,
            file_name="pothole_output.avi"
        )
