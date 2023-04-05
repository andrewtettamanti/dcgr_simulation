from model import LunarModel
from lunar_vis import LunarVis
import mesa
import json

SIM_WIDTH = 1000
SIM_HEIGHT = 550

DEFAULT_MODEL_PARAMS = json.dumps({
    # "size": (SIM_WIDTH, SIM_HEIGHT),
    "rssi_noise_stdev": 4.5,
    "rssi_noise_amp": 1,
    "model_speed_limit": 5,
})

DEFAULT_INITIAL_STATE = json.dumps({
    "agent_defaults": {
        # If this is provided, all nodes will have
        # these options. It can be overridden by an
        # individual node's options.
        "radio": {
            "detection_range": 300,
            "connection_range": 20,
        },
        "hdtn": {},
        "movement": {}
    },
    "agents": [
        # The model will create an agent for each
        # node defined here. If "id" or "pos" are
        # not provided, they will be assigned
        # randomly.
        {   
            "id": 0,
            "behavior": {
                "type": "fixed",
            },
            "pos": (SIM_WIDTH/2, SIM_HEIGHT/2),
            "hdtn": {},
        },
        {
            "behavior": {
                "type": "rssi_find_target",
                "options": {
                    "target_id": 0,
                },
            },
            "radio": {},
        },
    ]
})

vis = LunarVis(SIM_WIDTH, SIM_HEIGHT)

class ObjectOption(mesa.visualization.UserParam):
    def __init__(self, name="", value=None, choices=None, description=None):
        self.param_type = "object"
        self.name = name
        self._value = value

    @property
    def value(self):
        return json.loads(self._value)

    @value.setter
    def value(self, value):
        self._value = value

model_params = ObjectOption(
    "Model parameters",
    value=DEFAULT_MODEL_PARAMS,
)

initial_state = ObjectOption(
    "Initial agent states",
    value=DEFAULT_INITIAL_STATE,
)

server = mesa.visualization.ModularServer(
    LunarModel,
    [vis],
    "Model",
    {
        "size": (SIM_WIDTH, SIM_HEIGHT),
        "model_params":  model_params,
        "initial_state": initial_state,
    })
server.settings["template_path"] = "visualization"
server.port = 8521  # The default
server.launch(open_browser=True)
