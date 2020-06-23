from .Module import *
from hdff import *

class HDFileModule(Module):
    def __init__(self, parent=None):
        super(HDFileModule, self).__init__(parent)
        self.makeOutputPort("EGgraph", ExtremumGraph)
        self.makeOutputPort("data", HDData)

    #### FIXME the current load path is fix on the server ####
    def load(self, filename, isIncludeFunctionIndexInfo=False, cube_dim=2):
        # New is the flag stating whether there is the new hdfile file
        ## convert from unicode to ascii
        filename = str(filename)
        print("##### Load file:", filename, "  ######")
        collection = DataCollectionHandle()
        print("here1")
        collection.attach("data/"+filename)
        print("here2")
        dataset = collection.dataset(0)
        print("here3")
        # load EG
        handle = dataset.getDataBlock(0)
        print("handle: ", handle)
        print("EGRAPH: ", self.EGgraph)
        self._extremum_graph = ExtremumGraph()
        self._extremum_graph.load(handle, isIncludeFunctionIndexInfo, cube_dim)
        self.EGgraph.setData(self._extremum_graph)
        print("EGgraph data set")