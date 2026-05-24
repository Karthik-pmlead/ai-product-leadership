import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Face Recognition Attendance",
    layout="wide"
)

st.title("🧠 AI Face Recognition Attendance System")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Enroll Employee",
        "Authenticate Employee",
        "Attendance Dashboard",
        "System Metrics"
    ]
)

# =========================================================
# ENROLL EMPLOYEE
# =========================================================

if menu == "Enroll Employee":

    st.header("Enroll Employee")

    name = st.text_input("Employee Name")
    emp_id = st.text_input("Employee ID")

    uploaded_file = st.file_uploader(
        "Upload Face Image",
        type=["jpg", "jpeg", "png"],
        key="enroll_upload"
    )

    camera_image = st.camera_input(
        "Capture Face",
        key="enroll_camera"
    )

    if st.button("Enroll"):

        if not name or not emp_id:
            st.warning("Enter all details")

        elif not uploaded_file and not camera_image:
            st.warning("Upload or capture image")

        else:

            image = uploaded_file if uploaded_file else camera_image

            files = {
                "file": (image.name, image.getvalue(), image.type)
            }

            data = {
                "name": name,
                "employee_id": emp_id
            }

            try:
                with st.spinner("Enrolling..."):
                    res = requests.post(
                        f"{API_URL}/enroll",
                        files=files,
                        data=data
                    )

                st.json(res.json())

            except Exception as e:
                st.error(str(e))


# =========================================================
# AUTHENTICATION + ANTI-SPOOF HANDLING + EXPLAINABILITY
# =========================================================

elif menu == "Authenticate Employee":

    st.header("Authenticate Employee")

    uploaded_file = st.file_uploader(
        "Upload Face Image",
        type=["jpg", "jpeg", "png"],
        key="auth_upload"
    )

    camera_image = st.camera_input(
        "Capture Face",
        key="auth_camera"
    )

    if st.button("Authenticate"):

        if not uploaded_file and not camera_image:
            st.warning("Upload or capture image")

        else:

            image = uploaded_file if uploaded_file else camera_image

            files = {
                "file": (image.name, image.getvalue(), image.type)
            }

            try:
                with st.spinner("Authenticating..."):

                    res = requests.post(
                        f"{API_URL}/authenticate",
                        files=files
                    )

                data = res.json()

                # -------------------------
                # ANTI-SPOOF HANDLING
                # -------------------------
                if data.get("type") == "ANTISPOOF_FAILED":
                    st.error("🚨 Liveness Check Failed")
                    st.warning(data.get("message"))
                    st.stop()

                # -------------------------
                # SUCCESS / FAIL FLOW
                # -------------------------
                if data.get("status") == "SUCCESS":

                    st.success("Authentication Successful")

                    col1, col2, col3 = st.columns(3)

                    col1.metric("Employee", data.get("employee_name"))
                    col2.metric("Employee ID", data.get("employee_id"))
                    col3.metric("Confidence", f"{data.get('confidence')}%")

                else:
                    st.error("Authentication Failed")
                    st.warning(data.get("message"))

                # -------------------------
                # EXPLAINABILITY
                # -------------------------
                st.subheader("Top Match Candidates")

                if "top_matches" in data:
                    st.json(data["top_matches"])

            except Exception as e:
                st.error(f"Request failed: {str(e)}")


# =========================================================
# ATTENDANCE DASHBOARD
# =========================================================

elif menu == "Attendance Dashboard":

    st.header("Attendance Dashboard")

    try:
        res = requests.get(f"{API_URL}/attendance")
        df = pd.DataFrame(res.json())

        if df.empty:
            st.info("No records found")
        else:
            st.dataframe(df, use_container_width=True)

            st.subheader("Metrics")

            st.metric("Total Records", len(df))
            st.metric(
                "Success Rate",
                f"{len(df[df['status']=='SUCCESS']) / len(df) * 100:.2f}%"
            )

    except Exception as e:
        st.error(str(e))


# =========================================================
# SYSTEM METRICS
# =========================================================

elif menu == "System Metrics":

    st.header("System Metrics")

    try:
        res = requests.get(f"{API_URL}/metrics")
        data = res.json()

        st.metric("Total Auth", data["total_auth"])
        st.metric("Success Rate", f"{data['success_rate']}%")
        st.metric("Failure Rate", f"{data['failure_rate']}%")
        st.metric("Avg Confidence", f"{data['avg_confidence']}%")

        st.subheader("Hourly Usage")
        st.bar_chart(data["hourly_hits"])

    except Exception as e:
        st.error(str(e))
