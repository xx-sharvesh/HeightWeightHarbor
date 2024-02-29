import streamlit as st


def signup():
    st.title("Signup")
    name = st.text_input("Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        # Here you can save the signup data to your data source
        st.success("Signup Successful!")


def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Dummy authentication (no actual authentication)
        if username == "dummyuser" and password == "dummypassword":
            st.success("Login Successful!")
            return True
        else:
            st.error("Invalid Username or Password")
            return False


def calculate_bmi():
    st.title("Calculate BMI")
    height = st.number_input("Enter Height (in meters)")
    weight = st.number_input("Enter Weight (in kilograms)")
    if st.button("Calculate BMI"):
        bmi = weight / (height ** 2)
        st.write("Your BMI:", bmi)
        
        # Providing comments on BMI
        if bmi < 18.5:
            st.write("Your BMI indicates that you are underweight.")
        elif bmi >= 18.5 and bmi < 25:
            st.write("Your BMI indicates that you are within the healthy weight range.")
        elif bmi >= 25 and bmi < 30:
            st.write("Your BMI indicates that you are overweight.")
        else:
            st.write("Your BMI indicates that you are obese.")



def track_weight_over_time():
    st.title("Track Weight Over Time")
    time_period = st.selectbox("Select Time Period", ["Year", "Month", "Week"])
    start_date = st.date_input("Enter Start Date")
    end_date = st.date_input("Enter End Date")

    start_weight = st.number_input("Enter Weight at Start")
    start_height = st.number_input("Enter Height at Start")
    end_weight = st.number_input("Enter Weight at End")
    end_height = st.number_input("Enter Height at End")

    if start_height <= 0 or end_height <= 0:
        st.error("Height must be a positive value.")
        return

    start_bmi = start_weight / (start_height ** 2)
    end_bmi = end_weight / (end_height ** 2)

    bmi_change = end_bmi - start_bmi

    st.write("BMI at Start Date:", start_bmi)
    st.write("BMI at End Date:", end_bmi)
    st.write("Change in BMI:", bmi_change)

    if bmi_change > 0:
        st.write("Congratulations! You have become more fit.")
    elif bmi_change < 0:
        st.write("Be cautious! You might have gained weight.")
    else:
        st.write("Your BMI remains unchanged.")




def main():
    st.title("BMI calculator")

    page = st.sidebar.radio("Navigation", ["Login", "Signup", "Calculate BMI", "Track Weight Over Time"])

    if page == "Login":
        if login():
            pass  # Redirect to other pages after successful login

    elif page == "Signup":
        signup()

    elif page == "Calculate BMI":
        calculate_bmi()

    elif page == "Track Weight Over Time":
        track_weight_over_time()


if __name__ == "__main__":
    main()
