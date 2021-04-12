import archinstall
packages = "plasma kde-system-meta konqueror konsole dolphin sddm plasma-wayland-session"
if "nvidia" in _gfx_driver_packages:
	packages = packages + " egl-wayland"
installation.add_additional_packages(packages)
