from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
	def __init__(self, num_points = 5000):
		self.num_points = num_points
		
		self.x_values = [0]
		self.y_values = [0]
		
	def walk(self):
		
		x_direction = choice([-1,1])
		y_direction = choice([-1,1])
		x_step = choice(range(5))
		y_step = choice(range(50))
		
		next_x = self.x_values[-1] + x_direction* x_step
		next_y = self.y_values[-1] + y_direction* y_step
		
		self.x_values.append(next_x)
		self.y_values.append(next_y)
	
	def full_path(self, str_in= "scatter"):
		for num in range(self.num_points):
			self.walk()
		plt.figure(dpi=80, figsize = (17,10)) # size of figure, python default 80 pixels per inch (dpi)
		                                      # but we can change that
		
		if str_in=="line":
			plt.plot(self.x_values, self.y_values, linewidth=2)  #plot figure with line connect
		else:		
			point_numbers = list(range(self.num_points+1))
			
			# plot figure with series of dot
			plt.scatter(self.x_values, self.y_values,c=point_numbers, cmap=plt.cm.Reds,  
			            edgecolor='none', s=2)
			# plot some special dot, first and end point            
			plt.scatter(0, 0, c='green', edgecolors='none', s=10)
			plt.scatter(self.x_values[-1], self.y_values[-1], c='blue', edgecolors='none', s=10)
			
		# invisible x and y axis	
		# ~ plt.gca().get_xaxis().set_visible(False)
		# ~ plt.gca().get_yaxis().set_visible(False)
		
		#set off all axis
		plt.axis('off')
		
		#save figure into dir
		plt.savefig("RW_figure/picture"+str(choice(range(10000)))+".png", bbox_inches='tight')
		
		#show the result
		plt.show()

# ~ aWalk = RandomWalk(100)      # create one instance and plot a whole big path

str_in = input("line or scatter?\n")

while True:
	aWalk = RandomWalk(100000)      # create new instance every loop
	aWalk.full_path(str_in=str_in)

