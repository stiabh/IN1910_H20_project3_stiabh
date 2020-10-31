from chaos_game import *
import numpy as np
import pytest


@pytest.mark.parametrize(
    "n, r",
    [
        # n not an integer:
        ("str", 0.5),
        # r not a floating-point number:
        (4, 2),
        # n < 3:
        (1, 0.2),
        # r >= 1:
        (3, 2.5)
    ],
)
def test_ChaosGame_params(n, r):
    with pytest.raises(ValueError):
        cg = ChaosGame(n, r)


def test_ChaosGame_generate_ngon():
    tol = 1e-10
    corners = np.array([(0.,  1.),
                        (0.8660254037844387, -0.4999999999999998),
                        (-0.8660254037844385, -0.5000000000000004)])
    cg = ChaosGame(3, 0.5)
    assert np.all(abs(cg.corners - corners) < 1e-10)


def test_ChaosGame_iterate():
    n = 1000
    cg = ChaosGame(3, 0.5)
    cg.iterate(n)
    assert len(cg.X == n)
    assert len(cg.J == n)


def test_ChaosGame_plot():
    cg = ChaosGame(3, 0.5)
    with pytest.raises(AttributeError):
        cg.plot()
