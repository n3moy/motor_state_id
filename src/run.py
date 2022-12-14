import yaml
from yaml.loader import SafeLoader
import logging
import argparse
from pathlib import Path
from datetime import datetime
from utils import train_model, test_model, inference


def get_args():
    parser = argparse.ArgumentParser(
        description='NN pipeline'
    )
    parser.add_argument(
        '--config',
        type=str, default=Path(__file__).parent.parent / 'configs' / 'model' / 'train.yaml',
        help='Config path'
    )
    parser.add_argument(
        '--mode',
        type=str, default='train',
        choices=['train', 'test', 'inference'],
        help='Run mode'
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    config_path = args.config
    config = yaml.load(open(config_path), Loader=SafeLoader)
    mode = args.mode
    
    time = datetime.today().date().isoformat()
    log_filename = f'logging_{time}.log'
    log_path = Path(__file__).parent.parent / 'logs' / mode / log_filename
    logging.basicConfig(
        filename=log_path, 
        level=logging.DEBUG, 
        format='%(asctime)s %(levelname)s: %(message)s',
        filemode='a+'
    )

    if mode == 'train':
        train_model(config_path=config_path)
    if mode == 'test':
        test_model(config_path=config_path)
    if mode == 'inference':
        inference(config_path=config_path)


