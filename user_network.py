"""Parse Yelp Dataset Challenge data to list of objects.
"""

import simplejson as json
import networkx as nx
import matplotlib.pyplot as plt

json_file_path='/Users/juju/Downloads/yelp_data/yelp_data_user.json'

data=[]
with  open(json_file_path) as f:
      for line in f:
          data.append(json.loads(line))
          
       


"""Get user_id list"""        
user=[]       
for i in range(0, len(data)):
    user.append(data[i]['user_id'])

"""Build social network graph"""
"""Add nodes"""
G= nx.path_graph(len(user))
mapping= dict(zip(G.nodes(),user))
H=nx.relabel_nodes(G,mapping)

"""Add Edges"""
friends=[]
for i in range(0, len(data)):
    for j in range(0, len(data[i]['friends'])):
        friends.append((user[i],data[i]['friends'][j]))

H.add_edges_from(friends)

nx.draw(G)
         



class SocialNetworkGraph(object):
      user=""
      friends=[]
      
      def __int__(self):
          self.user=user
          self.friends=friends
          
         
         
         
class AjacencyListGraph(object):
    def __int__(self):
        self.node={}
        self.adj={}
        
    def add_node(self, node, **attrs):
        if node not in self.adj:
           self.adj[node]={}
           self.node[node]=attrs
        else #update attr even if node already exists
           self.node[node].update(attrs)
           
    def add_edge(self, u, v, **attrs):
        if u not in self.adj:
            self.adj[u]={}
            self.node[u]={}
        if v not in self.adj:
            self.adj[v]={}
            self.node[v]={}
            
        datadict=self.adj[u].get(v,{})
        datadict.update(attrs)
        
        self.adj[u][v]=datadict
        self.adj[v][u]=datadict
        
        
                

   