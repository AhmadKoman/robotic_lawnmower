# robotic_lawnmower
mini project


I. Notations and Recommended Approach

Ground Map: The lawn is represented as a CSV file with symbols L (lawn to be cut), O (obstacle), and S (robot's starting point).
Robot Movement: The robot moves with a constant speed and changes direction when it hits an obstacle.
Random Movement and Bouncing: When the robot hits an obstacle, it generates a new random velocity and tries to move in a new direction.
Robot Trace: Each step the robot takes across the lawn forms a trace, representing its movement over time.
Coverage: To estimate coverage, divide the lawn into a grid of smaller squares (pixels) and track the visited pixels in the coverage map.
II. Exercises and Grade Requirements
For Grade E:

Implement support for a single robot simulation that reads a ground map, visualizes it, computes a trace, and visualizes the trace.
For Grade C (in addition to Grade E requirements):

Calculate coverage as a percentage (e.g., 93.2%).
Create a visualization of the coverage map.
Answer questions about coverage, parameters' influences, effective cutting width, and workload.
For Grade A (in addition to Grade C requirements):

Add support for multiple simulations in a single run to compute average and standard deviation for coverage.
Suggest and experiment with improvements to the robot AI to enhance coverage.
Suggest improvements such as enhancing the bouncing mechanism or simulating grass growth.
You would need to write code to implement the above requirements and provide a report with the results, analysis, and experiments as specified.


Support for Multiple Simulations:
Modify your program to support running multiple simulations in a single run.
Allow users to specify the number of simulations and the simulation duration.
Average and Standard Deviation:
After running multiple simulations, calculate the average and standard deviation of the coverage for a given map after a given time.
Present these statistics in your report to provide a better understanding of the lawnmower's performance.
Improvements to Robot AI:
Suggest improvements to the robot AI that can enhance coverage over time. Some possible improvements include:
Optimized Bouncing Mechanism:
Experiment with more sophisticated algorithms for generating new random velocities when the robot hits an obstacle. For example, you can use methods like gradient descent to find a better path.
Simulating Grass Growth:
Implement a simple model for grass growth, where grass regrows in areas that have been cut. Adjust the cutting strategy based on grass height and growth speed.
Realistic Weekly Schedule:
Create a weekly schedule for the robot that considers factors like weather conditions and lawn usage. Optimize the cutting schedule for the highest coverage.
Obstacle Avoidance:
Implement obstacle avoidance algorithms to allow the robot to navigate around obstacles more effectively.
Experiments and Evaluation:
Perform experiments to test and evaluate the suggested improvements. For example, compare the coverage of the original AI with the enhanced AI under different scenarios.
Present visualizations and data to support your evaluations.
Report and Documentation:
Document the changes made to your code to support multiple simulations and improvements in the AI.
Explain the rationale behind the enhancements and how they affect coverage.
Present the results of your experiments, including any visualizations and statistical analysis.
Provide a clear and well-organized report with detailed explanations of your work.




To do list:
1. Read and visualize the ground map. Start with map simple.csv 
2. Convert map to x,y coordinate system, origo in lower left corner 
3. Implement is_outside(x,y) ⇒ True if x,y outside map or in obstacle 
4. Prepare trace ⇒ compute x0,y0, vx0,vy0, steps (steps to be taken) 
5. Implement support for generating random velocities 
6. Implement one_step(x,y,vx,vy) ⇒ new x,y,vx,vy after one step 
7. Compute and visualize trace (start with just a few steps) ⇒ Grade E 
8. Setup coverage grid ⇒ each ground square divided in N × N pixels 
9. Convert trace to coverage ⇒ Grade C 
10. Start writing the report 
11. Try grade A,B if time permits