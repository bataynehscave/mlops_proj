import logging
import os 
from pathlib import Path

list_of_files = [
    '.github/workflows/.gitkeep',
    'src/__init__.py',
    'src/logger/logging.py',
    'src/exception/exception.py'
    'src/components/__init__.py',
    'src/componenets/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evaluation.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    'init__setup.sh',
    'requirments.txt',
    'requirments_dev.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',
    'experiment/experiments.ipynb',

]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"creating directory: {file_dir} for file {file_name}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        


