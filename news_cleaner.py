import cosine_sim
import news_memory

outlets = news_memory.main()

def news_cleaner(message):
	global outlets

	message = message

	key = outlets.keys()
	values = outlets.values()

	similarities = cosine_sim.words_sim(message, key)

	name = key[similarities.index(max(similarities))]
	idn = values[similarities.index(max(similarities))]

	d = {"name": name, "idn": idn}

	return(d)

