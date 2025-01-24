import os
import sys
from pathlib import Path
sys.path.append('../almaqso')  # isort:skip
from almaqso.download_archive import download_archive
from almaqso.analysis import analysis

CURRENT_DIR = Path(__file__).parent
CASA_PATH = os.environ.get('ALMAQSO_CASA', 'casa')
DATA_PATH = './uid___A002_Xd68367_X9885'
TARFILE = './2018.1.01575.S_uid___A002_Xd68367_X9885.asdm.sdm.tar'

# Edit the following constants.
DOWNLOAD = True  # True: Download the tar file, False: Use the existing tar file
MODE = 'calonly'


def test_download():
    if DOWNLOAD:
        os.system(f'rm -rf {TARFILE}')
        download_archive(4, 'catalog/test_2.json')
        assert os.path.exists(TARFILE)


def test_analysis():
    os.system(f'rm -rf {DATA_PATH}')

    if MODE == 'aftercal':
        os.system(f'cp -r {DATA_PATH}_backup {DATA_PATH}')

    analysis('.', casacmd=CASA_PATH)

    if MODE == 'calonly':
        os.system(f'rm -rf {DATA_PATH}_backup')
        os.system(f'cp -r {DATA_PATH} {DATA_PATH}_backup')
