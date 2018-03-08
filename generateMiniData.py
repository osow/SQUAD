#geneartes a sub-sample of the training data, useful to debug at early stages


num_points = 128

context_file, qn_file, ans_file = open("data/train.context"), open("data/train.question"), open("data/train.span")

new_context,new_qn,new_ans = open("data/mini-train.context","w"), open("data/mini-train.question","w"),open("data/mini-train.span","w")

for i in range(num_points):
	new_context.write(context_file.next())
	new_qn.write(qn_file.next())
	new_ans.write(ans_file.next())