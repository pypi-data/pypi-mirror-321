"""Contains all rnavigate convenience plotting functions"""

from fpocketr.rnavigate import plots
from fpocketr.rnavigate import data
from fpocketr.rnavigate.helper_functions import (
    PlottingArgumentParser,
    _parse_plot_kwargs,
    fit_data,
)
from fpocketr.rnavigate.data_loading import get_sequence


__all__ = [
    "plot_options",
    "plot_ss",
]


def plot_options(samples):
    """Prints a list of plotting functions compatible with a sample or list of samples.

    Some plotting functions require specific data classes to be loaded into the
    sample. For plotting multiple samples, data keywords that are not shared, or are
    shared, but are not of the same data class, are considered invalid.

    Parameters
    ----------
    samples : rnavigate.Sample or list of rnavigate.Sample
        samples to check for compatible plotting functions
    """
    if not isinstance(samples, list):
        samples = [samples]
    if len(samples) == 0:
        raise ValueError("No samples provided.")
    # get all data keywords for each sample
    # remove " (default)" from data keyword strings
    # find data keywords that are shared by all samples
    data_keywords = samples[0].print_data_keywords(return_dict=True)
    for key in data_keywords:
        for i, keyword in enumerate(data_keywords[key]):
            keyword = keyword.split(" ")[0]
            data_keywords[key][i] = keyword
    for sample in samples[1:]:
        these_data_keywords = sample.print_data_keywords(return_dict=True)
        for key in data_keywords:
            data_keywords[key] = list(
                set(data_keywords[key]) & set(these_data_keywords[key])
            )
    
    # SecondaryStructures which contain drawing coordinates
    ss_with_coords = []
    for keyword in data_keywords["structures"]:
        if all("X_coordinate" in s.get_data(keyword).data.columns for s in samples):
            ss_with_coords.append(keyword)
    # any sequence data
    sequences = []
    for key in data_keywords:
        for keyword in data_keywords[key]:
            if all(isinstance(s.get_data(keyword), data.Sequence) for s in samples):
                sequences.append(keyword)

    print(
        """
All data keywords are optional inputs for each RNAvigate sample. However,
each plotting function has specific data requirements. This list contains
all plotting functions for which requirements are met by these samples,
and the specific data keywords that satisfy each requirement.

Further below, a list of compatible optional data keywords is provided.
These are likely to be useful for plotting, but are not required.


Compatible plotting functions and keywords for these samples:"""
    )

    if len(ss_with_coords) > 0:
        print(
            f"""
    plot_ss
        structures: {ss_with_coords}"""
        )
    else:
        print(
            """
    plot_ss
    NOT COMPATIBLE
        requires sample(s) which contain structures with coordinates."""
        )

    print("\n\nCompatible optional data for plotting functions\n")
    for key in data_keywords:
        print(f"    {key}: {data_keywords[key]}")


def plot_ss(
    # required
    samples,
    structure,
    # optional data inputs
    profile=None,
    annotations=None,
    interactions=None,
    interactions2=None,
    # optional data display
    labels=None,
    colors=None,
    nt_ticks=None,
    bp_style="dotted",
    # optional plot display
    colorbars=True,
    plot_kwargs=None,
):
    """Generates a multipanel secondary structure drawing with optional
    coloring by per-nucleotide data and display of inter-nucleotide data and/or
    sequence annotations. Each plot may display a unique sample and/or
    inter-nucleotide data filtering scheme.

    Parameters
    ----------
    samples : list of rnavigate Samples
        samples used to retrieve data
    structure : data keyword string or data object
        secondary structure to plot as arcs
        All data are mapped to this sequence before plotting
    profile : data keyword string or data object, defaults to None
        Profile used for coloring if "profile" used in colors dictionary
    annotations : list of data keyword strings or data objects, defaults to []
        Annotations used to highlight regions or sites of interest
    interactions : one of the formats below, defaults to None
        format 1 (data or data keyword)
            Interactions to plot on secondary structure, no filtering
        format 2 (dictionary)
            e.g. {"interactions": format 1}
            additional filtering options can be added to the dictionary
        format 3 (list of format 2 dictionaries)
            This format allows multiple filtering schemes to be applied,
            each will be plotted on a seperate axis
    interactions2 : one of the formats below, defaults to None
        format 1 (data or data keyword)
            Interactions to plot on secondary structure, no filtering
        format 2 (dictionary)
            e.g. {"interactions": format 1}
            additional filtering options can be added to the dictionary
    labels : list of strings, defaults to sample.sample for each sample
        list containing Labels to be used in plot legends
        Defaults to sample.sample for each sample
    colors : dictionary, optional
        a dictionary of element: value pairs that determines how colors
        will be applied to each plot element and if that element is plotted
        only the elements you wish to change need to be included
        value options and what the colors represent:
            None: don"t plot this elelement
            "sequence": nucleotide identity
            "position": position in sequence
            "annotations": sequence annotations
            "profile": per-nucleotide data from profile
                profile argument must be provided
            "structure": base-pairing status
            matplotlib color: all positions plotted in this color
            array of colors: a different color for each position
                must be the same length as structure
        "sequence" may also use "contrast" which automatically chooses
            white or black, which ever contrasts better with "nucleotide"
            color
        Defaults to {"sequence": None,
                        "nucleotides": "sequence",
                        "structure": "grey",
                        "basepairs": "grey"}
    nt_ticks : integer, defaults to None (no labels)
        gap between major tick marks
    bp_style : "dotted", "line", or "conventional", defaults to "dotted"
        "dotted" plots basepairs as a dotted line
        "line" plots basepairs as a solid line
        "conventional" plots basepairs using Leontis-Westhof conventions
            for canonical and wobble pairs ("G-A" plotted as solid dot)
    colorbars : bool, defaults to True
        Whether to plot color scales for all plot elements
    plot_kwargs : dict, defaults to {}
        Keyword-arguments passed to matplotlib.pyplot.subplots

    Returns
    -------
    rnavigate.plots.SS plot
        object containing matplotlib figure and axes with additional plotting and
        file saving methods
    """
    parsed_args = PlottingArgumentParser(
        samples=samples,
        labels=labels,
        structure=structure,
        annotations=annotations,
        profile=profile,
        interactions=interactions,
        interactions2=interactions2,
    )
    plot_kwargs = _parse_plot_kwargs(plot_kwargs, "rnavigate.plots.SS")
    parsed_args.update_rows_cols(plot_kwargs)
    # initialize plot using all structure drawings
    plot = plots.SS(num_samples=parsed_args.num_samples, **plot_kwargs)
    # loop through samples and filters, adding each as a new axis
    for data_dict in parsed_args.data_dicts:
        data_dict = fit_data(data_dict, data_dict["structure"].null_alignment)
        plot.plot_data(**data_dict, colors=colors, nt_ticks=nt_ticks, bp_style=bp_style)
    plot.set_figure_size()
    if colorbars:
        plot.plot_colorbars()
    return plot
