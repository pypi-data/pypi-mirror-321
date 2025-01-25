# Harmony to Organoid

## Example output

Check out [this page](example_output/README.md) for exemplary output files.

## How to Prepare

1. **Install UV**  
   Follow the [installation guide](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) for UV.

2. **Initial Setup**  
   Running the tool for the first time will automatically install all necessary dependencies.

## How to Run

### How to run from commandline

Process your data exported from Harmony by executing the following command:

**Parameters:**

- `--index-file`: **(Required)** Path to the Harmony export index XML file (`Index.idx.xml`) or (`Index.xml`) 
  located next to the corresponding TIFF files.
- `--output-dir`: **(Required)** Path to your desired output directory.
- `--lut-min`: **(Optional)** Comma-separated minimum LUT (Lookup Table) values for each channel.
- `--lut-max`: **(Optional)** Comma-separated maximum LUT values for each channel.
- `--colors`: **(Optional)** Comma-separated colors for each channel.

**Example:**

```bash
uv run https://gitlab.com/ida-mdc/harmony-to-organoid/-/raw/main/script.py process \
    --index-file MY/INPUT/DATA/Index.xml \
    --output-dir MY/OUTPUT/DATA \
    --lut-min 100,100,100,100 \
    --lut-max 2000,1000,1500,2000 \
    --colors white,orange,blue,#ff0000
```

**Output:**

After successfully running the processing command, your specified output directory (`MY/OUTPUT/DATA`) will contain the following:

- **Projections:**  
  Maximum intensity projection images (`projections/`) generated for each data group, providing 2D summaries of your 3D data.

- **Plots:**  
  Visual representations of the data are stored in `plots`, including group bounding boxes and projections placed within 
  their  respective areas, ensuring spatial consistency and aiding in data interpretation.

- **README Files:**  
  Automatically generated documentation (`README.md` and `README.html`) that includes embedded plots for easy reference and sharing.

### How to run from Jupyter notebook

```
micromamba activate YOUR_ENVIRONMENT
pip install 
```