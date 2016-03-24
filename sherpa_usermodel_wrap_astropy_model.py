from __future__ import print_function

import numpy as np
from astropy.modeling import models
from sherpa import ui
import matplotlib.pyplot as plt

class AstropyToSherpa(object):
    def __init__(self, model):
        self.model = model

    def __call__(self, pars, x):
        self.model.parameters[:] = pars
        return self.model(x)

ap_model = (models.Gaussian1D(amplitude=1.2, mean=0.9, stddev=0.5) +
            models.Gaussian1D(amplitude=2.0, mean=-0.9, stddev=0.75))
err = 0.02
x = np.arange(-3, 3, .1)
y = ap_model(x) + err * np.random.uniform(size=len(x))

sh_model = AstropyToSherpa(ap_model)

ui.load_arrays(1, x, y, err * np.ones_like(x))
ui.load_user_model(sh_model, 'sherpa_model')
ui.add_user_pars('sherpa_model', ap_model.param_names, ap_model.parameters)
ui.set_model(1, 'sherpa_model')

ui.fit(1)
ui.plot_fit(1)

print()
print('Params from astropy model: {}'.format(ap_model.parameters))

plt.show()

