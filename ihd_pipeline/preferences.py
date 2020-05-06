import os
from yacs.config import CfgNode

_PREFERENCES_FILE = os.path.join(
    os.path.join(os.path.dirname(__file__), "preferences.yaml")
)


class _Preferences(CfgNode):
    DATA_DIR = ""
    CACHE_DIR = "~/.ihd_pipeline/cache"
    MODELS_DIR = ""

    BATCH_SIZE = 16
    NUm_WORKERS = 0


def save_preferences(filename=None):
    if filename is None:
        filename = _PREFERENCES_FILE
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        f.write(PREFERENCES.dump())


PREFERENCES = _Preferences()
if not os.path.isfile(_PREFERENCES_FILE):
    save_preferences()
else:
    PREFERENCES.merge_from_file(_PREFERENCES_FILE)
