import torch
import torch.nn as nn
from torch_geometric.nn import GATv2Conv

class Model(nn.Module):
    def __init__(self, input_dim, output_dim, **kwargs):
        super().__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_dim = kwargs.get("hidden_dim", 64)
        self.num_layers = kwargs.get("num_layers", 8)
        self.n_heads = kwargs.get("n_heads", 4)
        self.linear_in = nn.Linear(self.input_dim, self.hidden_dim)
        self.conv = GATv2Conv(2*self.hidden_dim, self.hidden_dim, heads=self.n_heads, add_self_loops=False)
        self.activation = nn.Tanh()
        self.g_embed = nn.Linear(self.hidden_dim, self.output_dim)

    def forward(self, data):
        feat = data.feat
        edge_index = data.edge_index
        current_state = data.current_state
        h_0 = self.linear_in(feat.float())
        h = h_0
        for i in range(self.num_layers):
            h = self.conv(torch.cat([h, h_0], dim=1), edge_index).view(h.shape[0], self.n_heads, self.hidden_dim).sum(dim=1)
            h = self.activation(h)
        hg = h[current_state.bool()]
        return self.g_embed(hg)
