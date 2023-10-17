params = {
    "batch_size": 1,
    "channels": 30,
    "win_size": 256,
    "win_type": 'rect',
    "depth": 1,
    "nb_steps": 20,
    "in_channels": 1,
    "kernel_size": 3,
    "lr": 0.003,
    "out_channels": 4,
    "reduced_size": 80,
    "cuda": False,
    "gpu": 0,
    "M" : 20,
    "N" : 4
}
dataset_info = {'amc_86_01.4d': {'n_segs': 4, 'label': {588: 0, 1200: 1, 2006: 0, 2530: 2, 3282: 0, 4048: 3, 4579: 2}},
                'amc_86_02.4d': {'n_segs': 8,
                                 'label': {1009: 0, 1882: 1, 2677: 2, 3158: 3, 4688: 4, 5963: 0, 7327: 5, 8887: 6,
                                           9632: 7, 10617: 0}},
                'amc_86_03.4d': {'n_segs': 7,
                                 'label': {872: 0, 1938: 1, 2448: 2, 3470: 0, 4632: 3, 5372: 4, 6182: 5, 7089: 6,
                                           8401: 0}},
                'amc_86_07.4d': {'n_segs': 6,
                                 'label': {1060: 0, 1897: 1, 2564: 2, 3665: 1, 4405: 2, 5169: 3, 5804: 4, 6962: 0,
                                           7806: 5, 8702: 0}},
                'amc_86_08.4d': {'n_segs': 9,
                                 'label': {1062: 0, 1904: 1, 2661: 2, 3282: 3, 3963: 4, 4754: 5, 5673: 6, 6362: 4,
                                           7144: 7, 8139: 8, 9206: 0}},
                'amc_86_09.4d': {'n_segs': 5, 'label': {921: 0, 1275: 1, 2139: 2, 2887: 3, 3667: 4, 4794: 0}},
                'amc_86_10.4d': {'n_segs': 4, 'label': {2003: 0, 3720: 1, 4981: 0, 5646: 2, 6641: 3, 7583: 0}},
                'amc_86_11.4d': {'n_segs': 4,
                                 'label': {1231: 0, 1693: 1, 2332: 2, 2762: 1, 3386: 3, 4015: 2, 4665: 1, 5674: 0}},
                'amc_86_14.4d': {'n_segs': 3, 'label': {671: 0, 1913: 1, 2931: 0, 4134: 2, 5051: 0, 5628: 1, 6055: 2}},
                }
