import wave
from model import themodel
import argparse
from data-util import *


parser = argparse.ArgumentParser(description = "train the model")
parser.add_argument('data', help='The name of the wav file with the data.')
parser.add_argument('output', help='The name of the HDF5 file that the weights will be saved to.')
parser.add_argument('-m', '--model', help = 'The name of the HDF5 file to take the weights from.')
parser.add_argument('-s', '--sample', type = int, dest='sample_size' default = 44100, help='The number of frames to include in each sample.')
parser.add_argument('--full', dest='split', action='store_const', const=arrange_samples_full, default=arrange_samples_sequential, help='Take every possible sample instead of every sequential sample.')


def main():
	args = parser.parse_args()
	if args.model:
		themodel.load_weights(args.model)
	x, y = args.split(args.data, args.sample_size)
	themodel.fit(x, y, batch_size = 150, verbose = 2, nb_epoch = 1)
	themodel.save_weights(args.output, overwrite = True)

if __name__ == "__main__":
	main()