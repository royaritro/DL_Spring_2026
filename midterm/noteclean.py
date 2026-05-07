import nbformat

path = "dl_endterm.ipynb"

with open(path) as f:
    nb = nbformat.read(f, as_version=4)

if "widgets" in nb["metadata"]:
    del nb["metadata"]["widgets"]

with open(path, "w") as f:
    nbformat.write(nb, f)

print("Cleaned notebook")