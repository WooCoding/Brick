import numpy as np

from .layer import Layer


class Dropout(Layer):

    def __init__(self, keep_prob):
        self.keep_prob = keep_prob
    
    def forward(self, x, training):

        if training:
            keep_prob = self.keep_prob
        else:
            return x
        
        mask = np.random.rand(*x.shape) < keep_prob
        self.cache["mask"] = mask
        y = x*mask
        # scale values close to expected values
        y /= keep_prob
        return y

    def backward(self, dy, **kw):
        
        dy *= self.cache["mask"]
        dy /= self.keep_prob
        return dy