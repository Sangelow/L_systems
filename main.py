from turtle import Screen, RawPen, done
from time import sleep
from source.L_system import L_system, Rule
import yaml

# TODO:
#   - Parallelize the L_system generation

name_list = [
    'fractal_plant',
    'dragon_curve',
    'koch_curve',
    'sierpinski_triangle',
    'hilbert_curve',
    'levy_c_curve',
    'twindragon',
    'terdragon',
    'gosper_curve',
    ]

# Parameters
name = name_list[-1]
n_generation = 10

# Create the L_system
with open(f'input/{name}.yaml') as file:
    data = yaml.full_load(file)

# Load the L_system
variables = data['variables'].keys()
constants = data['constants'].keys()
axiom = data['axiom']
rules = []
for rule in data['rules']:
    rules.append(Rule(*rule))
system = L_system(variables, constants, axiom, rules)

# Load the actions
actions = dict(data['variables'], **data['constants'])

# Create the screen
screen = Screen()
screen.mode('logo')
screen.tracer(0, 0)

# Create the pens
pen = RawPen(screen)
# Hide the pen
pen.speed(0)

# Run the L_system
positions = []
angles = []
for i in range(n_generation):
    # Reset the screen
    screen.reset()
    pen.hideturtle()
    # Move the turtle
    for movement in system.axiom:
        exec(actions[movement])
    # Compute the next generation
    system.next_generation()
    # Update the screen
    screen.update()
    # Wait
    sleep(0.5)
    # Reset the positions
    positions = []
    angles = []

# Drawing is done
done()
