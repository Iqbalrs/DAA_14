#!/usr/bin/env python
# coding: utf-8

# In[42]:


import networkx as nx
import matplotlib.pyplot as plt


# In[43]:


vertices = range(1,10)
edges = [(7,2), (2,3), (7,4), (4,5), (7,3), (7,5), (1,6), (1,7), (2,8), (2,9)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True,node_color='y' ,node_size=800)


# In[44]:


nx.closeness_centrality(G)


# In[45]:


nx.degree_centrality(G)


# In[46]:


nx.betweenness_centrality(G)


# In[47]:


nx.closeness_centrality(G)


# In[48]:


centrality = nx.eigenvector_centrality(G)


# In[49]:


sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())


# In[50]:


vertices = range(1,9)
edges = [(7,2), (2,3), (3,1), (7,4), (4,2), (4,5), (7,3), (7,5), (5,1), (1,4), (1,6), (6,3), (6,5), (1,7), (8,9), (2,9)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True,node_color='y' ,node_size=1000)


# In[51]:


centrality = nx.eigenvector_centrality(G)


# In[52]:


sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())


# In[53]:


vertices = range(1,15)
edges = [(1,4), (1,10), (1,2), (2,11), (2,15), (2,12), (2,3), (3,5), (3,13), (2,6), (6,7), (6,8), (6,9), (6,14)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True,node_color='y' ,node_size=1000)


# In[54]:


centrality = nx.eigenvector_centrality(G)


# In[55]:


sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())


# In[ ]:




