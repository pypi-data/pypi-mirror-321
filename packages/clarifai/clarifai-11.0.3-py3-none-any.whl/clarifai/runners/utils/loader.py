import importlib.util
import json
import os
import subprocess

from clarifai.utils.logging import logger


class HuggingFaceLoader:

  HF_DOWNLOAD_TEXT = "The 'huggingface_hub' package is not installed. Please install it using 'pip install huggingface_hub'."

  def __init__(self, repo_id=None, token=None):
    self.repo_id = repo_id
    self.token = token
    if token:
      if self.validate_hftoken(token):
        subprocess.run(f'huggingface-cli login --token={os.environ["HF_TOKEN"]}', shell=True)
        logger.info("Hugging Face token validated")
      else:
        logger.info("Continuing without Hugging Face token")

  @classmethod
  def validate_hftoken(cls, hf_token: str):
    try:
      if importlib.util.find_spec("huggingface_hub") is None:
        raise ImportError(cls.HF_DOWNLOAD_TEXT)
      os.environ['HF_TOKEN'] = hf_token
      from huggingface_hub import HfApi

      api = HfApi()
      api.whoami(token=hf_token)
      return True
    except Exception as e:
      logger.error(
          f"Error setting up Hugging Face token, please make sure you have the correct token: {e}")
      return False

  def download_checkpoints(self, checkpoint_path: str):
    # throw error if huggingface_hub wasn't installed
    try:
      from huggingface_hub import list_repo_files, snapshot_download
    except ImportError:
      raise ImportError(self.HF_DOWNLOAD_TEXT)
    if os.path.exists(checkpoint_path) and self.validate_download(checkpoint_path):
      logger.info("Checkpoints already exist")
      return True
    else:
      os.makedirs(checkpoint_path, exist_ok=True)
      try:
        is_hf_model_exists = self.validate_hf_model()
        if not is_hf_model_exists:
          logger.error("Model %s not found on Hugging Face" % (self.repo_id))
          return False

        ignore_patterns = None  # Download everything.
        repo_files = list_repo_files(repo_id=self.repo_id, token=self.token)
        if any(f.endswith(".safetensors") for f in repo_files):
          logger.info(f"SafeTensors found in {self.repo_id}, downloading only .safetensors files.")
          ignore_patterns = ["original/*", "*.pth", "*.bin"]
        snapshot_download(
            repo_id=self.repo_id,
            local_dir=checkpoint_path,
            local_dir_use_symlinks=False,
            ignore_patterns=ignore_patterns)
      except Exception as e:
        logger.error(f"Error downloading model checkpoints {e}")
        return False
      finally:
        is_downloaded = self.validate_download(checkpoint_path)
        if not is_downloaded:
          logger.error("Error validating downloaded model checkpoints")
          return False
      return True

  def download_config(self, checkpoint_path: str):
    # throw error if huggingface_hub wasn't installed
    try:
      from huggingface_hub import hf_hub_download
    except ImportError:
      raise ImportError(self.HF_DOWNLOAD_TEXT)
    if os.path.exists(checkpoint_path) and os.path.exists(
        os.path.join(checkpoint_path, 'config.json')):
      logger.info("HF model's config.json already exists")
      return True
    os.makedirs(checkpoint_path, exist_ok=True)
    try:
      is_hf_model_exists = self.validate_hf_model()
      if not is_hf_model_exists:
        logger.error("Model %s not found on Hugging Face" % (self.repo_id))
        return False
      hf_hub_download(repo_id=self.repo_id, filename='config.json', local_dir=checkpoint_path)
    except Exception as e:
      logger.error(f"Error downloading model's config.json {e}")
      return False
    return True

  def validate_hf_model(self,):
    # check if model exists on HF
    try:
      from huggingface_hub import file_exists, repo_exists
    except ImportError:
      raise ImportError(self.HF_DOWNLOAD_TEXT)
    return repo_exists(self.repo_id) and file_exists(self.repo_id, 'config.json')

  def validate_download(self, checkpoint_path: str):
    # check if model exists on HF
    try:
      from huggingface_hub import list_repo_files
    except ImportError:
      raise ImportError(self.HF_DOWNLOAD_TEXT)
    checkpoint_dir_files = [
        f for dp, dn, fn in os.walk(os.path.expanduser(checkpoint_path)) for f in fn
    ]
    return (len(checkpoint_dir_files) >= len(list_repo_files(self.repo_id))) and len(
        list_repo_files(self.repo_id)) > 0

  @staticmethod
  def validate_config(checkpoint_path: str):
    # check if downloaded config.json exists
    return os.path.exists(checkpoint_path) and os.path.exists(
        os.path.join(checkpoint_path, 'config.json'))

  @staticmethod
  def fetch_labels(checkpoint_path: str):
    # Fetch labels for classification, detection and segmentation models
    config_path = os.path.join(checkpoint_path, 'config.json')
    with open(config_path, 'r') as f:
      config = json.load(f)

    labels = config['id2label']
    return labels
