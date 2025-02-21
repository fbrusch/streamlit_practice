import streamlit as st
from random import randint
from time import sleep

import matplotlib.pyplot as plt
import numpy as np

"""
# Birthday paradox

"""

def generate_class():
    return [randint(1,365) for _ in range(27)]


if "experiments" not in st.session_state:
    st.session_state["experiments"] = []

c = generate_class()

counter = 0

count = [c.count(i) for i in range(1, 366)]

countmap = [[0 for _ in range(31)] for _ in range(12)]

for i in range(12):
    for y in range(30):
        countmap[i][y] = count[y+30*i]



# Fixing random state for reproducibility

plt.imshow(countmap, cmap='hot', interpolation='nearest')
st.pyplot(plt)

there_are_collisions = not len(set(c)) == len(c)

if there_are_collisions:
    st.write("there are collisions!")
else:
    st.write("there are no collisions")

st.session_state.experiments.append(there_are_collisions)


estimated_prob = st.session_state.experiments.count(True)/len(st.session_state.experiments)

st.write(estimated_prob)

import matplotlib.pyplot as plt

labels = ["Collision", "No Collision"]
sizes = [st.session_state.experiments.count(True),
         st.session_state.experiments.count(False)]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', explode=(0.01,0))

st.pyplot(plt)

#st.write(st.session_state.experiments)

st.write("number of experiments so far: ", len(st.session_state.experiments))

st.button("generate another class")

reload = st.toggle("autoreload")

if st.button("reset"):
    st.session_state.experiments = []

st.write(reload)

def p_at_time(t):
    exps = st.session_state.experiments[:t]
    return sum(exps)/t



estimates = [p_at_time(t) for t in range(1, len(st.session_state.experiments))]

if len(estimates) != 0:
    st.line_chart(estimates)


#st.line_chart([1,2])

if reload:
    sleep(0.1)
    st.rerun()


