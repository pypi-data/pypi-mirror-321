import torch
import decord
from pathlib import Path
from torch.utils.tensorboard import SummaryWriter
from annolid.features import Embedding
# Temp fix of the no attribute 'get_filesytem' error
#import tensorflow as tf
#import tensorboard as tb
#tf.io.gfile = tb.compat.tensorflow_stub.io.gfile


def tensorboard_writer(logdir=None):

    if logdir is None:
        here = Path(__file__).parent.resolve()
        logdir = here.parent / 'runs' / 'logs'
    writer = SummaryWriter(log_dir=str(logdir))
    return writer


def frame_embeddings(frame):
    embed_vector = Embedding()(frame)
    return embed_vector


def main(video_url=None):
    decord.bridge.set_bridge('torch')
    if torch.cuda.is_available():
        ctx = decord.gpu(0)
    else:
        ctx = decord.cpu(0)
    vr = decord.VideoReader(
        video_url,
        ctx=ctx
    )

    writer = tensorboard_writer()
    frame_number = 0

    for frame in vr:
        frame_numpy = frame.numpy()
        embed_vector = frame_embeddings([frame_numpy])
        writer.add_histogram('Frame Embeddings', embed_vector)
        writer.add_embedding(embed_vector,
                             metadata=[1],
                             label_img=frame.permute(2, 0, 1).unsqueeze(0),
                             global_step=frame_number
                             )
        frame_number += 1
    writer.close()


if __name__ == "__main__":
    main()
