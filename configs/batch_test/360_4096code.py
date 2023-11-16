# _base_ = '../default.py'
_base_ = '../nerf_unbounded/nerf_unbounded_default.py'

expname = 'dvgo_360_bicycle'
basedir = './logs/360_bicycle'

data = dict(
    datadir='/ssd1/zhiwen/datasets/360_v2/bicycle',
    factor=4, # 1237x822
    movie_render_kwargs=dict(
        shift_x=0.0,  # positive right
        shift_y=0, # negative down
        shift_z=0,
        scale_r=1.0,
        pitch_deg=-10, # negative look downward
    ),
)


fine_train = dict(
    N_iters=2000,
    importance_step=2000,
    prune_step=2000,
)

fine_model_and_render = dict(
    i_fully_vq=1000000,
)

vq_model_and_render = dict(
    codebook_size=4096,
)

