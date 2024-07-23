import streamlit as st
from GoogleNews import GoogleNews
from youtube_search import YoutubeSearch

# Set the app to wide mode
st.set_page_config(layout="wide")

# Streamlit app
st.title("Search The Trend")

# Search box
search_query = st.text_input("Enter your search query:")

if search_query:
    # Google News Search
    googlenews = GoogleNews()
    googlenews.search(search_query)
    google_results = googlenews.result()

    # YouTube Search
    youtube_results = YoutubeSearch(search_query, max_results=10).to_dict()

    # Display results in columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Google News Results")
        if google_results:
            for result in google_results:
                st.write(f"**Title:** {result['title']}")
                st.write(f"**Link:** {result['link']}")
                st.write(f"**Description:** {result['desc']}")
                st.write('-' * 20)
        else:
            st.write("No results found on Google News.")

    with col2:
        st.subheader("YouTube Results")
        if youtube_results:
            for result in youtube_results:
                st.write(f"**Title:** {result['title']}")
                st.write(f"**Link:** https://www.youtube.com{result['url_suffix']}")
                st.write(f"**Channel:** {result['channel']}")
                st.write(f"**Duration:** {result['duration']}")
                st.write(f"**Views:** {result['views']}")
                st.write('-' * 20)
        else:
            st.write("No results found on YouTube.")
