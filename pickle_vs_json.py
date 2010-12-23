"""
	Pickle vs JSON by Konstantin Kovshenin
	Feel free to use this code as you wish
	
	Discussions: http://kovshenin.com/archives/pickle-vs-json-which-is-faster/
	Author: Konstantin Kovshenin -- http://kovshenin.com
	Written in December 2010 for Python 2.6
"""

import simplejson
import pickle

"""
	Other things to try:
	
	# Marshal vs Simple JSON:
	import marshal as pickle
	import simplejson
	
	# Marshal vs Pickle:
	import marshal as simplejson
	import pickle
	
	# Marshal vs cPickle:
	import marshal as simplejson
	import cPickle as pickle
	
	# Simple JSON vs cPickle
	import simplejson
	import cPickle as pickle
"""

import timeit
import random
import sys

source = []
json_result = []
pickle_result = []

def main():
	# Need access to these outside our functions.
	global source, pickle_result, json_result
	
	# Let's generate some junky source - lists, dictionaries and nested dictionaries.
	for i in range(10):
		l, d, nd = get_data(50)
		source.append(l)
		source.append(d)
		source.append(nd)
		
	# We'll use timeit to track the time of our function calls
	json_time = timeit.Timer('test_json()', 'from __main__ import test_json, source, json_result')
	pickle_time = timeit.Timer('test_pickle()', 'from __main__ import test_pickle, source, pickle_result')
	json_load_time = timeit.Timer('test_json_load()', 'from __main__ import test_json_load, source, json_result')
	pickle_load_time = timeit.Timer('test_pickle_load()', 'from __main__ import test_pickle_load, source, pickle_result')
	
	print "Dir\tEntries\tMethod\tTime\tLength"
	print
	
	# Feel free to try 500 and 1000 but beware that they could take.. Hours!
	for i in (10, 20, 50, 100):
		print "dump\t%s\tJSON\t%.3f\t%s" % (i, json_time.timeit(i), len(''.join(json_result)))
		print "load\t%s\tJSON\t%.3f\t%s" % (i, json_load_time.timeit(i), '-')
		print "dump\t%s\tPickle\t%.3f\t%s" % (i, pickle_time.timeit(i), len(''.join(pickle_result)))
		print "load\t%s\tPickle\t%.3f\t%s" % (i, pickle_load_time.timeit(i), '-')

		# Clear the results after each run since we need to measure size.
		json_result = []
		pickle_result = []

	return

def test_json():
	"""
		Runs the dumps JSON test.
	"""
	for entry in source:
		json_result.append(simplejson.dumps(entry))
	
def test_pickle():
	"""
		Runs the dumps Pickle test.
	"""
	for entry in source:
		pickle_result.append(pickle.dumps(entry))
		
def test_json_load():
	"""
		Runs the loads JSON test.
	"""
	for entry in json_result:
		simplejson.loads(entry)
		
def test_pickle_load():
	"""
		Runs the loads Pickle test.
	"""
	for entry in pickle_result:
		pickle.loads(entry)

def get_data(count):
	"""
		Use this function to generate data, returns a touple containing
		a list, a dictionary and a nested dictionary.
	"""
	l = []; d = {}; nd = {};
	for i in range(count):
		d[lipsum(1)] = lipsum(10)
		l.append(lipsum(3))
		nd[lipsum(1)] = {i: lipsum(1), i+1: [lipsum(2), lipsum(4), lipsum(3)], i+2: {i: lipsum(3), i+1: lipsum(4), i+2: [lipsum(2), lipsum(3)]}}

	return l, d, nd

def lipsum(count=50):
	"""
		This function generates lorem ipsum junk, use with caution ;)
	"""
	lipsum = """
		Donec ultrices ultricies libero, et tristique dolor euismod et. Cras volutpat nulla in turpis consequat et dignissim nunc rhoncus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed sit amet odio dolor. Mauris fermentum, quam vel volutpat lobortis, tellus eros tempus est, varius elementum arcu lectus volutpat felis. Duis aliquam justo eget neque lacinia vitae dictum urna mollis. Praesent id congue ligula. Maecenas vehicula faucibus mauris, id auctor velit mattis nec. Nulla facilisi. In a mauris quis orci malesuada tempor. Etiam molestie consequat tortor, nec vestibulum enim feugiat ac. Aenean vehicula laoreet mauris, eget tristique urna ultrices vitae. Morbi enim orci, consectetur et ornare eu, sollicitudin in libero. Phasellus nisl nunc, iaculis sed scelerisque non, pretium vel mauris. Curabitur sit amet augue sit amet lacus pellentesque facilisis. Nam in ipsum nulla, eu molestie mi. Praesent eget elementum erat.
		Vivamus ornare suscipit lectus, auctor eleifend mauris congue ut. Aenean vel ullamcorper ipsum. Aliquam erat volutpat. Fusce varius mollis nibh ut vestibulum. Nullam turpis velit, luctus id bibendum eu, commodo id lacus. Maecenas libero tortor, pretium at elementum et, pellentesque vitae magna. Morbi eu nulla eu dolor fermentum faucibus eu congue dui. Etiam eu nibh vitae neque rhoncus ultricies. Nunc vitae diam ligula, sit amet mollis libero. Ut fermentum nisl non sem commodo imperdiet. Morbi in mi vitae nunc eleifend varius eget sed nulla. Ut laoreet lacinia mi rhoncus luctus. Mauris blandit pretium ipsum, interdum gravida libero porttitor ut. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
		Proin commodo, leo elementum gravida iaculis, urna leo imperdiet elit, ac congue dolor ante ornare tortor. Proin dapibus ultricies lorem, imperdiet posuere purus scelerisque et. Morbi nulla eros, mattis nec egestas sed, imperdiet eu nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur pellentesque urna non diam dictum adipiscing. Duis vestibulum nibh mi, ac faucibus tortor. Fusce blandit diam eu odio viverra bibendum. Morbi a nunc tortor. Donec id odio dolor, vitae pulvinar massa.
		In aliquam congue felis at varius. Sed a erat elit, quis cursus sapien. Aenean venenatis urna et tellus posuere ut tempus neque imperdiet. Mauris a adipiscing massa. Fusce in dolor sem, eu iaculis nunc. Maecenas massa neque, scelerisque pellentesque posuere in, dignissim eget est. Donec sed ligula quis erat faucibus bibendum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque neque leo, feugiat ac dapibus nec, vestibulum sed est. Vivamus porta mi a erat facilisis eleifend. Duis vel dolor arcu, non mollis risus. Aenean commodo egestas dolor, a rhoncus sapien vestibulum et. Aenean dignissim, dui nec lacinia dapibus, mauris eros pharetra mi, eu varius dui dolor id urna. Aenean vitae nisi eu risus convallis lobortis in ac erat. Integer quis risus quam, nec commodo ligula. Suspendisse sit amet nibh nulla. Ut a nisi est. Phasellus in imperdiet risus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce ultrices faucibus pretium.
		Nam viverra, tortor vitae mollis adipiscing, elit nulla dapibus leo, non egestas massa lacus vel libero. Duis luctus magna eget tortor sollicitudin viverra. Donec id diam felis, sit amet bibendum metus. Sed bibendum feugiat fermentum. Sed eleifend ultricies vehicula. Nulla velit massa, sagittis eget vestibulum eu, semper sed lacus. Fusce non vehicula ipsum. Nullam ipsum orci, pharetra at aliquam sagittis, accumsan ac urna. Duis convallis luctus neque non adipiscing. Proin auctor congue arcu id cursus. Morbi nec turpis auctor neque porttitor malesuada in a ipsum. Phasellus gravida, augue non mattis suscipit, ligula arcu placerat mauris, quis consectetur erat velit sed nisi. In tincidunt, elit in scelerisque condimentum, tellus arcu pellentesque massa, a imperdiet justo leo id nibh.
		Nunc ligula lectus, rutrum non blandit nec, pellentesque et nunc. Suspendisse tellus tellus, sollicitudin eu faucibus et, mattis eget ipsum. Donec et aliquam nisl. Nulla vel felis lacus, id iaculis diam. Ut sed massa ipsum. Nulla facilisi. Donec a urna eu eros lobortis tempor vel nec mi. Maecenas rutrum sodales molestie. Curabitur consectetur condimentum nisl, id accumsan leo viverra id. Duis facilisis pellentesque ultricies. Duis a ipsum lorem, id feugiat sem. Nulla mattis lectus quis nisi sollicitudin sit amet volutpat libero tristique. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In id nunc purus. Fusce sapien ligula, pulvinar in mollis id, blandit sed elit. Sed id nunc rhoncus purus consequat aliquet. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer purus est, gravida et ornare eget, aliquam ac leo. Ut suscipit faucibus massa eget commodo. Suspendisse posuere erat id dolor tempor facilisis.
		Nunc at eleifend mi. Vestibulum a felis eu ligula sodales luctus at ac mi. Proin pellentesque convallis leo sit amet dictum. Vivamus consequat, quam ac pharetra venenatis, sapien ligula bibendum orci, quis consequat mauris ipsum ac magna. Aliquam at purus augue, consequat faucibus leo. Nulla metus lorem, interdum ut mollis a, tempor eget quam. Nulla sed tortor quis odio tempus scelerisque. Morbi consequat vestibulum erat porttitor euismod. Nullam nec tortor ante. Sed non diam non mi lacinia egestas. Nunc commodo faucibus tortor eget bibendum. Donec nec eros quam, sit amet iaculis libero. Morbi in metus nec ante malesuada semper sed ac tellus. Fusce pellentesque urna orci. Aliquam vitae diam vel nunc dictum egestas. Fusce suscipit, nibh et viverra tincidunt, diam magna interdum tellus, vitae porttitor magna arcu vitae odio. In sit amet nibh leo, ac tristique leo.
		Duis mauris ante, tempor bibendum malesuada vel, dictum quis odio. Mauris id dolor sed ligula ultricies aliquet. Donec eget quam quam, id congue neque. Nullam sit amet commodo nulla. Proin lobortis, sapien ut semper suscipit, erat nibh viverra turpis, vitae dignissim quam ipsum sed tellus. Sed pellentesque malesuada augue id aliquet. Aenean ac velit est. Praesent bibendum gravida pharetra. Integer pulvinar, lacus a pretium pellentesque, nulla dui blandit nunc, eget egestas turpis velit sed enim. Morbi laoreet neque sed eros blandit eu volutpat erat fringilla. In vitae est metus. Nulla lectus turpis, dignissim non adipiscing ut, malesuada a elit. Sed et pulvinar mi. Duis sed nibh velit. Pellentesque posuere hendrerit ligula in tempus. Maecenas sed mollis eros.
		Nulla purus velit, convallis et imperdiet sed, interdum faucibus felis. Morbi rhoncus magna a velit condimentum non consectetur leo facilisis. Sed aliquam fringilla cursus. Cras nibh libero, condimentum sit amet placerat nec, elementum eget metus. Fusce a neque purus, quis ullamcorper elit. Morbi vitae est id diam pretium ultricies. Duis nec turpis non nisl suscipit ultrices. Phasellus tristique ornare porta. Pellentesque hendrerit nisl id mauris sollicitudin id pellentesque sem sagittis. Ut libero libero, suscipit quis pulvinar a, semper sit amet metus. Morbi sit amet urna nunc, eget ullamcorper metus. Donec imperdiet tempus vulputate. Proin ornare, augue et condimentum vehicula, felis libero eleifend purus, non placerat est sapien ut sapien. Aenean a gravida lorem. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean iaculis velit eget est congue et posuere risus ultrices. Cras dictum luctus turpis, quis posuere tellus hendrerit mollis. Nulla sed lacus nec mauris sodales viverra.
		Donec ligula arcu, viverra a bibendum eu, dignissim in felis. Sed consectetur erat mollis risus blandit quis ornare nisl scelerisque. Vivamus sed risus a nulla dictum euismod id et dolor. Nam id pharetra nunc. Nunc ullamcorper varius leo, nec fermentum lacus sodales vel. Duis scelerisque dapibus mi, vel eleifend eros bibendum sit amet. Cras tristique justo id justo bibendum a elementum tortor volutpat. Maecenas ligula nibh, consectetur id malesuada sit amet, suscipit non risus. Proin faucibus pellentesque vehicula. Praesent iaculis malesuada erat. Fusce ac elit nec lorem sodales hendrerit.
		Phasellus diam sapien, cursus nec mattis tempor, facilisis ut odio. Maecenas felis eros, rhoncus eget dignissim quis, vulputate ut orci. Fusce posuere fringilla odio ut cursus. Suspendisse a adipiscing justo. Donec posuere varius mollis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc tempor elit eget quam euismod hendrerit feugiat a augue. Vivamus molestie consectetur urna sed condimentum. Fusce luctus consequat laoreet. Nulla facilisi. Suspendisse gravida laoreet odio, non bibendum magna facilisis et. Suspendisse at egestas metus. Nullam condimentum malesuada ultrices.
		Donec posuere hendrerit erat, non commodo lacus varius non. Sed sodales viverra sagittis. Duis congue scelerisque nunc, ut fermentum tellus adipiscing sit amet. Morbi ut eros neque. Aliquam semper, mauris ac cursus cursus, tortor sem pulvinar magna, non tristique purus mauris nec nisl. Sed eget adipiscing magna. Aliquam ullamcorper sollicitudin dolor, vitae mollis eros mattis quis. Cras gravida tristique nibh id fermentum. Sed accumsan vehicula metus, non imperdiet eros auctor sit amet. In facilisis justo et sem cursus dictum. Fusce consectetur, est nec suscipit vulputate, nisi urna sodales ante, id viverra urna ligula nec odio. Donec eu neque nulla, sed sodales augue.
		Duis eget magna elit. Vestibulum dolor lorem, fermentum ac condimentum sit amet, malesuada eget elit. Quisque justo odio, consequat ut blandit id, ullamcorper quis massa. Aliquam lectus augue, commodo eu pharetra vitae, luctus nec est. In accumsan consectetur commodo. Vivamus nec massa lacus, sed lobortis erat. Quisque non pharetra leo. In et arcu odio. Sed fringilla elementum mauris, lacinia adipiscing est accumsan a. Aliquam erat volutpat. Ut nisi massa, ultrices eu congue ut, consectetur sed mauris. Integer arcu nunc, mattis mollis imperdiet tincidunt, ultrices eget neque. Curabitur rhoncus viverra ipsum, ac iaculis dolor rutrum at. Cras ac pharetra arcu. Nulla felis justo, venenatis ut molestie id, ultricies vel ante. Nam non lacus libero.
		Nulla posuere molestie tincidunt. Nulla nec tristique justo. Pellentesque nec condimentum eros. Nulla nec turpis id urna fermentum porttitor ut ut velit. In placerat odio porta augue facilisis ut sagittis ipsum volutpat. Morbi urna quam, fringilla eu facilisis eu, aliquet rutrum ipsum. Mauris feugiat justo id tellus rhoncus sit amet mattis lacus imperdiet. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In at nunc quis nisl interdum feugiat vel a lectus. Proin sed arcu at lectus dictum mattis vel vel mauris. Suspendisse sollicitudin rhoncus tempor. Praesent massa nunc, consectetur sit amet pellentesque vitae, faucibus quis urna. In ut metus non orci consectetur aliquam. Nullam congue, mi et egestas vulputate, nibh leo ullamcorper dui, eget fermentum diam nisl id nulla. Donec dapibus dapibus justo, in pretium magna interdum et. In vitae mi non tortor gravida pulvinar at ac arcu. In hac habitasse platea dictumst. Proin pretium, tortor placerat suscipit auctor, lacus mi vestibulum lectus, vel accumsan arcu diam nec lectus. Aenean euismod fringilla purus vel tincidunt.
		Donec dignissim posuere mollis. Pellentesque convallis ipsum et nibh facilisis interdum. Nullam velit mauris, mattis et eleifend a, molestie tempor elit. Cras hendrerit, arcu at faucibus bibendum, ante diam pulvinar sapien, non viverra purus leo sed risus. Aliquam tempor rutrum augue, in ultrices lorem ultrices quis. Donec auctor laoreet cursus. Integer non elit lorem, nec pulvinar justo. Cras sagittis eleifend semper. Cras at lobortis tortor. Nam quis mi eget purus semper lobortis posuere vel magna. Sed porta, felis ac auctor fringilla, urna magna iaculis justo, at ullamcorper libero lectus vel tortor. Praesent at nunc tortor, vel fringilla lorem. Etiam quis rhoncus magna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin ac libero tortor.
		Aenean ut orci at orci rhoncus aliquet. Proin feugiat, diam sed sodales aliquam, diam sem tincidunt urna, non viverra massa orci quis urna. Quisque tincidunt felis ut elit pretium ac posuere mi cursus. Vivamus quis dapibus ligula. Suspendisse potenti. Praesent ac diam ac nisl congue posuere. Nam sit amet risus faucibus orci vulputate porta et suscipit magna. Vivamus at quam quis lectus vehicula commodo eu vitae leo. Nunc dolor purus, ornare sed congue ac, feugiat et purus. In mi lorem, ultrices non varius sed, dapibus posuere eros. Sed faucibus venenatis risus vel elementum.
		Duis eget ornare mi. Phasellus iaculis nulla eget lacus vehicula venenatis. Pellentesque non tellus quis lorem congue pellentesque. Suspendisse vestibulum, nulla sed hendrerit tincidunt, quam nunc cursus libero, a feugiat arcu enim at odio. Ut vestibulum imperdiet tellus id imperdiet. Aliquam et dolor libero, a tempor erat. Cras sagittis venenatis interdum. Mauris nec consequat diam. Etiam condimentum, odio at fermentum elementum, risus elit malesuada magna, et fringilla massa ante et tellus. Cras ut leo quis mauris imperdiet fringilla in et augue. Vivamus vestibulum metus sed enim faucibus id pharetra sem ornare. Suspendisse eget justo nibh, eu auctor mi. Aliquam accumsan egestas mollis.
		Sed semper hendrerit enim vel pellentesque. Praesent vehicula turpis at ipsum faucibus non feugiat libero volutpat. Etiam sed dolor eu arcu porttitor lobortis nec non magna. Morbi sit amet viverra orci. Mauris sagittis erat sed diam ullamcorper facilisis. Donec purus neque, vestibulum ut ullamcorper eget, placerat in est. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id diam turpis. Sed vestibulum, felis sed venenatis tempus, libero enim molestie ante, vel luctus nibh nisl a tortor. Mauris fermentum, quam eget rutrum sodales, tortor velit fringilla leo, id cursus purus nisi sed turpis. Nulla nibh mauris, pulvinar placerat ornare id, dapibus non ante. Mauris pretium viverra quam, eu tristique nisl sodales non. Nam sit amet dolor eros. Nulla facilisi.
		Nulla facilisi. Ut ultrices hendrerit consequat. Nam ligula orci, scelerisque varius tempor vel, convallis et nunc. Proin ullamcorper tempor posuere. Aenean et mi a sapien hendrerit mollis vel ornare ante. Suspendisse porta, velit sit amet dignissim placerat, ipsum lectus semper ligula, in bibendum felis urna a tortor. Suspendisse potenti. Fusce pretium, nunc quis varius viverra, sapien sem eleifend purus, sed tempus tortor sapien ut nisl. Suspendisse posuere venenatis risus vitae facilisis. Vestibulum consectetur metus lacus. Sed aliquam augue nisl. Suspendisse non purus in erat sodales dictum. Sed condimentum pellentesque gravida. Quisque vulputate, mi quis fringilla auctor, leo tellus porttitor eros, sed commodo enim metus vel mi. Phasellus in nulla lacinia lorem aliquam pretium in et justo. Nulla ac venenatis nisi. Praesent interdum pretium velit, et pulvinar ante consectetur quis. Morbi ut elit id orci tempor semper. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
		Nam porta accumsan tempus. Duis tellus sapien, commodo ut dapibus commodo, ornare id dui. Mauris at arcu neque, nec pretium nunc. Suspendisse nec nulla et erat malesuada varius. Pellentesque varius nisi ac metus egestas vitae ultricies mi porttitor. Praesent luctus adipiscing nunc, eu ornare metus gravida eget. Sed vel justo lorem, vitae tincidunt eros. Aliquam eleifend felis ac libero lobortis nec suscipit orci facilisis. Quisque convallis, velit non sodales hendrerit, risus odio sollicitudin nisl, sed porttitor mi dolor non turpis. Sed ac est quis felis lobortis porttitor. Nulla volutpat ipsum sodales magna commodo ut commodo metus convallis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
		Curabitur vestibulum sapien ac erat volutpat ultrices. In dignissim luctus leo sit amet mollis. Integer eget sagittis nunc. Cras felis turpis, pretium aliquet fringilla in, dapibus ut justo. Mauris sit amet pharetra leo. Nulla lectus elit, laoreet nec scelerisque eu, bibendum eget diam. Nunc vehicula blandit sem vel ultricies. Praesent sollicitudin eleifend imperdiet. Sed eget lectus vel sapien varius facilisis. Cras felis nisl, vehicula vitae feugiat nec, tincidunt a lacus. Aliquam enim neque, scelerisque et euismod non, ornare ut ipsum. Donec lectus lorem, sodales ac porta id, condimentum a metus. Nullam et lobortis augue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum mollis tortor non diam sodales tincidunt. Mauris vestibulum lorem a lectus lobortis commodo. Sed tempor, libero ac dictum posuere, leo massa hendrerit libero, at sodales eros enim in diam. Praesent tincidunt ligula eget augue ornare sit amet vehicula tellus tristique. Etiam vel pretium felis.
		Cras aliquam auctor auctor. Duis dictum sapien non urna posuere feugiat. Aliquam rutrum sem non metus auctor placerat. Nulla laoreet, erat eu sodales imperdiet, nisl arcu condimentum augue, sed dictum nisl tortor sit amet elit. Suspendisse ullamcorper magna ac dolor convallis sed aliquet quam commodo. Pellentesque eget magna tortor, non rhoncus est. Suspendisse malesuada vestibulum commodo. Maecenas venenatis, lacus sed venenatis convallis, lectus dolor gravida libero, porttitor ultrices urna purus ut lectus. Praesent mollis vulputate nibh, nec interdum tortor elementum id. Aenean lacinia accumsan purus, nec sodales enim tempus eget. Pellentesque aliquam tempor nisl, at volutpat orci dignissim in. Fusce sit amet sapien nec justo commodo auctor id sed augue. Aliquam ultricies consectetur lorem, eu accumsan dui facilisis at. Sed tristique porttitor nunc, at auctor diam gravida sit amet. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed eget nibh odio. Nullam et ipsum eu tortor dictum viverra. Sed et mauris ante, nec commodo quam. Proin purus mi, tristique eu lacinia quis, tincidunt sit amet dolor.
		Quisque congue fermentum sem, et ultricies lorem pharetra at. Pellentesque tincidunt placerat odio tempus semper. Mauris pretium tempor diam, eget fermentum elit aliquet at. Aenean pulvinar lorem eget arcu ultrices sodales. Maecenas elementum, enim ut aliquet tincidunt, neque diam convallis felis, eu tempus justo leo a nunc. Phasellus iaculis lobortis ullamcorper. Aenean posuere faucibus porttitor. Pellentesque dapibus dictum ornare. Suspendisse quis varius ipsum. Etiam porta, ante vitae sodales elementum, dui urna dapibus tellus, vel accumsan lacus odio et lorem. Aliquam elementum accumsan purus vitae elementum. Aenean non bibendum lacus. Nunc hendrerit blandit posuere. Curabitur sed tortor et orci facilisis ullamcorper. Suspendisse et ipsum sem, ac porttitor nisl. Phasellus tempor egestas tellus, vitae dictum lorem pellentesque ac. Donec ut dictum magna. Mauris fringilla sapien a elit pulvinar et aliquam diam aliquam. Suspendisse congue imperdiet risus non hendrerit. Vestibulum tristique quam eget ipsum gravida ultricies.
		Aliquam dui tortor, elementum ut tristique vel, euismod at libero. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam est metus, euismod in condimentum eu, porttitor et nisl. Aliquam eu vestibulum massa. Ut ac aliquam mauris. Donec ultrices bibendum nunc sit amet faucibus. Sed erat lacus, rhoncus at pharetra quis, semper eget nunc. Praesent luctus ligula in urna convallis viverra. Sed et faucibus elit. Aenean eleifend, dolor vel ultricies egestas, turpis tortor pharetra purus, non malesuada dolor lectus et quam. Proin et est ligula. Suspendisse faucibus placerat tincidunt. Nulla condimentum dictum magna. Nullam dignissim, dui at vulputate vulputate, urna libero porta mauris, pharetra viverra mi odio eget enim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per.
	"""

	words = lipsum.split()
	max_start = len(words) - count
	start = random.randrange(0, max_start)

	output = ' '.join(words[start:start+count]).capitalize()

	return output

if __name__ == "__main__":
	main()
