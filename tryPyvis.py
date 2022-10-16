# import streamlit

from pyvis import network as net
import streamlit as st
from stvis import pv_static

g=net.Network(height='500px', width='500px',heading='')
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_edge(1,2)
g.add_edge(2,3)
#
#
pv_static(g)
# # import networkx as nx
# # import matplotlib.pyplot as plt
# # from pyvis.network import Network
# # import pandas as pd
# # import streamlit as st
# # import streamlit.components.v1 as components
# #
# # def got_func(physics):
# #   got_net = Network(height="600px", width="100%", font_color="black",heading='Game of Thrones Graph')
# #
# # # set the physics layout of the network
# #   got_net.barnes_hut()
# #   got_data = pd.read_csv("https://www.macalester.edu/~abeverid/data/stormofswords.csv")
# #   #got_data = pd.read_csv("stormofswords.csv")
# #   #got_data.rename(index={0: "Source", 1: "Target", 2: "Weight"})
# #   sources = got_data['Source']
# #   targets = got_data['Target']
# #   weights = got_data['Weight']
# #
# #   edge_data = zip(sources, targets, weights)
# #
# #   for e in edge_data:
# #     src = e[0]
# #     dst = e[1]
# #     w = e[2]
# #
# #     got_net.add_node(src, src, title=src)
# #     got_net.add_node(dst, dst, title=dst)
# #     got_net.add_edge(src, dst, value=w)
# #
# #   neighbor_map = got_net.get_adj_list()
# #
# # # add neighbor data to node hover data
# #   for node in got_net.nodes:
# #     node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
# #     node["value"] = len(neighbor_map[node["id"]])
# #   if physics:
# #     got_net.show_buttons(filter_=['physics'])
# #   got_net.show("gameofthrones.html")
# #
# #
# # def simple_func(physics):
# #   nx_graph = nx.cycle_graph(10)
# #   nx_graph.nodes[1]['title'] = 'Number 1'
# #   nx_graph.nodes[1]['group'] = 1
# #   nx_graph.nodes[3]['title'] = 'I belong to a different group!'
# #   nx_graph.nodes[3]['group'] = 10
# #   nx_graph.add_node(20, size=20, title='couple', group=2)
# #   nx_graph.add_node(21, size=15, title='couple', group=2)
# #   nx_graph.add_edge(20, 21, weight=5)
# #   nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
# #
# #
# #   nt = Network("500px", "500px",notebook=True,heading='')
# #   nt.from_nx(nx_graph)
# #   #physics=st.sidebar.checkbox('add physics interactivity?')
# #   if physics:
# #     nt.show_buttons(filter_=['physics'])
# #   nt.show('test.html')
# #
# #
# # def karate_func(physics):
# #   G = nx.karate_club_graph()
# #
# #
# #   nt = Network("500px", "500px",notebook=True,heading='Zachary’s Karate Club graph')
# #   nt.from_nx(G)
# #   #physics=st.sidebar.checkbox('add physics interactivity?')
# #   if physics:
# #     nt.show_buttons(filter_=['physics'])
# #   nt.show('karate.html')
# #
# #   #Network(notebook=True)
# # st.title('Hello Pyvis')
# # # make Network show itself with repr_html
# #
# # #def net_repr_html(self):
# # #  nodes, edges, height, width, options = self.get_network_data()
# # #  html = self.template.render(height=height, width=width, nodes=nodes, edges=edges, options=options)
# # #  return html
# #
# # #Network._repr_html_ = net_repr_html
# # st.sidebar.title('Choose your favorite Graph')
# # option=st.sidebar.selectbox('select graph',('Simple','Karate', 'GOT'))
# # physics=st.sidebar.checkbox('add physics interactivity?')
# # simple_func(physics)
# #
# # if option=='Simple':
# #   HtmlFile = open("test.html", 'r', encoding='utf-8')
# #   source_code = HtmlFile.read()
# #   components.html(source_code, height = 900,width=900)
# #
# #
# # got_func(physics)
# #
# # if option=='GOT':
# #   HtmlFile = open("gameofthrones.html", 'r', encoding='utf-8')
# #   source_code = HtmlFile.read()
# #   components.html(source_code, height = 1200,width=1000)
# #
# #
# #
# # karate_func(physics)
# #
# # if option=='Karate':
# #   HtmlFile = open("karate.html", 'r', encoding='utf-8')
# #   source_code = HtmlFile.read()
# #   components.html(source_code, height = 1200,width=1000)
