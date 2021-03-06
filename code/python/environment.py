'''
Class for agent environments in Moral Dynamics

Felix Sosa
'''
import pymunk
import pygame
import pymunk.pygame_util
from pygame.locals import *
import handlers
from agents import Agent

class Environment:
	def __init__(self, a_params, p_params, f_params, vel, handlers=None, 
				 view=True, frict=0.05):
		'''
		Environment class that contains all necessary components to configure
		and run scenarios.

		a_params -- parameters for the Blue Agent
		p_params -- parameters for the Green Agent
		f_params -- parameters for the Fireball
		vel 	 -- velcoties associated with each agent in the scenario
		handlers -- optional collision handlers
		view 	 -- flag for whether you want to view the scenario or not
		frict 	 -- friction value for pymunk physics
		'''
		self.view = view
		# Objects in environent
		self.agent = Agent(a_params['loc'][0], a_params['loc'][1], 
						   a_params['color'], a_params['coll'], 
						   a_params['moves'])
		self.patient = Agent(p_params['loc'][0], p_params['loc'][1], 
							 p_params['color'], p_params['coll'], 
							 p_params['moves'])
		self.fireball = Agent(f_params['loc'][0], f_params['loc'][1], 
							  f_params['color'], f_params['coll'], 
							  f_params['moves'])
		# Initial location of objects in environment
		self.p_loc = p_params['loc']
		self.a_loc = a_params['loc']
		self.f_loc = f_params['loc']
		# Pymunk space friction
		self.friction = frict
		# Agent velocities
		self.vel = vel
		# Engine parameters
		self.space = None
		self.screen = None
		self.options = None
		self.clock = None
		# Collision handlers
		self.coll_handlers = [x for x in handlers] if handlers else handlers
		# Values needed for rendering the scenario in Blender
		self.tick = 0
		self.agent_collision = None
		self.patient_fireball_collision = 0
		self.position_dict = {
			'agent':[],
			'patient':[],
			'fireball':[]
		}
		self.screen_size = (1000,600)
		# Configure and run environment
		self.configure()

	def configure(self):
		'''
		Configuration method for Environments. Sets up the pymunk space
		for scenarios.
		'''
		# Configure pymunk space and pygame engine parameters (if any)
		if self.view:
			pygame.init()
			self.screen = pygame.display.set_mode((1000,600))
			self.options = pymunk.pygame_util.DrawOptions(self.screen)
			self.clock = pygame.time.Clock()
		self.space = pymunk.Space()
		self.space.damping = self.friction
		# Configure collision handlers (if any)
		if self.coll_handlers:
			for ob1, ob2, rem in self.coll_handlers:
				ch = self.space.add_collision_handler(ob1, ob2)
				ch.data["surface"] = self.screen
				ch.post_solve = rem
		# Add agents to the pymunk space
		self.space.add(self.agent.body, self.agent.shape,
					   self.patient.body, self.patient.shape,
					   self.fireball.body, self.fireball.shape)
		
	def update_blender_values(self):
		'''
		All scenarios are rendered in the physics engine Blender. In order to do this,
		we store relevant values such as object position, simulation tick count, and
		collision in a JSON file. This file is passed into a bash script that uses it
		to render the relevant scenario in Blender. 

		This method is used to update the JSON files for each scenario.
		'''
		# Append positional information to the dict
		self.position_dict['agent'].append({'x':self.agent.body.position[0], 
											'y':self.agent.body.position[1]})
		self.position_dict['patient'].append({'x':self.patient.body.position[0], 
											  'y':self.patient.body.position[1]})
		self.position_dict['fireball'].append({'x':self.fireball.body.position[0], 
											   'y':self.fireball.body.position[1]})
		# Increment the simulation tick
		self.tick += 1
		# Record when the Agent collides with someone else
		if not handlers.PF_COLLISION: self.agent_collision = self.tick

	def run(self):
		'''
		Forward method for Environments. Actually runs the scenarios you
		view on (or off) screen.
		'''
		# Agent velocities
		a_vel, p_vel, f_vel = self.vel
		# Agent action generators (yield actions of agents)
		a_generator = self.agent.act(a_vel, self.clock, self.screen,
									 self.space, self.options, self.view)
		p_generator = self.patient.act(p_vel, self.clock, self.screen,
									   self.space, self.options, self.view)
		f_generator = self.fireball.act(f_vel, self.clock, self.screen,
										self.space, self.options, self.view)
		# Running flag
		running = True
		# Main loop. Run simulation until collision between Green Agent 
		# 	and Fireball
		while running and not handlers.PF_COLLISION:
			try:
				# Generate the next tick in the simulation for each object
				next(a_generator)
				next(p_generator)
				next(f_generator)
				# Render space on screen (if requested)
				if self.view:
					self.screen.fill((255,255,255))
					self.space.debug_draw(self.options)
					pygame.display.flip()
					self.clock.tick(50)
				self.space.step(1/50.0)
				# Update the values for the Blender JSON file
				self.update_blender_values()
			except:
				running = False
		if self.view:
			pygame.quit()
			pygame.display.quit()
		# Record whether Green Agent and Fireball collision occurred
		coll = 1 if handlers.PF_COLLISION else 0
		# Reset collision handler
		handlers.PF_COLLISION = []