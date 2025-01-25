# NWGraph

Graph library built on top of Pytorch to help the creation of GNNs.

Implementation based on (working draft) semantics defined at: https://www.overleaf.com/read/vfbqdgxtxnws

It does not define any trainer code (so no lightning), just graph semantics, edges, nodes and message passing. The
training code is left to be done on a project by project basis.

## Examples

- See [ngclib](https://gitlab.com/neural-graph-consensus/ngclib/-/tree/master/ngclib/trainer) trainer code, for example
where they define a sequential way of training each edge independently. Upon training, the entire graph is loaded
into memory to produce pseudo-labels, followed by a semi-supervised iteration. LME is used here for training.

- See [mnist-ensemble-graph](https://gitlab.com/meehai/ml-experiments/-/tree/master/mnist-ensemble-graph) for a simple
example where we train 5 edges in the same time. Each edge starts from a RGB image.
Simple pytorch-lightning Trainer code is used here.
