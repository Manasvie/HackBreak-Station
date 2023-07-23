import streamlit as st
import time

def countdown_timer(total_time):
    remaining_placeholder = st.sidebar.empty()

    while total_time:
        mins, secs = divmod(total_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        remaining_placeholder.write("Remaining Time: {}".format(timeformat))
        time.sleep(1)
        total_time -= 1

    remaining_placeholder.write("Time's up!")

def main():
    st.title("Pomodoro Timer App")
    st.sidebar.title("Your Time Starts now!")

    # Add content to the sidebar
    st.sidebar.write("Enjoy! 🍔🍿🥤")

    # Add Lottie animation to the sidebar
    lottie_url =  "https://lottie.host/?file=73bc16a5-4e97-486c-9615-ce4047f8a93f/0fIFzJf4k0.json"
    lottie_html = f'<iframe src="{lottie_url}" width="100%" height="200px"></iframe>'
    st.sidebar.markdown(lottie_html, unsafe_allow_html=True)

    # Pomodoro timer settings
    session_length = st.number_input(
        "Enter the length of the session (in minutes):", min_value=1, value=25
    )
    break_length = st.number_input(
        "Enter the length of the break (in minutes):", min_value=1, value=5
    )

    if st.sidebar.button("Start Pomodoro"):
        total_time = session_length * 60
        countdown_timer(total_time)

if __name__ == "__main__":
    main()
