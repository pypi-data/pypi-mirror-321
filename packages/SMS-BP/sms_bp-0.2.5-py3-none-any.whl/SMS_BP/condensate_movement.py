"""
Contains class for storing condensate data. Condensates are defined as spherical always; defined by a
center (x,y,z), radius (r), and time (t). The complete description of the condensate at any time (t) is:
(x,y,z,r,t).

Usage:
------
    Initialize the class as follows:
        condensate = Condensate(**{
            "initial_position":np.array([0, 0, 0]),
            "initial_time":0,
            "diffusion_coefficient":0,
            "hurst_exponent":0,
            "units_time":'ms',
            "units_position":'um',
            "condensate_id":0,
            "initial_scale":0,
        })
    Call the class object as follows to get the position and scale of the condensate at a given time:
        condensate(times, time_unit) -> dict{"Position":np.ndarray, "Scale":float}
"""

import matplotlib.pyplot as plt
import numpy as np

import SMS_BP.simulate_foci as sf
from SMS_BP.decorators import cache


class Condensate:
    """Condensate class for storing condensate data.

    Parameters:
    -----------
    initial_position: np.ndarray = np.array([0, 0, 0])
        Initial position of the condensate.
    initial_time: float = 0
        Initial time of the condensates.
    diffusion_coefficient: float = 0
        Diffusion coefficient of the condensate.
    hurst_exponent: float = 0
        Hurst exponent of the condensate.
    units_time: str = 's'
        Units of time. Units work as follows: in the class reference frame, start from 0 and iterate by 1 each time.
        For a units_time of "ms", 1 represents 1ms.
        For a units_time of "s", 1 represents 1s.
        For a units_time of "20ms", 1 represents 20ms.
    units_position: str = 'um'
        Units of position.
    condensate_id: int = 0
        ID of the condensate.
    initial_scale: float = 0
        Initial scale of the condensate.
    cell_space: np.ndarray = np.array([[0,0],[0,0],[0,0]])
        Space of the cell.
    cell_axial_range: float|int = 0
        Axial range of the cell.

    """

    def __init__(
        self,
        initial_position: np.ndarray = np.array([0, 0, 0]),
        initial_time: int = 0,
        diffusion_coefficient: float = 0,  # same units as position and time
        hurst_exponent: float = 0,  # 0<hurst_exponent<1
        units_time: str = "ms",
        units_position: str = "um",
        condensate_id: int = 0,
        initial_scale: float = 0,
        # min/max (eg: [[min_x, max_x], ... ]
        cell_space: np.ndarray = np.array(
            [
                [0, 0],
                [0, 0],
                [0, 0],
            ]
        ),  # last [0, 0] are from the cell_axial_range (eg: +-5 from 0, so -5, 5)
        cell_axial_range: float | int = 0,
    ):
        self.initial_position = initial_position
        self.initial_time = initial_time
        self.diffusion_coefficient = diffusion_coefficient
        self.hurst_exponent = hurst_exponent
        self.units_time = units_time
        self.units_position = units_position
        self.condensate_id = condensate_id
        self.initial_scale = initial_scale
        self.dim = self.initial_position.shape[0]
        self.cell_space = cell_space
        self.cell_axial_range = cell_axial_range

        # initialize the properties of the condensate
        self._initialize_properties()

    def _initialize_properties(self) -> None:
        """Initializes the properties of the condensate."""
        self.times = np.array([self.initial_time])
        self.condensate_positions = np.array([self.initial_position])
        self.scale = np.array([self.initial_scale])

    @property
    def times(self) -> np.ndarray:
        """Returns the times of the condensate."""
        return self._times

    @times.setter
    def times(self, value) -> None:
        # make sure this is a numpy array
        if not isinstance(value, np.ndarray):
            raise TypeError("Times must be a numpy array.")
        self._times = value

    @property
    def condensate_positions(self) -> np.ndarray:
        """Returns the positions of the condensate."""
        # make sure this is a numpy array and that it is the same dimension as the initial position
        return self._condensate_positions

    @condensate_positions.setter
    def condensate_positions(self, value) -> None:
        if not isinstance(value, np.ndarray):
            raise TypeError("Condensate positions must be a numpy array.")
        if value.shape[1] != self.dim:
            raise ValueError(
                "Condensate positions must be the same dimension as the initial position."
            )
        self._condensate_positions = value

    @property
    def scale(self) -> np.ndarray:
        """Returns the scale of the condensate."""
        return self._scale

    @scale.setter
    def scale(self, value) -> None:
        self._scale = value

    def add_positions(
        self, time: np.ndarray, position: np.ndarray, scale: np.ndarray
    ) -> None:
        """Adds positions to the condensate.

        Parameters:
        -----------
        time: np.ndarray
            Times at which to add positions.
        position: np.ndarray
            Positions to add to the condensate.
        scale: np.ndarray
            Scale to add to the condensate.
        """
        self.times = np.append(self.times, time)
        self.condensate_positions = np.append(
            self.condensate_positions, position, axis=0
        )
        self.scale = np.append(self.scale, scale)

    @cache
    def __call__(self, time: int, time_unit: str) -> dict:
        """Returns the position and scale of the condensate at a given time.

        Parameters:
        -----------
        time: float
            Time at which to return the position of the condensate. User needs to convert to the reference frame of the condensate class.
        time_unit: str
            Units of time.
            Just to make sure the user is aware of the conversion they need to do to get into the reference frame of the condensate class.

        Returns:
        --------
        Dict of the position and scale of the condensate at the given time.
            Keys:
                Position: np.ndarray
                    Position of the condensate at the given time.
                Scale: float
                    Scale of the condensate at the given time.
        """
        if time_unit != self.units_time:
            # raise error that you need to ask for the time units in the condensates reference frame
            raise ValueError("Time units do not match to the condensate.")
        # check if the _condensate_positions exists
        if not hasattr(self, "_condensate_positions"):
            # if it doesn't then we need to generate the condensate positions
            self.times = np.array([self.initial_time])
            self.condensate_positions = np.array([self.initial_position])
            self.scale = np.array([self.initial_scale])
        # if the time larger than the last time in the condensate_positions then we need to generate more positions
        if time > self.times[-1]:
            self.generate_condensate_positions(time)

        return {
            "Position": self.condensate_positions[self.times == time][0],
            "Scale": self.scale[self.times == time][0],
        }

    '''
    @deprecated("Use generate_condensate_positions instead.")
    def _generate_condensate_positions(self, time: int) -> None:
        """Generates the condensate positions up to a given time.

        Parameters:
        -----------
        time: int
            Time up to which to generate the condensate positions.
        """

        # find the difference between the time and the last time in the condensate_positions
        time_difference = time - self.times[-1]
        # make a time array starting from the last time +1 and goin to the time inclusive
        time_array = np.arange(self.times[-1] + 1, time + 1)
        # since time is positive consecutive integers we can just use the length of the time array to be the difference we calculated
        t, xy = fbm.get_fbm_sample(
            l=time_difference,
            n=int(time_difference) + 1,
            h=self.hurst_exponent,
            d=self.dim,
        )
        # convert the xy into [[x,y],...] format
        x, y = xy
        coords = np.stack((x, y), axis=-1) * np.sqrt(2 * self.diffusion_coefficient)
        # use the last position as a starting point
        # the first position is the last position in the condensate_positions so ignore it when adding to the condensate_positions
        coords = coords + self.condensate_positions[-1]
        # get the scale for the time array and positions
        scales = self.calculate_scale(time_array, coords[1:])
        # add the positions to the condensate_positions
        self.add_positions(time_array, coords[1:], scales)
    '''

    def generate_condensate_positions(self, time: int) -> None:
        """Generates the condensate positions up to a given time.

        Parameters:
        -----------
        time: int
            Time up to which to generate the condensate positions.
        """
        # find the time difference
        time_difference = time - self.times[-1]
        # make a time array starting from the last time +1 and goin to the time inclusive
        time_array = np.arange(self.times[-1] + 1, time + 1)
        # we need to use the track generator class
        track_generator = sf.Track_generator(
            cell_space=self.cell_space,
            cell_axial_range=self.cell_axial_range,
            frame_count=500,
            exposure_time=20,
            interval_time=0,
            oversample_motion_time=20,
        )
        track = track_generator.track_generation_no_transition(
            diffusion_coefficient=self.diffusion_coefficient,
            hurst_exponent=self.hurst_exponent,
            track_length=time_difference,
            initials=self.condensate_positions[-1],
            start_time=self.times[-1],
        )
        track_xyz = track["xy"][:]
        # take all the x,y,z
        track_xyz = track_xyz[:, :]
        # get the scale for the time array and positions
        scales = self.calculate_scale(time_array, track_xyz)
        # add the positions to the condensate_positions
        self.add_positions(time_array, track_xyz, scales)

    def calculate_scale(self, time: np.ndarray, position: np.ndarray) -> np.ndarray:
        """Calculates the scale of the condensate at a given time.

        Parameters:
        -----------
        time: np.ndarray
            Times at which to calculate the scale.
        position: np.ndarray
            Positions at which to calculate the scale.
        """
        # find the last scale in the scale array
        last_scale = self.scale[-1]
        # make array of length time with the last scale
        scale = np.full(time.shape, last_scale)
        return scale

    def plot_condensate(self, ax, **kwargs):
        """
        Plots the condensate

        Parameters:
        -----------
        ax: plt.Axes
            Axes to plot the condensate on.
        **kwargs:
            Keyword arguments to pass to the plot function.
        """
        # check if the _condensate_positions exists
        if not hasattr(self, "_condensate_positions"):
            # if it doesn't then we need to generate the condensate positions
            self.times = np.array([self.initial_time])
            self.condensate_positions = np.array([self.initial_position])
            self.scale = np.array([self.initial_scale])

        # plot the condensate positions
        ax.plot(
            self.condensate_positions[:, 0], self.condensate_positions[:, 1], **kwargs
        )

        # plot a circle at all the positions with the scale as the radius
        for i in range(len(self.condensate_positions)):
            ax.add_patch(
                plt.Circle(
                    self.condensate_positions[i], self.scale[i], color="r", fill=False
                )
            )

        # plot the initial position in a different colour
        ax.scatter(self.initial_position[0], self.initial_position[1], color="g")
        # plot the final position in a different colour
        ax.scatter(
            self.condensate_positions[-1][0],
            self.condensate_positions[-1][1],
            color="b",
        )
        if "save_path" in kwargs:
            plt.savefig(kwargs["save_path"])
        # plt.show()
        return ax
