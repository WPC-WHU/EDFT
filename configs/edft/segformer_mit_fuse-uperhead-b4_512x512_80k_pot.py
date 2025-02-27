_base_ = ['./segformer_mit_fuse-b0_512x512_80k_pot.py']

# model settings
model = dict(
    pretrained='pretrain/mit_b4.pth',
    backbone=dict(
        weight=0.4,
        embed_dims=64,
        num_heads=[1, 2, 5, 8],
        num_layers=[3, 8, 27, 3]),
    decode_head=dict(
        type='UPerHead',
        in_channels=[64, 128, 320, 512],
        pool_scales=(1, 2, 3, 6)))
