import streamlit as st


st.title("Request System")

    # Sidebar navigation
selected_option = st.sidebar.radio("Navigation", ("Appointment", "Telecom"))

    # Display request form based on selected option
if selected_option == "Appointment":
        appointment_request()
elif selected_option == "Telecom":
        telecom_request()
    

def appointment_request():
    st.header("Appointment Request")
    st.image(r"C:\Users\barat\Downloads\doctor\images.jpg", width=100)
    selected_doctor = st.selectbox("Select Doctor", ["Dr.Barathvasan", "Dr.jaswanth Raj", "Dr.Rashmi"])
    date = st.date_input("Date")
    time = st.time_input("Time")
    reason = st.text_area("Reason for Appointment", "")
    
    # Doctor selection dropdown
    
    submit_button = st.button("Submit Appointment Request")

if submit_button:
        # Process appointment request (e.g., store in database)
        st.success("Appointment request submitted successfully!")

def telecom_request():
    st.header("Telecom Request")
    st.image(r"C:\Users\barat\Downloads\doctor\call.png", width=100)
    selected_doctor = st.selectbox("Select Doctor", ["Dr.Barathvasan", "Dr.jaswanth Raj", "Dr.Rashmi"])
    
    # Dictionary mapping doctor name to phone number
    doctor_phone_numbers = {
        "Dr.Barathvasan": "8249431753",
        "Dr.jaswanth Raj": "7836472643",
        "Dr.Rashmi": "8793746285"
    }
    
    # Display selected doctor's phone number
if selected_doctor in doctor_phone_numbers:
        phone_number = doctor_phone_numbers[selected_doctor]
        st.write(f"Phone Number: {phone_number}")
else:
        st.write("Phone Number not available")

request_details = st.text_area("Request Details", "")
    
    # Doctor selection dropdown
    
submit_button = st.button("Submit Telecom Request")

if submit_button:
        # Process telecom request (e.g., send request to telecom provider)
        st.success("Telecom request submitted successfully!")


