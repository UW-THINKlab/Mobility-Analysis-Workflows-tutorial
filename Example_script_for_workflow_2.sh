#!/bin/bash

# Specify the working directory.
Data_path='/example_workflow'

# Specify where the input data is stored.
input_csv='/example_workflow/input_data/input_case2_v2.csv'

# Specify where the output should be stored.
output_csv='/example_workflow/output.csv'

# This line runs the Incremental Clustering container with the specified input_csv and distance threshold of 1 km and duration threshold of 0 second (which means the duration threshold will not be applied).
singularity exec --bind ${Data_path}:${Data_path} docker://uwthinklab/maw_containers_1:v6 python /IncrementalClustering.py ${input_csv} ${output_csv} 1.0 0

# This line runs the Duration Calculator container for the specified output_csv and overwrites the file. The duration threshold is set to 300 seconds.
singularity exec --bind ${Data_path}:${Data_path} docker://uwthinklab/maw_containers_1:v6 python /UpdateStayDuration.py ${output_csv} ${output_csv} 300

# This line runs the Oscillation Corrector container with time window of 300 seconds. The input file will be overwritten by the output.
singularity exec --bind ${Data_path}:${Data_path} docker://uwthinklab/maw_containers_1:v6 python /AddressOscillation.py ${output_csv} ${output_csv} 300

# This line re-runs the Duration Calculator container with duration threshold of 300 seconds, and overwrites the input file with output.
singularity exec --bind ${Data_path}:${Data_path} docker://uwthinklab/maw_containers_1:v6 python UpdateStayDuration.py ${output_csv} ${output_csv} 300
