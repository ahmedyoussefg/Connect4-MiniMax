import { Nodes, Edges, Layouts } from "v-network-graph"
import { reactive } from "vue"

const nodes: Nodes = {
  node1: { name: "N1" , icon: "&#xe5c7"},
  node2: { name: "N2" , icon: "&#xe5c5"},
  node3: { name: "N3" , icon: "&#xe5c5"},
  node4: { name: "N4" , icon: "&#xe5c7"},
  node5: { name: "N5" , icon: "&#xe5c5"},
  node6: { name: "N6" , icon: "&#xe5c5"},
  node7: { name: "N7" , icon: "&#xe5c7"},
}

const edges: Edges = {
  edge1: { source: "node1", target: "node2" },
  edge2: { source: "node2", target: "node3" },
  edge3: { source: "node3", target: "node4" },
  edge4: { source: "node3", target: "node5" },
  edge5: { source: "node2", target: "node6" },
  edge6: { source: "node6", target: "node7" },
}

const layouts: Layouts = reactive({
  nodes: {},
})

export default {
  nodes,
  edges,
  layouts,
}