from die import Die
import pygal

num_sides = 6
die_1 = Die(num_sides)
die_2 = Die(num_sides)
results = []

#this is two type of defination for a list of 0
frequencies = [0 for whatever in range(num_sides*2)]
frequency = [0]*num_sides*2


for i in range(10000):
	result = die_1.roll() + die_2.roll()
	frequencies[result-1]+=1
	frequency[result-1]+=1
	results.append(result)


print(results)
print(frequencies)	
print(frequency)
	
hist = pygal.Bar()

hist.title = "Results of rolling two D6 10000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6' , '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6+D6", frequencies)
hist.render_to_file('die_visual.svg')
