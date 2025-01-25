from os import path

from autogalaxy.interferometer.model.plotter_interface import (
    PlotterInterfaceInterferometer as AgPlotterInterfaceInterferometer,
)

from autolens.interferometer.fit_interferometer import FitInterferometer
from autolens.interferometer.plot.fit_interferometer_plotters import (
    FitInterferometerPlotter,
)
from autolens.analysis.plotter_interface import PlotterInterface

from autolens.analysis.plotter_interface import plot_setting


class PlotterInterfaceInterferometer(PlotterInterface):
    interferometer = AgPlotterInterfaceInterferometer.interferometer

    def fit_interferometer(
        self,
        fit: FitInterferometer,
        during_analysis: bool,
        subfolders: str = "fit_dataset",
    ):
        """
        Visualizes a `FitInterferometer` object, which fits an interferometer dataset.

        Images are output to the `image` folder of the `image_path` in a subfolder called `fit`. When
        used with a non-linear search the `image_path` is the output folder of the non-linear search.

        Visualization includes individual images of attributes of the `FitInterferometer` (e.g. the model data,
        residual map) and a subplot of all `FitInterferometer`'s images on the same figure.

        The images output by the `PlotterInterface` are customized using the file `config/visualize/plots.yaml` under the
        [fit] header.

        Parameters
        ----------
        fit
            The maximum log likelihood `FitInterferometer` of the non-linear search which is used to plot the fit.
        during_analysis
            Whether visualization is performed during a non-linear search or once it is completed.
        visuals_2d
            An object containing attributes which may be plotted over the figure (e.g. the centres of mass and light
            profiles).
        """

        def should_plot(name):
            return plot_setting(section=["fit", "fit_interferometer"], name=name)

        mat_plot_1d = self.mat_plot_1d_from(subfolders="")
        mat_plot_2d = self.mat_plot_2d_from(subfolders="")

        fit_plotter = FitInterferometerPlotter(
            fit=fit,
            include_2d=self.include_2d,
            mat_plot_1d=mat_plot_1d,
            mat_plot_2d=mat_plot_2d,
        )

        if should_plot("subplot_fit"):
            fit_plotter.subplot_fit()

        if should_plot("subplot_fit_dirty_images"):
            fit_plotter.subplot_fit_dirty_images()

        if should_plot("subplot_fit_real_space"):
            fit_plotter.subplot_fit_real_space()

        mat_plot_1d = self.mat_plot_1d_from(subfolders=subfolders)
        mat_plot_2d = self.mat_plot_2d_from(subfolders=subfolders)

        fit_plotter = FitInterferometerPlotter(
            fit=fit,
            include_2d=self.include_2d,
            mat_plot_1d=mat_plot_1d,
            mat_plot_2d=mat_plot_2d,
        )

        fit_plotter.figures_2d(
            data=should_plot("data"),
            noise_map=should_plot("noise_map"),
            signal_to_noise_map=should_plot("signal_to_noise_map"),
            model_data=should_plot("model_data"),
            residual_map_real=should_plot("residual_map"),
            chi_squared_map_real=should_plot("chi_squared_map"),
            normalized_residual_map_real=should_plot("normalized_residual_map"),
            residual_map_imag=should_plot("residual_map"),
            chi_squared_map_imag=should_plot("chi_squared_map"),
            normalized_residual_map_imag=should_plot("normalized_residual_map"),
            dirty_image=should_plot("data"),
            dirty_noise_map=should_plot("noise_map"),
            dirty_signal_to_noise_map=should_plot("signal_to_noise_map"),
            dirty_model_image=should_plot("model_data"),
            dirty_residual_map=should_plot("residual_map"),
            dirty_normalized_residual_map=should_plot("normalized_residual_map"),
            dirty_chi_squared_map=should_plot("chi_squared_map"),
        )

        if plot_setting(section="inversion", name="subplot_mappings"):
            fit_plotter.subplot_mappings_of_plane(
                plane_index=len(fit.tracer.planes) - 1
            )

        if not during_analysis and should_plot("all_at_end_png"):
            mat_plot_1d = self.mat_plot_1d_from(subfolders=path.join(subfolders, "end"))
            mat_plot_2d = self.mat_plot_2d_from(subfolders=path.join(subfolders, "end"))

            fit_plotter = FitInterferometerPlotter(
                fit=fit,
                include_2d=self.include_2d,
                mat_plot_1d=mat_plot_1d,
                mat_plot_2d=mat_plot_2d,
            )

            fit_plotter.figures_2d(
                data=True,
                noise_map=True,
                signal_to_noise_map=True,
                model_data=True,
                residual_map_real=True,
                chi_squared_map_real=True,
                normalized_residual_map_real=True,
                residual_map_imag=True,
                chi_squared_map_imag=True,
                normalized_residual_map_imag=True,
                dirty_image=True,
                dirty_noise_map=True,
                dirty_signal_to_noise_map=True,
                dirty_model_image=True,
                dirty_residual_map=True,
                dirty_normalized_residual_map=True,
                dirty_chi_squared_map=True,
            )

            plane_index_max = len(fit.tracer.planes) - 1

            fit_plotter.figures_2d_of_planes(
                plane_index=plane_index_max, plane_image=True
            )

        if not during_analysis and should_plot("all_at_end_fits"):
            mat_plot_2d = self.mat_plot_2d_from(
                subfolders=path.join("fit_dataset", "fits"), format="fits"
            )

            fit_plotter = FitInterferometerPlotter(
                fit=fit, include_2d=self.include_2d, mat_plot_2d=mat_plot_2d
            )

            fit_plotter.figures_2d(
                dirty_image=True,
                dirty_noise_map=True,
                dirty_signal_to_noise_map=True,
                dirty_model_image=True,
                dirty_residual_map=True,
                dirty_normalized_residual_map=True,
                dirty_chi_squared_map=True,
            )

            plane_index_max = len(fit.tracer.planes) - 1

            fit_plotter.figures_2d_of_planes(
                plane_index=plane_index_max, plane_image=True
            )
