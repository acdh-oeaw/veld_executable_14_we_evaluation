import os
import gensim

import yaml


# file mounts, model
MODEL_PATH = "/veld/input/model/"
MODEL_INFO_PATH = "/veld/input/metadata.yaml"

# file mounts, evaluation
EVAL_DATA_PATH = "/veld/input/eval_data.yaml"
EVAL_SUMMARY_PATH = "/veld/output/summary.yaml"
EVAL_LOG_PATH = "/veld/output/logs/"

# environment metadata
MODEL_ARCH = os.environ.get("MODEL_ARCH")
MODEL_ID = os.environ.get("MODEL_ID")
MODEL_TRAIN_REPRODUCIBLE = os.environ.get("MODEL_TRAIN_REPRODUCIBLE")

# load optional meta info, if it exists
MODEL_INFO = None
try:
    with open(MODEL_INFO_PATH, "r") as f:
        MODEL_INFO = yaml.safe_load(f)
        MODEL_INFO["training_reproducible_at"]: MODEL_TRAIN_REPRODUCIBLE
except:
    pass


# TODO: ADAPT THIS TO YOUR SETUP
class ModelLogicContainer:
    """
    template class for all code dealing with model specifics
    """

    def __init__(self):
        """
        template method for any initialization logic. This method should not need any parameters.
        """
        for file in os.listdir(MODEL_PATH):
            if file.endswith(".model"):
                break
        self.model = gensim.models.Word2Vec.load(MODEL_PATH + "/" + file)
    
    def cos_sim_of_words(self, w1, w2):
        """
        template method for calculating cosine similarity between two words

        Parameters:
        w1 (str): One of two words
        w2 (str): One of two words

        Returns:
        float: cosine similarity, ranging from 0 to 1 
        """
        try:
            # Calculate cosine similarity between the word vectors
            similarity_score = self.model.wv.similarity(w1, w2)
            return similarity_score
        except KeyError:
             # Handle the case where one or both words are not in the vocabulary
            return None
