import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    area_min = 3e6
    pop_min = 25e6
    big_countries = world[
        (world['area']>=area_min)
        |
        (world['population']>=pop_min)
        ]
    return big_countries[['name','population','area']]
