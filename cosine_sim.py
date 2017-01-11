from collections import Counter

def letterise(strng):
	letters = []
	for letter in strng: letters.append(letter)
	return letters

def cosine_sim(a,b):
    
    # count letter occurrences
    a_vals = Counter(a)
    b_vals = Counter(b)
    
    # convert to letter-vectors
    words = list(set(a_vals) | set(b_vals))
    a_vect = [a_vals.get(word, 0) for word in words]       
    b_vect = [b_vals.get(word, 0) for word in words]       
    
    # find cosine
    len_a  = sum(av*av for av in a_vect) ** 0.5            
    len_b  = sum(bv*bv for bv in b_vect) ** 0.5            
    dot    = sum(av*bv for av,bv in zip(a_vect, b_vect))
    cosine = dot / (len_a * len_b) 
    return cosine

def words_sim(item, lst):
	similarities = []

	item_ltr = letterise(item.lower())

	for other in lst:
		other_ltr = letterise(other.lower())
		similarities.append(cosine_sim(item_ltr, other_ltr))

	return(similarities)
