def localmax1d(data, win=3, thresh=None):
    r"""find local maximum points

    `Pytorch Argrelmax (or C++) function <https://discuss.pytorch.org/t/pytorch-argrelmax-or-c-function/36404/2>`_

    Parameters
    ----------
    data : list, ndarray or Tensor
        the input data
    win : int, optional
        the local window size, by default 3
    thresh : list, ndarray, Tensor or None, optional
        the threshhold, by default :obj:`None`

    Examples
    --------

    ::

        x = th.zeros(100, )
        x[10] = 1.
        x[30] = 1.2
        x[31] = 0.9
        x[80] = 1.
        x[90] = 0.3

        print(localmax1d(x, win=3, thresh=None))
        print(localmax1d(x, win=5))
        print(localmax1d(x, win=5, thresh=0.8))

    """

def localmax2d(data, win=3, thresh=None):
    r"""find local maximum points

    `Pytorch Argrelmax (or C++) function <https://discuss.pytorch.org/t/pytorch-argrelmax-or-c-function/36404/2>`_

    Parameters
    ----------
    data : list, ndarray or Tensor
        the input data
    win : int, optional
        the local window size, by default 3
    thresh : list, ndarray, Tensor or None, optional
        the threshhold, by default :obj:`None`

    Examples
    --------

    ::

        x = th.zeros(100, 100)
        x[10, 20] = 1.
        x[90, 60] = 0.3

        print(localmax2d(x, win=3, thresh=None))

    """

def localmax3d(data, win=3, thresh=None):
    r"""find local maximum points

    `Pytorch Argrelmax (or C++) function <https://discuss.pytorch.org/t/pytorch-argrelmax-or-c-function/36404/2>`_

    Parameters
    ----------
    data : list, ndarray or Tensor
        the input data
    win : int, optional
        the local window size, by default 3
    thresh : list, ndarray, Tensor or None, optional
        the threshhold, by default :obj:`None`

    Examples
    --------

    ::

        x = th.zeros(100, 100, 128)
        x[10, 20, 60] = 1.
        x[90, 60, 30] = 0.3

        print(localmax3d(x, win=3, thresh=None))

    """


