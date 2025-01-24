import librosa
import matplotlib.pyplot as plt
import pandas as pd
import librosa.display
import numpy as np
from PIL import Image
import tensorflow as tf
import json
import os

### define functions
def detect_barking(path_to_file):
    try:
        y, sr = librosa.load(path_to_file)
        print('File reading was successful')
        #print(type(y))
        #print(type(sr))
    except Exception as e:
        print('Following error occured: \n')
        print(f'{e}')
        return

    #matplotlib.use('Agg')
    
    input_wave = pd.DataFrame(y)
    input_wave.reset_index(inplace=True)
    input_wave = input_wave.rename(columns={'index':'t',0:'f'})
    input_wave['t'] = input_wave['t']/sr # --> sr == number of points per second
    #input_wave = input_wave.loc[input_wave['t']<=1.000]
    y = input_wave['f'].values
   
    S_full, phase = librosa.magphase(librosa.stft(y))
    fig, ax = plt.subplots(figsize=(16,8))
    img = librosa.display.specshow(librosa.amplitude_to_db(S_full, ref=np.max),y_axis='log',x_axis='time', sr=sr, ax=ax)
    plt.axis('off')
    fig.canvas.draw()

    width, height = fig.canvas.get_width_height()
    
    image = Image.frombytes('RGB', (width, height), fig.canvas.tostring_rgb())
    
    new_image = image.resize((128, 128))
    np_img = np.array(new_image)

    plt.close()

    ### ------ Define model path and load a model ------
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_h5_path = os.path.join(current_dir, 'model', 'wdog_trained.h5')

    loaded_model = tf.keras.models.load_model(model_h5_path)  # Example for TensorFlow

    ### ------------------------------------------------

    # ------ Prepare img for NN ------
    prepared_img = np_img / 255.0
    prepared_img = np.expand_dims(prepared_img, axis=0)
    ### ------------------------------------------------

    prediction = loaded_model.predict(prepared_img)

    prediction = round(prediction[0][0])

    if prediction == 1:
        return_stmnt = [{'type':'bark', 'ts':0},
                        {'type':'howl', 'ts':0}]
    else:
        return_stmnt = {}

    return json.dumps(return_stmnt)