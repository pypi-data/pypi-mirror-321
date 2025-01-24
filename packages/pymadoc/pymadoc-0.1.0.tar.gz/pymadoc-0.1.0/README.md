# pyMADOC

Python package to download and combine parts of MADOC dataset from Zenodo (record: 14637314).

## Installation

```bash
pip install pymadoc
```

## Usage

### As a Python Package

```python
from pymadoc import list_available_data, download_file, download_community_pair

# List available platforms and communities
data_info = list_available_data()
print(data_info["platforms"])  # ['reddit', 'voat', 'bluesky', 'koo']
print(data_info["communities"])  # ['CringeAnarchy', 'fatpeoplehate', ...]

# Download a specific file
# For Reddit/Voat, specify both platform and community
file_path = download_file("reddit", community="funny", output_dir="data")
# For Bluesky/Koo, specify only platform
file_path = download_file("bluesky", output_dir="data")

# Load directly as DataFrame
df = download_file("reddit", community="funny", as_dataframe=True)

# Download and combine Reddit-Voat community pair
# As files
reddit_file, voat_file = download_community_pair("funny", output_dir="data")
# As combined DataFrame
combined_df = download_community_pair("funny", as_dataframe=True)
```

### Command Line Interface

List available platforms and communities:
```bash
pymadoc list
```

Download a specific file:
```bash
# Reddit/Voat (requires community)
pymadoc download reddit --community funny --output-dir data
# Bluesky/Koo
pymadoc download bluesky --output-dir data
```

Download Reddit-Voat community pair:
```bash
pymadoc pair funny --output-dir data
```

## Available Data

### Platforms
- Reddit
- Voat
- Bluesky
- Koo

### Communities (Reddit/Voat only)
- CringeAnarchy
- fatpeoplehate
- funny
- gaming
- gifs
- greatawakening
- KotakuInAction
- MensRights
- milliondollarextreme
- pics
- technology
- videos

## License

MIT License
