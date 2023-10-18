import streamlit as st
import time
from exercises import exercises

st.set_page_config(page_title="Let's get fit! 🖤 ", page_icon="🏋🏽‍♀️")
st.title('Workout :red[Session] 💪🏽')

# Function to add new log entries
def add_log(exercise, repetitions, series, page):
    new_log = f"""Group: {page} 
    Exercise: {exercise}
    Reps: {repetitions} 
    Series: {series}"""
    if 'logs' not in st.session_state:
        st.session_state.logs = []  # Initialize logs if not already present
    st.session_state.logs.append(new_log)  # Add the new log to session_state

page = st.sidebar.selectbox("Choose a muscle group", tuple(exercises.keys()))
#Add icon to the side bar
icon_svg = '''
<div style="display: flex; justify-content: center; opacity: 0.3; margin-top: 40px; margin-bottom: 40px">
    <svg xmlns="http://www.w3.org/2000/svg" height="5em" viewBox="0 0 640 512"><!--! Font Awesome Pro 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><style>svg{fill:#4a4a4a}</style><path d="M208 64c8.8 0 16 7.2 16 16V256 432c0 8.8-7.2 16-16 16H176c-8.8 0-16-7.2-16-16V368 144 80c0-8.8 7.2-16 16-16h32zM128 413.3V432c0 26.5 21.5 48 48 48h32c26.5 0 48-21.5 48-48V272H384V432c0 26.5 21.5 48 48 48h32c26.5 0 48-21.5 48-48V413.3c5 1.8 10.4 2.7 16 2.7h32c26.5 0 48-21.5 48-48V272h16c8.8 0 16-7.2 16-16s-7.2-16-16-16H608V144c0-26.5-21.5-48-48-48H528c-5.6 0-11 1-16 2.7V80c0-26.5-21.5-48-48-48H432c-26.5 0-48 21.5-48 48V240H256V80c0-26.5-21.5-48-48-48H176c-26.5 0-48 21.5-48 48V98.7C123 97 117.6 96 112 96H80c-26.5 0-48 21.5-48 48v96H16c-8.8 0-16 7.2-16 16s7.2 16 16 16H32v96c0 26.5 21.5 48 48 48h32c5.6 0 11-1 16-2.7zM512 144c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16V256 368c0 8.8-7.2 16-16 16H528c-8.8 0-16-7.2-16-16V144zM480 368v64c0 8.8-7.2 16-16 16H432c-8.8 0-16-7.2-16-16V256 80c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16v64V368zM128 144V368c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V256 144c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16z"/></svg>
</div>
'''
st.sidebar.markdown(icon_svg, unsafe_allow_html=True)



# Setting background based on the selected muscle group
if page == 'Legs':
    background_image_url = "https://images.unsplash.com/photo-1516481157630-05bc0aeb8b19?auto=format&fit=crop&q=80&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&w=2670"
elif page == 'Back':
    background_image_url = "https://images.unsplash.com/photo-1434682881908-b43d0467b798?auto=format&fit=crop&q=80&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&w=2674"
elif page == 'Chest':
    background_image_url = "https://images.unsplash.com/photo-1597452485677-d661670d9640?auto=format&fit=crop&q=80&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&w=2572"
else:
    background_image_url = ""  # This will be empty or you can set a default background

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: linear-gradient(rgba(0, 0, 0, 0.9), rgba(10, 10, 10, 0.5)), url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


# Table of Contents in Sidebar
st.sidebar.title(f'{page} Exercises 🏋🏽')
for exercise in exercises[page]:
    exercise_name = exercise['name'].replace(' ', '-')
    st.sidebar.markdown(f'<a href="#{exercise_name}">{exercise["name"]}</a>', unsafe_allow_html=True)

# Display exercises for selected muscle group
st.write(f'<span style="font-size: 40px">{page} Training </span>', unsafe_allow_html=True)
for idx, exercise in enumerate(exercises[page]):
    st.markdown(f'<a id="{exercise["name"].replace(" ", "-")}"></a>', unsafe_allow_html=True)  # Anchor
    
    # Exercise Name
    st.write(f'<span style="font-size: 23px">Exercise: {exercise["name"]}</span>', unsafe_allow_html=True)
    
    # Exercise Video
    video_link = exercise['video_link']
    st.video(video_link)
    
    # Exercise Description
    with st.expander(f'{exercise["name"]} Guide and Tips 📚', expanded=False):
        exercise["description"]
    
    # Repetitions Counter
    rep_count = st.session_state.get(f"rep_count_{idx}", 0)
    col, buff2 = st.columns([0.1, 1])
    series = col.text_input(f"Reps:", value="12", key=f"series_txt_{idx}")


    st.markdown(f'<div style="margin-bottom: 5px;"><span style="font-size:20px;"> Series:  &nbsp;&nbsp;{rep_count}+ </span></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([0.1, 1])
    # Addition button
    with col1:
        if st.button(f"➕", key=f"btn_add_{idx}"):
            rep_count += 1
            st.session_state[f"rep_count_{idx}"] = rep_count
            st.rerun()  # Rerun to refresh the count immediately

    # Subtraction button
    with col2:
        if st.button(f"➖", key=f"btn_sub_{idx}"):
            rep_count -= 1  # Decrease the counter
            rep_count = max(0, rep_count)  # Prevent going below zero
            st.session_state[f"rep_count_{idx}"] = rep_count
            st.rerun()  # Rerun to refresh the count immediately
    
    # Button to display the logs
    if st.button("Log Exercise", key=f"logs_{idx}"):
        add_log(exercise["name"], series, rep_count, page)
    # Separator
    st.write('---')

st.sidebar.subheader(' ')

# Display the review section
st.sidebar.title("Review Your Activity ♻️")

if st.sidebar.button("Exercise Logs", key=f"dlogs_{idx}"):
    if 'logs' in st.session_state and st.session_state.logs:
        # Display each log in the sidebar
        for log in st.session_state.logs:
            st.sidebar.text(log)
    else:
        st.sidebar.text("No exercises were logged.")
        
# Stopwatch
st.subheader('Stopwatch')
rhythm = st.number_input(
    'Enter the length in seconds:', value=30, min_value=1,
)

# Initializing placeholder for the countdown
countdown_placeholder = st.empty()

# Function to start stopwatch/countdown
def start_stopwatch(stopwatch_state):
    t = rhythm
    while t >= 0 and stopwatch_state:
        if t > 0:
            countdown_placeholder.subheader(f'Time Remaining: {t} s ⏳')  # Update the countdown
        else:
            countdown_placeholder.subheader('FINISHED ⌛️')  # Display finished message
        t -= 1
        time.sleep(1)

st.markdown('<a id="stopwatch-section"></a>', unsafe_allow_html=True)  # Anchor
st.subheader('Stopwatch')
col1, col2 = st.columns([0.1, 1])

with col1:
    # Start button
    stopwatch_state = st.cache_data()(lambda: True)()
    btn_start = st.button('⏱️')
    if btn_start and stopwatch_state:
        countdown_placeholder.empty()  # Clear the countdown display
        countdown_placeholder.subheader(f'Time Remaining: {rhythm} s')  # Initial countdown value
        start_stopwatch(stopwatch_state)

with col2:
    # Stop button
    btn_stop = st.button('🛑')
    if btn_stop:
        stopwatch_state = False
        countdown_placeholder.empty()  # Clears the countdown display

st.markdown("""
    <style>
        .floating-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #FF2E63;
            color: white;
            border: none;
            border-radius: 50%;
            padding: 10px 20px;
            font-size: 24px;
            cursor: pointer;
            z-index: 9999;
        }
    </style>
    <a href="#stopwatch-section">
        <button class="floating-btn">⏱️</button>
    </a>
""", unsafe_allow_html=True)
