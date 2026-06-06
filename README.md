# Assignment 1

## Overview

This project was developed using a code-first CAD modeling approach with the Build123d Python library.

## Methodology

1. The required profile geometry was first identified in Fusion 360.
2. A custom Fusion 360 script was used to extract the coordinates of selected sketch points.
3. The extracted coordinates were imported into Build123d and used to construct closed polygon profiles.
4. The polygon profiles were then used to create 3D geometry through operations such as extrusion and feature modifications.
5. The final model was generated entirely through Python code.

## Advantages
- Improved dimensional consistency by generating profiles from precise coordinate data.
- Reduced geometric and volumetric deviations compared to manually recreating complex profiles.

## Tools Used

- Build123d library
- Python
- Fusion 360

## Output

The final CAD model was generated programmatically from coordinate-defined profiles and exported for further visualization and manufacturing purposes.
