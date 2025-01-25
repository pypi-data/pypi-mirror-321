import sys
import os
from huggingface_hub import login, create_repo, upload_file

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cusGPTdataset import Dataset
from cusGPTmodel import ModelGPT
try:
    from cusGPTvoice import Voice
except:
    print("WARNING: The voice function is not working as expected... Please wait until it's fixed")
dataset = Dataset()
model = ModelGPT(mix_pre=False,use_default=False)
login_hf_code = None

def login_hf(token):
    global login_hf_code
    login_hf_code = token
    login(token)

def data(file_name,first_n=None,start_from=0,name="WICKED4950/MentalHeathEsther",local=False,answer_only=True,batch_size=8,maskq=False):
    if model.tokenizer == None:
        raise Exception("You have to load the model first because this functions uses the tokneizer of that model")
    else:
        dataset(file_name=file_name,tokenizer = model.tokenizer,first_n=first_n,start_from=start_from,name=name,local=local,answer_only=answer_only,batch_size=batch_size,maskq=maskq)

def reinitmodel(mix_pre=False,use_default=False):
    global model
    del model
    model = ModelGPT(mix_pre,use_default)

def initVoice(voice_name=""):
    global voice
    voice = Voice(voice_name)

def train(epochs=1, lr=5e-5, decay_rate=1.00, decay_steps=1000,loss_avg=1500,distr=True,change_batch=500,split_training=False,val_split=0,val_log=500):
    if dataset.return_tf() == None:
        raise ValueError("You have to first load and process the data to train the model!")
    else:
        model.train_model(dataset.return_tf(),epochs,lr,decay_rate,decay_rate,loss_avg,distr,change_batch,split_training,val_split=val_split,val_log=val_log)
        print("training done!")

def push_model(name="saved_model",resp_name=None):
    if login_hf_code == None:
        raise ValueError("You have to log in into your hf account using .login_tf('Code here')")
    if resp_name == None:
        raise Exception("You have to give a name for the place to save the model")
    model.save_model(name)
    model.push_model(resp_name,login_hf_code)