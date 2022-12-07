# authored-streamlits

Collection of streamlits written by zyBook authors.


## Structure

Each book has a separate folder. Ex: Data Science Foundations book has folder DataScienceFoundations.

Each file in each book folder is a streamlit app, like: DataScienceFoundations/example.py (TODO: update this example)

## Streamlit authoring process

    1. Create your own branch from main. Ex: Rissler1207
    2. Create stub of streamlit in the folder for your book. Ex: DataScienceFoundations/new_streamlit.py
    3. Push your branch and Slack Matt Rissler to spin up your applet. He will respond with your URL.
    4. Author per normal. (Hopefully you don't need to see the Console.) Put URL in the gdoc as we've been doing.
    5. After applet has gone through review and is final state, submit a pull request to the the main branch.
    6. Put the new URL that Matt sends after the merge into the gdoc and process.

## st-cache discussion

TODO later. Add note of CPU vs memory trade-off and that we should profile against author streamlits (previous profiling was against random apps found online)