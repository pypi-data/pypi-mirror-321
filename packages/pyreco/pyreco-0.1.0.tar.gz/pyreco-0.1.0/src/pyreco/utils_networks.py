"""
Helper routines for networks
"""
import networkx as nx
import numpy as np


def gen_ER_graph(nodes: int, density: float, spec_rad: float = 0.9, directed: bool=True, seed=None):
    """Generate an Erdős-Rényi random graph with specified properties.
    
    Bug Fix Documentation:
    ---------------------
    Previous Bug:
        The line `G.remove_nodes_from(list(nx.isolates(G)))` removed isolated nodes from the graph
        before converting to a numpy array. This caused the final matrix to sometimes be smaller
        than the specified size (e.g., 29x29 instead of 30x30) when isolated nodes were present.
        This led to dimension mismatches in reservoir computations where other matrices expected
        the full size.

    Solution:
        Instead of removing isolated nodes, we now connect them to maintain the specified
        network size. This ensures consistency between the reservoir weight matrix and
        other matrices in the computation.

    Parameters:
        nodes (int): Number of nodes in the graph
        density (float): Desired connection density (0 to 1)
        spec_rad (float): Desired spectral radius
        directed (bool): Whether to create a directed graph
        seed (int, optional): Random seed for reproducibility

    Returns:
        np.ndarray: Adjacency matrix with shape (nodes, nodes)
    """
    # use networkx to generate a random graph
    G = nx.erdos_renyi_graph(nodes, density, seed=seed, directed=directed)

    # Instead of removing isolated nodes (old buggy behavior):
    # G.remove_nodes_from(list(nx.isolates(G)))
    
    # New: Connect isolated nodes to maintain matrix size
    isolated_nodes = list(nx.isolates(G))
    if isolated_nodes:
        non_isolated = list(set(G.nodes()) - set(isolated_nodes))
        for node in isolated_nodes:
            if non_isolated:
                target = np.random.choice(non_isolated)
                G.add_edge(node, target)
                if directed:
                    G.add_edge(target, node)

    GNet = nx.to_numpy_array(G)
    curr_spec_rad = max(abs(np.linalg.eigvals(GNet)))
    graph = GNet * spec_rad/curr_spec_rad

    return graph


def compute_density(network: np.ndarray) -> float:
    # compute density of a given adjacency matrix by the fraction of non-zero entries over  N^2
    if type(network) is not np.ndarray:
        raise (TypeError('Expect a np.ndarray as reservoir network'))

    # check if the matrix is square
    if network.shape[0] != network.shape[1]:    
        raise (ValueError('Expect network of square size!'))

    N = len(network)
    num_links = np.sum(network.flatten()>0)
    return num_links / (N**2)


def get_num_nodes(network: np.ndarray) -> int:

    # returns the number of nodes in the given network. Assumes the adjacency matrix to be of square size
    if type(network) is not np.ndarray:
        raise (TypeError('Expect a np.ndarray as reservoir network'))

    if network.shape[0] != network.shape[1]:
        raise (ValueError('Expect network of square size!'))

    non_zero_rows = np.any(network != 0, axis=1)

    # Identify columns that are not entirely zero
    non_zero_columns = np.any(network != 0, axis=0)

    # Identify nodes where both row and column are not zero
    non_isolated_nodes = np.where(non_zero_rows & non_zero_columns)[0]

    # Number of non-isolated nodes
    num_non_isolated_nodes = len(non_isolated_nodes)

    return num_non_isolated_nodes


def compute_spec_rad(network: np.ndarray) -> float:
    # compute the spectral radius of the network (max. eigenvalue)
    if type(network) is not np.ndarray:
        raise (TypeError('Expect a np.ndarray as reservoir network'))

    if network.shape[0] != network.shape[1]:
        raise (ValueError('Expect network of square size!'))

    return np.max(np.abs(np.linalg.eigvals(network)))


def set_spec_rad(network: np.ndarray, spec_radius:float) -> np.ndarray:
    # obtains a network with given spectral radius

    if spec_radius <= 0:
        raise(ValueError('spectral radius must be larger than zero'))
    elif (spec_radius > 1.0):
        raise(Warning('a spectral radius larger than 1 is unusual!'))

    # compute current spectral radius
    current_spectral_radius = compute_spec_rad(network)

    if current_spectral_radius < 10**(-9):
        print('spectral radius smaller than 10^-9!')
        current_spectral_radius = 10**(-6)

    scaling_factor = spec_radius / current_spectral_radius


    return network * scaling_factor


def is_zero_col_and_row(x: np.ndarray, idx: int) -> bool:
    # returns zero if adjacency matrix x carries only zeros in column and row of index idx (i.e. missing node)

    is_zero_column = np.all(x[:, idx] == 0)
    is_zero_row = np.all(x[idx, :] == 0)

    if is_zero_column and is_zero_row:
        return True
    else:
        return False


def remove_node(x: np.ndarray, idx: int | list) -> np.ndarray:
    if type(idx) is not list:
        idx = [idx]

    if x.ndim == 1:
        for idxx in idx:
            x[idxx] = 0
    elif x.ndim == 2:
        for idxx in idx:
            x[:, idxx] = 0
            x[idxx, :] = 0

    return x

def gen_init_states(num_nodes: int, method: str = 'random'):
    # returns an array of length <num_nodes>
    # creates the entries based on different sampling methods
    # when not setting specific values, the range is normalized to abs(1)

    if method == 'random':
        init_states = np.random.random(num_nodes)
    elif method == 'random_normal':
        init_states = np.random.randn(num_nodes)
    elif method == 'ones':
        init_states = np.ones(num_nodes)
    elif method == 'zeros':
        init_states = np.zeros(num_nodes)
    else:
        raise(ValueError(f'Sampling method {method} is unknown for generating initial reservoir states'))

    # normalize to max. absolute value of 1
    if method != 'zeros':
        init_states = init_states / np.max(np.abs(init_states))

    return init_states

def extract_density(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    return nx.density(G)

def extract_spectral_radius(adjacency_matrix):
    return np.max(np.abs(np.linalg.eigvals(adjacency_matrix)))

def extract_in_degree_av(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    in_degrees = G.in_degree()
    avg_in_degree = np.mean(list(dict(in_degrees).values()))
    return avg_in_degree

def extract_out_degree_av(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    out_degrees = G.out_degree()
    avg_out_degree = np.mean(list(dict(out_degrees).values()))
    return avg_out_degree

def extract_clustering_coefficient(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    return nx.average_clustering(G)

def extract_node_degree(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    return dict(G.degree())

def extract_node_in_degree(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    return dict(G.in_degree())

def extract_node_out_degree(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    return dict(G.out_degree())

def extract_node_clustering_coefficient(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    return nx.clustering(G)

def extract_node_betweenness_centrality(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    return nx.betweenness_centrality(G)

def extract_node_pagerank(adjacency_matrix):
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    return nx.pagerank(G)

# Add more network property extraction functions as needed
