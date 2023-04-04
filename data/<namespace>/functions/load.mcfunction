#> <namespace>:private/load
# Load function (with Lantern Load compatibility)
# Lantern Load: https://github.com/LanternMC/load
# @handles load

#> Lantern Load
scoreboard players set <namespace> load.status 1

#> Start ticking
# https://github.com/LanternMC/load
schedule function <namespace>:tick 1t