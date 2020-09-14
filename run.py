import pytest,multiprocessing


def runall():
	pytest.main(['-v', '-s'])


if __name__ == '__main__':
	p_list=[]
	b_list=['chrome1','firefox']
	for m in b_list:
		p_list.append(multiprocessing.Process(target=runall,args=(b_list,)))

	for m1 in p_list:
		m1.start()
