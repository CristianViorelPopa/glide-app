import streamlit as st

# from PIL import Image
# from IPython.display import display
# import torch as th

from glide_text2im.download import load_checkpoint
from glide_text2im.model_creation import (
    create_model_and_diffusion,
    model_and_diffusion_defaults,
    model_and_diffusion_defaults_upsampler
)
#
# device = 'cpu'
#
st.title('GLIDE App')
#
#
# @st.cache(allow_output_mutation=True)
# def setup_glide_model():
#     # Create base model.
#     options = model_and_diffusion_defaults()
#     options['use_fp16'] = False
#     options['timestep_respacing'] = '100'  # use 100 diffusion steps for fast sampling
#     model, diffusion = create_model_and_diffusion(**options)
#     model.eval()
#     model.to(device)
#     model.load_state_dict(load_checkpoint('base', device))
#     # st.write('total base parameters', sum(x.numel() for x in model.parameters()))
#     return model
#
#
# @st.cache(allow_output_mutation=True)
# def setup_glide_upsampler_model():
#     # Create upsampler model.
#     options_up = model_and_diffusion_defaults_upsampler()
#     options_up['use_fp16'] = False
#     options_up['timestep_respacing'] = 'fast27'  # use 27 diffusion steps for very fast sampling
#     model_up, diffusion_up = create_model_and_diffusion(**options_up)
#     model_up.eval()
#     model_up.to(device)
#     model_up.load_state_dict(load_checkpoint('upsample', device))
#     # st.write('total upsampler parameters', sum(x.numel() for x in model_up.parameters()))
#     return model_up
#
#
# # initial setup
# with st.spinner(text='In progress'):
#     model = setup_glide_model()
#     # model_up = setup_glide_upsampler_model()
