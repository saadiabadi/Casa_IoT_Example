from fedn.utils.kerashelper import KerasHelper
from models.casa_model import create_seed_model

if __name__ == '__main__':

	# Create a initial_model model and push to Minio
	model = create_seed_model()
	outfile_name = "../initial_model/initial_model.npz"

	weights = model.get_weights()
	helper = KerasHelper()
	helper.save_model(weights, outfile_name)
