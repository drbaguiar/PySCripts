##Load the dataset
import csv
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

##test data
#filename = 'pima-indians-diabetes.csv'
#dataset = loadCsv(filename)
#print('Loaded data file {0} with {1} rows').format(filename, len(dataset))	
	
#SpiltDataset Function
import random
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

## We can test this by defining a dataset with 5 instances, split it into training and testing datasets and print them out to see which data instances ended up where.
#dataset = [[1], [2], [3], [4], [5]]
#splitRatio = 0.67
#train, test = splitDataset(dataset, splitRatio)
#print('Split {0} rows into train with {1} and test with {2}').format(len(dataset), train, test)

# Separate Data By Class: The first task is to separate the training dataset instances by class value so that we can calculate statistics for each class. 
def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

##We can test the separateByClass function with some sample data, as follows:	
#dataset = [[1,20,1], [2,21,0], [3,22,1]]
#separated = separateByClass(dataset)
#print('Separated instances: {0}').format(separated)

#Calculate Mean & Std Deviation
import math
def mean(numbers):
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

##We can test the mean and std deviation calculator	
#numbers = [1,2,3,4,5]
#print('Summary of {0}: mean={1}, stdev={2}').format(numbers, mean(numbers), stdev(numbers))

#Summarize function
def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries
	
## We can test the summarize() function with some test data that shows markedly different mean and standard deviation values for the first and second data attributes.
#dataset = [[1,20,0], [2,21,1], [3,22,0]]
#summary = summarize(dataset)
#print('Attribute summaries: {0}').format(summary)

#Summarize Attributes By Class
#We can pull it all together by first separating our training dataset into instances grouped by class. Then calculate the summaries for each attribute.
def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.iteritems():
		summaries[classValue] = summarize(instances)
	return summaries
	
#We can test this summarizeByClass() function with a small test dataset.
#dataset = [[1,20,1], [2,21,0], [3,22,1], [4,22,0]]
#summary = summarizeByClass(dataset)
#print('Summary by class value: {0}').format(summary)

#Calculate Gaussian Probability Density Function
import math
def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
	
##Sample data to test
#x = 71.5
#mean = 73
#stdev = 6.2
#probability = calculateProbability(x, mean, stdev)
#print('Probability of belonging to this class: {0}').format(probability)

def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.iteritems():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities

##test data
#summaries = {0:[(1, 0.5)], 1:[(20, 5.0)]}
#inputVector = [1.1, '?']
#probabilities = calculateClassProbabilities(summaries, inputVector)
#print('Probabilities for each class: {0}').format(probabilities)

#Make predictions
def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.iteritems():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel

##Test data  
#summaries = {'A':[(1, 0.5)], 'B':[(20, 5.0)]}
#inputVector = [1.1, '?']
#result = predict(summaries, inputVector)
#print('Prediction: {0}').format(result)	

def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	return predictions
	
##test data
#summaries = {'A':[(1, 0.5)], 'B':[(20, 5.0)]}
#testSet = [[1.1, '?'], [19.1, '?']]
#predictions = getPredictions(summaries, testSet)
#print('Predictions: {0}').format(predictions)

#Calculate accuracies
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
##test data
#testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
#predictions = ['a', 'a', 'a']
#accuracy = getAccuracy(testSet, predictions)
#print('Accuracy: {0}').format(accuracy)

def main():
	filename = 'pima-indians-diabetes.csv'
	splitRatio = 0.67
	dataset = loadCsv(filename)
	trainingSet, testSet = splitDataset(dataset, splitRatio)
	print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
	# prepare model
	summaries = summarizeByClass(trainingSet)
	# test model
	predictions = getPredictions(summaries, testSet)
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: {0}%').format(accuracy)
 
main()