'''
The set of scenarios from Moral Kinematics that were replicated for the Moral
Dynamics project.

Each function below defines a scenario. The block comments below the 
function declaration detail the scenario:

P = Patient
A = Agent
F = Fireball
> = Moving Right
< = Moving Left
^ = Moving Up
- = Empty Space

Felix Sosa
'''
from environment import Environment
from handlers import rem0

# Scenarios used in experiment 1 (see paper)
__experiment1__ = ["long_distance","dodge","bystander","stays_put",
		 		   "short_distance","med_push","long_push","push_patient", 
				   "double_push"]

# Scenarios used in experiment 2 (see paper)
__experiment2__ = ["long_distance","dodge","bystander","stays_put",
				   "short_distance","med_push","long_push","push_patient", 
				   "double_push","harm_moving_moving","harm_moving_static",
  				   "harm_static_moving","harm_static_static",
  				   "victim_moving_moving","victim_moving_static",
  				   "victim_static_moving","victim_static_static"]

def long_distance(view=True):
	# - - - - - - -
	# A > > > P - F
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (100,300)
	a_params['color'] = "blue"
	a_params['moves'] = ['R', 'R', 'R', 'R', 'N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (800,300)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N', 'N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (900,300)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,150,150
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def dodge(view=True):
	# - - - ^ - - -
	# P > > A - - F
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (500,300)
	a_params['color'] = "blue"
	a_params['moves'] = ['N', 'N', 'DS', 'N', 'N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (100,300)
	p_params['color'] = "green"
	p_params['moves'] = ['R','R','R','R','R']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (900,300)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def bystander(view=True):
	# - - - A - - -
	# P > > > > > F
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (500,500)
	a_params['color'] = "blue"
	a_params['moves'] = ['N', 'N', 'N', 'N', 'N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (100,300)
	p_params['color'] = "green"
	p_params['moves'] = ['R','R','R','R','R']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (900,300)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def stays_put(view=True):
	# - - - - P - -
	# F > > A - - -
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (500,250)
	a_params['color'] = "blue"
	a_params['moves'] = ['S', 'S', 'S', 'S', 'S']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (600,350)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N','N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (300,290)
	f_params['color'] = "red"
	f_params['moves'] = ['R','R','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def short_distance(view=True):
	# - - - - - - -
	# - - A > P - F
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (740,300)
	a_params['color'] = "blue"
	a_params['moves'] = ['R', 'R', 'R', 'R', 'R']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (820,300)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N', 'N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (900,300)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def med_push(view=True):
	# - - - - - - -
	# A > > P - - F
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (100,300)
	a_params['color'] = "blue"
	a_params['moves'] = ['R', 'R', 'R', 'R', 'N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (500,300)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N', 'N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (900,300)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def long_push(view=True):
	# - - - - - - -
	# A P > > > > F
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (100,300)
	a_params['color'] = "blue"
	a_params['moves'] = ['R', 'R', 'R', 'R', 'N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (200,300)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N', 'N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (900,300)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def push_patient(view=True):
	# Test two types of agents, good and bad in the scenario
	# - F - - - - -
	# - - - ^ < < P
	# - - - A - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (500,400)
	a_params['color'] = "blue"
	a_params['moves'] = ['N','NS','DS2','N','N','N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (900,300)
	p_params['color'] = "green"
	p_params['moves'] = ['L','L','L','N','N', 'N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (300,200)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def double_push(view=True):
	# - - - - - - -
	# A P > - > - F
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (200,300)
	a_params['color'] = "blue"
	a_params['moves'] = ['R','S','N','R','R','R']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (300,300)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N','N','N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (800,300)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def harm_moving_moving(view=True):
	# Test two types of agents, good and bad in the scenario
	# > > P - - - -
	# - - - < < < F
	# - - - A - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	# a_params['loc'] = (550,100) # <- check this out
	a_params['loc'] = (550,450)
	a_params['color'] = "blue"
	a_params['moves'] = ['NS2','D','D','D','N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	# p_params['loc'] = (900,300) # <- check this out
	p_params['loc'] = (50,210)
	p_params['color'] = "green"
	p_params['moves'] = ['R','R','R','N', 'N']
	p_params['coll'] = 1
	# Fireball parameters
	# f_params['loc'] = (450,500) # <- check this out
	f_params['loc'] = (850,330)
	f_params['color'] = "red"
	f_params['moves'] = ['L','L','L','N', 'N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def victim_moving_moving(view=True):
	# Test two types of agents, good and bad in the scenario
	# > > F - - - -
	# - - - < < < P
	# - - - A - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	# a_params['loc'] = (550,100) # <- check this out
	a_params['loc'] = (550,450)
	a_params['color'] = "blue"
	a_params['moves'] = ['NS2','D','D','D','N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	# p_params['loc'] = (900,300) # <- check this out
	p_params['loc'] = (850,330)
	p_params['color'] = "green"
	p_params['moves'] = ['L','L','L','N', 'N']
	p_params['coll'] = 1
	# Fireball parameters
	# f_params['loc'] = (450,500) # <- check this out
	f_params['loc'] = (50,210)
	f_params['color'] = "red"
	f_params['moves'] = ['R','R','R','N', 'N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def harm_moving_static(view=True):
	# Test two types of agents, good and bad in the scenario
	# - P - - - - -
	# - - - < < < F
	# - - - A - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (500,400)
	a_params['color'] = "blue"
	a_params['moves'] = ['N','NS','D','D','N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	# p_params['loc'] = (900,300) # <- check this out
	p_params['loc'] = (340,230)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N', 'N']
	p_params['coll'] = 1
	# Fireball parameters
	# f_params['loc'] = (450,500) # <- check this out
	f_params['loc'] = (900,300)
	f_params['color'] = "red"
	f_params['moves'] = ['L','L','L','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def victim_moving_static(view=True):
	# Test two types of agents, good and bad in the scenario
	# - F - - - - -
	# - - - < < < P
	# - - - A - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	# a_params['loc'] = (550,100) # <- check this out
	a_params['loc'] = (500,400)
	a_params['color'] = "blue"
	a_params['moves'] = ['N','NS','D','D','N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	# p_params['loc'] = (900,300) # <- check this out
	p_params['loc'] = (900,300)
	p_params['color'] = "green"
	p_params['moves'] = ['L','L','L','N', 'N']
	p_params['coll'] = 1
	# Fireball parameters
	# f_params['loc'] = (450,500) # <- check this out
	f_params['loc'] = (340,230)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def harm_static_moving(view=True):
	# Test two types of agents, good and bad in the scenario
	# - - - < < < P
	# - - - F - - -
	# - - - A - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (500,330)
	a_params['color'] = "blue"
	a_params['moves'] = ['N','DS2','S','S','S']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (900,130)
	p_params['color'] = "green"
	p_params['moves'] = ['L','L','L','N','N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (500,230)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def victim_static_moving(view=True):
	# Test two types of agents, good and bad in the scenario
	# - - - < < < F
	# - - - P - - -
	# - - - A - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (500,330)
	a_params['color'] = "blue"
	a_params['moves'] = ['N','DS2','S','S','S']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (500,230)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N','N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (900,130)
	f_params['color'] = "red"
	f_params['moves'] = ['L','L','L','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def harm_static_static(view=True):
	# - - - - - - -
	# A > > F - - P
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (200,300)
	a_params['color'] = "blue"
	a_params['moves'] = ['R','RS','S','N','N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (800,300)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N','N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (500,300)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env

def victim_static_static(view=True):
	# - - - - - - -
	# A > > P - - F
	# - - - - - - -
	a_params, p_params, f_params = {}, {}, {}
	# Agent parameters
	a_params['loc'] = (200,300)
	a_params['color'] = "blue"
	a_params['moves'] = ['R','RS','S','N','N']
	a_params['coll'] = 0
	a_params['type'] = 'B'
	# Patient parameters
	p_params['loc'] = (500,300)
	p_params['color'] = "green"
	p_params['moves'] = ['N','N','N','N','N']
	p_params['coll'] = 1
	# Fireball parameters
	f_params['loc'] = (800,300)
	f_params['color'] = "red"
	f_params['moves'] = ['N','N','N','N','N']
	f_params['coll'] = 2
	# Collision handlers
	handlers =[(1,2,rem0)]
	# Agent velocities
	vel = 300,300,300
	env = Environment(a_params,p_params,f_params,vel,handlers,view)
	env.run()
	return env