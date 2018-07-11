import sys
from pathlib import Path
#sys.path.append(str(Path(Path(__file__).absolute()).parents[0]))

from src.silenium.run_complaint import complain

def main():
	if sys.argv[1] == 'complain':
		userTarget, timeDelayed, trainStationFrom, trainStationTo = sys.argv[2:]
		complain(userTarget, timeDelayed, trainStationFrom, trainStationTo)
	else:
		print('Only takes arguments complain')

if __name__ == '__main__':
	main()
