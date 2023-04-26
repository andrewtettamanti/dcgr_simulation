# DCGR Simulation

## Running the simulation
1. Make sure the required Python modules are installed: `pip3 install numpy scipy mesa`
2. Run the visualization server: `python3 run_model_vis.py`
3. If it does not open automatically in a browser, go to `localhost:8521`

## CLI Options

```
-i                          used to provide path to json file containing initial agent states
-m                          used to provide path to json file containing model parameters
-nv                         if present, simulator runs without web server visualization
--make-contact-plan         used to generate a contact plan between RouterAgents within the simulator
                                (must have a max_step number in model params)
```

## Running the rssi simulation

```
python3 run_model_vis.py -i 'simulations/rssi_scenario/rssi_scenario.json' -m 'simulations/rssi_scenario/rssi_scenario_modelparams.json'

```

### Experimental RSSI Interpolation used for simulation 

Under the rssi directory, the rssi data is interpolated in a jupyter notebook

