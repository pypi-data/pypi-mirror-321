from os import path
from typing import List

import autoarray.plot as aplt

from autogalaxy.imaging.model.plotter_interface import PlotterInterfaceImaging as AgPlotterInterfaceImaging

from autolens.analysis.plotter_interface import PlotterInterface
from autolens.imaging.fit_imaging import FitImaging
from autolens.imaging.plot.fit_imaging_plotters import FitImagingPlotter

from autolens.analysis.plotter_interface import plot_setting


class PlotterInterfaceImaging(PlotterInterface):

    imaging = AgPlotterInterfaceImaging.imaging
    imaging_combined = AgPlotterInterfaceImaging.imaging_combined

    def fit_imaging(
        self, fit: FitImaging, during_analysis: bool, subfolders: str = "fit_dataset"
    ):
        """
        Visualizes a `FitImaging` object, which fits an imaging dataset.

        Images are output to the `image` folder of the `image_path` in a subfolder called `fit`. When
        used with a non-linear search the `image_path` points to the search's results folder and this function
        visualizes the maximum log likelihood `FitImaging` inferred by the search so far.

        Visualization includes individual images of attributes of the `FitImaging` (e.g. the model data, residual map)
        and a subplot of all `FitImaging`'s images on the same figure.

        The images output by the `PlotterInterface` are customized using the file `config/visualize/plots.yaml` under the
        [fit] header.

        Parameters
        ----------
        fit
            The maximum log likelihood `FitImaging` of the non-linear search which is used to plot the fit.
        during_analysis
            Whether visualization is performed during a non-linear search or once it is completed.
        visuals_2d
            An object containing attributes which may be plotted over the figure (e.g. the centres of mass and light
            profiles).
        """

        if plot_setting(section="tracer", name="subplot_tracer"):

            mat_plot_2d = self.mat_plot_2d_from(subfolders="")

            fit_plotter = FitImagingPlotter(
                fit=fit, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
            )

            fit_plotter.subplot_tracer()

        def should_plot(name):
            return plot_setting(section=["fit", "fit_imaging"], name=name)

        mat_plot_2d = self.mat_plot_2d_from(subfolders=subfolders)

        fit_plotter = FitImagingPlotter(
            fit=fit, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
        )

        fit_plotter.figures_2d(
            data=should_plot("data"),
            noise_map=should_plot("noise_map"),
            signal_to_noise_map=should_plot("signal_to_noise_map"),
            model_image=should_plot("model_data"),
            residual_map=should_plot("residual_map"),
            chi_squared_map=should_plot("chi_squared_map"),
            normalized_residual_map=should_plot("normalized_residual_map"),
        )

        fit_plotter.figures_2d_of_planes(
            subtracted_image=should_plot("subtracted_images_of_planes"),
            model_image=should_plot("model_images_of_planes"),
            plane_image=should_plot("plane_images_of_planes"),
        )

        mat_plot_2d = self.mat_plot_2d_from(subfolders="")

        fit_plotter = FitImagingPlotter(
            fit=fit, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
        )

        if should_plot("subplot_fit"):
            fit_plotter.subplot_fit()

        if should_plot("subplot_fit_log10"):
            try:
                fit_plotter.subplot_fit_log10()
            except ValueError:
                pass

        if should_plot("subplot_of_planes"):
            fit_plotter.subplot_of_planes()

        if plot_setting(section="inversion", name="subplot_mappings"):
            try:
                fit_plotter.subplot_mappings_of_plane(plane_index=len(fit.tracer.planes) - 1)
            except IndexError:
                pass

        if not during_analysis and should_plot("all_at_end_png"):

            mat_plot_2d = self.mat_plot_2d_from(
                subfolders=path.join("fit_dataset", "end"),
            )

            fit_plotter = FitImagingPlotter(
                fit=fit, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
            )

            fit_plotter.figures_2d(
                data=True,
                noise_map=True,
                signal_to_noise_map=True,
                model_image=True,
                residual_map=True,
                normalized_residual_map=True,
                chi_squared_map=True,
            )

            fit_plotter.figures_2d_of_planes(
                subtracted_image=True, model_image=True, plane_image=True
            )

        if not during_analysis and should_plot("all_at_end_fits"):

            mat_plot_2d = self.mat_plot_2d_from(
                subfolders=path.join("fit_dataset", "fits"), format="fits"
            )

            fit_plotter = FitImagingPlotter(
                fit=fit, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
            )

            fit_plotter.figures_2d(
                data=True,
                noise_map=True,
                signal_to_noise_map=True,
                model_image=True,
                residual_map=True,
                normalized_residual_map=True,
                chi_squared_map=True,
            )

            fit_plotter.figures_2d_of_planes(
                subtracted_image=True, model_image=True, plane_image=True, interpolate_to_uniform=True
            )

    def fit_imaging_combined(self, fit_list: List[FitImaging]):
        """
        Output visualization of all `FitImaging` objects in a summed combined analysis, typically during or after a
        model-fit is performed.

        Images are output to the `image` folder of the `image_path` in a subfolder called `combined`. When used
        with a non-linear search the `image_path` is the output folder of the non-linear search.
        `.
        Visualization includes individual images of attributes of each fit (e.g. data, normalized residual-map) on
        a single subplot, such that the full suite of multiple datasets can be viewed on the same figure.

        The images output by the `PlotterInterface` are customized using the file `config/visualize/plots.yaml` under
        the `fit` header.

        Parameters
        ----------
        fit
            The list of imaging fits which are visualized.
        """

        def should_plot(name):
            return plot_setting(section=["fit", "fit_imaging"], name=name)

        mat_plot_2d = self.mat_plot_2d_from(subfolders="combined")

        fit_plotter_list = [
            FitImagingPlotter(
                fit=fit, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
            )
            for fit in fit_list
        ]

        subplot_columns = 6

        subplot_shape = (len(fit_list), subplot_columns)

        multi_plotter = aplt.MultiFigurePlotter(
            plotter_list=fit_plotter_list, subplot_shape=subplot_shape
        )

        if should_plot("subplot_fit"):

            def make_subplot_fit(filename_suffix):

                multi_plotter.subplot_of_figures_multi(
                    func_name_list=["figures_2d"],
                    figure_name_list=[
                        "data",
                    ],
                    filename_suffix=filename_suffix,
                    number_subplots=len(fit_list) * subplot_columns,
                    close_subplot=False,
                )

                multi_plotter.subplot_of_figures_multi(
                    func_name_list=["figures_2d_of_planes"],
                    figure_name_list=[
                        "subtracted_image",
                    ],
                    filename_suffix=filename_suffix,
                    number_subplots=len(fit_list) * subplot_columns,
                    open_subplot=False,
                    close_subplot=False,
                    subplot_index_offset=1,
                    plane_index=1
                )

                multi_plotter.subplot_of_figures_multi(
                    func_name_list=["figures_2d_of_planes"],
                    figure_name_list=[
                        "model_image",
                    ],
                    filename_suffix=filename_suffix,
                    number_subplots=len(fit_list) * subplot_columns,
                    open_subplot=False,
                    close_subplot=False,
                    subplot_index_offset=2,
                    plane_index=0
                )

                multi_plotter.subplot_of_figures_multi(
                    func_name_list=["figures_2d_of_planes"],
                    figure_name_list=[
                        "model_image",
                    ],
                    filename_suffix=filename_suffix,
                    number_subplots=len(fit_list) * subplot_columns,
                    open_subplot=False,
                    close_subplot=False,
                    subplot_index_offset=3,
                    plane_index=len(fit_list[0].tracer.planes) - 1
                )

                multi_plotter.subplot_of_figures_multi(
                    func_name_list=["figures_2d_of_planes"],
                    figure_name_list=[
                        "plane_image",
                    ],
                    filename_suffix=filename_suffix,
                    number_subplots=len(fit_list) * subplot_columns,
                    open_subplot=False,
                    close_subplot=False,
                    subplot_index_offset=4,
                    plane_index=len(fit_list[0].tracer.planes) - 1
                )

                multi_plotter.subplot_of_figures_multi(
                    func_name_list=["figures_2d"],
                    figure_name_list=[
                        "normalized_residual_map",
                    ],
                    filename_suffix=filename_suffix,
                    number_subplots=len(fit_list) * subplot_columns,
                    subplot_index_offset=5,
                    open_subplot=False,
                )

            make_subplot_fit(filename_suffix="fit")

            # for plotter in multi_plotter.plotter_list:
            #     plotter.mat_plot_2d.use_log10 = True
            #
            # make_subplot_fit(filename_suffix="fit_log10")