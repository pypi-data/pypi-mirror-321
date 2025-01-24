import numpy as np
import lindi


def load_real_1(
    *, num_samples: int, num_channels: int, start_channel: int
) -> np.ndarray:
    # https://neurosift.app/?p=/nwb&url=https://api.dandiarchive.org/api/assets/7e1de06d-d478-40e2-9b64-9dd04eafaa4c/download/&dandisetId=000876&dandisetVersion=draft
    nwb_url = "https://api.dandiarchive.org/api/assets/7e1de06d-d478-40e2-9b64-9dd04eafaa4c/download/"
    h5f = lindi.LindiH5pyFile.from_hdf5_file(nwb_url)
    ds = h5f["/acquisition/ElectricalSeriesAP/data"]
    assert isinstance(ds, lindi.LindiH5pyDataset)
    ret = ds[:num_samples, start_channel : start_channel + num_channels]
    return ret

    # # https://neurosift.app/?p=/nwb&url=https://api.dandiarchive.org/api/assets/c04f6b30-82bf-40e1-9210-34f0bcd8be24/download/&dandisetId=000409&dandisetVersion=draft
    # nwb_url = "https://api.dandiarchive.org/api/assets/c04f6b30-82bf-40e1-9210-34f0bcd8be24/download/"
    # h5f = lindi.LindiH5pyFile.from_hdf5_file(nwb_url)
    # ds = h5f['/acquisition/ElectricalSeriesAp/data']
    # assert isinstance(ds, lindi.LindiH5pyDataset)
    # ret = ds[:num_samples, start_channel:start_channel + num_channels]
    # return ret
