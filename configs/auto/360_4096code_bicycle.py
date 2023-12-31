expname = '360_4096code_bicycle'
basedir = './logs/360_4096code'
data = dict(
    datadir='/ssd1/zhiwen/datasets/360_v2//bicycle',
    dataset_type='llff',
    inverse_y=False,
    flip_x=False,
    flip_y=False,
    annot_path='',
    split_path='',
    sequence_name='',
    load2gpu_on_the_fly=True,
    testskip=1,
    white_bkgd=True,
    rand_bkgd=True,
    half_res=False,
    bd_factor=0.75,
    movie_render_kwargs=dict(
        shift_x=0.0, shift_y=0, shift_z=0, scale_r=1.0, pitch_deg=-10),
    ndc=False,
    spherify=True,
    factor=4,
    width=None,
    height=None,
    llffhold=8,
    load_depths=False,
    unbounded_inward=True,
    unbounded_inner_r=1.0)
coarse_train = dict(
    N_iters=0,
    N_rand=8192,
    lrate_density=0.1,
    lrate_k0=0.1,
    lrate_rgbnet=0.001,
    lrate_featnet=0.001,
    lrate_decay=20,
    pervoxel_lr=True,
    pervoxel_lr_downrate=1,
    ray_sampler='random',
    weight_main=1.0,
    weight_entropy_last=0.01,
    weight_nearclip=0,
    weight_distortion=0,
    weight_rgbper=0.1,
    tv_every=1,
    tv_after=0,
    tv_before=0,
    tv_dense_before=0,
    weight_tv_density=0.0,
    weight_tv_k0=0.0,
    pg_scale=[],
    decay_after_scale=1.0,
    skip_zero_grad_fields=[],
    maskout_lt_nviews=0,
    prune_step=10000000)
fine_train = dict(
    N_iters=4000,
    N_rand=4096,
    lrate_density=0.1,
    lrate_k0=0.1,
    lrate_rgbnet=0.001,
    lrate_featnet=0.001,
    lrate_decay=80,
    pervoxel_lr=False,
    pervoxel_lr_downrate=1,
    ray_sampler='flatten',
    weight_main=1.0,
    weight_entropy_last=0.001,
    weight_nearclip=1.0,
    weight_distortion=0.01,
    weight_rgbper=0.01,
    tv_every=1,
    tv_after=0,
    tv_before=20000,
    tv_dense_before=20000,
    weight_tv_density=1e-06,
    weight_tv_k0=1e-07,
    pg_scale=[2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000],
    decay_after_scale=1.0,
    skip_zero_grad_fields=['density', 'k0'],
    maskout_lt_nviews=0,
    prune_step=10000000,
    importance_step=1000000)
coarse_model_and_render = dict(
    num_voxels=1024000,
    num_voxels_base=1024000,
    density_type='DenseGrid',
    k0_type='DenseGrid',
    density_config=dict(),
    k0_config=dict(),
    mpi_depth=128,
    nearest=False,
    pre_act_density=False,
    in_act_density=False,
    bbox_thres=0.001,
    mask_cache_thres=0.001,
    rgbnet_dim=0,
    rgbnet_full_implicit=False,
    rgbnet_direct=True,
    rgbnet_depth=3,
    rgbnet_width=128,
    alpha_init=1e-06,
    fast_color_thres=1e-07,
    maskout_near_cam_vox=True,
    world_bound_scale=1,
    stepsize=0.5)
fine_model_and_render = dict(
    num_voxels=32768000,
    num_voxels_base=32768000,
    density_type='DenseGrid',
    k0_type='DenseGrid',
    density_config=dict(),
    k0_config=dict(),
    mpi_depth=128,
    nearest=False,
    pre_act_density=False,
    in_act_density=False,
    bbox_thres=0.001,
    mask_cache_thres=0.001,
    rgbnet_dim=12,
    rgbnet_full_implicit=False,
    rgbnet_direct=True,
    rgbnet_depth=3,
    rgbnet_width=128,
    alpha_init=0.0001,
    fast_color_thres=dict({
        0: 5e-06,
        1500: 1e-05,
        2500: 2.5e-05,
        3500: 3.3333333333333335e-05,
        4500: 5e-05,
        5500: 0.0001,
        6500: 0.0001
    }),
    maskout_near_cam_vox=False,
    world_bound_scale=1,
    stepsize=0.5)
vq_model_and_render = dict(
    num_voxels=4096000,
    num_voxels_base=4096000,
    density_type='DenseGrid',
    k0_type='DenseGrid',
    density_config=dict(),
    k0_config=dict(),
    mpi_depth=128,
    nearest=False,
    pre_act_density=False,
    in_act_density=False,
    bbox_thres=0.001,
    mask_cache_thres=0.001,
    rgbnet_dim=12,
    rgbnet_full_implicit=False,
    rgbnet_direct=True,
    rgbnet_depth=3,
    rgbnet_width=128,
    alpha_init=0.01,
    fast_color_thres=0.0001,
    maskout_near_cam_vox=False,
    world_bound_scale=1.05,
    stepsize=0.5,
    use_vq=True,
    use_cosine_sim=False,
    codebook_size=4096)
vq_train = dict(
    N_iters=10000,
    N_rand=8192,
    lrate_density=0.1,
    lrate_k0=0.1,
    lrate_rgbnet=0.001,
    lrate_featnet=0.001,
    lrate_decay=20,
    pervoxel_lr=False,
    pervoxel_lr_downrate=1,
    ray_sampler='in_maskcache',
    weight_main=1.0,
    weight_entropy_last=0.001,
    weight_nearclip=0,
    weight_distortion=0,
    weight_rgbper=0.01,
    tv_every=1,
    tv_after=0,
    tv_before=0,
    tv_dense_before=0,
    weight_tv_density=0.0,
    weight_tv_k0=0.0,
    pg_scale=[1000, 2000, 3000, 4000],
    decay_after_scale=1.0,
    skip_zero_grad_fields=['density', 'k0'],
    maskout_lt_nviews=0,
    prune_step=10000000,
    importance_step=1000000)
alpha_init = 0.0001
stepsize = 0.5
