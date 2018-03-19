mport matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

#Referenced these conversations to figure out how to build this.
#https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
#https://stackoverflow.com/questions/40601552/visualizing-attention-activation-in-tensorflow

#modify the file you want to visualize here
a = np.loadtxt("attn_dist/question-to-context_drop_25_reg_0001_b_9")


#COPY THE TEXT OF THE EXAMPLES THE MODEL CHOSE WHEN GENERATING THE DATA
context = "in early 2012 , nfl commissioner roger goodell stated that the league planned to make the 50th super bowl \" spectacular \" and that it would be \" an important game for us as a league \""
question = "what one word did the nfl commissioner use to describe what super bowl 50 was intended to be ?"
context = context.split(" ")
#context = context + [""]*(a.shape[0]-len(context))
question = question.split(" ")
#question = question + [""]*(a.shape[1]-len(context))
for i,c in enumerate(context):
	print "%d - %s" % (i,c)
for i,c in enumerate(question):
	print "%d - %s" % (i,c)
a = a[:len(context),:len(question)]
#full = np.zeros((a.shape[0]*2,a.shape[1]*2))
#print full.shape
#full[::2,::2] = a
fig, axs = plt.subplots(1)
plt.imshow(a, cmap='hot', interpolation='nearest')
print context
fig.autofmt_xdate()
tick_spacing = 1
axs.tick_params(axis='x', which='major', width=1)
question_ = []
context_ = []
for word in context:
	context_.append(word)
	context_.append("")
for word in question:
	question_.append(word)
	question_.append("")
axs.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
axs.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
axs.set_xticklabels(question, fontsize=8)
axs.set_yticklabels(context)

plt.show()
