import random, asyncio, sys, os
from collections import deque
from functools import reduce
from re import A
import copy
import time, math, requests,json
import random
from datetime import datetime
import concurrent.futures
import threading
from toolz.itertoolz import reduceby
from web3 import Web3
import eth_abi
import web3



import abi 
from polygon_info import pairs 
import utils, polygon_info


get_rates_contract = utils.web3.eth.contract(
    abi=abi.alpha1_abi,
    address='0x3Da0baa6D3cb200811ff6Ae10dbF29a8CC5E6772'
).functions



lock = threading.Lock()
dir = os.getcwd()



class Creategraph:
    def __init__(self):
        self.graph = {}
    
    def edges(self, vertice):
        return self.graph[vertice]
    def all_vertices(self):
        return self.graph.keys()
    
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self,edge):
        edge = tuple(edge)
        #print(edge)
        for v1,v2,w, exchange in edge:
            if v1 not in self.graph:
                with lock:
                    self.graph[v1] = {}
            if v2 not in self.graph:
                with lock:
                    self.graph[v2] = {}
            if not self.graph[v1].get(v2, None):
                with lock:
                    self.graph[v1][v2] = {exchange: w}
            else:
                with lock:
                    self.graph[v1][v2].update({exchange: w})
         

    def update_edges(self,edge):
        edge = tuple(edge)
        for v1,v2,w, exchange in edge:
            prev_edge = copy.deepcopy(self.graph[v1][v2])
            #print(f'\n Updating prev edge {prev_edge}       line 51\n')
            with lock:
                self.graph[v1][v2].update({exchange: w})
            new_edge =self.graph[v1][v2]
            #print(f'\n New edge {new_edge}       line 53 \n')
            '''with lock:
                with open(f'{dir}/arbitrage_results.txt', 'a') as file:
                    file.write(f'Prev Edge {prev_edge} \n New Edge {new_edge} \n Graph len {len(self.graph)}\n\n')'''
            
    """
    Function used during parallel computation, used to create graph from data gotten from get_exchange_rate function
    """
    def add_edges(self,edge):
        edge = tuple(edge)
        for v1,v2,w in edge:
            if v1 not in self.graph:
                self.graph[v1] = {}
            if v2 not in self.graph:
               self.graph[v2] = {}
            self.graph[v1][v2] = w
        print('added edge')

    
    def view_graph(self, readable=False):
        if readable:
            readable = {
                self.tokens[token]['symbol']: {self.tokens[neighbor]['symbol']: exchanges for neighbor, exchanges in neighbors.items() } for token,neighbors in self.graph.items()}
            print(readable)
        else:
            print(self.graph)
       
        
    def return_graph(self):
        return self.graph


class Arbitrage(Creategraph):
    def __init__(self, graph={},tokens={}, pairs={}):
        self.graph = graph
        self.tokens = tokens
        self.pairs = copy.deepcopy(pairs)
        self.len = len(graph.keys())
        self.epochs = 0
        self.tx_count = 0
        self.stop = False
        self.success = False
        self.prev_block_number = 0
        self.choice_tokens = polygon_info.choice_tokens
    

    def init_params(self, start, multiplier=1):
        self.start = start
        self.end = None
        self.parents = {key: None for key in self.graph}
        self.costs = {key: 0 for key in self.graph}
        self.positive_cycle_with_start = False
        self.positive_cycle = False
        self.paths = {key: [] for key in self.graph}
        self.multiplier = multiplier
        
    def add_graph(self, graph):
        self.graph = graph

    def fees(self,cost):
        return 0 #((0.59/100) * cost)
    def get_best_rates(self,exchange_rates):
        exchange = None
        best_rate = 0
        for _exchange, _exchange_rate in exchange_rates.items():
            if _exchange_rate > best_rate:
                best_rate = _exchange_rate 
                exchange = _exchange
        return (exchange, best_rate)

    def get_potential_excluded_path(self, token):
        def _(neighbor, exchange):
            return f'{token} {neighbor} {exchange}'                #{neighbor:{'token':token, 'exchange': exchange}}

        return _


    def run_graph(self, graph, start, start_cost, multiplier=0):
        graph = copy.deepcopy(self.graph)
        paths = {key: deque([]) for key in graph}
        parents = {key: None for key in graph}
        costs = {key: 0 for key in graph}
        costs[start] = start_cost
        excluded_paths  = self.tokens[start].get('excluded_paths',set([]))
       
        for i in range(len(graph.keys()) -1 ) :
            # deduct previous fees if i == self.multiplier 
            
            for (token, neighbors) in graph.items():
                for neighbor, exchange_rates in neighbors.items():  
                    exchange = None
                    best_rate = 0
                    for _exchange, _exchange_rate in exchange_rates.items():
                        if _exchange_rate > best_rate:
                            best_rate = _exchange_rate 
                            exchange = _exchange
                    
                  
                                          
                    new_cost  = costs[token]  * best_rate
                    not_in_excluded_paths = f'{token} {neighbor} {exchange}' not in excluded_paths
                    
                
                    if( costs[neighbor] < new_cost) and not_in_excluded_paths:
                        # self.path neighbor will be the self.path[node] plus the node
                        # logic is that if this node is the new parent,
                        # get the path to this node add the node to it
                     
                        new_path = list(paths[token])
                        new_path.append({'token':token, 'exchange': exchange})
                        if new_path in paths[neighbor]:
                            pass
                        else:
                            i = 0                     
                            while True:
                                cycles_index_of_i = self.get_next_index(new_path[i],new_path)                   
                                if len(cycles_index_of_i):                               
                                    new_path = [*new_path[:(cycles_index_of_i[0]+1)]]
                                    if len(cycles_index_of_i)> 1:
                                        new_path = [*new_path,*new_path[(cycles_index_of_i[-1]+1):]]
                                else:
                                    pass
                                i+=1
                                if i== len(new_path):
                                    break
                            paths[neighbor] = deque(new_path)

                        costs[neighbor] = new_cost
                        parents[neighbor] = token

           



        #print(paths)
        paths_with_cycles = []
        best_path = None
        #1 + 0.1% 
        best_cost = 1.0009
        profit_percent = None
        amounts = []

        for start, path in paths.items(): 
            if len(path) > 2:
                    
                    #path = [path[i] for i in range(len(path)) if i == (len(path) - 1) or path[i+1] != path[i]]
                    #get the cyces
                    #index where start_token occurs in path, excluding path[0] 

                    indices_of_start = self.get_next_index(path[0], path)
                    #print(len(indices_of_start), len(path), self.tokens[path[0]['token']]['symbol'])
                    if len(indices_of_start):               
                        #get the first cycle [path[0] up to next path[0]+1]
                        _path = [path[i] for i in range(indices_of_start[0]+1)]
                        #print(len(_path))
                        _start_cost = 1
                        _amounts = [1]
                        if _path and (_path[0] == _path[-1]):                         
                            for i in range(len(_path) - 1):
                                # get the next token's exchange rate 
                                next = max(graph[_path[i]['token']][_path[i+1]['token']].values())
                                _start_cost = (_start_cost - self.fees(_start_cost)) * next
                                _amounts.append(_start_cost)
                            # if start cost greater than 1 + 0.12%   
                                
                        
                            if _start_cost >= best_cost:
                                    best_path = _path
                                    best_cost = _start_cost
                                    amounts = _amounts 

                
        if best_path:
            profit_percent = (best_cost - 1)/ 1 * 100
        print(best_cost)
        return [best_path, profit_percent, amounts]


    def get_exchange_rates(self):
        for exchange, pairs in self.pairs.items():
            #pass in an array of pairs and bool that specifies whether token details should be returned
            
            infos = get_rates_contract.getRates(list(pairs.keys()), True).call()
            for i in range(len(pairs)):
                (
                    pair_addr, token0_addr,token1_addr, 
                    decimals0,decimals1,  symbol0, symbol1, reserves 
                ) = infos[i]

                if not self.pairs[exchange].get(pair_addr):
                    self.pairs[exchange][pair_addr] = {}

                if self.pairs[exchange][pair_addr].get('token0', None):
                        
                        self.pairs[exchange][pair_addr].update({
                                'reserve0': reserves[0],
                                'reserve1': reserves[1], 
                        })
                    
                        token0_addr = self.pairs[exchange][pair_addr].get('token0')
                        token1_addr = self.pairs[exchange][pair_addr].get('token1')

                        if not (
                            token0_addr in polygon_info.choice_tokens or
                            token1_addr in polygon_info.choice_tokens
                        ):
                            return []

                        symbol0 = self.tokens[token0_addr]['symbol']
                        symbol1 = self.tokens[token1_addr]['symbol']
                        decimals0 = self.tokens[token0_addr]['decimals']
                        decimals1 = self.tokens[token1_addr]['decimals']
                        exchange_rate1 = (1*10**decimals0*997 * reserves[1]) / (reserves[0]* 1000 +( 1*10**decimals0*997)) / 10**decimals1
                        exchange_rate0 = (1*10**decimals1*997 * reserves[0]) / (reserves[1]* 1000 + (1*10**decimals1*997) ) / 10**decimals0
                        self.tokens[token0_addr]['pairs'][pair_addr].update({
                                'reserves': reserves,
                                'reserve': reserves[0],
                                'exchange_rate': exchange_rate1
                        })
                    
                        self.tokens[token1_addr]['pairs'][pair_addr].update({
                            'reserves': reserves,
                            'reserve': reserves[1],
                            'exchange_rate': exchange_rate0
                        
                        })

                else:
                    exchange_rate1 = (1*10**decimals0*997 * reserves[1]) / (reserves[0]* 1000 +( 1*10**decimals0*997)) / 10**decimals1
                    exchange_rate0 = (1*10**decimals1*997 * reserves[0]) / (reserves[1]* 1000 + (1*10**decimals1*997) ) / 10**decimals0
                    self.pairs[exchange][pair_addr] = {
                        'address': pair_addr,
                        'token0':token0_addr,
                        'token1': token1_addr,
                        'symbol0': symbol0,
                        'symbol1': symbol1,
                        'decimals0': decimals0,
                        'decimals1': decimals1,
                        'reserve0': reserves[0],
                        'reserve1': reserves[1], 
                    }
                
            
                    if self.tokens.get(token0_addr, None): 
                        self.tokens[token0_addr]['pairs'][pair_addr] = {
                                    'pair': pair_addr,
                                    'exchange': exchange,
                                    'is_token_0': True,
                                    'reserves': reserves,
                                    'token0': token0_addr,
                                    'token1': token1_addr,
                                    'reserve': reserves[0],
                                    'exchange_rate': exchange_rate1
                        }
                    else:
                        self.tokens[token0_addr] = {
                            'symbol': symbol0,
                            'address': token0_addr,
                            'decimals':decimals0,
                            'pairs': {
                                pair_addr: {
                                    'pair': pair_addr,
                                    'exchange': exchange,
                                    'is_token_0': True,
                                    'reserves': reserves,
                                    'token0': token0_addr,
                                    'token1': token1_addr,
                                    'reserve': reserves[0],
                                    'exchange_rate': exchange_rate1

                                }
                            }
                        }

                    if self.tokens.get(token1_addr, None): 
                        self.tokens[token1_addr]['pairs'][pair_addr] =  {
                                    'pair': pair_addr,
                                    'exchange': exchange,
                                    'is_token_0': False,
                                    'reserves': reserves,
                                    'token0': token0_addr,
                                    'token1': token1_addr,
                                    'reserve': reserves[1],
                                        'exchange_rate': exchange_rate0

                                }
                    else:
                        self.tokens[token1_addr] = {
                                'symbol': symbol1,
                                'address': token1_addr,
                                'decimals': decimals1,
                                'pairs': {
                                    pair_addr: {
                                        'pair': pair_addr,
                                        'exchange': exchange,
                                        'is_token_0': False,
                                        'reserves': reserves,
                                        'token0': token0_addr,
                                        'token1': token1_addr,
                                        'reserve': reserves[1],
                                        'exchange_rate': exchange_rate0

                                        
                                    }
                                }
                            }
                                
                
                edge = [(token0_addr, token1_addr,exchange_rate1, exchange),(token1_addr, token0_addr ,exchange_rate0, exchange)]
                self.add_edge(edge)
              


    def run(self):
        while True:
            if len(self.graph):
                for start in self.choice_tokens:
                    (path, profit_percent, amounts) = self.run_graph(self.graph, start, 1)
                    if path:
                        print('found a profitable path',  path)


                        #next step, connect a flashloan contract 
                        # and execute a swap with this path
                        

                #sleep for polygon avg block time
            time.sleep(2)

    def get_next_index(self,i, path):
        a= []
        r = 1
        while r < len(path):
        
            try:
                w = path.index(i, path.index(i)+r)
                a.append(w)
                r+=w    
            except:
                break
        return a

    def update_rates(self):
        while True:
            self.get_exchange_rates()
            #sleep for polygon avg block time
            time.sleep(2)



r = Arbitrage(pairs=pairs)


#update rates every 2 seconds
thread0 = threading.Thread(target=r.update_rates)
thread0.start()
# run graph every 2 seconds and capture opportunities
thread1 = threading.Thread(target=r.run)
thread1.start()

