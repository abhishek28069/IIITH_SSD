# SSD LAB ACTIVITY 12

## Pressure Sensing Mat
- 42 * 25 pressure mat fitted with sensors to track pressure applied by feet is the source of the input data.
- Non-zero values represent the foot stepped on the given position.

## Logic of The Code
- First, find whether the left or right foot is being placed by looking for non-zero value.
- Then, record the y-coordinate and timestamp whenever the first non-zero value appears alternatively on the left and right side.
- Repeat the same and record left_foot_postions, right_foot_postions, left_foot_timestamps, right_foot_timestamps and calculate stride distance, velocity and cadence.

## Assumptions
- Foot is placed alternatively, i.e., left->right->left->>>>> etc
- Distance for stride is calculated as (first touching point) to (first touching point).
- Noise in the data is not taken into coonsideration, i.e., isolated non-zero values.
- Output is printed with descriptive labels.
