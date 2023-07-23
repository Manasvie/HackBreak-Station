import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests


from src import pomodoro, hackBot, home, guess_number, guess_word, tic_tac_toe


def init():
    st.session_state.page = 'Homepage'
    st.session_state.project = False
    st.session_state.game = False

    st.session_state.pages = {
        'Homepage': home.main,
        # 'About me': about.main,
        # 'Source': source.main,
        'Pomodoro':pomodoro.main,
        'Hack-Bot': hackBot.main,
        'Guess Number': guess_number.main,
        'Guess Word': guess_word.main,
        'Tic Tac Toe': tic_tac_toe.main,
    }


def draw_style():
    st.set_page_config(page_title='HackBreak-Station', page_icon='🎮')

    style = """
        <style>
            header {visibility: visible;}
            footer {visibility: hidden;}
        </style>
    """

    st.markdown(style, unsafe_allow_html=True)


def load_page():
    st.session_state.pages[st.session_state.page]()


def set_page(loc=None, reset=False):
    if not st.session_state.page == 'Homepage':
        for key in list(st.session_state.keys()):
            if key not in ('page', 'project', 'game', 'pages', 'set'):
                st.session_state.pop(key)

    if loc:
        st.session_state.page = loc
    else:
        st.session_state.page = st.session_state.set

    if reset:
        st.session_state.project = False
    elif st.session_state.page in ('Hack-Bot'):
        st.session_state.project = True
        st.session_state.game = False
    else:
        pass


def change_button():
    set_page('Guess Number')
    st.session_state.game = True
    st.session_state.project = True


def main():
    if 'page' not in st.session_state:
        init()

    draw_style()
    st.sidebar.title("Choose your break hack here!")
    with st.sidebar:
        project, hackbot, pomodoro = st.columns([1.2, 1, 1])

        if not st.session_state.project:
            project.button('🎮 GameZone', on_click=change_button)
        else:
            project.button('🏠 Homepage', on_click=set_page, args=('Homepage', True))

        if st.session_state.project and st.session_state.game:
            st.selectbox(
                'List of games',
                ['Guess Number', 'Guess Word', 'Tic Tac Toe'],
                key='set',
                on_change=set_page,
            )

        hackbot.button('🤖 HackBot', on_click=set_page, args=('Hack-Bot',))
        pomodoro.button('🍅 Pomodoro', on_click=set_page, args=('Pomodoro',))


        if st.session_state.page == 'Homepage':
            url = requests.get("https://lottie.host/d5cde596-466c-472c-85f1-5f17f964af5a/BuhizxOEIP.json")

            url_json=dict()

            if url.status_code == 200:
                url_json=url.json()
            else:
                print('error')
            st_lottie(url_json)

    load_page()


if __name__ == '__main__':
    main()