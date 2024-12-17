import random as rd
import streamlit as st

st.title("Rock Paper Scissors 🪨📰✂️")
st.write("Let's play a classic game of Rock Paper Scissors. Make your choice and see if you can beat the computer!")

user_choice = st.selectbox("Select your choice:", options=["Choose...", "🪨 Rock", "📰 Paper", "✂️ Scissors"])
st.write("\n\n")

if st.button("Go!"):
    if user_choice == "Choose...":
        st.write("Please select a choice!")
    else:
        comp_choice = rd.choice(["🪨 Rock", "📰 Paper", "✂️ Scissors"])
        st.subheader(f"Computer's choice: {comp_choice}")

        if user_choice == comp_choice:
            st.write("It's a tie! 🤝")

        elif (user_choice == "🪨 Rock" and comp_choice == "📰 Paper") or \
             (user_choice == "📰 Paper" and comp_choice == "✂️ Scissors") or \
             (user_choice == "✂️ Scissors" and comp_choice == "🪨 Rock"):
            st.write(f"{comp_choice} beats {user_choice}")
            st.write("You lose! 😢")
            st.snow()
            
        else:
            st.write(f"{user_choice} beats {comp_choice}")
            st.write("You win! 🎉")
            st.balloons()
else:
    st.write("Please select a choice and click Go!")
