# IntelLX

intellx is a Python package that provides a simple interface for machine learning model management, training, and inference.

## Installation

```bash
pip install intellx-api
```

## Configuration

Before using IntelLX, you need to set up your API key. You can do this in two ways:

1. Create a `.env` file in your project directory:
```
INTELLX_API_KEY=your_api_key_here
```

2. Set an environment variable:
```bash
export INTELLX_API_KEY=your_api_key_here
```

## CLI Usage

IntelLX provides a command-line interface for building and running experiments.

### Building Configuration

Create a configuration file for your experiment:

```bash
intellx build --stages feature_engineering,model_tune,model_train,model_evaluate
```

Available stages:
- `feature_engineering`
- `model_tune`
- `model_train`
- `model_evaluate`

Add `--verbose` flag for detailed output:
```bash
intellx build --stages model_train,model_evaluate --verbose
```

### Running Experiments

After creating and configuring `intellx_config.yaml`, run your experiment:

```bash
intellx run
```

## API Usage

### Model Prediction

```python
from intellx import predict

# Make predictions
data = {
    "feature1": [1, 2, 3],
    "feature2": ["A", "B", "C"]
}
predictions = predict(model_name="my_model", data=data)

# Use specific model state/version
predictions = predict(model_name="my_model", data=data, model_state="production")
```

### Get Model Information

```python
from intellx import get_model_info

# Get model metadata
model_info = get_model_info(model_name="my_model")

# Get information for specific model state
model_info = get_model_info(model_name="my_model", model_state="production")
```

### Get Model Features

```python
from intellx import get_model_features

# Get list of features used by the model
features = get_model_features(model_name="my_model")

# Get features for specific model state
features = get_model_features(model_name="my_model", model_state="production")
```

## Configuration File Structure

The `intellx_config.yaml` file structure contains:

```yaml
user_name: "your_username"
project_name: "your_project"
experiment_name: "your_experiment"
experiment_description: "description"
problem_type: "classification"
data_injestion:
  data_source: ""
  data_config: ""
  target: ""
verbose: false

# Optional sections based on selected stages
feature_engineering:
  step1:
    task: ""
    expected_output: ""
  step2:
    task: ""
    expected_output: ""

model_tune:
  model1:
    model_name: ""
    parameters:
      param1:
        name: ""
        type: ""
        range: ""
    objective:
      metric: ""
      sampler: ""
      trials: ""

model_train:
  model1:
    name: ""
    source: ""
    input: ""
    output: ""

model_evaluate:
  metric1:
    name: ""
    source: ""
    input: ""
    output: ""
```

## Error Handling

The package includes built-in error handling for:
- Missing API keys
- Invalid API keys
- Missing configuration files
- Invalid configuration formats
- API request errors

For any errors, check the error message for specific instructions on how to resolve the issue.

## Support

Visit intellx.bydata.com to manage your runs and access additional documentation.