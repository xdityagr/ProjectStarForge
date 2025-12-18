"""
StarForge - Generate beautiful star charts
==========================================

Simple example: Generate a star chart for your location.
For more examples, see examples.py

Developed by Aditya Gaur (@xdityagr)
"""

from Starforge import StarForge

# Generate a beautiful star chart
(StarForge("Paris")
    .at_date("2024-12-25 22:00")
    .with_fov(75)
    .with_magnitude_limit(5.0)
    .with_circular_mask()
    .with_colors(
        background="#001122",
        stars="#FFFFFF",
        lines="#6699CC",
        labels="#AADDFF"
    )
    .render("starmap.svg"))


print("\nDone! Open 'starmap.svg' to see your star chart.")
