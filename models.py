class BotFlow:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.nodes = []

class FlowNode:
    def __init__(self, id, bot_flow_id, content):
        self.id = id
        self.bot_flow_id = bot_flow_id
        self.content = content

class FlowEdge:
    def __init__(self, id, source_node_id, target_node_id):
        self.id = id
        self.source_node_id = source_node_id
        self.target_node_id = target_node_id

class FlowExecution:
    def __init__(self, id, bot_flow_id, start_time, end_time):
        self.id = id
        self.bot_flow_id = bot_flow_id
        self.start_time = start_time
        self.end_time = end_time
