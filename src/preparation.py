from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path
from typing import List
from zipfile import ZipFile

# Public Modules
import requests

# import pdb

# Internal Modules

# Classes


@dataclass(frozen=True, slots=True)
class DataGetter:
    """Class for fetching the data from overwatchleague (Blizzard's published free data for Overwatch)"""

    dataFolder: Path = Path(__file__).parent.parent / "data" / "raw"

    website: str = "https://overwatchleague.com/en-us/statslab"

    downloadLinksList: dict = field(
        default_factory=lambda: {
            "stats_2018": "https://assets.blz-contentstack.com/v3/assets/blt321317473c90505c/bltc1b83b55692b42f4/5e4c1368de213a0dff736e29/phs_2018.zip",
            "stats_2019": "https://assets.blz-contentstack.com/v3/assets/blt321317473c90505c/blt034e0b484f2dae47/5e4c1369b6a7c40dd9c69e9f/phs_2019.zip",
            "stats_2020": "https://assets.blz-contentstack.com/v3/assets/blt321317473c90505c/blt5ee09cc6725e80eb/60b956b0b078b00d8a90a3dc/phs_2020.zip",
            "stats_2021": "https://assets.blz-contentstack.com/v3/assets/blt321317473c90505c/blt27d1892d31782bff/6154e94b19501a1ef19120a0/phs_2021-1.zip",
            "maps_stats": "https://assets.blz-contentstack.com/v3/assets/blt321317473c90505c/blt4c7ee43fcc7a63c2/61537dcd1bb8c23cf8bbde70/match_map_stats.zip",
        }
    )

    def run(self):
        self.dataFolder.mkdir(parents=True, exist_ok=True)
        for key, value in self.downloadLinksList.items():
            resp = requests.get(value)
            with ZipFile(BytesIO(resp.content)) as zipfile:
                zipfile.extractall(self.dataFolder)
