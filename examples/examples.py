"""
StarForge Library - Complete Usage Examples
============================================

This file demonstrates all features of the StarForge library through
practical examples. The StarForge class provides an intuitive,
fluent API for generating beautiful astronomical star charts.

Run specific examples:
    python examples.py basic
    python examples.py dates
    python examples.py colors
    python examples.py all

Developed by Aditya Gaur (@xdityagr)
"""

import sys
from Starforge import StarForge, ChartConfig, Log, LogLevel, create_starmap


def example_basic():
    """Basic usage examples."""
    print("\n=== BASIC EXAMPLES ===\n")

    # Simple one-liner
    StarForge("New York").render("output/basic_simple.svg")

    # With coordinates
    StarForge("48.8566, 2.3522").render("output/basic_coords.svg")

    # City lookup with fuzzy matching
    StarForge("Mumbai").render("output/basic_mumbai.svg")


def example_dates():
    """Date and time examples."""
    print("\n=== DATE/TIME EXAMPLES ===\n")

    # Specific date
    StarForge("London").at_date("2024-12-25").render("output/date_christmas.svg")

    # Date with time
    StarForge("Tokyo").at_date("2024-07-04 22:30").render("output/date_with_time.svg")

    # European format
    StarForge("Paris").at_date("14/07/2024").render("output/date_european.svg")

    # Current time
    StarForge("Sydney").now().render("output/date_now.svg")


def example_fov():
    """Field of view examples."""
    print("\n=== FIELD OF VIEW EXAMPLES ===\n")

    StarForge("Berlin").with_fov(90).render("output/fov_full.svg")
    StarForge("Berlin").with_fov(60).render("output/fov_medium.svg")
    StarForge("Berlin").with_fov(30).render("output/fov_tight.svg")


def example_magnitude():
    """Star magnitude examples."""
    print("\n=== MAGNITUDE EXAMPLES ===\n")

    StarForge("Rome").with_magnitude_limit(3.0).render("output/mag_bright.svg")
    StarForge("Rome").with_magnitude_limit(5.0).render("output/mag_normal.svg")
    StarForge("Rome").with_magnitude_limit(6.5).render("output/mag_many.svg")


def example_labels():
    """Label styling examples."""
    print("\n=== LABEL EXAMPLES ===\n")

    StarForge("Athens").with_labels(True).render("output/labels_on.svg")
    StarForge("Athens").without_labels().render("output/labels_off.svg")

    (StarForge("Athens")
        .with_label_style(font_size="14px", font_family="Georgia, serif", opacity=0.8)
        .render("output/labels_styled.svg"))


def example_colors():
    """Color theme examples."""
    print("\n=== COLOR THEME EXAMPLES ===\n")

    # Classic dark
    (StarForge("Cairo")
        .with_colors(background="#000000", stars="#FFFFFF", lines="#FFFFFF", labels="#FFD700")
        .render("output/theme_classic.svg"))

    # Deep blue
    (StarForge("Cairo")
        .with_colors(background="#0a0a1a", stars="#E8E8FF", lines="#4466AA", labels="#88AAFF")
        .render("output/theme_blue.svg"))

    # Printable (light)
    (StarForge("Cairo")
        .with_colors(background="#FFFFFF", stars="#000000", lines="#333333", labels="#666666")
        .render("output/theme_printable.svg"))

    # Vintage
    (StarForge("Cairo")
        .with_colors(background="#1a1510", stars="#F5DEB3", lines="#CD853F", labels="#DAA520")
        .render("output/theme_vintage.svg"))


def example_effects():
    """Visual effects examples."""
    print("\n=== VISUAL EFFECTS EXAMPLES ===\n")

    # Circular mask
    StarForge("Helsinki").with_circular_mask().render("output/effect_circular.svg")

    # Sphere effect
    (StarForge("Dublin")
        .with_sphere_effect(True, strength=0.5)
        .render("output/effect_sphere.svg"))

    # Procedural stars
    (StarForge("Warsaw")
        .with_procedural_stars(True, count=500)
        .render("output/effect_procedural.svg"))


def example_sizing():
    """Size and dimension examples."""
    print("\n=== SIZE EXAMPLES ===\n")

    StarForge("Vienna").with_size(800).render("output/size_small.svg")
    StarForge("Vienna").with_size(2000).render("output/size_large.svg")
    StarForge("Vienna").with_size(1200, 800).render("output/size_wide.svg")


def example_styling():
    """Detailed styling examples."""
    print("\n=== STYLING EXAMPLES ===\n")

    # Star sizes
    (StarForge("Stockholm")
        .with_star_sizes(constellation=20, background=5)
        .render("output/style_stars.svg"))

    # Line style
    (StarForge("Oslo")
        .with_line_style(width=2.0, opacity=0.6)
        .render("output/style_lines.svg"))


def example_complete():
    """Fully configured example."""
    print("\n=== COMPLETE EXAMPLE ===\n")

    (StarForge("Reykjavik")
        .at_date("2024-03-20 23:00")
        .with_fov(70)
        .with_magnitude_limit(5.5)
        .with_size(1500)
        .with_colors(
            background="#050510",
            stars="#EEEEFF",
            lines="#5577AA",
            labels="#99BBDD"
        )
        .with_star_sizes(constellation=15, background=7)
        .with_line_style(width=1.0, opacity=0.6)
        .with_label_style(font_size="13px", opacity=0.85)
        .with_circular_mask()
        .with_sphere_effect(True, 0.5)
        .render("output/complete.svg"))


def example_special_dates():
    """Special occasion examples."""
    print("\n=== SPECIAL OCCASIONS ===\n")

    # Birthday sky
    (StarForge("Jaipur")
        .at_date("24/06/2007")
        .with_fov(75)
        .with_magnitude_limit(4.5)
        .without_labels()
        .with_circular_mask()
        .with_colors(background="#0a0a15", stars="#FFFFEE", lines="#FFFFFF")
        .render("output/special_birthday.svg"))

    # Wedding/Anniversary
    (StarForge("Venice")
        .at_date("2020-09-15 21:00")
        .with_size(1400)
        .with_sphere_effect(True, 0.4)
        .with_colors(background="#0d0d1a", stars="#FFF8E7", lines="#C0A060", labels="#E8D4A0")
        .render("output/special_anniversary.svg"))

    # New Year's Eve
    (StarForge("New York")
        .at_date("2024-12-31 23:59")
        .with_fov(60)
        .with_circular_mask()
        .render("output/special_newyear.svg"))


def example_data_access():
    """Accessing calculated data."""
    print("\n=== DATA ACCESS EXAMPLE ===\n")

    chart = StarForge("Amsterdam")
    chart.at_date("2024-08-12")
    chart.with_magnitude_limit(5.0)
    chart.calculate()

    print(f"Location: {chart.place_name}")
    print(f"Coordinates: ({chart.latitude:.4f}, {chart.longitude:.4f})")
    print(f"Observation time: {chart.observation_time}")
    print(f"Visible stars: {len(chart.visible_stars)}")
    print(f"Constellations: {len(chart.constellations)}")

    chart.render("output/data_access.svg")


def example_log_levels():
    """Log level control examples."""
    print("\n=== LOG LEVEL EXAMPLES ===\n")

    # Silent mode
    Log.set_level(LogLevel.SILENT)
    StarForge("Brussels").render("output/log_silent.svg")

    # Warnings only
    Log.set_level(LogLevel.WARNING)
    StarForge("Madrid").render("output/log_warnings.svg")

    # Back to default
    Log.set_level(LogLevel.INFO)
    StarForge("Lisbon").render("output/log_info.svg")


def example_legacy():
    """Legacy API example."""
    print("\n=== LEGACY API ===\n")

    cc = ChartConfig()
    cc.circular_mask = True
    create_starmap('Delhi', 'output/legacy.svg',
                   '24/06/2007', 4.5, 75, show_labels=False, style_config=cc)


def run_all():
    """Run all examples."""
    import os
    os.makedirs("output", exist_ok=True)

    example_basic()
    example_dates()
    example_fov()
    example_magnitude()
    example_labels()
    example_colors()
    example_effects()
    example_sizing()
    example_styling()
    example_complete()
    example_special_dates()
    example_data_access()
    example_log_levels()
    example_legacy()

    print("\n=== All examples generated! Check the 'output' folder. ===\n")


if __name__ == "__main__":
    import os
    os.makedirs("output", exist_ok=True)

    examples = {
        "basic": example_basic,
        "dates": example_dates,
        "fov": example_fov,
        "magnitude": example_magnitude,
        "labels": example_labels,
        "colors": example_colors,
        "effects": example_effects,
        "sizing": example_sizing,
        "styling": example_styling,
        "complete": example_complete,
        "special": example_special_dates,
        "data": example_data_access,
        "logs": example_log_levels,
        "legacy": example_legacy,
        "all": run_all,
    }

    if len(sys.argv) > 1:
        choice = sys.argv[1].lower()
        if choice in examples:
            examples[choice]()
        else:
            print(f"Unknown example: {choice}")
            print(f"Available: {', '.join(examples.keys())}")
    else:
        print("StarForge Examples")
        print("==================")
        print(f"Usage: python examples.py <example_name>")
        print(f"\nAvailable examples:")
        for name in examples:
            print(f"  - {name}")
