# SRC-AnnaUniv-Template
This is a sample template of folders for transitioning from ipynb to py codes for SRC related works.

## Getting Started
1. Clone the repository
```
git clone https://github.com/rohithmsr/SRC-AnnaUniv-Template.git
```
2. Create a new branch
- Create a new branch for any new feature and commit the changes to keep track of it. Name the branch as the feature/task name.

## Setup your repo
- Edit [config.py](./setup/config.py) file according to your local system
- Run [main.py](./main.py)
```
$ python main.py
```

Call your helper functions here, if needed. For example:
The function that is used to verify whether the idwt of the waveform is equivalent to the actual time domain values of the waveform
```
    verify_transform.plot_verify(
        'vinn', 
        'typical_3.3V_-15.csv', 
        os.path.join(config.SPLIT_TRAIN_SET_PATH, region), 
        os.path.join(config.SPLIT_VINN_FILES_TRAIN, region)
    )
```

## Training
```
$ python train.py
```

## Predictions (Testing)
```
$ python predictions.py
```

## Metrics
```
$ python metrics.py
```

## Plot waveforms predicted
```
$ python visualize.py
```

To get the bar_plot of the metrics
```
$ python bar_plot_metrics.py
```


