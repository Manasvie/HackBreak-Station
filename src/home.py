import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests


def main():
    st.markdown(
        '''
        <h1 align="center">
            Welcome to HackBreak Station 👋
        </h1>

        ---
        Wanna take a break? You are at the right place.

        You might be tired from hacking for so long, realax for a bit and play a game or chat with our Hack-bot.

        Do not worry we'll let you know when its time to go back to hacking.

        Until then explore Games and our Hack-Bot and have a nice break!
        Happy Hacking!


        ''',
        unsafe_allow_html=True,
    )

    url = requests.get("https://lottie.host/b9870614-efb9-40cf-9e32-2dcc39c350c8/KTVSxyFKM2.json")

    url_json=dict()

    if url.status_code == 200:
        url_json=url.json()
    else:
        print('error')
    # Use HTML to embed the GIF in the sidebar
    st_lottie(url_json)



if __name__ == '__main__':
    main()