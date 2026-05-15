"""
LLM assisted code
"""

import sys
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components # this is getting deprecated after 2026-06-01, so watch out

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from structures.graph import Graph
from graph.bfs import bfs
from visualization.graph_visualizer import GraphVisualizer


def build_graph() -> Graph:
    graph = Graph(directed=False)

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")

    return graph


ALGORITHMS = {
    "BFS": bfs,
}


graph = build_graph()

st.title("Graph Algorithm Visualizer")

selected_algorithm = st.selectbox(
    "Choose an algorithm",
    list(ALGORITHMS.keys())
)

start_node = st.selectbox(
    "Choose a start node",
    list(graph.nodes.keys())
)

st.markdown("### Legend")

legend_col1, legend_col2, legend_col3, legend_col4 = st.columns(4)

with legend_col1:
    st.markdown(
        "<div style='display:flex;align-items:center;'>"
        "<div style='width:20px;height:20px;background-color:yellow;"
        "margin-right:10px;border:1px solid black;'></div>"
        "Current Node"
        "</div>",
        unsafe_allow_html=True
    )

with legend_col2:
    st.markdown(
        "<div style='display:flex;align-items:center;'>"
        "<div style='width:20px;height:20px;background-color:lightgreen;"
        "margin-right:10px;border:1px solid black;'></div>"
        "Visited Node"
        "</div>",
        unsafe_allow_html=True
    )

with legend_col3:
    st.markdown(
        "<div style='display:flex;align-items:center;'>"
        "<div style='width:20px;height:20px;background-color:lightblue;"
        "margin-right:10px;border:1px solid black;'></div>"
        "Queued Node"
        "</div>",
        unsafe_allow_html=True
    )

with legend_col4:
    st.markdown(
        "<div style='display:flex;align-items:center;'>"
        "<div style='width:20px;height:20px;background-color:lightgray;"
        "margin-right:10px;border:1px solid black;'></div>"
        "Unvisited Node"
        "</div>",
        unsafe_allow_html=True
    )

algorithm = ALGORITHMS[selected_algorithm]
states = list(algorithm(graph, start_node))

if "step" not in st.session_state:
    st.session_state.step = 0

if st.session_state.step >= len(states):
    st.session_state.step = 0

state = states[st.session_state.step]

visualizer = GraphVisualizer()
html = visualizer.render_to_html(graph, state)

components.html(html, height=700, scrolling=True)


st.write(f"Step {st.session_state.step + 1} / {len(states)}")

col1, col2 = st.columns(2)

with col1:
    if st.button("Previous Step"):
        st.session_state.step = max(0, st.session_state.step - 1)
        st.rerun()

with col2:
    if st.button("Next Step"):
        st.session_state.step = min(len(states) - 1, st.session_state.step + 1)
        st.rerun()

with st.expander("Current Algorithm State"):
    st.json({
        "current": state.get("current"),
        "visited": list(state.get("visited", [])),
        "queue": state.get("queue", []),
        "order": state.get("order", []),
    })