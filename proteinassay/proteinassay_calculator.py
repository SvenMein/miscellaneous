"""
This script contains the ProteinAssayCalculator class,
which is responsible for calculating the concentration of a protein sample based on the absorbance readings
obtained from a protein assay.
The class uses the standard curve generated from known concentrations
of a standard protein to determine the concentration of the unknown sample. It
also includes methods for plotting the standard curve and calculating the concentration
of the sample based on its absorbance reading.
"""
# Standard sample concentrations in µg/µl
standard_sample = [0, 200, 400, 600, 800, 1000]

# Define nested dictionary containing raw data. Keys correspond to plate row, inner keys to plate column. Values are absorbance.
absorbance_readings = {}
absorbance_readings["A"] = {1:0.075599998, 2:0.333900005, 3:0.568199992, 4:0.777800024, 5:0.998199999, 6:1.099400043}
absorbance_readings["B"] = {1:0.078699999, 2:0.349900007, 3:0.586600006, 4:0.728299975, 5:1.003600001, 6:1.148399949}
absorbance_readings["C"] = {1:0.481700003, 2:0.151600003, 3:0.484699994, 4:0.146400005}
absorbance_readings["D"] = {1:0.460700005, 2:0.167199999, 3:0.485399991, 4:0.148800001}

# Calculate mean of technical duplicates. Pairs in this example are "A"/"B" and "C"/"D".
# Save means into lists.
mean_standard = []
for reading in absorbance_readings["A"]:
    value = 0
    value = (absorbance_readings["A"][reading] + absorbance_readings["B"][reading]) / 2
    mean_standard.append(value)

mean_sample = []
for reading in absorbance_readings["C"]:
    value = 0
    value = (absorbance_readings["C"][reading] + absorbance_readings["D"][reading]) / 2
    mean_sample.append(value)

# Currently no regression curve is calculated. It is on the to-do list. For now just simple line is used.
# Calculate standard regression curve. On the x-axis we place the concentration, on y-axis the meassured absorbance
slope = (mean_standard[1]-mean_standard[0]) / (standard_sample[1] - standard_sample[0])

# Calculate y-axis intercept.
intercept = mean_standard[0] - slope * standard_sample[0]

# Calculate sample concentration.
sample_concentration = []
counter = 1
for elem in mean_sample:
    concentration = (elem - intercept) / slope
    sample_concentration.append(concentration)
    print(f"Sample {counter} contains {round(concentration, 2)} µg/µl protein.")
    counter += 1

# Normalization so that samples will be 500 µl with a concentration of 50 µg/µl.
# For this, we assume 750 µl sample is left after the protein assay.
# cv = cv
# conc / 50 µg/µl 